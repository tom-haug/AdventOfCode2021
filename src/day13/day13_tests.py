import unittest

from src.day13.day13_part01 import get_part_one_result
from src.day13.day13_part02 import get_part_two_result


class TestDay13(unittest.TestCase):
    def test_part01_sample01_one_fold(self):
        result = get_part_one_result("input_sample01.txt", 1)
        self.assertEqual(result, 17)

    def test_part01_sample01_all_folds(self):
        result = get_part_one_result("input_sample01.txt")
        self.assertEqual(result, 16)

    def test_part01(self):
        result = get_part_one_result("input.txt", 1)
        self.assertEqual(result, 765)

    @unittest.skip("nothing to assert, must visually read the letters")
    def test_part02(self):
        sheet = get_part_two_result("input.txt")
        print(sheet)


if __name__ == "__main__":
    unittest.main()
