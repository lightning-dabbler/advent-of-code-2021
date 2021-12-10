# https://adventofcode.com/2021/day/8

def part1():
    total = 0
    num_of_uni_sizes = [3,2,4,7]
    with open("solutions/day_08_input.txt") as f:
        for line in f:
            line = line.strip().split('|')
            output = line[1].strip().split(' ')
            patterns = line[0].strip().split(' ')
            for pattern in patterns:
                if len(pattern) not in num_of_uni_sizes:
                    continue
                for signal in output:
                    if len(set(pattern)&set(signal)) == len(signal) == len(pattern):
                        total +=1
            
    return total

def part2():
    total_sum = 0
    with open("solutions/day_08_input.txt") as f:
        for line in f:
            line = line.strip().split('|')
            output = line[1].strip().split(' ')
            patterns = line[0].strip().split(' ')
            map_ = {}
            values = [0 for i in range(4)]
            for pattern in patterns:
                if len(pattern) == 3:
                    map_[7] = pattern
                elif len(pattern) == 7:
                    map_[8] = pattern
                elif len(pattern) == 2:
                    map_[1] = pattern
                elif len(pattern) == 4:
                    map_[4] = pattern
            for pattern in patterns:
                if len(pattern) == 5 and len(set(pattern)&set(map_[1])) == 2:
                    value = '3'
                elif len(pattern) == 5 and len(set(pattern)&set(map_[4])) == 2:
                    value = '2'
                elif len(pattern) == 5 and len(set(pattern)&set(map_[4])) == 3:
                    value = '5'
                elif len(pattern) == 6 and len(set(pattern)&set(map_[1])) == 2 and len(set(pattern)&set(map_[4])) == 3:
                    value = '0'
                elif len(pattern) == 6 and len(set(pattern)&set(map_[1])) == 2 and len(set(pattern)&set(map_[4])) == 4:
                    value = '9'
                elif len(pattern) == 6 and len(set(pattern)&set(map_[1])) == 1:
                    value = '6'
                elif len(pattern) == 3:
                    value = '7'
                elif len(pattern) == 7:
                    value = '8'
                elif len(pattern) == 2:
                    value = '1'
                elif len(pattern) == 4:
                    value = '4'
                for idx,signal in enumerate(output):
                    if len(set(pattern)&set(signal)) == len(signal) == len(pattern):
                        values[idx] = value
            total = int(''.join(values))
            total_sum+=total
    return total_sum

if __name__ == '__main__':
    # part 1
    print(part1())

    # part 2
    print(part2())
