from src.day16.part01 import get_part_one_result


class TestDay16:
    def test_part01_sample01(self):
        result = get_part_one_result("src/day16/input_sample01.txt")
        assert result == 16

    def test_part01_sample02(self):
        result = get_part_one_result("src/day16/input_sample02.txt")
        assert result == 12

    def test_part01_sample03(self):
        result = get_part_one_result("src/day16/input_sample03.txt")
        assert result == 23

    def test_part01_sample04(self):
        result = get_part_one_result("src/day16/input_sample04.txt")
        assert result == 31

    def test_part01(self):
        result = get_part_one_result("src/day16/input.txt")
        assert result == 860
