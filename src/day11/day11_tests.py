import unittest

from src.day11.day11_part01 import get_part_one_result
from src.day11.day11_part02 import get_part_two_result


class TestDay11(unittest.TestCase):
    def test_part01_sample01(self):
        result = get_part_one_result("input_sample01.txt", 100)
        self.assertEqual(result, 1656)

    def test_part01(self):
        result = get_part_one_result("input.txt", 100)
        self.assertEqual(result, 1613)

    def test_part02_sample01(self):
        result = get_part_two_result("input_sample01.txt")
        self.assertEqual(result, 195)

    def test_part02(self):
        result = get_part_two_result("input.txt")
        self.assertEqual(result, 510)


if __name__ == "__main__":
    unittest.main()
