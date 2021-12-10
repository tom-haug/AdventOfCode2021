import unittest

from src.day08.day08_part01 import get_part_one_result
from src.day08.day08_part02 import get_part_two_result


class TestDay08(unittest.TestCase):
    def test_part01_sample01(self):
        result = get_part_one_result("input_sample01.txt")
        self.assertEqual(result, 0)

    def test_part01_sample02(self):
        result = get_part_one_result("input_sample02.txt")
        self.assertEqual(result, 26)

    def test_part01(self):
        result = get_part_one_result("input.txt")
        self.assertEqual(result, 239)

    def test_part02_sample01(self):
        result = get_part_two_result("input_sample01.txt")
        self.assertEqual(result, 5353)

    def test_part02_sample02(self):
        result = get_part_two_result("input_sample02.txt")
        self.assertEqual(result, 61229)

    def test_part02(self):
        result = get_part_two_result("input.txt")
        self.assertEqual(result, 946346)


if __name__ == "__main__":
    unittest.main()
