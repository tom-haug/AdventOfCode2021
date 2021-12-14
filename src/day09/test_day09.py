from src.day09.part01 import get_part_one_result
from src.day09.part02 import get_part_two_result


class TestDay09:
    def test_part01_sample01(self):
        result = get_part_one_result("src/day09/input_sample01.txt")
        assert result == 15

    def test_part01(self):
        result = get_part_one_result("src/day09/input.txt")
        assert result == 504

    def test_part02_sample01(self):
        result = get_part_two_result("src/day09/input_sample01.txt")
        assert result == 1134

    def test_part02(self):
        result = get_part_two_result("src/day09/input.txt")
        assert result == 1558722
