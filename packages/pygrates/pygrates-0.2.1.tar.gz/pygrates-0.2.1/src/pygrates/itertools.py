from __future__ import annotations # Default behavior pending PEP 649

from collections.abc import (Hashable, Set, Generator,
                             Iterable, Iterator, Callable)
from typing import TypeVar

from itertools import chain

# Helper functions for lazy iteration

H = TypeVar('H', bound=Hashable)

def unique(xs: Iterable[H],
           exclude: Set[H] = frozenset()) -> Generator[H, None, set[H]]:
    """Iterate unique elements from xs."""
    
    seen: set[H] = set()
    for x in xs:
        if (x not in exclude) and (x not in seen):
            seen.add(x)
            yield x
    return seen

# Convenience function for common pattern

A = TypeVar('A')
B = TypeVar('B')

def chainmap(f: Callable[[A], Iterable[B]], xs: Iterable[A]) -> Iterator[B]:
    """Map f over xs and chain result."""
    
    return chain.from_iterable(map(f, xs))
