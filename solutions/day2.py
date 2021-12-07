# https://adventofcode.com/2021/day/2

import sys

def part1():
    horizontal = 0
    depth = 0
    with open('solutions/day2_input.txt',mode='r') as f:
        for line in f:
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
    with open('solutions/day2_input.txt',mode='r') as f:
        for line in f:
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

if __name__ == "__main__":
    # part 1
    print(part1())

    # part 2
    print(part2())
