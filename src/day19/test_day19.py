import pytest

from src.day19.part01 import get_part_one_result


class TestDay17:
    def test_part01_sample01(self):
        result = get_part_one_result("src/day19/input_sample01.txt")
        assert result == 79

    @pytest.mark.skip("long-running test")
    def test_part01(self):
        result = get_part_one_result("src/day19/input.txt")
        assert result == 367
