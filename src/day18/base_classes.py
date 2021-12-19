from __future__ import annotations

from abc import abstractmethod, ABC
from typing import Callable


class Searchable(ABC):
    @abstractmethod
    def _recursive_search(self, current_depth: int, search_criteria: Callable[[Searchable, int], bool]) -> Searchable:
        ...


class Explodable(Searchable):
    @property
    @abstractmethod
    def exploding_criteria(self, *args):
        ...

    def try_explode(self) -> bool:
        found_statement = self._recursive_search(0, self.exploding_criteria)

        if found_statement is not None:
            found_statement.explode()
            return True

    @abstractmethod
    def explode(self):
        ...


class Splittable(Searchable):
    @property
    @abstractmethod
    def splitting_criteria(self, *args):
        ...

    def try_split(self) -> bool:
        found_statement = self._recursive_search(0, self.splitting_criteria)

        if found_statement is not None:
            found_statement.split()
            return True

    @abstractmethod
    def split(self):
        ...