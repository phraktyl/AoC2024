import pytest
from aoc.day02 import Day02

def test_testLevel():
    d2 = Day02([])
    assert d2.testLevel([1, 2, 3, 4, 5]) == True
    assert d2.testLevel([1, 2, 3, 4, 7]) == True
    assert d2.testLevel([1, 2, 3, 4, 8]) == False
    assert d2.testLevel([1, 3, 2, 4, 5]) == False
    assert d2.testLevel([1, 2, 2, 4, 5]) == False
    assert d2.testLevel([5, 4, 3, 2, 1]) == True
    assert d2.testLevel([7, 4, 3, 2, 1]) == True
    assert d2.testLevel([8, 4, 3, 2, 1]) == False
    assert d2.testLevel([5, 4, 2, 3, 1]) == False
    assert d2.testLevel([5, 4, 2, 2, 1]) == False

def test_testLevel_withTolerance():
    d2 = Day02([])
    d2.setTolerance()
    assert d2.testLevel([1, 2, 3, 4, 5]) == True
    assert d2.testLevel([1, 2, 3, 4, 7]) == True
    assert d2.testLevel([1, 2, 3, 4, 8]) == True
    assert d2.testLevel([1, 2, 3, 7, 8]) == False
    assert d2.testLevel([1, 3, 2, 4, 5]) == True
    assert d2.testLevel([1, 2, 2, 4, 5]) == True
    assert d2.testLevel([1, 4, 3, 2, 5]) == False
    assert d2.testLevel([1, 2, 2, 2, 5]) == False
    assert d2.testLevel([5, 4, 3, 2, 1]) == True
    assert d2.testLevel([7, 4, 3, 2, 1]) == True
    assert d2.testLevel([8, 4, 3, 2, 1]) == True
    assert d2.testLevel([8, 7, 3, 2, 1]) == False
    assert d2.testLevel([5, 4, 2, 3, 1]) == True
    assert d2.testLevel([5, 4, 2, 2, 1]) == True

def test_getPart1():
    d2 = Day02([
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
    ])
    assert d2.getPart1() == 2

def test_getPart2():
    d2 = Day02([
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
    ])
    d2.setTolerance()
    assert d2.getPart2() == 4
