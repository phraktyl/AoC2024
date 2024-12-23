#!/usr/bin/python3

from aoc.day02 import Day02

print("2024 Advent of Code")
print("Day 2")

levelData = []

with open("files/aoc-2024-02-input", "r") as f:
    levelData = [list(map(int, x.split())) for x in f if x.strip()]

safeCount = 0

print("Part 1")

d2 = Day02(levelData)

print(d2.getPart1())

print("\nPart 2")

d2 = Day02(levelData)
d2.setTolerance()

print(d2.getPart2())
