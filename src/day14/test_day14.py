from src.day14.part01 import get_part_one_result
from src.day14.part02 import get_part_two_result


class TestDay14:
    def test_part01_sample01(self):
        result = get_part_one_result("src/day14/input_sample01.txt", 10)
        assert result == 1588

    def test_part01(self):
        result = get_part_one_result("src/day14/input.txt", 10)
        assert result == 3306

    def test_part02_sample01(self):
        result = get_part_two_result("src/day14/input_sample01.txt", 40)
        assert result == 2188189693529

    def test_part02(self):
        result = get_part_two_result("src/day14/input.txt", 40)
        assert result == 3760312702877
