from __future__ import annotations # Default behavior pending PEP 649

from dataclasses import dataclass

import pytest

import pygrates as pg

# Simple 2D grid coordinate class

@dataclass(frozen=True, slots=True)
class GridPoint2D(pg.abc.DGCoords):
    x: int
    y: int

    def children(self) -> tuple[GridPoint2D, GridPoint2D]:
        return GridPoint2D(self.x + 1, self.y), GridPoint2D(self.x, self.y + 1)

    def parents(self) -> tuple[GridPoint2D, GridPoint2D]:
        return GridPoint2D(self.x - 1, self.y), GridPoint2D(self.x, self.y - 1)

    def __hash__(self) -> int: # Dataclass hash undetected by Mypy
        return hash((self.x, self.y))

    def __eq__(self, other: object) -> bool: # Dataclass EQ undetected by Mypy
        if isinstance(other, GridPoint2D):
            return (self.x, self.y) == (other.x, other.y)
        else:
            return NotImplemented

# Simple 2D grid coordinate fixtures

@pytest.fixture
def origin() -> GridPoint2D:
    return GridPoint2D(0, 0)

@pytest.fixture
def up_one() -> set[GridPoint2D]:
    return {GridPoint2D(1, 0), GridPoint2D(0, 1)}

@pytest.fixture
def down_one() -> set[GridPoint2D]:
    return {GridPoint2D(-1, 0), GridPoint2D(0, -1)}

@pytest.fixture
def up_two() -> set[GridPoint2D]:
    return {GridPoint2D(1, 0), GridPoint2D(0, 1),
            GridPoint2D(2, 0), GridPoint2D(0, 2),
            GridPoint2D(1, 1)}

@pytest.fixture
def down_two() -> set[GridPoint2D]:
    return {GridPoint2D(-1, 0), GridPoint2D(0, -1),
            GridPoint2D(-2, 0), GridPoint2D(0, -2),
            GridPoint2D(-1, -1)}

@pytest.fixture
def side_two() -> set[GridPoint2D]:
    return {GridPoint2D(1, -1), GridPoint2D(-1, 1)}

# Move function unit tests

def test_adjacent(origin : GridPoint2D,
                  up_one: set[GridPoint2D],
                  down_one: set[GridPoint2D]):
    """Test adjacent move function."""

    assert set(pg.adjacent(origin)) == up_one | down_one
    assert set(pg.adjacent(origin, lambda c: c not in up_one)) == down_one
    assert set(pg.adjacent(origin, lambda c: c not in down_one)) == up_one

def test_children(origin : GridPoint2D,
                  up_one: set[GridPoint2D]):
    """Test children move function."""

    assert set(pg.children(origin)) == up_one

def test_parents(origin : GridPoint2D,
                 down_one: set[GridPoint2D]):
    """Test parents move function."""

    assert set(pg.parents(origin)) == down_one

def test_neighborhood(origin : GridPoint2D,
                      up_one: set[GridPoint2D],
                      down_one: set[GridPoint2D],
                      up_two: set[GridPoint2D],
                      down_two: set[GridPoint2D],
                      side_two):
    """Test neighborhood move function."""

    assert set(pg.neighborhood(origin, 1)) == up_one | down_one
    assert set(pg.neighborhood(origin, 2)) == up_two | down_two | side_two

def test_descendants(origin : GridPoint2D,
                     up_two: set[GridPoint2D]):
    """Test descendants move function."""

    assert set(pg.descendants(origin, 2)) == up_two

def test_ancestors(origin : GridPoint2D,
                   down_two: set[GridPoint2D]):
    """Test ancestors move function."""

    assert set(pg.ancestors(origin, 2)) == down_two
