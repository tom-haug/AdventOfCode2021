from src.day16.part01 import get_part_one_result
from src.day16.part02 import get_part_two_result


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

    def test_part02_sample05(self):
        result = get_part_two_result("src/day16/input_sample05_sum.txt")
        assert result == 3

    def test_part02_sample06(self):
        result = get_part_two_result("src/day16/input_sample06_product.txt")
        assert result == 54

    def test_part02_sample07(self):
        result = get_part_two_result("src/day16/input_sample07_min.txt")
        assert result == 7

    def test_part02_sample08(self):
        result = get_part_two_result("src/day16/input_sample08_max.txt")
        assert result == 9

    def test_part02_sample09(self):
        result = get_part_two_result("src/day16/input_sample09_less_than.txt")
        assert result == 1

    def test_part02_sample10(self):
        result = get_part_two_result("src/day16/input_sample10_greater_than.txt")
        assert result == 0

    def test_part02_sample11(self):
        result = get_part_two_result("src/day16/input_sample11_not_equal.txt")
        assert result == 0

    def test_part02_sample12(self):
        result = get_part_two_result("src/day16/input_sample12_complex.txt")
        assert result == 1

    def test_part02(self):
        result = get_part_two_result("src/day16/input.txt")
        assert result == 470949537659