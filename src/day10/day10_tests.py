import unittest

from src.day10.day10_part01 import get_part_one_result


class TestDay95(unittest.TestCase):
    def test_part01_sample01(self):
        result = get_part_one_result("input_sample01.txt")
        self.assertEqual(result, 26397)

    def test_part01(self):
        result = get_part_one_result("input.txt")
        self.assertEqual(result, 392421)


if __name__ == "__main__":
    unittest.main()
