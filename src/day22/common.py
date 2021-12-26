from src.day22.cuboid_operation import OperationType
from src.day22.cuboid_operation_list import CuboidOperationList


def get_final_on_volume(file_name: str, reboot_only: bool) -> int:
    operations = CuboidOperationList(file_name, reboot_only)
    operations.reduce_overlapping_operations()
    on_volume = operations.volume_of_type(OperationType.ON)
    return on_volume
