from src.day22.cuboid_operation import CuboidOperation, OperationType
from src.day22.splittable_cuboid import SplittableCuboid
from src.shared import load_text_file, Point3D


class CuboidOperationList(list[CuboidOperation]):
    def __init__(self, file_name: str, reboot_only: bool):
        super().__init__()
        self._load_from_file(file_name, reboot_only)

    def _load_from_file(self, file_name, reboot_only: bool):
        lines = load_text_file(file_name)
        for line in lines:
            first_parts = line.split(" ")
            type = OperationType.ON if first_parts[0] == "on" else OperationType.OFF
            coordinate_parts = first_parts[1].split(",")
            x_parts = coordinate_parts[0].split("=")[1].split("..")
            y_parts = coordinate_parts[1].split("=")[1].split("..")
            z_parts = coordinate_parts[2].split("=")[1].split("..")
            location1 = Point3D(int(x_parts[0]), int(y_parts[0]), int(z_parts[0]))
            location2 = Point3D(int(x_parts[1]), int(y_parts[1]), int(z_parts[1]))
            cuboid = SplittableCuboid(location1, location2)

            if reboot_only and not -50 <= cuboid.left <= 50:
                continue

            self.append(CuboidOperation(type, cuboid))

    def reduce_overlapping_operations(self):
        '''
        Methodology: last operation has the highest priority, so go through them in reverse and
        remove any overlapping regions of lower priority operations. If area is not entirely contained,
        the cuboid is split up so that we can remove just the overlapping portion.
        '''

        idx_higher_priority = len(self)
        while idx_higher_priority >= 2:
            idx_higher_priority -= 1
            operation_higher_priority = self[idx_higher_priority]

            idx_lower_priority = idx_higher_priority
            while idx_lower_priority >= 1:
                idx_lower_priority -= 1
                operation_lower_priority = self[idx_lower_priority]

                # nothing to do if they don't intersect
                if not operation_lower_priority.region.intersects(operation_higher_priority.region):
                    continue

                # get list of non-overlapping portions of the cuboids
                new_operations = operation_lower_priority.explode(operation_higher_priority)

                # remove the original operation and add back in the new ones at the same location
                self.remove(operation_lower_priority)
                for operation in new_operations:
                    self.insert(idx_lower_priority, operation)

            idx_higher_priority = self.index(operation_higher_priority)

    def volume_of_type(self, type: OperationType) -> int:
        operations_of_type = [x for x in self if x.type == type]
        volume = sum([x.region.volume for x in operations_of_type])
        return volume
