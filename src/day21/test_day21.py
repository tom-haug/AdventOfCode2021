from src.day21.part01 import get_part_one_result
from src.day21.part02 import get_part_two_result


class TestDay20:
    def test_part01_sample01(self):
        result = get_part_one_result("src/day21/input_sample01.txt")
        assert result == 739785

    def test_part01(self):
        result = get_part_one_result("src/day21/input.txt")
        assert result == 504972

    def test_part02_sample01(self):
        result = get_part_two_result("src/day21/input_sample01.txt")
        assert result == 444356092776315

    def test_part02(self):
        result = get_part_two_result("src/day21/input.txt")
        assert result == 446968027750017
