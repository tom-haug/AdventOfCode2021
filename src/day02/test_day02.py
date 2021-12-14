import src.day02.part01 as part01
import src.day02.part02 as part02


class TestDay02:
    def test_part01_sample01(self):
        result = part01.get_part_one_result("src/day02/input_sample01.txt")
        assert result == 150

    def test_part01(self):
        result = part01.get_part_one_result("src/day02/input.txt")
        assert result == 1962940

    def test_part02_sample01(self):
        result = part02.get_part_two_result("src/day02/input_sample01.txt")
        assert result == 900

    def test_part02(self):
        result = part02.get_part_two_result("src/day02/input.txt")
        assert result == 1813664422

