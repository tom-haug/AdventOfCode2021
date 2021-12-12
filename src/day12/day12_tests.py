import unittest

from src.day12.day12_part01 import get_part_one_result
from src.day12.day12_part02 import get_part_two_result


class TestDay12(unittest.TestCase):
    def test_part01_sample01(self):
        result = get_part_one_result("input_sample01.txt")
        self.assertEqual(result, 10)

    def test_part01_sample02(self):
        result = get_part_one_result("input_sample02.txt")
        self.assertEqual(result, 19)

    def test_part01_sample03(self):
        result = get_part_one_result("input_sample03.txt")
        self.assertEqual(result, 226)

    def test_part01(self):
        result = get_part_one_result("input.txt")
        self.assertEqual(result, 3230)

    def test_part02_sample01(self):
        result = get_part_two_result("input_sample01.txt")
        self.assertEqual(result, 36)

    def test_part02_sample02(self):
        result = get_part_two_result("input_sample02.txt")
        self.assertEqual(result, 103)

    def test_part02_sample03(self):
        result = get_part_two_result("input_sample03.txt")
        self.assertEqual(result, 3509)

    @unittest.skip("long-running test")
    def test_part02(self):
        result = get_part_two_result("input.txt")
        self.assertEqual(result, 83475)


if __name__ == "__main__":
    unittest.main()
