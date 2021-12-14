import unittest

import src.day03.part01 as part01
import src.day03.part02 as part02

class TestDay03:
    def test_part01_sample01(self):
        result = part01.get_part_one_result("src/day03/input_sample01.txt")
        assert result == 198

    def test_part01(self):
        result = part01.get_part_one_result("src/day03/input.txt")
        assert result == 693486

    def test_part02_sample01(self):
        result = part02.get_part_two_result("src/day03/input_sample01.txt")
        assert result == 230

    def test_part02(self):
        result = part02.get_part_two_result("src/day03/input.txt")
        assert result == 3379326
