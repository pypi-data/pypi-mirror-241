"""Abstract base classes for user-defined coordinates.

The base classes in this module form an interface for using the
functions in `pygrates.moves`. The user creates a coordinate class
by explicitly subclassing one of the bases and implementing its
abstract methods, or implicitly by implementing all of its methods.
All coordinates need to be *hashable* and to define *equality* with
coordinates of the same type: this can easily achieved with a named
tuple or dataclass implementation.

Examples
--------
>>> from dataclasses import dataclass
>>> @dataclass(frozen=True)
... class Point2D(pg.abc.DGCoords):
...   x: int
...   y: int
...
...   def children(self):
...     return Point2D(self.x + 1, self.y), Point2D(self.x, self.y + 1)
...
...   def parents(self):
...     return Point2D(self.x - 1, self.y), Point2D(self.x, self.y - 1)
...
>>> origin = Point2D(0, 0)
>>> isinstance(origin, pg.abc.DGCoords)
True
"""

from __future__ import annotations # Default behavior pending PEP 649

from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Self

from itertools import chain

# Base coordinate classes to implement for using the library functions

class GCoords(ABC):
    """Base class for graph coordinates.

    Interface for using the functions in `pygrates.moves`. User-created
    coordinate class implicitly defines an undirected or directed
    graph.

    Methods to implement are `__eq__`, `__hash__` and `adjacent`.
    """

    __slots__ = ()
    
    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """Return True if self is equal to other coordinate.

        Parameters
        ----------
        other : Self
            Coordinate object of the same type as self.

        Returns
        -------
        bool
            True if passed coordinate is equal to self.
        """

        raise NotImplementedError
    
    @abstractmethod
    def __hash__(self) -> int:
        """Return hash value of self.

        Returns
        -------
        int
            Hash value of self.
        """

        raise NotImplementedError
    
    @abstractmethod
    def adjacent(self) -> Iterable[Self]:
        """Return iterable containing adjacent coordinates.

        Returns
        -------
        Iterable[Self]
            Iterable containing coordinates adjacent to self, of the
            same type.
        """

        raise NotImplementedError
    
    def is_adjacent(self, other: Self) -> bool:
        """Return True if self is adjacent to other coordinate.

        Parameters
        ----------
        other : Self
            Coordinate object of the same type as self.

        Returns
        -------
        bool
            True if self is adjacent to passed coordinate.
        """

        adjacent: Iterable[Self] = self.adjacent()
        return any(coords == other for coords in adjacent)

class DGCoords(GCoords, ABC):
    """Base class for directed graph coordinates.

    Interface for using the functions in `pygrates.moves`. User-created
    coordinate class implicitly defines a directed graph.

    Methods to implement are `__eq__`, `__hash__`, `children`,
    and `parents`.
    """

    __slots__ = ()
    
    @abstractmethod
    def children(self) -> Iterable[Self]:
        """Return iterable containing child coordinates.

        Returns
        -------
        Iterable[Self]
            Iterable containing child coordinates of self, of the same
            type.
        """

        raise NotImplementedError
    
    @abstractmethod
    def parents(self) -> Iterable[Self]:
        """Return iterable containing parent coordinates.

        Returns
        -------
        Iterable[Self]
            Iterable containing parent coordinates of self, of the same
            type.
        """
        
        raise NotImplementedError
    
    def adjacent(self) -> Iterable[Self]:
        """Return iterable containing adjacent coordinates.

        Returns
        -------
        Iterable[Self]
            Iterable containing coordinates adjacent to self, of the
            same type.
        """

        return chain(self.children(), self.parents())
    
    def is_child(self, other: Self) -> bool:
        """Return True if self is a child of other coordinate.

        Parameters
        ----------
        other : Self
            Coordinate object of the same type as self.

        Returns
        -------
        bool
            True if self is a child of passed coordinate.
        """

        parents: Iterable[Self] = self.parents()
        return any(coords == other for coords in parents)
    
    def is_parent(self, other: Self) -> bool:
        """Return True if self is a parent of other coordinate.

        Parameters
        ----------
        other : Self
            Coordinate object of the same type as self.

        Returns
        -------
        bool
            True if self is a parent of passed coordinate.
        """

        children: Iterable[Self] = self.children()
        return any(coords == other for coords in children)

class DAGCoords(DGCoords, ABC):
    """Base class for directed-acyclic-graph coordinates.

    Interface for using the functions in `pygrates.moves`. User-created
    coordinate class implicitly defines a directed acyclyc graph.

    Methods to implement are `__eq__`, `__hash__`, `children`,
    and `parents`.
    """

    __slots__ = ()

class TGCoords(DAGCoords, ABC):
    """Base class for tree coordinates.

    Interface for using the functions in `pygrates.moves`. User-created
    coordinate class implicitly defines a tree graph.

    Methods to implement are `__eq__`, `__hash__`, `children`,
    and `parents`.
    """

    __slots__ = ()
