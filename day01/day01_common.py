def count_increasing_items(items: list[int]) -> int:
    total = 0
    for idx in range(1, len(items)):
        if items[idx] > items[idx - 1]:
            total += 1
    return total


def reduce_three_measurement_sum(items: list[int]) -> list[int]:
    result_list: list[int] = []
    for idx in range(0, len(items) - 2):
        result_list.append(items[idx] + items[idx + 1] + items[idx + 2])
    return result_list