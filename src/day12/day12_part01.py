from src.day12.cave_node import CaveNode
from src.day12.cave_node_path import CaveNodePath
from src.day12.cave_node_system import CaveNodeSystem
from src.day12.processor import Processor


class NoSmallRevisitPath(CaveNodePath):
    def can_visit(self, node: CaveNode):
        if node.is_large_cave:
            return True
        return self._visited_cave_count(node) == 0


def get_part_one_result(file_name: str) -> int:
    system = CaveNodeSystem(file_name)
    processor = Processor()
    empty_path = NoSmallRevisitPath()
    completed_paths = processor.process(system, empty_path)
    return len(completed_paths)


if __name__ == "__main__":
    result = get_part_one_result("input.txt")
    print(result)
