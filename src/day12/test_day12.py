import pytest

from src.day12.part01 import get_part_one_result
from src.day12.part02 import get_part_two_result


class TestDay12:
    def test_part01_sample01(self):
        result = get_part_one_result("src/day12/input_sample01.txt")
        assert result == 10

    def test_part01_sample02(self):
        result = get_part_one_result("src/day12/input_sample02.txt")
        assert result == 19

    def test_part01_sample03(self):
        result = get_part_one_result("src/day12/input_sample03.txt")
        assert result == 226

    def test_part01(self):
        result = get_part_one_result("src/day12/input.txt")
        assert result == 3230

    def test_part02_sample01(self):
        result = get_part_two_result("src/day12/input_sample01.txt")
        assert result == 36

    def test_part02_sample02(self):
        result = get_part_two_result("src/day12/input_sample02.txt")
        assert result == 103

    def test_part02_sample03(self):
        result = get_part_two_result("src/day12/input_sample03.txt")
        assert result == 3509

    @pytest.mark.skip("src/day12/long-running test")
    def test_part02(self):
        result = get_part_two_result("src/day12/input.txt")
        assert result == 83475
