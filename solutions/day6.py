# https://adventofcode.com/2021/day/6

def num_lanternfish(arr,days):
    tally = {f'{i}':0 for i in range(9)}
    for i in arr:
        tally[i]+=1
    for i in range(days):
        pre_tally = tally.copy()
        if pre_tally['8']:
            tally['8'] -= pre_tally['8']
            tally['7'] += pre_tally['8']
        if pre_tally['7']:
            tally['7'] -= pre_tally['7']
            tally['6'] += pre_tally['7']
        if pre_tally['6']:
            tally['6'] -= pre_tally['6']
            tally['5'] += pre_tally['6']
        if pre_tally['5']:
            tally['5'] -= pre_tally['5']
            tally['4'] += pre_tally['5']
        if pre_tally['4']:
            tally['4'] -= pre_tally['4']
            tally['3'] += pre_tally['4']
        if pre_tally['3']:
            tally['3'] -= pre_tally['3']
            tally['2'] += pre_tally['3']
        if pre_tally['2']:
            tally['2'] -= pre_tally['2']
            tally['1'] += pre_tally['2']
        if pre_tally['1']:
            tally['1'] -= pre_tally['1']
            tally['0'] += pre_tally['1']
        if pre_tally['0']:
            tally['0'] -= pre_tally['0']
            tally['8'] += pre_tally['0']
            tally['6'] += pre_tally['0']
    total_fish = 0
    for _,v in tally.items():
        total_fish +=v
    return total_fish

if __name__ == '__main__':
    input_txt = open("solutions/day6_input.txt").read()
    arr = input_txt.strip().split(',')
    # part 1
    print(num_lanternfish(arr,80))
    # part 2
    print(num_lanternfish(arr,256))
