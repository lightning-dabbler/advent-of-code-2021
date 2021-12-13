def part1():
    folds = []
    points = []
    max_y = max_x = 0
    with open("solutions/day_13_input.txt") as f:
        for line in f:
            line = line.strip()
            if line.startswith('fold'):
                axis,magnitude = line.split(' ')[-1].split('=')
                folds.append((axis,int(magnitude)))
            elif not line:
                pass
            else:
                x,y = line.split(',')
                max_y = max(max_y,int(y))
                max_x = max(max_x,int(x))
                points.append((int(x),int(y)))
    grid = [[0 for i in range(max_x+1)] for j in range(max_y+1)]
    for point in points:
        grid[point[1]][point[0]] = 1
    boundary_x =max_x
    boundary_y = max_y
    for axis,magnitude in folds:
        if axis == 'y':
            idx = magnitude - (boundary_y-magnitude)
            for j in range(boundary_y,boundary_y-magnitude,-1):
                if idx >=0:
                    for i in range(boundary_x+1):
                        grid[idx][i] = max(grid[j][i],grid[idx][i])
                idx+=1
            boundary_y = magnitude-1
        else:
            idx = magnitude - (boundary_x-magnitude)
            for i in range(boundary_x,boundary_x-magnitude,-1):
                if idx >=0:
                    for j in range(boundary_y+1):
                        grid[j][idx] = max(grid[j][i],grid[j][idx])
                idx+=1
            boundary_x = magnitude-1
        break
    total_dots = 0
    for i in range(boundary_x+1):
        for j in range(boundary_y+1):
            total_dots+=grid[j][i]
    return total_dots
        
        
def part2():
    folds = []
    points = []
    max_y = max_x = 0
    with open("solutions/day_13_input.txt") as f:
        for line in f:
            line = line.strip()
            if line.startswith('fold'):
                axis,magnitude = line.split(' ')[-1].split('=')
                folds.append((axis,int(magnitude)))
            elif not line:
                pass
            else:
                x,y = line.split(',')
                max_y = max(max_y,int(y))
                max_x = max(max_x,int(x))
                points.append((int(x),int(y)))
    grid = [[0 for i in range(max_x+1)] for j in range(max_y+1)]
    for point in points:
        grid[point[1]][point[0]] = 1
    boundary_x =max_x
    boundary_y = max_y
    for axis,magnitude in folds:
        if axis == 'y':
            idx = magnitude - (boundary_y-magnitude)
            for j in range(boundary_y,boundary_y-magnitude,-1):
                if idx >=0:
                    for i in range(boundary_x+1):
                        grid[idx][i] = max(grid[j][i],grid[idx][i])
                idx+=1
            boundary_y = magnitude-1
        else:
            idx = magnitude - (boundary_x-magnitude)
            for i in range(boundary_x,boundary_x-magnitude,-1):
                if idx >=0:
                    for j in range(boundary_y+1):
                        grid[j][idx] = max(grid[j][i],grid[j][idx])
                idx+=1
            boundary_x = magnitude-1
    return [[grid[j][i] for i in range(boundary_x+1)] for j in range(boundary_y+1)]

if __name__ == '__main__':
    # part 1
    print("part 1:")
    print(part1())

    # part 2
    print("part 2:")
    print(*part2(),sep='\n') # decipher printed grid
