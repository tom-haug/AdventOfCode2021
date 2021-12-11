import unittest

from src.day09.day09_part01 import get_part_one_result
from src.day09.day09_part02 import get_part_two_result


class TestDay95(unittest.TestCase):
    def test_part01_sample01(self):
        result = get_part_one_result("input_sample01.txt")
        self.assertEqual(result, 15)

    def test_part01(self):
        result = get_part_one_result("input.txt")
        self.assertEqual(result, 504)

    def test_part02_sample01(self):
        result = get_part_two_result("input_sample01.txt")
        self.assertEqual(result, 1134)

    def test_part02(self):
        result = get_part_two_result("input.txt")
        self.assertEqual(result, 1558722)

if __name__ == "__main__":
    unittest.main()
