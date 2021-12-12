from src.day12.cave_node import CaveNode
from src.day12.cave_node_path import CaveNodePath
from src.day12.cave_node_system import CaveNodeSystem
from src.day12.processor import Processor


class AllowOneSmallRevisitPath(CaveNodePath):
    def can_visit(self, node: CaveNode):
        if node.is_large_cave:
            return True
        else:
            visited_count = self._visited_cave_count(node)
            has_visited = visited_count > 0
            disallow_revisit = node.disallow_revisit()
            revisited_small_cave_count = self.revisited_small_cave_count()
            if has_visited and disallow_revisit:  # start and end caves
                return False
            elif visited_count > 1 or revisited_small_cave_count > 1:  # can only revisit a small cave once
                return False
            return True


def get_part_two_result(file_name: str) -> int:
    system = CaveNodeSystem(file_name)
    processor = Processor()
    empty_path = AllowOneSmallRevisitPath()
    completed_paths = processor.process(system, empty_path)

    path_str_list = sorted([str(path) for path in completed_paths])
    for path in path_str_list:
        print(path)

    return len(completed_paths)


if __name__ == "__main__":
    result = get_part_two_result("input.txt")
    print(result)
