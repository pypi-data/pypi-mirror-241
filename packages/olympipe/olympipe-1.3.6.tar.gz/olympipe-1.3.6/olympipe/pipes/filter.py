from multiprocessing.managers import DictProxy
from typing import Callable, List, Optional, TypeVar

from olympipe.shuttable_queue import ShuttableQueue

from .generic import GenericPipe

R = TypeVar("R")


class FilterPipe(GenericPipe[R, R]):
    def __init__(
        self,
        father_process_dag: "DictProxy[str, List[str]]",
        source: "ShuttableQueue[R]",
        keep_if_true: Optional[Callable[[R], bool]],
        target: "ShuttableQueue[R]",
    ):
        self._keep_if_true = self.filter_none if keep_if_true is None else keep_if_true
        super().__init__(father_process_dag, source, target)

    @staticmethod
    def filter_none(packet: R) -> bool:
        return packet is not None

    @property
    def shortname(self) -> str:
        return f"filter:{self._keep_if_true.__name__}"

    def _perform_task(self, data: R) -> R:
        if self._keep_if_true(data):
            super()._send_to_next(data)
        return data

    def _send_to_next(self, processed: R):
        pass
