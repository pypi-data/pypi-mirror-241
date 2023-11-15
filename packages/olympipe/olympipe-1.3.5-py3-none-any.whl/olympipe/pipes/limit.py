from multiprocessing.managers import DictProxy
from typing import List, TypeVar

from olympipe.shuttable_queue import ShuttableQueue

from .generic import GenericPipe

R = TypeVar("R")
S = TypeVar("S")
T = TypeVar("T")


class LimitPipe(GenericPipe[R, R]):
    def __init__(
        self,
        father_process_dag: "DictProxy[str, List[str]]",
        source: "ShuttableQueue[R]",
        target: "ShuttableQueue[R]",
        limit: int,
    ):
        self._limit: int = limit
        self._seen: int = 0
        super().__init__(father_process_dag, source, target)

    @property
    def shortname(self) -> str:
        return f"Limit:{self._limit}"

    def _perform_task(self, data: R) -> R:
        self._seen += 1

        if self._limit > self._seen - 1:
            return data

        raise Exception(f"Limit of {self._limit} packets attained")
