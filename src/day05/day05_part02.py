from src.day05.vent_map import VentMap


def get_part_two_result(file_name: str):
    vent_map = VentMap(file_name, True)
    return vent_map.get_dangerous_vent_count()


if __name__ == "__main__":
    result = get_part_two_result("input.txt")
    print(result)
