#!/usr/bin/python3

from aoc.day01 import Day01

print("2024 Advent of Code")
print("Day 1")

print("Part 1")

file = open("aoc-2024-01-input", "r")

locationsA = []
locationsB = []

for line in file:
    locs = line.split()
    locationsA.append(locs[0])
    locationsB.append(locs[1])

d1 = Day01(locationsA, locationsB)

print("Total distance: ", d1.getPart1(), "\n")

print("Part 2")

print("Similarity: ", d1.getPart2(), "\n")
