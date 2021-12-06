from src.day05.vent_map import VentMap


def get_part_one_result(file_name: str):
    vent_map = VentMap(file_name, False)
    return vent_map.get_dangerous_vent_count()


if __name__ == "__main__":
    result = get_part_one_result("input.txt")
    print(result)
