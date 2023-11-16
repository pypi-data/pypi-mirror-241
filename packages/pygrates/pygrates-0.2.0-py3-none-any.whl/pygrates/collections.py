from __future__ import annotations # Default behavior pending PEP 649

from collections.abc import Hashable
from typing import TypeVar, Generic, Any, NoReturn

# Immutable and hashable hash-map classes

A = TypeVar('A', bound=Hashable)
B = TypeVar('B', bound=Hashable)

class NamedFrozenSet(frozenset[A], Generic[A]):
    """Hashable and immutable named set."""
    
    __slots__ = ()
    
    def __repr__(self) -> str:
        
        name = type(self).__name__
        items = ''
        for i in self:
            if items == '':
                items += repr(i)
            else:
                items += (', ' + repr(i))
        
        return f'{name}({{{items}}})'

class NamedFrozenDict(dict[A, B], Generic[A, B]):
    """Hashable and immutable named mapping."""
    
    __slots__ = ()
    
    def __repr__(self) -> str:
        
        name = type(self).__name__
        
        return f'{name}({super().__repr__()})'
    
    def __hash__(self) -> int: # type: ignore
        
        return hash(frozenset(self.items()))
