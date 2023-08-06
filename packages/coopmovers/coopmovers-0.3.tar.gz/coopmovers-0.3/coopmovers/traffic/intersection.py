from coopgraph.graphs import Graph, Node
from typing import List

class Intersection():
    def __init__(self, name: str, node_list: List[Node]):
        self._node_list = set(node_list)
        self.name = name

    def add_nodes(self, node: Node):
        self._node_list.add(node)

    def remove_nodes(self, node: Node):
        self._node_list.discard(node)

    def nodes(self):
        return list(self._node_list)

    def combine(self, other):
        if isinstance(other, type(self)):
            self._node_list = other._node_list.union(self._node_list)

    def remove(self, other):
        if isinstance(other, type(self)):
            self._node_list = self._node_list.difference(other._node_list)

    def __str__(self):
        ret = f"Intersection {self.name}: {len(self._node_list)} nodes"
        for node in self._node_list:
            ret += f"\n{node}"
        return ret

    def __eq__(self, other):
        if isinstance(other, Intersection) and other.__str__() == self.__str__():
            return True
        else:
            return False

    def __hash__(self):
        return hash(str(self.name))

if __name__ == "__main__":
    pass