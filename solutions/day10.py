# https://adventofcode.com/2021/day/10

def part1():
    chunks = {'(':')',')':'(','{':'}','}':'{','[':']',']':'[','<':'>','>':'<'}
    open_ = ['(','{','[','<']
    close = [')''}',']','>']
    points = {'}':1197,'>':25137,']':57,')':3}
    total = 0
    with open("solutions/day10_input.txt") as f:
        for line in f:
            stack = []
            corrupted = False
            first_corrupted = ''
            for char in line.strip():
                if char == '':
                    break
                if char in open_:
                    stack.append(char)
                elif char in close and not stack:
                    corrupted = True
                    first_corrupted = char
                    break
                else:
                    if chunks[stack[-1]] == char:
                        stack.pop()
                    else:
                        corrupted = True
                        first_corrupted = char
                        break
            if corrupted:
                total += points[first_corrupted]
    return total


def part2():
    chunks = {'(':')',')':'(','{':'}','}':'{','[':']',']':'[','<':'>','>':'<'}
    open_ = ['(','{','[','<']
    close = [')''}',']','>']
    points = {'}':3,'>':4,']':2,')':1}
    total_points = []
    with open("solutions/day10_input.txt") as f:
        for line in f:
            stack = []
            corrupted = False
            for char in line.strip():
                if char == '':
                    break
                if char in open_:
                    stack.append(char)
                elif char in close and not stack:
                    corrupted = True
                    break
                else:
                    if chunks[stack[-1]] == char:
                        stack.pop()
                    else:
                        corrupted = True
                        break
            if stack and not corrupted:
                total = 0
                for i in range(len(stack)-1,-1,-1):
                    total = (total*5) + points[chunks[stack[i]]]
                total_points.append(total)
                

    sorted_total = sorted(total_points)
    middle = sorted_total[len(sorted_total)//2]
    return middle
            
        
if __name__ == '__main__':
    # part 1
    print(part1())

    # part 2
    print(part2())
