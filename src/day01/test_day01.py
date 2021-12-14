import src.day01.part01 as part01
import src.day01.part02 as part02


class TestDay01:
    def test_part01_sample01(self):
        result = part01.get_part_one_result("src/day01/input_sample01.txt")
        assert result == 7

    def test_part01(self):
        result = part01.get_part_one_result("src/day01/input.txt")
        assert result == 1195

    def test_part02_sample01(self):
        result = part02.get_part_two_result("src/day01/input_sample01.txt")
        assert result == 5

    def test_part02(self):
        result = part02.get_part_two_result("src/day01/input.txt")
        assert result == 1235
