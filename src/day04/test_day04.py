import src.day04.part01 as part01
import src.day04.part02 as part02


class TestDay04:
    def test_part01_sample01(self):
        result = part01.get_part_one_result("src/day04/input_sample01.txt")
        assert result == 4512

    def test_part01(self):
        result = part01.get_part_one_result("src/day04/input.txt")
        assert result == 25410

    def test_part02_sample01(self):
        result = part02.get_part_two_result("src/day04/input_sample01.txt")
        assert result == 1924

    def test_part02(self):
        result = part02.get_part_two_result("src/day04/input.txt")
        assert result == 2730
