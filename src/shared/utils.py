from typing import Callable


ComparerFunc = Callable[[int, int], bool]


def noop(*_): return None
