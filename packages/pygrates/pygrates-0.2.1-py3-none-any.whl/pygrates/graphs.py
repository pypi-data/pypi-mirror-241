"""Functions for transforming graph adjacency maps.

All of the functions in this module work on a dictionary mapping from
one type to sets of objects from the same or another type. If the types
are the same, this mapping can be thought of as an adjacency map of a
directed graph, or if every edge is present in both directions, an
undirected graph. If the types are different, it can be thought of as
a bipartite graph.

Examples
--------
>>> groups = {1: {'Miles', 'John', 'Red', 'Paul', 'Philly Joe'},
...           2: {'John', 'McCoy', 'Jimmy', 'Elvin'},
...           3: {'Miles', 'Wayne', 'Herbie', 'Ron', 'Tony'}}
>>> sizes = pg.degrees(groups)
>>> sizes == {1: 5, 2: 4, 3: 5}
True
>>> members = pg.inverse(groups)
>>> members == {'Miles': {1, 3}, 'John': {1, 2},
...             'Red': {1}, 'Paul': {1}, 'Philly Joe': {1},
...             'McCoy': {2}, 'Jimmy': {2}, 'Elvin': {2},
...             'Wayne': {3}, 'Herbie': {3}, 'Ron': {3}, 'Tony': {3}}
True
>>> collaborations = pg.compound(members, groups)
>>> collaborations['Miles'] == {'John', 'Red', 'Paul', 'Philly Joe',
...                             'Wayne', 'Herbie', 'Ron', 'Tony'}
True
"""

from __future__ import annotations # Default behavior pending PEP 649

from collections.abc import Hashable, Mapping, Collection, Callable
from typing import TypeVar

# Functions for operating on adjacency maps

A = TypeVar('A', bound=Hashable)
B = TypeVar('B', bound=Hashable)
C = TypeVar('C', bound=Hashable)
D = TypeVar('D', bound=Hashable)

def inverse(a: Mapping[A, Collection[B]]) -> dict[B, set[A]]:
    """Return inverse of adjacency map.

    If the input map is thought of as a directed graph, the output map
    will be the graph with every edge reversed.

    Parameters
    ----------
    a : Mapping[A, Collection[B]]
        Dictionary or other mapping from generic type A to a set or
        other collection of generic type B.

    Returns
    -------
    dict[B, set[A]]
        Dictionary representing the inverse adjacency map of the input.

    Examples
    --------
    >>> a = {1: {'y', 'z'}, 2: {'x', 'z'}, 3: {'x', 'y'}}
    >>> pg.inverse(a) == {'x': {2, 3}, 'y': {1, 3}, 'z': {1, 2}}
    True
    """

    inv: dict[B, set[A]] = {}
    
    for f, ts in a.items():
        for t in ts:
            inv.setdefault(t, set()).add(f)
            
    return inv

def compound(a: Mapping[A, Collection[B]],
             b: Mapping[B, Collection[C]]) -> dict[A, set[C]]:
    """Return linked adjacency map from two adjacency maps.

    If the input maps are thought of as two directed graphs, the output
    map will be the graph with source nodes of the left graph, sink
    nodes of the right graph, and edges from the former to the latter
    for every time the sink of an edge in the left graph is equal to the
    source of an edge in the right graph.

    If both inputs are the same map, the output can be thought of as a
    graph with the same nodes and an edge for every walk of length two
    on the input graph. Self-edges are excluded.

    Parameters
    ----------
    a : Mapping[A, Collection[B]]
        Dictionary or other mapping from generic type A to a set or
        other collection of generic type B.
    b : Mapping[B, Collection[C]]
        Dictionary or other mapping from generic type B to a set or
        other collection of generic type C.

    Returns
    -------
    dict[A, set[C]]
        Dictionary representing the linked adjacency map of the inputs.

    Examples
    --------
    >>> a = {1: {'y', 'z'}, 2: {'x', 'z'}, 3: {'x', 'y'}}
    >>> b = {'x': {2, 3}, 'y': {1, 3}, 'z': {1, 2}}
    >>> pg.compound(a, b) == {1: {2, 3}, 2: {1, 3}, 3: {1, 2}}
    True
    """

    comp: dict[A, set[C]] = {}
    
    for f, ts in a.items():
        for t in ts:
            comp.setdefault(f, set()).update(set(b.get(t, [])).difference([f]))
    
    return comp

