from src.day08.part01 import get_part_one_result
from src.day08.part02 import get_part_two_result


class TestDay08:
    def test_part01_sample01(self):
        result = get_part_one_result("src/day08/input_sample01.txt")
        assert result == 0

    def test_part01_sample02(self):
        result = get_part_one_result("src/day08/input_sample02.txt")
        assert result == 26

    def test_part01(self):
        result = get_part_one_result("src/day08/input.txt")
        assert result == 239

    def test_part02_sample01(self):
        result = get_part_two_result("src/day08/input_sample01.txt")
        assert result == 5353

    def test_part02_sample02(self):
        result = get_part_two_result("src/day08/input_sample02.txt")
        assert result == 61229

    def test_part02(self):
        result = get_part_two_result("src/day08/input.txt")
        assert result == 946346
