import pytest

from src.day15.part01 import get_part_one_result
from src.day15.part02 import get_part_two_result


class TestDay15:
    def test_part01_sample01(self):
        result = get_part_one_result("src/day15/input_sample01.txt")
        assert result == 40

    def test_part01(self):
        result = get_part_one_result("src/day15/input.txt")
        assert result == 595

    def test_part01_sample02(self):
        result = get_part_two_result("src/day15/input_sample01.txt", 5)
        assert result == 315

    @pytest.mark.skip("long-running test")
    def test_part02(self):
        result = get_part_two_result("src/day15/input.txt")
        assert result == 2914