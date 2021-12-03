import sys
sys.path.append("..")
from shared.utils import load_text_file


def get_part_one_result(file_name: str):
    lines = load_text_file(file_name)
    num_digits = len(lines[0])
    gamma_parts = ["0" for _ in range(num_digits)]

    for position in range(num_digits):
        num_ones = 0
        for line in lines:
            if line[position] == "1":
                num_ones += 1
        if num_ones > len(lines) / 2:
            gamma_parts[position] = "1"

    gamma_value = int(''.join(gamma_parts), 2)
    epsilon_value = bitwise_not(gamma_value, num_digits)

    result = gamma_value * epsilon_value
    return result


def bitwise_not(n, numbits=8):
    return (1 << numbits) - 1 - n


if __name__ == "__main__":
    result = get_part_one_result("input.txt")
    print(result)