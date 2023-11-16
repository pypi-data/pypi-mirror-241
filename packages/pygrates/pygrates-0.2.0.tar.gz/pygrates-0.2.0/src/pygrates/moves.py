"""Move functions for lazy iteration of user-defined coordinates.

All of the functions in this module work with a user-defined class
that implements one of the abstract base classes from `pygrates.abc`.
The functions take one instance of said user-defined class as their
first input, along with an optional filter function, and return an
iterator with coordinates in a specific direction.
"""

from __future__ import annotations # Default behavior pending PEP 649

from collections.abc import Callable, Iterable, Iterator, Generator
from typing import TypeVar, Optional

from .abc import GCoords, DGCoords
from .itertools import chainmap, unique

# Coordinate types

GC = TypeVar('GC', bound=GCoords)
DGC = TypeVar('DGC', bound=DGCoords)

# Passable function types

Guard = Callable[[GC], bool]
Direction = Callable[[GC, Optional[Guard[GC]]], Iterable[GC]]

# Main library functions

def adjacent(coords: GC,
             guard: Optional[Guard[GC]] = None) -> Iterator[GC]:
    """Iterate adjacent coordinates.

    Parameters
    ----------
    coords : GC
        Generic coordinate object. Instance of a class that implements
        `pygrates.abc.GCoords`.
    guard : Callable[[GC], bool], optional
        Callable from the passed coordinate type to a boolean.

    Returns
    -------
    Iterator[GC]
        Iterator containing coordinate objects adjacent to the input
        coordinate. Usable once only.
    """

    return filter(guard, coords.adjacent())

def children(coords: DGC,
             guard: Optional[Guard[DGC]] = None) -> Iterator[DGC]:
    """Iterate child coordinates.

    Parameters
    ----------
    coords : DGC
        Generic coordinate object. Instance of a class that implements
        `pygrates.abc.DGCoords`.
    guard : Callable[[DGC], bool], optional
        Callable from the passed coordinate type to a boolean.

    Returns
    -------
    Iterator[DGC]
        Iterator containing coordinate objects that are children of the
        input coordinate. Usable once only.
    """

    return filter(guard, coords.children())

def parents(coords: DGC,
            guard: Optional[Guard[DGC]] = None) -> Iterator[DGC]:
    """Iterate parent coordinates.

    Parameters
    ----------
    coords : DGC
        Generic coordinate object. Instance of a class that implements
        `pygrates.abc.DGCoords`.
    guard : Callable[[DGC], bool], optional
        Callable from the passed coordinate type to a boolean.

    Returns
    -------
    Iterator[DGC]
        Iterator containing coordinate objects that are parents of the
        input coordinate. Usable once only.
    """

    return filter(guard, coords.parents())

def neighborhood(coords: GC, 
                 depth: int = 1,
                 guard: Optional[Guard[GC]] = None) -> Iterable[GC]:
    """Iterate neighboring coordinates to given depth.

    Parameters
    ----------
    coords : GC
        Generic coordinate object. Instance of a class that implements
        `pygrates.abc.GCoords`.
    depth : int, default=1
        Maximum depth of iteration.
    guard : Callable[[GC], bool], optional
        Callable from the passed coordinate type to a boolean.

    Returns
    -------
    Iterator[GC]
        Iterator containing coordinate objects from the neighborhood of
        the input coordinate. Usable once only.
    """

    return explore(coords, adjacent, depth, guard)

def descendants(coords: DGC, 
                depth: int = 1,
                guard: Optional[Guard[DGC]] = None) -> Iterator[DGC]:
    """Iterate descendant coordinates to given depth.

    Parameters
    ----------
    coords : DGC
        Generic coordinate object. Instance of a class that implements
        `pygrates.abc.DGCoords`.
    depth : int, default=1
        Maximum depth of iteration.
    guard : Callable[[DGC], bool], optional
        Callable from the passed coordinate type to a boolean.

    Returns
    -------
    Iterator[DGC]
        Iterator containing coordinate objects that are descendants of
        the input coordinate. Usable once only.
    """

    return explore(coords, children, depth, guard)

def ancestors(coords: DGC, 
              depth: int = 1,
              guard: Optional[Guard[DGC]] = None) -> Iterator[DGC]:
    """Iterate ancestor coordinates to given depth.

    Parameters
    ----------
    coords : DGC
        Generic coordinate object. Instance of a class that implements
        `pygrates.abc.DGCoords`.
    depth : int, default=1
        Maximum depth of iteration.
    guard : Callable[[DGC], bool], optional
        Callable from the passed coordinate type to a boolean.

    Returns
    -------
    Iterator[DGC]
        Iterator containing coordinate objects that are ancestors of
        the input coordinate. Usable once only.
    """

    return explore(coords, parents, depth, guard)

def explore(coords: GC,
            direction: Direction[GC],
            depth: int = 1,
            guard: Optional[Guard[GC]] = None) -> Generator[GC, None, None]:
    """Iterate coordinates in given direction to given depth.

    Parameters
    ----------
    coords : GC
        Generic coordinate object. Instance of a class that implements
        `pygrates.abc.GCoords`.
    depth : int, default=1
        Maximum depth of iteration.
    direction : Callable[[GC, Guard | None], Iterable[GC]]
        One of the functions `adjacent`, `children`, `parents`, or a
        custom callable from the passed coordinate type and filter
        function to an iterator containing coordinate objects.
    guard : Callable[[GC], bool], optional
        Callable from the passed coordinate type to a boolean.

    Returns
    -------
    Iterator[GC]
        Iterator containing coordinate objects in the given direction
        from the input coordinate. Usable once only.
    """

    step = lambda c: direction(c, guard)
    
    seen: set[GC] = {coords}
    queue: set[GC] = {coords}
    
    for d in range(depth):
        seen = seen | queue
        queue = yield from unique(chainmap(step, queue), seen)
