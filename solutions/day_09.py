# https://adventofcode.com/2021/day/9

import heapq

def part1():
    total_sum = 0
    matrix = []
    with open("solutions/day_09_input.txt") as f:
        for line in f:
            matrix.append(line.strip())
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if i > 0 and j<m-1 and j>0 and i<n-1:
                values = [int(matrix[i-1][j]),int(matrix[i][j+1]),int(matrix[i+1][j]),int(matrix[i][j-1])] 
                
            elif i == 0 and j==m-1:
                values = [int(matrix[i+1][j]),int(matrix[i][j-1])]
            
            elif i == 0 and j==0:
                values = [int(matrix[i+1][j]),int(matrix[i][j+1])]
                
            elif i == n-1 and j==0:
                values = [int(matrix[i-1][j]),int(matrix[i][j+1])]
            
            elif i == n-1 and j==m-1:
                values = [int(matrix[i-1][j]),int(matrix[i][j-1])]
            
            elif i >0 and i<n-1 and j ==0:
                values = [int(matrix[i-1][j]),int(matrix[i+1][j]),int(matrix[i][j+1])]
                
            
            elif i >0 and i<n-1 and j ==m-1:
                values = [int(matrix[i+1][j]),int(matrix[i][j-1]),int(matrix[i-1][j])]
        
            
            elif j >0 and j<m-1 and i ==0:
                values = [int(matrix[i+1][j]),int(matrix[i][j-1]),int(matrix[i][j+1])]
                
            elif j >0 and j<m-1 and i ==n-1:
                values = [int(matrix[i-1][j]),int(matrix[i][j-1]),int(matrix[i][j+1])]
                
            
            if min(values) > int(matrix[i][j]):
                total_sum += int(matrix[i][j])+1
            
    return total_sum

class Basin:
    def __init__(self,basins):
        self.basins = basins
        self.size = 0

    def find_basin_size(self,n,m,i,j):
        if i < 0 or j>m-1 or j <0 or i >n-1:
            return
        if self.basins[i][j] != 1:
            return
        else:
            self.size+=1
            self.basins[i][j] = 0
            self.find_basin_size(n,m,i-1,j)
            self.find_basin_size(n,m,i,j-1)
            self.find_basin_size(n,m,i+1,j)
            self.find_basin_size(n,m,i,j+1)

def part2():
    matrix = []
    with open("solutions/day_09_input.txt") as f:
        for line in f:
            matrix.append(line.strip())
    low_points = []
    n = len(matrix)
    m = len(matrix[0])
    basins_matrix = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if int(matrix[i][j])!= 9:
                basins_matrix[i][j] = 1      
            if i > 0 and j<m-1 and j>0 and i<n-1:
                values = [int(matrix[i-1][j]),int(matrix[i][j+1]),int(matrix[i+1][j]),int(matrix[i][j-1])]
                
            elif i == 0 and j==m-1:
                values = [int(matrix[i+1][j]),int(matrix[i][j-1])]
            
            elif i == 0 and j==0:
                values = [int(matrix[i+1][j]),int(matrix[i][j+1])]
                
            elif i == n-1 and j==0:
                values = [int(matrix[i-1][j]),int(matrix[i][j+1])]
            
            elif i == n-1 and j==m-1:
                values = [int(matrix[i-1][j]),int(matrix[i][j-1])]
            
            elif i >0 and i<n-1 and j ==0:
                values = [int(matrix[i-1][j]),int(matrix[i+1][j]),int(matrix[i][j+1])]
                
            
            elif i >0 and i<n-1 and j ==m-1:
                values = [int(matrix[i+1][j]),int(matrix[i][j-1]),int(matrix[i-1][j])]
        
            
            elif j >0 and j<m-1 and i ==0:
                values = [int(matrix[i+1][j]),int(matrix[i][j-1]),int(matrix[i][j+1])]
                
            else:
                values = [int(matrix[i-1][j]),int(matrix[i][j-1]),int(matrix[i][j+1])]
                
            
            if min(values) > int(matrix[i][j]):
                low_points.append([i,j])

    sizes =[]
    for i,j in low_points:
        basin = Basin(basins_matrix)
        basin.find_basin_size(n,m,i,j)
        heapq.heappush(sizes,(-1*basin.size,basin.size))

    return heapq.heappop(sizes)[1]*heapq.heappop(sizes)[1]*heapq.heappop(sizes)[1]

if __name__ == '__main__':
    # part 1
    print(part1())

    # part 2
    print(part2())    
