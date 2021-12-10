import unittest

from src.day07.day07_part01 import get_part_one_result
from src.day07.day07_part02 import get_part_two_result


class TestDay07(unittest.TestCase):
    def test_part01_sample01(self):
        result = get_part_one_result("input_sample01.txt")
        self.assertEqual(result, 37)

    def test_part01(self):
        result = get_part_one_result("input.txt")
        self.assertEqual(result, 333755)

    def test_part02_sample02(self):
        result = get_part_two_result("input_sample01.txt")
        self.assertEqual(result, 168)

    def test_part02(self):
        result = get_part_two_result("input.txt")
        self.assertEqual(result, 94017638)


if __name__ == "__main__":
    unittest.main()
