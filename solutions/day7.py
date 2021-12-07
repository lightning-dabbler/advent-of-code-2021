# https://adventofcode.com/2021/day/7

def part1(arr):
    start = min(positions)
    end = max(positions)
    min_cost = float('inf')
    for i in range(start,end+1):
        total = 0
        for position in positions:
            total += abs(position-i)
        if total < min_cost:
            min_cost = total
    return min_cost

def part2(arr):
    start = min(positions)
    end = max(positions)
    min_cost = float('inf')
    for i in range(start,end+1):
        total = 0
        for position in positions:
            distance = abs(position-i)
            total += (distance*(distance+1)//2)
        if total < min_cost:
            min_cost = total
    return min_cost

if __name__ == '__main__':
    positions = list(map(int,open("solutions/day7_input.txt").read().strip().split(',')))
    # part 1
    print(part1(positions))

    # part 2
    print(part2(positions))
