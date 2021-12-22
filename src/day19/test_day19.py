import pytest

from src.day19.part01 import get_part_one_result
from src.day19.part02 import get_part_two_result


class TestDay17:
    def test_part01_sample01(self):
        result = get_part_one_result("src/day19/input_sample01.txt")
        assert result == 79

    @pytest.mark.skip("long-running test")
    def test_part01(self):
        result = get_part_one_result("src/day19/input.txt")
        assert result == 367

    def test_part02_sample01(self):
        result = get_part_two_result("src/day19/input_sample01.txt")
        assert result == 3621

    @pytest.mark.skip("long-running test")
    def test_part02(self):
        result = get_part_two_result("src/day19/input.txt")
        assert result == 11925
