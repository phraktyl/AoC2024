import pytest
from aoc.day01 import Day01

def test_getDistance():
    d1 = Day01([1], [5])
    assert d1.getDistance(3, 1) == 2
    assert d1.getDistance(-1, 3) == 4

def test_getPart1():
    d1 = Day01([5, 2, 1], [2, 3, 6])
    assert d1.getPart1() == 3

def test_getPart2():
    d1 = Day01([5, 2, 1], [1, 5, 5])
    assert d1.getPart2() == 11
