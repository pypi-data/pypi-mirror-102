from coopgraph.graphs import Graph, Node
from coopmovers.IAgentTracker import IAgentTracker
from typing import List, Dict, Set
from coopstructs.vectors import Vector2
from cooplock.resourcelock import ResourceLock
import logging
from uuid import uuid4
from coopmovers.traffic.intersection import Intersection
from coopmovers.traffic.intersectionHub import IntersectionHub
import copy
from coopbugger.monitoredclass import MonitoredClass
from pprint import pformat
from enum import Enum

logger = logging.Logger("trafficdirector")
DEFAULT_ENTRY_POS = Vector2(-1, -1)



class RegisteredDestination:
    def __init__(self, task_id:str, agent_name: str, destination_node: Node, submitted: int):
        self.task_id = task_id
        self.agent_name = agent_name
        self.destination_node = destination_node
        self.submitted = submitted
        self.reached = 0

    def copy(self):
        ret = RegisteredDestination(self.task_id, self.agent_name, Node(self.destination_node.name, self.destination_node.pos), self.submitted)
        ret.reached = self.reached
        return ret


class TrafficDirectorRunLoopResults:
    def __init__(self):
        self.completed_registered_destination = None
        self.agent_position = None
        self.open_destinations = None

class WaypointType(Enum):
    DESTINATION = 1
    WAYPOINT = 2
    JOG = 3

class Waypoint:
    def __init__(self, node: Node, waypoint_type: WaypointType):
        self.node = node
        self.waypoint_type = waypoint_type

    @property
    def name(self):
        return self.node.name

    def pos(self):
        return self.node.pos

