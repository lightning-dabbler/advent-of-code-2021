# https://adventofcode.com/2021/day/4

class GiantSquid:
    def __init__(self):
        self.matrix = []
        with open('solutions/day_04_input.txt',mode='r') as f:
            self.nums_to_draw = list(map(int,f.readline().strip().split(',')))
            for line in f:
                line = line.strip()
                if not line:
                    continue
                line = line.replace('  ',' ')
                self.matrix.append(list(map(int,line.split(' '))))

    def col_sum(self,matrix,start,col):
        return sum(matrix[i][col] for i in range(start,start+5))
    
    def row_sum(self,matrix,start,row):
        return sum(matrix[start+row])
    
    def final_score_part_1(self):
        type_,idx,group,last_num = self.determine_winner_part_1()
        start = group*5
        total = 0
        if type_ == 'row':
            for i in range(start,start+5):
                if i%5 == idx:
                    continue
                for j in range(5):
                    if self.score[i][j] == 0:
                        total+= self.matrix[i][j]
        else:
            for i in range(start,start+5):
                for j in range(5):
                    if j == idx:
                        continue
                    if self.score[i][j] == 0:
                        total+= self.matrix[i][j]
        return total*last_num

    def determine_winner_part_1(self):
        n =len(self.matrix)
        self.score = [[0 for i in range(5)] for j in range(n)]
        for num in self.nums_to_draw:
            for i in range(n):
                for j in range(5):
                    if self.matrix[i][j] == num:
                        self.score[i][j] +=1
            for i in range(0,n,5):
                for j in range(5):
                    col = self.col_sum(self.score,i,j)         
                    row = self.row_sum(self.score,i,j)
                    if col == 5:
                        return "col",j,i//5,num
                    if row ==5:
                        return "row",j,i//5,num

    def final_score_part_2(self):
        type_,idx,group,last_num = self.determine_winner_part_2()
        start = group*5
        total = 0
        if type_ == 'row':
            for i in range(start,start+5):
                if i%5 == idx:
                    continue
                for j in range(5):
                    if self.score[i][j] == 0:
                        total+= self.matrix[i][j]
        else:
            for i in range(start,start+5):
                for j in range(5):
                    if j == idx:
                        continue
                    if self.score[i][j] == 0:
                        total+= self.matrix[i][j]
        return total*last_num

    def determine_winner_part_2(self):
        n =len(self.matrix)
        boards = n//5
        winners = []
        self.score = [[0 for i in range(5)] for j in range(n)]
        for num in self.nums_to_draw:
            for i in range(n):
                for j in range(5):
                    if self.matrix[i][j] == num:
                        self.score[i][j] +=1
            for i in range(0,n,5):
                if i//5 in winners:
                    continue
                for j in range(5):
                    if i//5 in winners:
                        break
                    col = self.col_sum(self.score,i,j)         
                    row = self.row_sum(self.score,i,j)
                    if row ==5 and len(winners) == boards-1:
                        return "row",j,i//5,num

                    if col == 5 and len(winners) == boards-1:
                        return "col",j,i//5,num

                    if col == 5 or row == 5:
                        winners.append(i//5)
                    



if __name__ =='__main__':
    # part 1    
    gs_p1 = GiantSquid()
    print(gs_p1.final_score_part_1())

    # part 2
    gs_p2 = GiantSquid()
    print(gs_p2.final_score_part_2())
