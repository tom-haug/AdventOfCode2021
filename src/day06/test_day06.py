from src.day06.common import get_fish_count_after_days


class TestDay06:
    def test_part01_sample01(self):
        result = get_fish_count_after_days("src/day06/input_sample01.txt", 80)
        assert result == 5934

    def test_part01(self):
        result = get_fish_count_after_days("src/day06/input.txt", 80)
        assert result == 375482

    def test_part02(self):
        result = get_fish_count_after_days("src/day06/input.txt", 256)
        assert result == 1689540415957