class TrafficDirector(MonitoredClass):
    def __init__(self, graph: Graph, agentTracker: IAgentTracker, resource_lock_provider: ResourceLock, graph_scale: Vector2 = None):
        MonitoredClass.__init__(self)
        self._agentTracker = agentTracker
        self._intersectionHub = IntersectionHub()
        self._registered_destinations = {}
        self._agent_paths = {}
        self._agent_waypoints = {}
        self._nodeLock = resource_lock_provider
        self.blockers = {}
        self.recalculation_eligibles = set()

        self._graph = None
        self._graph_scale = None
        self._graph_validator = None
        self.set_graph(graph, graph_scale)

        self.jog_attempts = {}
        self.recalculation_attempts = {}

        self.total_time = 0

    @MonitoredClass.timer
    def traffic_director_main_update(self, time_delta_ms: int, seconds_to_reserve: int = 3, recalculation_interval_ms: int = 2000, recalculate_path_at_every_node: bool = True):
        """"""
        self.total_time += time_delta_ms

        ''' Get updated agent Positions'''
        agent_updates = self._agentTracker.get_agent_status()

        ret = {}
        for agent_name in agent_updates.keys():

            self.blockers[agent_name] = set()

            '''
            Steps needed to perform:
            0. Check for any un-submitted destinations and attempt to add
            1. Perform Reservations: Do first as not to override other operations that may perform un-reserves
            2. Handle Arrivals at nodes. Should result in update to agent current nodes and reservations of old nodes
            3. Recalculate Paths. any agent that is marked as recalculation eligible should have a new path calculated
            4. Jog. Identify any agents that are mutually conflicting and jog one to escape deadlock. Relies on paths becoming un-reserved so dont do prior to reserving
            '''

            '''Check for any un-submitted destinations and attempt to add'''
            if self._registered_destinations.get(agent_name, None) is not None:
                open_registered_dest = next((register for id, register in self._registered_destinations[agent_name].items() if register.submitted == 0), None)
                if open_registered_dest:
                    blockers = self._find_and_add_path_to_registered_destination(open_registered_dest)
                    self.blockers[agent_name] = self.blockers[agent_name].union(blockers)


            ''' Perform Reservations'''
            meters_to_reserve = (self._agentTracker.agents[agent_name].current_velocity).length() * seconds_to_reserve
            blockers = self._reserve_nodes_for_agent(agent_name, meters_to_reserve)
            self.blockers[agent_name] = self.blockers[agent_name].union(blockers)

            ''' Handle agent arrivals at nodes'''
            reached_registered_destination = None
            if agent_updates[agent_name].reached_waypoint is True:
               reached_registered_destination = self._handle_reached_pos(self._agent_space_to_node_space(agent_updates[agent_name].pos), agent_name, recalculate_on_arrival=recalculate_path_at_every_node)

            ''' Recalculate Paths'''
            if agent_name in self.recalculation_eligibles:
                self._recalculate_path(agent_name, recalculation_interval_ms)
                self.recalculation_eligibles.discard(agent_name)

            ''' Check and handle any block conditions'''
            # self._deb_validate_graph_dict_didnt_change()

            '''If blocked and has a list of agent_paths'''
            if len(self.blockers[agent_name]) > 0 and self._agent_paths.get(agent_name, None) is not None:
                jog_node = self._handle_blockers(agent_name, graph=self._graph, agent_waypoints=self._agent_paths, block_status=self.blockers, jog_attempts=self.jog_attempts)
                if jog_node is not None:
                    self.jog_attempts[agent_name].add(jog_node)
            else:
                self.jog_attempts[agent_name] = set()

            ''' Set return value for current agent'''
            run_loop_results = TrafficDirectorRunLoopResults()
            run_loop_results.agent_position = self._agentTracker.agents[agent_name].pos
            run_loop_results.completed_registered_destination = reached_registered_destination
            run_loop_results.open_destinations = [x for agent, x in self._registered_destinations.get(agent_name, {}).items() if x.reached == 0]
            ret[agent_name] = run_loop_results
            # ret[agent_name] = (self._agentTracker.agents[agent_name].pos, reached_registered_destination)


            # self._deb_validate_graph_dict_didnt_change()

        # self._deb_validate_agents_dont_share_pos()
        # self._deb_validate_agent_paths_match_agent_tracking()

        return ret

    @property
    def graph_representation(self):
        return self._graph.copy() #Graph(self._graph._graph_dict)

    @MonitoredClass.timer
    def set_graph(self, graph: Graph, graph_scale: Vector2 = None):
        self._graph = graph
        if graph_scale is None:
            graph_scale = Vector2(1, 1)
        self._graph_scale = graph_scale
        self._graph_validator = copy.deepcopy(self._graph._graph_dict)

    @MonitoredClass.timer
    def add_or_append_intersection(self, name: str, nodes: List[Node]):
        self._intersectionHub.add_or_append_intersection(name=name, nodes=nodes)

    @MonitoredClass.timer
    def remove_from_intersection(self, name: str, nodes: List[Node]):
        return self._intersectionHub.remove_from_intersection(name, nodes)

    @MonitoredClass.timer
    def register_intersection(self, intersection: Intersection):
        self._intersectionHub.set_intersection(intersection)

    @MonitoredClass.timer
    def remove_intersection(self, intersection: Intersection):
        self._intersectionHub.remove_intersection(intersection)

    @MonitoredClass.timer
    def nodes_in_intersections(self, intersection_names: List[str] = None):
        return self._intersectionHub.nodes_in_intersection(intersection_names)

    @MonitoredClass.timer
    def intersections_by_node(self, node: Node):
        return self._intersectionHub.intersections_by_node(node_name=node.name)

    @MonitoredClass.timer
    def add_agent(self, name: str, pos: Vector2, max_velo: int = 5, max_accel: int = 5):
        self._agentTracker.build_and_add_agent(name, pos, max_speed=max_velo, max_accel=max_accel)

        ''' Handle if agent isnt entered on the graph (move to nearest)'''
        nodes = self._graph.nodes_at_point(pos)
        if nodes is None or len(nodes) == 0:
            closest_node = self._graph.closest_nodes(pos)[0]
            self._add_path_to_agent(name, [closest_node])

    @MonitoredClass.timer
    def _reserve_nodes_for_agent(self, agent_name: str, reservation_length_threshold: float) -> Set[str]:
        projected_length = 0
        last_agent_pos = None
        ii = 0

        blockers = set()

        # self.blockers[agent_name] = None

        for ii in range(0, len(self._agent_paths.get(agent_name, []))):
            node = self._agent_paths[agent_name][ii]

            if ii == 0:
                last_agent_pos = self._agentTracker.agents[agent_name].pos
            else:
                projected_length += self._node_space_to_agent_space(node.pos).distance_from(last_agent_pos)
                last_agent_pos = self._node_space_to_agent_space(node.pos)

            ''' Continue if already reserved (most likely done in previous iteration)'''
            if self._nodeLock.check_if_reserved(node.name, agent_name):
                continue

            '''Break if reached the reservation threshold. Must attempt to reserve at least one segment'''
            if projected_length > reservation_length_threshold and ii > 1:
                break

            ''' Check if node is part of any intersections'''
            if len(self._intersectionHub.intersections_by_node(node_name=node.name)) > 0:
                ''' Check if a full path can be reserved across all applicable intersections, if not break'''
                if not self._check_if_node_is_reservable_across_intersections(self._agent_paths[agent_name][ii:], agent_name):
                    break
            else:
                '''Try to reserve'''
                reserve = self._reserve_node(node, agent_name)

                '''Mark blocker if fail to reserve'''
                if not reserve:
                    blocker = self._nodeLock.check_for_lock(node.name)
                    blockers.add(blocker) if blocker else None
                    # self.blockers[agent_name] = blocker
                    break

            ii += 1

        logging.debug(f"Reserving Segments for: {agent_name} --> {self._nodeLock.get_active_reservations()}")



        dest = self.get_next_destination(agent_name)
        if dest is None:
            return blockers

        dest_check = self._nodeLock.check_for_lock(dest.name)

        ''' if only able to reserve a single space (current space), and dest is open or locked for this agent, decide to recalculate path'''
        if ii == 0 and (dest_check is None or dest_check == agent_name):
            self.recalculation_eligibles.add(agent_name)

        return blockers

    @MonitoredClass.timer
    def _check_if_node_is_reservable_across_intersections(self, path: List[Node], agent_name: str):
        reservable = True
        soft_reserved = []
        active_intersections = set()

        ''' For each node in the path'''
        ii = 0
        while ii < len(path) and reservable:
            node = path[ii]
            ''' Gather the intersections this node is a part of'''
            intersections = self._intersectionHub.intersections_by_node(node.name)

            ''' Update active intersections to be inclusive of any new intersections provided by the new node (if no new intersections, break)'''
            if len(active_intersections) == 0 or len(active_intersections.intersection(intersections)) > 0:
                active_intersections.update(intersections)

                ''' Check the reservation status of the node'''
                reserved = self._nodeLock.check_for_lock(node.name)

                ''' if the node is locked but it is for a different agent, the node ii is not reservable'''
                if reserved is not None and reserved != agent_name:
                    reservable = False
                elif reserved is None:
                    self._nodeLock.reserve_resource(node.name, f"SOFT_{agent_name}")
                    soft_reserved.append(node.name)
            else:
                break

            ii += 1

        ''' Remove all soft reservations'''
        for node_name in soft_reserved:
            self._nodeLock.check_and_unreserve(node_name, f"SOFT_{agent_name}")

        ''' Hard reserve all reservation if full soft reservation was accomplished'''
        if reservable:
            for node_name in soft_reserved:
                self._nodeLock.reserve_resource(node_name, agent_name)

        return reservable

    @MonitoredClass.timer
    def _unreserve_node(self, node: Node, agent_name):
        unreserve = self._nodeLock.check_and_unreserve(node.name, agent_name)
        if unreserve:
            self._graph.enable_edges_to_node(node, agent_name)


        logging.info(f"Agent: {agent_name} unreserved node: {node} -- {unreserve}")
        return unreserve

    @MonitoredClass.timer
    def _reserve_node(self, node: Node, agent_name):
        reserve = self._nodeLock.check_and_reserve(node.name, agent_name)
        if reserve:
            self._graph.disable_edges_to_node(node, agent_name)

        return reserve

    @MonitoredClass.timer
    def register_new_agent_destination(self, agent_name: str, destination_node: Node, task_id: str):

        self._registered_destinations.setdefault(agent_name, {})[task_id] = RegisteredDestination(task_id, agent_name, destination_node, 0)

        blockers = self._find_and_add_path_to_registered_destination(self._registered_destinations[agent_name][task_id])
        #
        # if len(self._agent_paths.get(agent_name, [])) > 0:
        #     start = self._agent_paths[agent_name][-1]
        # else:
        #     start = self._graph.nodes_at_point(self._agent_space_to_node_space(self._agentTracker.agents[agent_name].pos))[0]
        #
        # path = None
        # if start:
        #     path = self._find_path(agent_name, start, destination_node)
        #
        # ''' If cant find a path, still register the new goal'''
        # #TODO: How to ensure that agent wont move to this waypoint without a path
        # if path is None:
        #     return
        #     # path = [destination_node]
        #
        #
        # ''' If this is not the first path, dont include the start position'''
        # if len(self._agent_paths[agent_name]) > 1:
        #     path = path[1:]
        #
        # self._add_path_to_agent(agent_name, path, path_id=task_id)

        if len(blockers) == 0:
            logging.info(f"new destination registered for agent: {agent_name} to {destination_node}")
        else:
            logging.info(f"destination registered, but no path found for: {agent_name} to {destination_node}")

    @MonitoredClass.timer
    def _find_and_add_path_to_registered_destination(self, registered_destination: RegisteredDestination) -> Set[str]:
        if len(self._agent_paths.get(registered_destination.agent_name, [])) > 0:
            start = self._agent_paths[registered_destination.agent_name][-1]
        else:
            start = self._graph.nodes_at_point(self._agent_space_to_node_space(self._agentTracker.agents[registered_destination.agent_name].pos))[0]

        path = None
        if start:
            path = self._find_path(registered_destination.agent_name, start, registered_destination.destination_node)

        blockers = set()
        if path is None:
            blocked_path = self._find_path(registered_destination.agent_name, start, registered_destination.destination_node, honor_disablers=False)
            blocking_agents = []
            for node in blocked_path:
                reservation = self._nodeLock.check_for_lock(node.name)
                blocking_agents.append(reservation) if reservation else None

            # agent_blocking = self._nodeLock.check_for_lock(registered_destination.destination_node.name)

            adjacents = self._graph.adjacent_nodes(self._agent_paths[registered_destination.agent_name][0], only_enabled=False,
                                             ignored_disablers={registered_destination.agent_name})
            immediate_blockers = [self._nodeLock.check_for_lock(node.name) for node in adjacents]
            immediate_blockers = [x for x in immediate_blockers if x and x != registered_destination.agent_name]

            blockers = set(immediate_blockers + blocking_agents)

            # agent_blocking = self.agent_at_node(registered_destination.destination_node)
            # return blockers
            path = blocked_path

        ''' If this is not the first path, dont include the start position'''
        if len(self._agent_paths.get(registered_destination.agent_name, [])) > 1:
            path = path[1:]

        self._add_path_to_agent(registered_destination.agent_name, path, path_id=registered_destination.task_id)
        self._registered_destinations[registered_destination.agent_name][registered_destination.task_id].submitted = 1
        return blockers

    @MonitoredClass.timer
    def _find_path(self, agent_name: str, start_node: Node, end_node: Node, honor_disablers: bool = True) -> List[Node]:
        """:return"""

        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG
        # reservation_snapshot = self.current_reservations()
        # graph_enabled_state = self._graph.edges()
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG

        # logging.debug("Performing _enablenodes_findpath_disablenodes()")

        '''unreserve all edges currently disabled for usage by this agent'''
        # enabled = [
        # for ii in range(0, len(self._agent_paths.get(agent_name, []))):
        #     node = self._agent_paths[agent_name][ii]
        #     for edge in self._graph.edges_to_node(node):
        #         if agent_name in edge.disablers():
        #             edge.remove_disabler(agent_name)
        #             enabled.append(edge)

        # logging.debug(f"nodes unreserved during _enablenodes_findpath_disablenodes(): {enabled}")

        '''Get Path'''
        astar = self._get_path(start_node, end_node, agent_name, honor_disablers=honor_disablers)

        '''Re-reserve agent segments'''
        # for edge in enabled:
        #     edge.add_disabler(agent_name)


        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG
        # self._deb_verify_reservation_snapshots(reservation_snapshot)
        # self._deb_verify_graph_config(graph_enabled_state)
        # self._deb_agent_at_unreserved_node()
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG

        return astar

    @MonitoredClass.timer
    def _get_path(self, start_node: Node, end_node: Node, agent: str, honor_disablers: bool = True) -> List[Node]:
        if not (start_node and end_node):
            raise Exception(f"{start_node}{end_node}")


        if not honor_disablers:
            ignored_disablers = [agent for agent in self._agentTracker.agents.keys()]
        else:
            ignored_disablers = [agent]

        astar = self._graph.astar(start_node, end_node, ignored_disablers=ignored_disablers)
        logging.debug(f"Calculating a path"
                      f"\n\tStart Node Position: {start_node.pos}"
                      f"\n\tEnd Node Postion: {end_node.pos}"
                      f"\n\tResult: {astar}")
        return astar.path

    @MonitoredClass.timer
    def _add_path_to_agent(self, agent_name: str, points: List[Node], index: int = -1, as_destination: bool = True, path_id: str = None):
        if path_id is None:
            path_id = str(uuid4())

        if points:
            # traffic_waypoints = [Waypoint(point, WaypointType.WAYPOINT) for point in points]
            # traffic_waypoints[-1].waypoint_type = WaypointType.DESTINATION
            waypoints = {x.name: self._node_space_to_agent_space(x.pos) for x in points} if points else {}
            self._agent_paths.setdefault(agent_name, [])

            ''' Handle index out of range'''
            if index < 0 or index > len(self._agent_paths[agent_name]):
                self._agent_paths[agent_name] += points
                # self._agent_paths[agent_name] += traffic_waypoints
            else:
                self._agent_paths[agent_name][index:index] = points
                # self._agent_paths[agent_name][index:index] = traffic_waypoints


            self._agentTracker.add_waypoints(agent_name, waypoints, index, path_id, as_destination = as_destination)

    @MonitoredClass.timer
    def _node_space_to_agent_space(self, agent_pos: Vector2) -> Vector2:
        return agent_pos.hadamard_product(self._graph_scale)

    @MonitoredClass.timer
    def _agent_space_to_node_space(self, agent_pos: Vector2):
        return agent_pos.hadamard_division(self._graph_scale, num_digits=None)

    @MonitoredClass.timer
    def _get_deep_block(self, agent_name: str, block_status: Dict[str, Set[str]], checked_vals: Set[str] = None) -> (Set[str], Set[str]):

        if checked_vals is None:
            checked_vals = {agent_name}

        blockers = set(block_status.get(agent_name, []))

        end_of_chain_blockers = {}
        end_of_chain_blockers.setdefault(agent_name, set())

        for blocker in blockers:
            if blocker not in checked_vals:
                checked_vals.add(blocker)
                blocks, checked_vals = self._get_deep_block(blocker, block_status=block_status, checked_vals=checked_vals)
                end_of_chain_blockers[agent_name] = end_of_chain_blockers[agent_name].union(blocks)
            else:
                end_of_chain_blockers[agent_name].add(blocker)

        ret = set()

        if len(end_of_chain_blockers[agent_name]) == 0:
            ret = ret.union([None])
        else:
            for x in end_of_chain_blockers.values():
                ret = ret.union(x)
        return ret, checked_vals

    @MonitoredClass.timer
    def _handle_blockers(self, agent_name: str, graph: Graph, agent_waypoints: Dict[str, List[Node]], block_status: Dict[str, Set[str]], jog_attempts: Dict[str, Set[Node]]) -> Node:

        ''' If agent is on a jog, dont do anything'''
        # if len(jog_attempts.get(agent_name, set())) > 0 and len(self._agent_paths[agent_name]) > 2:
        #     return None

        # if len(jog_attempts.get(agent_name, set())) > 0 and len(self._agent_paths[agent_name]) >= 2 and any(attempt in self._agent_paths[agent_name][0:1] for attempt in jog_attempts[agent_name]):
        #     return None


        ''' Find end of blocked chain for this agent (either None, some other agent, or this agent if loop)'''
        blockers, checked = self._get_deep_block(agent_name, block_status=block_status)

        # if any(len(self.jog_attempts.get(agent, set())) > 0 for agent in checked):
        #     return None


        '''
        If statement description
            1. # any jog attempts for this agent
            2. # agent currently has at least one next waypoint
            3. # one of the agents that was checked is currently jogging
            
        **Want to return early if all of the above are true since this cummulatively means that the agent is currently jogging 
        '''
        # if any(len(jog_attempts.get(agent_name, set())) > 0 \
        #        and len(self._agent_paths[agent_name]) >= 2 \
        #        and
        '''Return early if any agents that were checked in blockers chain are currently jogging'''
        at_or_almost = lambda attempt, agent: attempt in self._agent_paths[agent][0:1]
        if any(any(at_or_almost(attempt, agent) for attempt in jog_attempts.get(agent, []))for agent in checked):
            return None

        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG
        # self._deb_agent_at_unreserved_node()
        # self._deb_validate_graph_dict_didnt_change()
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG


        '''Switch to decide how/when to jog an agent:
            1. Jog agent if it is the end of the blocked chain and the next waypoint is the destination
            2. Do nothing if the agent is currently jogging
            2. if there is no blocker or end blocker is a different agent
                (assumes jog check has already been performed), reset jog_attempts and return
            3. Unknown Situation, raise error
        '''

        if all(x == agent_name for x in blockers):
            jog_node = self._jog_agent(agent_name, graph, agent_waypoints[agent_name], jog_attempts.get(agent_name, []))
            return jog_node
        elif all(x is None for x in blockers):
            jog_attempts[agent_name] = set()
        else:
            return None

        # if blocker == agent_name and len(agent_waypoints[blocker]) == 2:
        #     jog_node = self._jog_agent(agent_name, graph, agent_waypoints[agent_name], jog_attempts[agent_name])
        #
        #     return jog_node
        # else:
        #     # self.jog_attempts[agent_name] = set()
        #     return None

    @MonitoredClass.timer
    def _jog_agent(self, agent_name, graph: Graph, agent_waypoints: List[Node], agent_jog_attempts: Set[Node]) -> Node:
        current_occupied_waypoint = agent_waypoints[0]
        blocked_segment = agent_waypoints[1] if len(agent_waypoints) > 1 else current_occupied_waypoint

        adjacents = graph.adjacent_nodes(current_occupied_waypoint, only_enabled=True, ignored_disablers={agent_name})

        if len(adjacents) == 0 or adjacents is None:
            logging.debug(f"Jog insertion fail for agent {agent_name}. No adjacent nodes found")
            return None

        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG
        self._deb_validate_graph_dict_didnt_change()
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG

        ''' Choose which node to "jog" to'''
        # adj_index = None
        jog_node = None
        # for ii in range(0, len(adjacents)):
        for node in adjacents:
            ''' If adjacent is the one thats blocked or if jog direction has been attempted dont choose'''
            if (self._node_space_to_agent_space(node.pos) == blocked_segment.pos) \
                or node in agent_jog_attempts:
            # if (self._node_space_to_agent_space(adjacents[0].pos) == blocked_segment.pos) \
            #     or (ii in self.jog_attempts.get(agent_name, set())):
                continue
            else:
                jog_node = node
                # adj_index = ii
                break

        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG
        self._deb_validate_graph_dict_didnt_change()
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG

        if jog_node is None:
            logging.debug(f"Jog insertion fail for agent {agent_name}. No appropriate direction found to jog in")
            return None

        ''' Reset Reservations
                Need to do full un-reservation followed by reserving current waypoint because future waypoints might 
                be equivelant. Dont want to accidentally un-reserve the current node by naievely unreserving indexes x+
        '''
        self._unreserve_all_waypoints(agent_name=agent_name)
        reserved_successfully = self._reserve_node(current_occupied_waypoint, agent_name=agent_name)

        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG
        self._deb_validate_graph_dict_didnt_change()
        self._deb_agent_at_unreserved_node()
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG

        ''' Register jog movement'''
        # new_jog_attempt = jog
        # self.jog_attempts.setdefault(agent_name, set()).add(jog_node)
        self._add_path_to_agent(agent_name, [jog_node, current_occupied_waypoint], index=1, as_destination=False, path_id="jog")

        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG
        self._deb_validate_graph_dict_didnt_change()
        self._deb_agent_at_unreserved_node()
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG
        
        logging.info(f"Jog insertion success for agent {agent_name} inserting a movement to {jog_node}")
        return jog_node

    @MonitoredClass.timer
    def _handle_reached_pos(self, pos: Vector2, agent_name: str, recalculate_on_arrival: bool = False):

        '''Handle Position Switch:
            1. do nothing unless there is at least one entry in agent_path (init)
            2. if agent_position is the next position and the next position is not the current position (happy path)
                -> unreserve current, update
            3. if agent_pos is next position, but next position is current position (duplicate entries)
                -> update without unreserving
            '''

        if len(self._agent_paths.get(agent_name, [])) <= 1:
            pass
        elif self._agent_paths[agent_name][1].pos == pos and pos != self._agent_paths[agent_name][0].pos:
            ''' Unreserve the node i just came from'''
            self._unreserve_node(self._agent_paths[agent_name][0], agent_name)
            ''' Remove the old node from the queue'''
            self._agent_paths[agent_name].pop(0)
            ''' Verify reservation of the new current node'''
            self._reserve_node(self._agent_paths[agent_name][0], agent_name)
        elif self._agent_paths[agent_name][1].pos == pos:
            self._agent_paths[agent_name].pop(0)


        ''' Re-calculate path for agent'''
        if recalculate_on_arrival:
            self.recalculation_eligibles.add(agent_name)

        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG
        # self._deb_agent_at_unreserved_node()
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG


        ''' Return'''
        open_destination = None
        if self._registered_destinations.get(agent_name, None) is not None:
            open_destination = next((register for task, register in self._registered_destinations[agent_name].items() if register.reached == 0 and register.submitted == 1 and pos == register.destination_node.pos), None)
        if open_destination:
            open_destination.reached = 1
            return open_destination
        else:
            return None

    @MonitoredClass.timer
    def _unreserve_all_waypoints(self, agent_name: str):
        for ii in range(0, len(self._agent_paths[agent_name])):
            waypoint = self._agent_paths[agent_name][ii]

            self._unreserve_node(waypoint, agent_name)

    @MonitoredClass.timer
    def _recalculate_path(self, agent_name: str, recalculation_interval_ms: int):
        '''Find the current destination'''
        destination_node = self.get_next_destination(agent_name)
        if not destination_node:
            return

        last_attempt = self.recalculation_attempts.get(agent_name, None)
        if last_attempt is not None and self.total_time - last_attempt < recalculation_interval_ms:
            return

        agent_path = self._agent_paths[agent_name]

        logging.debug(agent_path)
        logging.debug(f"Attempting to find a new path for agent: {agent_name} to destination: {destination_node}")

        '''Create path from agents next completed segment to destination. Decide if we will calculate a path from the 
        node where the agent currently is, or from the node the agent is on the way to. If the next node is reserved, assume
        that the agent is on the way to that node. Therefore, calculate path from there.'''
        insertion_index = None
        current_pos_node = agent_path[0]
        current_goal_node = agent_path[1]
        if self._nodeLock.check_for_lock(current_goal_node.name) == agent_name:
            start_node = current_goal_node
            insertion_index = 2
        else:
            start_node = current_pos_node
            insertion_index = 1

        path = self._find_path(agent_name, start_node, destination_node)

        logging.debug(f"Path found: {path}")

        ''' If no path is found, a "jog" (go to adjacent node and back to current node). handles a deadlock against another agent where both are at each other's destination'''
        ''' If path is found, delete the old path, and insert the new one into the agent's segment queue'''
        if path is None:
            self.recalculation_attempts[agent_name] = self.total_time
        else:
            '''reset recalculation attempt tracking'''
            if agent_name in self.recalculation_attempts.keys():
                del self.recalculation_attempts[agent_name]

            ''' Unreserve all nodes that have been reserved for this agent'''
            for ii in range(insertion_index, len(agent_path)):
                self._unreserve_node(self._agent_paths[agent_name][ii], agent_name)


            ''' update the agent's node path to be the path up until insertion index'''
            if insertion_index == 1:
                self._agent_paths[agent_name] = [agent_path[0]]
            else:
                self._agent_paths[agent_name] = agent_path[0:1]

            ''' Reset the agent waypoints in traffic and send to the agent tracker'''
            next_dest = self._agentTracker.get_next_destination(agent_name)
            self._agentTracker.clear_waypoints(agent_name=agent_name, last_keep_index=insertion_index-1)
            self._add_path_to_agent(agent_name, path[1:], index=insertion_index, path_id=next_dest.path_id)
            logging.debug(f"New path found for agent {agent_name} to {destination_node}, old deleted and new added")

            logging.debug(self._agent_paths[agent_name])

    @MonitoredClass.timer
    def get_next_destination(self, agent_name: str) -> Node:
        if self._agent_paths.get(agent_name, None) and len(self._agent_paths[agent_name]) > 1:
            destination = self._agent_paths[agent_name][-1]
            return destination
        else:
            return None

    @MonitoredClass.timer
    def reserved_nodes(self):
        return {self._graph.node_by_name(node_name): agent_name for node_name, agent_name in self.current_reservations().items()}

    @MonitoredClass.timer
    def current_reservations(self):
        return self._nodeLock.get_active_reservations()

    @MonitoredClass.timer
    def get_nodes_to_next_destination(self, agent_name: str):
        return self._agent_paths.get(agent_name, None)

    @MonitoredClass.timer
    def agent_current_waypoint(self, agent_name: str):
        if len(self._agent_paths.get(agent_name, [])) > 0:
            return self._agent_paths[agent_name][0]
        else:
            return None

    @MonitoredClass.timer
    def agent_at_node(self, node: Node):
        return next((agent_name for agent_name, waypoints in self._agent_paths.items() if waypoints[0] == node), None)

    def __str__(self):
        return f"nodes: {len(self._graph.nodes())}" \
               f"\nedges: {len(self._graph.edges())}" \
               f"\nagents: {len(self._agentTracker.agents)}" \
               f"\ngraph: {str(self._graph)}"


    #region Debug Methods
    @MonitoredClass.timer
    def _deb_validate_agents_dont_share_pos(self):
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG
        agent_pos = [paths[0].pos if len(paths) > 0 else None for agent, paths in self._agent_paths.items()]

        for ii in range(0, len(agent_pos)):
            for jj in range(ii + 1, len(agent_pos)):
                if agent_pos[ii] is not None and (agent_pos[ii] == agent_pos[jj] != Vector2(0, 0)):
                    print("error: agents share position")
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG

    @MonitoredClass.timer
    def _deb_validate_graph_dict_didnt_change(self):
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG
        if self._graph_validator != self._graph._graph_dict:
            print(self._graph_validator)
            print(self._graph._graph_dict)
            print("error: _graph_dict changed")
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG

    @MonitoredClass.timer
    def _deb_agent_at_unreserved_node(self):
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG
        for agent, paths in self._agent_paths.items():
            if len(paths) == 0:
                continue

            if isinstance(paths[0], list):
                print("Wtf")
            if paths[0].pos != Vector2(0, 0) and self._nodeLock.check_for_lock(paths[0].name) != agent:
                print("error: agent at unreserved location")
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG

    @MonitoredClass.timer
    def _deb_verify_graph_config(self, state):
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG
        if not self._graph.verify_edge_configuration(state):
            bef = ""
            for edge in state:
                bef += "\n" + str(edge) + "\n" + str(edge.disablers())
            after = ""
            for edge in self._graph.edges():
                after += "\n" + str(edge) + "\n" + str(edge.disablers())
            raise Exception(f"Error: Did not correctly recreate edge config state during _enablenodes_findpath_disablenodes()"
                            f"\n\tBefore: {bef}"
                            f"\n\tAfter:  {after}")
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG

    @MonitoredClass.timer
    def _deb_verify_reservation_snapshots(self, reservation_snapshot):
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG
        if reservation_snapshot != self.current_reservations():
            raise Exception(f"Error: Did not correctly recreate lock state during _enablenodes_findpath_disablenodes()"
                            f"\n\tBefore: {reservation_snapshot}"
                            f"\n\tAfter:  {self.current_reservations()}")
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG

    @MonitoredClass.timer
    def _deb_validate_agent_paths_match_agent_tracking(self):
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG
        for agent_name, agent in self._agentTracker.agents.items():
            if len(self._agent_paths[agent_name]) > 0 and len(self._agent_paths[agent_name]) != len(self._agentTracker.agents[agent_name].segments):
                raise Exception(f"The agent paths and tracker has gotten out of sync during update"
                                f"\nAgent: {agent_name}"
                                f"\npaths: {pformat(self._agent_paths[agent_name])}"
                                f"\nagent_waypoints: {pformat(self._agentTracker.agents[agent_name].segments)}")
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG

    #endregion

    @MonitoredClass.timer
    def get_registered_destinations(self) -> Dict[str, List[RegisteredDestination]]:
        ret = {}

        for agent in self._registered_destinations.keys():
            ret[agent] = [dest.copy() for name, dest in self._registered_destinations[agent].items()]

        return ret

    # def current_jogs(self) -> Dict[str, List[Node]]:
    #     return Dict(self.jog_attempts)

    # @property
    # def _agent_paths(self):
    #     return {name: agent.segments for name, agent in self._agentTracker.agents.items()}


