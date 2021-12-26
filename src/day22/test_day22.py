import pytest

from src.day22.part01 import get_part_one_result
from src.day22.part02 import get_part_two_result


class TestDay20:
    def test_part01_sample01(self):
        result = get_part_one_result("src/day22/input_sample01.txt")
        assert result == 39

    def test_part01_sample02(self):
        result = get_part_one_result("src/day22/input_sample02.txt")
        assert result == 590784

    def test_part01(self):
        result = get_part_one_result("src/day22/input.txt")
        assert result == 588200

    def test_part02_sample03(self):
        result = get_part_two_result("src/day22/input_sample03.txt")
        assert result == 2758514936282235

    @pytest.mark.skip("long-running test")
    def test_part02(self):
        result = get_part_two_result("src/day22/input.txt")
        assert result == 1207167990362099
