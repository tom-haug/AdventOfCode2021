from src.day10.part01 import get_part_one_result
from src.day10.part02 import get_part_two_result


class TestDay10:
    def test_part01_sample01(self):
        result = get_part_one_result("src/day10/input_sample01.txt")
        assert result == 26397

    def test_part01(self):
        result = get_part_one_result("src/day10/input.txt")
        assert result == 392421

    def test_part02_sample01(self):
        result = get_part_two_result("src/day10/input_sample01.txt")
        assert result == 288957

    def test_part02(self):
        result = get_part_two_result("src/day10/input.txt")
        assert result == 2769449099
