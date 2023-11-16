from abc import ABCMeta, abstractmethod
from typing import Callable

from atap_corpus.interfaces import Clonable, Serialisable
from atap_corpus._types import Docs, Doc, TFreqTable


class BaseFreqTable(metaclass=ABCMeta):
    pass


class BaseDTM(Clonable, Serialisable, metaclass=ABCMeta):
    # todo: core interface functions need to be defined here.
    @abstractmethod
    def to_freqtable(self) -> TFreqTable:
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def from_docs(cls, docs: Docs, tokeniser_func: Callable[[Doc], list[str]], *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    @property
    def num_terms(self):
        raise NotImplementedError()

    @abstractmethod
    @property
    def num_docs(self):
        raise NotImplementedError()

    @abstractmethod
    @property
    def total(self):
        raise NotImplementedError()
