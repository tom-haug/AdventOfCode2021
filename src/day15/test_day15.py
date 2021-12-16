from src.day15.part01 import get_part_one_result


class TestDay15:
    def test_part01_sample01(self):
        result = get_part_one_result("src/day15/input_sample01.txt")
        assert result == 40

    def test_part01(self):
        result = get_part_one_result("src/day15/input.txt")
        assert result == 595
