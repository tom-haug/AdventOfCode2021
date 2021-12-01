import unittest
import day01_part01 as part01

class TestDay01(unittest.TestCase):
    def test_part01_sample01(self):
        items = part01.load_int_list_from_file("input_sample01.txt")
        result = part01.get_part_one_result(items)
        self.assertEqual(result, 7)

    def test_part01(self):
        items = part01.load_int_list_from_file("input.txt")
        result = part01.get_part_one_result(items)
        self.assertEqual(result, 1195)


if __name__ == "__main__":
    unittest.main()