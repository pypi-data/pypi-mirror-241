from __future__ import annotations # Default behavior pending PEP 649

import pytest

import pygrates as pg

# Simple graph adjacency map fixtures

@pytest.fixture
def up_triple() -> dict[int, set[str]]:
    return {1: {'b', 'c'}, 2: {'a', 'c'}, 3: {'a', 'b'}}

@pytest.fixture
def up_single() -> dict[int, set[str]]:
    return {1: {'b', 'c'}}

@pytest.fixture
def down_triple() -> dict[str, set[int]]:
    return {'a': {2, 3}, 'b': {1, 3}, 'c': {1, 2}}

@pytest.fixture
def down_single() -> dict[str, set[int]]:
    return {'b': {1}, 'c': {1}}

@pytest.fixture
def triangle() -> dict[int, set[int]]:
    return {1: {2, 3}, 2: {1, 3}, 3: {1, 2}}

@pytest.fixture
def triangle_degrees() -> dict[int | str, int]:
    return {n: 2 for n in (1, 2, 3)}

@pytest.fixture
def pair() -> dict[int, set[int]]:
    return {2: {3}, 3: {2}}

@pytest.fixture
def hexagon() -> dict[int | str, set[int | str]]:
    return {1: {'b', 'c'}, 2: {'a', 'c'}, 3: {'a', 'b'},
            'a': {2, 3}, 'b': {1, 3}, 'c': {1, 2}}

# Graph function unit tests

def test_inverse(up_triple: dict[int, set[str]],
                 down_triple: dict[str, set[int]]):
    """Test graph inverse function."""

    assert pg.inverse(up_triple) == down_triple
    assert pg.inverse(down_triple) == up_triple

def test_compound(up_triple: dict[int, set[str]],
                  down_triple: dict[str, set[int]],
                  triangle: dict[int, set[int]]):
    """Test graph compound function."""

    assert pg.compound(up_triple, down_triple) == triangle

def test_merge(up_triple: dict[int, set[str]],
               up_single: dict[int, set[str]],
               down_triple: dict[str, set[int]],
               down_single: dict[str, set[int]],
               hexagon: dict[int | str, set[int | str]]):
    """Test graph merge function."""

    assert pg.merge(up_triple, down_triple) == hexagon
    assert pg.merge(down_single, down_triple) == down_triple
    assert pg.merge(up_single, up_triple, left=True) == up_single

def test_degrees(triangle: dict[int, set[int]],
                 triangle_degrees: dict[int, int]):
    """Test graph degrees function."""

    assert pg.degrees(triangle) == triangle_degrees

def test_subsources(up_triple: dict[int, set[str]],
                    up_single: dict[int, set[str]]):
    """Test graph subsources function."""

    assert pg.subsources(up_triple, lambda n: n==1) == up_single

def test_subsinks(down_triple: dict[str, set[int]],
                  down_single: dict[str, set[int]]):
    """Test graph subsinks function."""

    assert pg.subsinks(down_triple, lambda n: n==1) == down_single

def test_subgraph(triangle: dict[int, set[int]],
                  pair: dict[int, set[int]]):
    """Test graph subgraph function."""

    assert pg.subgraph(triangle, lambda n: n!=1) == pair
