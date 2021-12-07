# https://adventofcode.com/2021/day/3

import os
from collections import defaultdict

# part 1
def part1():
    tally = defaultdict(dict)
    gamma = ''
    epsilon = ''
    with open('solutions/day3_input.txt',mode='r') as f:
        for line in f:
            binary_num = line.strip()
            for idx,i in enumerate(binary_num):
                tally[idx].setdefault(i,0)
                tally[idx][i]+=1

    for k,v in tally.items():
        if v['0'] > v['1']:
            gamma+='0'
            epsilon+='1'
        else:
            gamma+='1'
            epsilon+='0'
    
    return int(gamma,2)*int(epsilon,2)


# part 2

class LifeSupport:
    def __init__(self):
        self.co2 = self.o2 = ''
    def start(self):
        arr = []
        with open('solutions/day3_input.txt',mode='r') as f:
            for line in f:
                binary_num = line.strip()
                arr.append(binary_num)
        max_length = len(arr[0])
        self.get_o2_and_co2_ratings(arr,0,max_length)
        self.get_o2_and_co2_ratings(arr,0,max_length,o2_rating=False)
        return int(self.co2,2)*int(self.o2,2)
    
    def get_o2_and_co2_ratings(self,arr,index,max_length,o2_rating=True):
        if index == max_length:
            return
        tally = [0,0]
        new_arr = []
        for num in arr:
            if num[index] =='0':
                tally[0]+=1
            else:
                tally[1]+=1
        
        if tally[0] > tally[1]:
            if o2_rating:
                self.o2+='0'
            else:
                self.co2+='1'
        else:
            if o2_rating:
                self.o2+='1'
            else:
                self.co2+='0'
        for item in arr:
            if o2_rating and item[index]==self.o2[-1]:
                new_arr.append(item)
            elif not o2_rating and item[index] == self.co2[-1]:
                new_arr.append(item)
        if len(new_arr) == 1:
            if o2_rating:
                self.o2 =new_arr[0]
            else:
                self.co2 =new_arr[0]
            return
        self.get_o2_and_co2_ratings(new_arr,index+1,max_length,o2_rating=o2_rating)

if __name__ == '__main__':
    # part 1
    print(part1())

    # part 2
    ls = LifeSupport()
    print(ls.start())
