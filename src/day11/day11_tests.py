import unittest

from src.day11.day11_part01 import get_part_one_result


class TestDay11(unittest.TestCase):
    def test_part01_sample01(self):
        result = get_part_one_result("input_sample01.txt", 100)
        self.assertEqual(result, 1656)

    def test_part01(self):
        result = get_part_one_result("input.txt", 100)
        self.assertEqual(result, 1613)


if __name__ == "__main__":
    unittest.main()
