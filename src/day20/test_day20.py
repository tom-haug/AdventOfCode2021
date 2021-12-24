import pytest

from src.day20.common import get_image_after_steps


class TestDay20:
    def test_part01_sample01(self):
        image, num_pixels = get_image_after_steps("src/day20/input_sample01.txt", 2, False)
        assert num_pixels == 35

    @pytest.mark.skip("long-running test")
    def test_part01(self):
        image, num_pixels = get_image_after_steps("src/day20/input.txt", 2, False)
        assert num_pixels == 5483

    def test_part02_sample01(self):
        image, num_pixels = get_image_after_steps("src/day20/input_sample01.txt", 50, False)
        assert num_pixels == 3351

    @pytest.mark.skip("long-running test")
    def test_part02(self):
        image, num_pixels = get_image_after_steps("src/day20/input.txt", 50, False)
        assert num_pixels == 18732
