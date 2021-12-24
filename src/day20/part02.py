from __future__ import annotations
import time
from src.day20.common import get_image_after_steps


if __name__ == "__main__":
    start = time.time()
    image, result = get_image_after_steps("src/day20/input.txt", 50, False)
    end = time.time()

    print(f"Running Time: {end - start}")
    print(f"Result: {result}")
