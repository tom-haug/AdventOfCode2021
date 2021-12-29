from src.day23.walkable_location import WalkableLocation
from src.shared import LinkedNode


class FloorMap(dict[WalkableLocation, LinkedNode]):
    def append(self, location: WalkableLocation):
        new_node = LinkedNode(str(location))
        self[location] = new_node

        # link up adjacent floor segments
        for other_location, other_node in self.items():
            if other_location.adjacent_to(location):
                other_node.linked_nodes.append(new_node)
                new_node.linked_nodes.append(other_node)

    def get_location(self, node: LinkedNode) -> WalkableLocation:
        for key, value in self.items():
            if value == node:
                return key