if __name__ == "__main__":
    from simulation.agentEmulationHub import AgentEmulationHub
    from resourceLock import ResourceLock
    rl = ResourceLock()

    a = Node(name='A', pos=Vector2(0, 0))
    b = Node(name='B', pos=Vector2(3, 3))
    c = Node(name='C', pos=Vector2(2, 0))
    d = Node(name='D', pos=Vector2(2, 1))
    e = Node(name='E', pos=Vector2(3, 4))
    f = Node(name='F', pos=Vector2(5, 5))

    g = {a: [d],
         b: [c],
         c: [b, d, e],
         d: [a, c],
         e: [c],
         f: []
         }

    graph = Graph(g)
    edges = graph.edges()
    i1 = Intersection("i1", [a, b, c])
    assert len(i1.nodes()) == 3
    print(i1)

    i2 = Intersection("i2", [d, e, f])
    assert len(i2.nodes()) == 3
    print(i2)

    i1.combine(i2)
    assert len(i1.nodes()) == 6
    print(i1)

    i1.remove(i2)
    assert len(i1.nodes()) == 3
    print(i1)

    at = AgentEmulationHub(rl.check_if_reserved)
    agent1_name = "Coop"
    graph_scale = Vector2(2, 2)
    td = TrafficDirector(graph=graph, agentTracker=at, graph_scale=graph_scale, resource_lock_provider=rl)
    td.add_agent(agent1_name, Vector2(0, 0))
    print(td)

    td.register_new_agent_destination(agent1_name, e, task_id="test")

    print(td._agent_paths)
    print(at.agent_segments)

    time_delta_ms = 100
    print(at.agents)
    at.update_agents(time_delta_ms, 1)
    print(at.agents)

    td.traffic_director_main_update(time_delta_ms)
    i3 = Intersection("i3", [d, c, f])

    td.register_intersection(i3)
    td._nodeLock.reserve_resource(c, "Test")

    print(td.current_reservations())

    cc = 0
    while cc < 100:
        at.update_agents(time_delta_ms, 1)
        print(f"Agents: {at.agents}")
        td.traffic_director_main_update(time_delta_ms)
        print(f"Reservations: {td.current_reservations()}")
        cc += 1

    td._nodeLock.unreserve_resource(c)

    import time
    time.sleep(2)

    cc = 0
    while cc < 100:
        at.update_agents(time_delta_ms, 1)
        print(f"Agents: {at.agents}")
        td.traffic_director_main_update(time_delta_ms)
        print(f"Reservations: {td.current_reservations()}")
        cc += 1






    # at.update_agents(time_delta_ms, 1) # Reach init
    # at.update_agents(time_delta_ms, 1) # Create Pos Accel
    # at.update_agents(time_delta_ms, 1)  # Create Pos Velo
    # at.update_agents(time_delta_ms, 1)  # First Movement
    # print(at.agents)
    #
    #
    # td.traffic_director_main_update(time_delta_ms)
    # print(td.current_reservations())
    # at.update_agents(time_delta_ms, 1) # Create Pos
    # print(at.agents)
    # at.update_agents(time_delta_ms, 1)  # Create Pos Velo
    # print(at.agents)
    # at.update_agents(time_delta_ms, 1)  # First Movement
    # print(at.agents)