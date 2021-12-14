import pytest

from src.day13.part01 import get_part_one_result
from src.day13.part02 import get_part_two_result


class TestDay13:
    def test_part01_sample01_one_fold(self):
        result = get_part_one_result("src/day13/input_sample01.txt", 1)
        assert result == 17

    def test_part01_sample01_all_folds(self):
        result = get_part_one_result("src/day13/input_sample01.txt")
        assert result == 16

    def test_part01(self):
        result = get_part_one_result("src/day13/input.txt", 1)
        assert result == 765

    @pytest.mark.skip("nothing to assert, must visually read the letters")
    def test_part02(self):
        sheet = get_part_two_result("src/day13/input.txt")
        print(sheet)

