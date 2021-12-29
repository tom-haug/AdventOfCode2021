from src.shared import LinkedNode


START_LABEL = "start"
END_LABEL = "end"


class CaveNode(LinkedNode):
    def disallow_revisit(self):
        return self.is_start or self.is_end

    @property
    def is_start(self):
        return self.label == START_LABEL

    @property
    def is_end(self):
        return self.label == END_LABEL

    @property
    def is_small_cave(self) -> bool:
        return self.label.islower()

    @property
    def is_large_cave(self) -> bool:
        return not self.is_small_cave
