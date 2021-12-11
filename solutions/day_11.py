# https://adventofcode.com/2021/day/11

class Part1:
    def __init__(self,grid):
        self.grid = grid
        self.flashed = None
        self.total_flashes = 0
    
    def cascade_flash(self,i,j):
        if i < 0 or j < 0 or i >9 or j >9:
            return
        if self.flashed[i][j]:
            return
        self.grid[i][j]+=1
        if self.grid[i][j] > 9:
            self.grid[i][j] = 0
            self.flashed[i][j]= True
            self.cascade_flash(i+1,j)
            self.cascade_flash(i,j+1)
            self.cascade_flash(i-1,j)
            self.cascade_flash(i,j-1)
            self.cascade_flash(i+1,j+1)
            self.cascade_flash(i-1,j+1)
            self.cascade_flash(i-1,j-1)
            self.cascade_flash(i+1,j-1)
            self.total_flashes+=1
    
    def start(self):
        for _ in range(100):
            self.flashed = [[False for i in range(10)] for j in range(10)]
            for i in range(10):
                for j in range(10):
                    if self.flashed[i][j]:
                        continue    
                    self.grid[i][j]+=1
                    if self.grid[i][j] > 9:
                        self.grid[i][j] = 0
                        self.flashed[i][j]= True
                        self.cascade_flash(i+1,j)
                        self.cascade_flash(i,j+1)
                        self.cascade_flash(i-1,j)
                        self.cascade_flash(i,j-1)
                        self.cascade_flash(i+1,j+1)
                        self.cascade_flash(i-1,j+1)
                        self.cascade_flash(i-1,j-1)
                        self.cascade_flash(i+1,j-1)
                        self.total_flashes+=1

def part1():
    grid = []

    with open("solutions/day_11_input.txt") as f:
        for line in f:
            grid.append([int(num) for num in line.strip()])

    p = Part1(grid)
    p.start()
    return p.total_flashes



class Part2:
    def __init__(self,grid):
        self.grid = grid
        self.flashed = None
        self.grid_total = 0
        self.step = 1
        for i in range(10):
            for j in range(10):
                self.grid_total+=grid[i][j]

    def cascade_flash(self,i,j):
        if i < 0 or j < 0 or i >9 or j >9:
            return
        if self.flashed[i][j]:
            return
        self.grid[i][j]+=1
        self.grid_total+=1
        if self.grid[i][j] > 9:
            self.grid[i][j] = 0
            self.grid_total -= 10
            self.flashed[i][j]= True
            self.cascade_flash(i+1,j)
            self.cascade_flash(i,j+1)
            self.cascade_flash(i-1,j)
            self.cascade_flash(i,j-1)
            self.cascade_flash(i+1,j+1)
            self.cascade_flash(i-1,j+1)
            self.cascade_flash(i-1,j-1)
            self.cascade_flash(i+1,j-1)
    
    def start(self):
        while True:
            self.flashed = [[False for i in range(10)] for j in range(10)]
            for i in range(10):
                for j in range(10):
                    if self.flashed[i][j]:
                        continue    
                    self.grid[i][j]+=1
                    self.grid_total+=1
                    if self.grid[i][j] > 9:
                        self.grid[i][j] = 0
                        self.grid_total -= 10
                        self.flashed[i][j]= True
                        self.cascade_flash(i+1,j)
                        self.cascade_flash(i,j+1)
                        self.cascade_flash(i-1,j)
                        self.cascade_flash(i,j-1)
                        self.cascade_flash(i+1,j+1)
                        self.cascade_flash(i-1,j+1)
                        self.cascade_flash(i-1,j-1)
                        self.cascade_flash(i+1,j-1)
                        
            if self.grid_total == 0:
                return
            self.step+=1

def part2():
    grid = []

    with open("solutions/day_11_input.txt") as f:
        for line in f:
            grid.append([int(num) for num in line.strip()])
    p = Part2(grid)
    p.start()
    return p.step

if __name__ == '__main__':
    # part 1
    print(part1())

    # part 2
    print(part2())
