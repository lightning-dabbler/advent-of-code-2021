# https://adventofcode.com/2021/day/2

import sys

def part1():
    horizontal = 0
    depth = 0
    for line in sys.stdin:
        direction,units = line.strip().split(' ')
        units = int(units)
        if direction == "forward":
            horizontal+=units
        elif direction == "down":
            depth += units
        else:
            depth-=units
    return horizontal*depth

def part2():
    horizontal = 0
    depth = 0
    aim = 0
    for line in sys.stdin:
        direction,units = line.strip().split(' ')
        units = int(units)
        if direction == "forward":
            horizontal+=units
            depth+=(units*aim)
        elif direction == "down":
            aim += units
        else:
            aim-=units
    return horizontal*depth
        