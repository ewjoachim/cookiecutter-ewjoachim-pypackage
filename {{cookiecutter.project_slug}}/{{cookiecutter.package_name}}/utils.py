import logging
from typing import Optional


logger = logging.getLogger(__name__)


def causes(exc: Optional[BaseException]):
    """
    From a single exception with a chain of causes and contexts, make an iterable
    going through every exception in the chain.
    """
    while exc:
        yield exc
        exc = exc.__cause__ or exc.__context__
