import pytest

from src.day07.part01 import get_part_one_result
from src.day07.part02 import get_part_two_result


class TestDay07:
    def test_part01_sample01(self):
        result = get_part_one_result("src/day07/input_sample01.txt")
        assert result == 37

    def test_part01(self):
        result = get_part_one_result("src/day07/input.txt")
        assert result == 333755

    def test_part02_sample02(self):
        result = get_part_two_result("src/day07/input_sample01.txt")
        assert result == 168

    @pytest.mark.skip("long-running test")
    def test_part02(self):
        result = get_part_two_result("src/day07/input.txt")
        assert result == 94017638