def merge(a: Mapping[A, Collection[C]],
          b: Mapping[B, Collection[D]],
          left: bool = False) -> dict[A | B, set[C | D]]:
    """Return merged adjacency map from two adjacency maps.

    If the input maps are thought of as two directed graphs, the output
    graph will be the graph with all nodes and edges from both graphs.
    Optionally, only the source nodes of the left map are kept, with
    just the edges for which the source is a source node on the left.

    Parameters
    ----------
    a : Mapping[A, Collection[C]]
        Dictionary or other mapping from generic type A to a set or
        other collection of generic type C.
    b : Mapping[B, Collection[D]]
        Dictionary or other mapping from generic type B to a set or
        other collection of generic type C.
    left : bool, default=False
        If True, keep only the sources already present in the left map
        and merge the sinks for those.

    Returns
    -------
    dict[A | B, set[C | D]]
        Dictionary representing the merged adjacency map of the inputs.

    Examples
    --------
    >>> a = {1: {'y'}, 2: {'x'}}
    >>> b = {1: {'z'}, 2: {'z'}, 3: {'x', 'y'}}
    >>> pg.merge(a, b) == {1: {'y', 'z'}, 2: {'x', 'z'}, 3: {'x', 'y'}}
    True
    >>> pg.merge(a, b, left=True) == {1: {'y', 'z'}, 2: {'x', 'z'}}
    True
    """

    mer: dict[A | B, set[C | D]] = {f: set(ts) for f, ts in a.items()}
    
    for f, ts in b.items():
        if left:
            mer.get(f, set()).update(ts)
        else:
            mer.setdefault(f, set()).update(ts)
    
    return mer

def degrees(a: Mapping[A, Collection[B]]) -> dict[A, int]:
    """Return degree map of adjacency map.
    
    If the input map is thought of as a directed graph, the output map
    will be a mapping from the nodes to their number of outgoing edges.

    Parameters
    ----------
    a : Mapping[A, Collection[B]]
        Dictionary or other mapping from generic type A to a set or
        other collection of generic type B.

    Returns
    -------
    dict[B, set[A]]
        Dictionary with the number of edges leaving each node.

    Examples
    --------
    >>> a = {'x': {1}, 'y': {1, 2}, 'z': {1, 2, 3}}
    >>> pg.degrees(a) == {'x': 1, 'y': 2, 'z': 3}
    True
    """

    return {f: len(ts) for f, ts in a.items()}

def subsources(a: Mapping[A, Collection[B]],
               condition: Callable[[A], bool]) -> dict[A, set[B]]:
    """Return adjacency map with sources filtered by condition.

    If the input map is thought of as a directed graph, the output
    will be the graph with edges removed if their source node does
    not satisfy the condition, and their source node removed if it
    is not the sink node of any remaining edge.

    Parameters
    ----------
    a : Mapping[A, Collection[B]]
        Dictionary or other mapping from generic type A to a set or
        other collection of generic type B.
    condition : Callable[[A], bool]
        A filtering function that maps from passed type A to a boolean.

    Returns
    -------
    dict[A, set[C]]
        Dictionary representing the source-filtered adjacency map.

    Examples
    --------
    >>> a = {1: {2, 3}, 2: {1, 3}, 3: {1, 2}}
    >>> pg.subsources(a, lambda n: n < 3) == {1: {2, 3}, 2: {1, 3}}
    True
    """

    return {f: set(ts) for f, ts in a.items() if condition(f)}

def subsinks(a: Mapping[A, Collection[B]],
             condition: Callable[[B], bool]) -> dict[A, set[B]]:
    """Return adjacency map with sinks filtered by condition.

    If the input map is thought of as a directed graph, the output
    will be the graph with edges removed if their sink node does
    not satisfy the condition, and their sink node removed if it
    is not the source node of any remaining edge.

    Parameters
    ----------
    a : Mapping[A, Collection[B]]
        Dictionary or other mapping from generic type A to a set or
        other collection of generic type B.
    condition : Callable[[A], bool]
        A filtering function that maps from passed type B to a boolean.

    Returns
    -------
    dict[A, set[C]]
        Dictionary representing the sink-filtered adjacency map.

    Examples
    --------
    >>> a = {1: {2, 3}, 2: {1, 3}, 3: {1, 2}}
    >>> pg.subsinks(a, lambda n: n < 3) == {1: {2}, 2: {1}, 3: {1, 2}}
    True
    """

    return {f: set(filter(condition, ts)) for f, ts in a.items()
            if len(tuple(filter(condition, ts))) != 0}

def subgraph(a: Mapping[A, Collection[B]],
             condition: Callable[[A | B], bool]) -> dict[A, set[B]]:
    """Return adjacency map with nodes filtered by condition.

    If the input map is thought of as a directed graph, the output
    will be the graph with nodes removed if they do not satisfy the
    condition, along with their ingoing and outgoing edges.

    Parameters
    ----------
    a : Mapping[A, Collection[B]]
        Dictionary or other mapping from generic type A to a set or
        other collection of generic type B.
    condition : Callable[[A | B], bool]
        A filtering function that maps from passed types A or B to a
        boolean.

    Returns
    -------
    dict[A, set[C]]
        Dictionary representing the filtered adjacency map.

    Examples
    --------
    >>> a = {1: {2, 3}, 2: {1, 3}, 3: {1, 2}}
    >>> pg.subgraph(a, lambda n: n < 3) == {1: {2}, 2: {1}}
    True
    """

    return subsinks(subsources(a, condition), condition)
