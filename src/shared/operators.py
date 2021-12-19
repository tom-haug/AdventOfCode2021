def bitwise_not(number, num_bits):
    return (1 << num_bits) - 1 - number


def middle_item(items: list) -> int:
    length = len(items)
    if length % 2 == 0:
        raise Exception("cannot get middle item for an even number of items")
    middle_index = int((length - 1) / 2)
    return items[middle_index]


