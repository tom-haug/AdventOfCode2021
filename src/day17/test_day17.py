from src.day17.part01 import get_part_one_result
from src.day17.part02 import get_part_two_result


class TestDay17:
    def test_part01_sample01(self):
        result = get_part_one_result("src/day17/input_sample01.txt")
        assert result == 45

    def test_part01(self):
        result = get_part_one_result("src/day17/input.txt")
        assert result == 5253

    def test_part02_sample01(self):
        result = get_part_two_result("src/day17/input_sample01.txt")
        assert result == 112

    def test_part02(self):
        result = get_part_two_result("src/day17/input.txt")
        assert result == 1770
