from src.day11.part01 import get_part_one_result
from src.day11.part02 import get_part_two_result


class TestDay11:
    def test_part01_sample01(self):
        result = get_part_one_result("src/day11/input_sample01.txt", 100)
        assert result == 1656

    def test_part01(self):
        result = get_part_one_result("src/day11/input.txt", 100)
        assert result == 1613

    def test_part02_sample01(self):
        result = get_part_two_result("src/day11/input_sample01.txt")
        assert result == 195

    def test_part02(self):
        result = get_part_two_result("src/day11/input.txt")
        assert result == 510
