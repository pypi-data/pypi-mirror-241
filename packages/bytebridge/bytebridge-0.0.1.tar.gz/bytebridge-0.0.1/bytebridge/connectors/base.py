from abc import ABC, abstractmethod
from typing import Iterator, List


class Connector(ABC):
    @abstractmethod
    def extract(
        self,
        *,
        source_object: str,
        source_query: str,
        batch_size: int,
    ):
        pass

    @abstractmethod
    def load(
        self,
        *,
        batch_iterator: Iterator[List[dict]],
        target_object: str,
    ):
        pass
