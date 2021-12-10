# https://adventofcode.com/2021/day/1

import sys
import queue

def part1():
    prev = None
    count = 0
    with open('solutions/day_01_input.txt',mode='r') as f:
        for line in f:
            depth = float(line.strip())
            if prev and depth > prev:
                count+=1
            prev = depth
    return count


def part2():
    q = queue.Queue(maxsize=3)
    sum_depths = 0
    count = 0
    prev_sum = 0
    with open('solutions/day_01_input.txt',mode='r') as f:
        for line in f:
            depth = float(line.strip())
            if q.qsize() ==3:
                first = q.get()
                prev_sum = sum_depths
                sum_depths -= first
                sum_depths+=depth
                q.put(depth)
                if sum_depths > prev_sum:
                    count+=1
            else:
                sum_depths+=depth
                q.put(depth)
    return count

if __name__ == '__main__':
    # part 1
    print(part1())

    # part 2
    print(part2())
