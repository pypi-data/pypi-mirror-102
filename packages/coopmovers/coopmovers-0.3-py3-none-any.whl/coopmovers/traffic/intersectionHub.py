from coopmovers.traffic.intersection import Intersection
from coopgraph.graphs import Node
from typing import List

class IntersectionHub:
    def __init__(self):
        self._intersections = {}
        self._node_intersection_map = {}

    def add_or_append_intersection(self, name: str, nodes: List[Node]):
        if name in self._intersections.keys():
            new_intersection = Intersection("dummy", node_list=nodes)
            self._intersections[name].combine(new_intersection)
        else:
            self._intersections[name] = Intersection(name, node_list=nodes)
        self._build_maps()

    def remove_from_intersection(self, name: str, nodes: List[Node]):
        if name not in self._intersections.keys():
            return

        cut = Intersection("dummy", node_list=nodes)
        self._intersections[name].remove(cut)
        self._build_maps()

    def set_intersection(self, intersection: Intersection):
        self._intersections[intersection.name] = intersection
        self._build_maps()

    def remove_intersection(self, intersection: Intersection):
        if intersection.name in self._intersections.keys():
            del self._intersections[intersection.name]
        self._build_maps()

    def _build_maps(self):
        self._build_node_intersection_map()

    def _build_node_intersection_map(self):
        self._node_intersection_map.clear()

        for name, intersection in self._intersections.items():
            for node in intersection.nodes():
                self._node_intersection_map.setdefault(node.name, []).append(intersection.name)

    def intersections_by_node(self, node_name: str):
        return [intersection for i_name, intersection in self._intersections.items() if i_name in self._node_intersection_map.get(node_name, [])]

    def nodes_in_intersection(self, intersection_list: List[str] = None):
        if intersection_list is None:
            intersection_list = self._intersections.keys()

        nodes = set()

        for intersection in intersection_list:
            nodes.update(set(self._intersections[intersection].nodes()))

        return list(nodes)

