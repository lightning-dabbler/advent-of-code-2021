# https://adventofcode.com/2021/day/5

def part1():
    verticals = []
    horizontals= []
    max_x = 0
    max_y = 0 
    with open("solutions/day_05_input.txt") as f:
        for line in f:
            left,right = line.strip().split('->')
            x1,y1 = map(int,left.strip().split(','))
            x2,y2 = map(int,right.strip().split(','))
            if x1==x2:
                verticals.append([x1,y1,y2])
            if y1==y2:
                horizontals.append([y1,x1,x2])
            if x1!=x2 and y1!=y2:
                continue
            max_x = max(max_x,x1,x2)
            max_y = max(max_y,y1,y2)

    matrix = [[0 for i in range(max_x+1)] for j in range(max_y+1)]

    for arr in verticals:
        positions = arr[1:]
        for i in range(min(positions),max(positions)+1):
            matrix[i][arr[0]]+=1

    for arr in horizontals:
        positions = arr[1:]
        for i in range(min(positions),max(positions)+1):
            matrix[arr[0]][i]+=1
    count = 0
    for i in range(max_x+1):
        for j in range(max_y+1):
            if matrix[i][j] >1:
                count+=1
    return count


def part2():
    verticals = []
    horizontals= []
    diagonal_eqs = []
    max_x = 0
    max_y = 0 
    with open("solutions/day_05_input.txt") as f:
        for line in f:
            left,right = line.strip().split('->')
            x1,y1 = map(int,left.strip().split(','))
            x2,y2 = map(int,right.strip().split(','))
            if x1==x2:
                verticals.append([x1,y1,y2])
            if y1==y2:
                horizontals.append([y1,x1,x2])
            if x1!=x2 and y1!=y2:
                m = (y2-y1)//(x2-x1)
                b = y2-(m*x2)
                diag_min_x = min(x1,x2)
                diag_max_x = max(x1,x2)
                diag_max_y = max(y1,y2)
                diag_min_y = min(y1,y2)
                
                diagonal_eqs.append(dict(slope=m,intercept=b,max_x=diag_max_x,min_x=diag_min_x,max_y=diag_max_y,min_y=diag_min_y))
            
            max_x = max(max_x,x1,x2)
            max_y = max(max_y,y1,y2)

    matrix = [[0 for i in range(max_x+1)] for j in range(max_y+1)]

    for arr in verticals:
        positions = arr[1:]
        for i in range(min(positions),max(positions)+1):
            matrix[i][arr[0]]+=1

    for arr in horizontals:
        positions = arr[1:]
        for i in range(min(positions),max(positions)+1):
            matrix[arr[0]][i]+=1
    
    for x in range(max_x+1):
        for obj in diagonal_eqs:
            if x < obj['min_x'] and x> obj['max_x']:
                continue
            y = (obj['slope']*x)+obj['intercept']
            if y >= obj['min_y'] and y<= obj['max_y']:
                matrix[y][x] +=1

    count = 0
    for i in range(max_x+1):
        for j in range(max_y+1):
            if matrix[i][j] >1:
                count+=1
    return count


if __name__ == '__main__':
    # part 1
    print(part1())

    # part 2
    print(part2())
