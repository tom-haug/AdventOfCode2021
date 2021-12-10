import unittest
from day06_common import get_fish_count_after_days


class TestDay06(unittest.TestCase):
    def test_part01_sample01(self):
        result = get_fish_count_after_days("input_sample01.txt", 80)
        self.assertEqual(result, 5934)

    def test_part01(self):
        result = get_fish_count_after_days("input.txt", 80)
        self.assertEqual(result, 375482)

    def test_part02(self):
        result = get_fish_count_after_days("input.txt", 256)
        self.assertEqual(result, 1689540415957)


if __name__ == "__main__":
    unittest.main()
