import numpy as np
from attr import dataclass


@dataclass
class ImageEnhancementAlgorithm:
    binary_code: list[int]

    def process(self, input_image: np.ndarray, step: int) -> np.ndarray:
        height, width = input_image.shape
        background_alternates = self.binary_code[0] == 1 and self.binary_code[-1] == 0
        background_value = 0 if not background_alternates or step % 2 == 0 else 1
        output_image = np.zeros((height, width), dtype=int)

        for y in range(height):
            for x in range(width):
                code_index = self._get_code_index_for_coordinates(input_image, x, y, background_value)
                output_value = self.binary_code[code_index]
                output_image[y, x] = output_value
        return output_image

    @staticmethod
    def _get_code_index_for_coordinates(image: np.ndarray, desired_x: int, desired_y: int, background_value: int):
        input_height, input_width = image.shape
        output_parts: list[str] = []
        for y in range(desired_y - 1, desired_y + 2):
            if 0 <= y < input_height:
                for x in range(desired_x - 1, desired_x + 2):
                    if 0 <= x < input_width:
                        value = image[y, x]
                        output_parts.append(str(value))
                    else:
                        output_parts.append(str(background_value))
            else:
                output_parts = output_parts + [str(background_value) for x in range(3)]
        value = int("".join(output_parts), 2)
        return value
