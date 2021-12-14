import pytest

import src.day05.part01 as part01
import src.day05.part02 as part02


class TestDay05:
    def test_part01_sample01(self):
        result = part01.get_part_one_result("src/day05/input_sample01.txt")
        assert result == 5

    def test_part01(self):
        result = part01.get_part_one_result("src/day05/input.txt")
        assert result == 6225

    def test_part02_sample01(self):
        result = part02.get_part_two_result("src/day05/input_sample01.txt")
        assert result == 12

    @pytest.mark.skip("long-running test")
    def test_part02(self):
        result = part02.get_part_two_result("src/day05/input.txt")
        assert result == 22116
