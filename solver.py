class Solver:
    def __init__ (self, board, block_size):
        self.board = board
        self.block_size = block_size
        self.w = self.block_size[0]
        self.h = self.block_size[1]
        self.size = self.w * self.h

    def next_empty(self):
        # Find empty spot in the board
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    '''print("Next empty space: ({},{})".format(i, j))'''
                    return i, j
        return None

    def valid(self, x, y, num):
        # check if num can be placed at (x, y)
        for i in range(self.size):           # Check the Row
            if self.board[i][y] == num: return False

        for i in range(self.size):           # Check the Column
            if self.board[x][i] == num: return False

        block_x = x//self.w             # Check the Block
        block_y = y//self.h
        for i in range(block_x * self.w, block_x * self.w + self.w):
            for j in range(block_y * self.h, block_y * self.h + self.h):
                '''print("block space: ", i, j)'''
                if self.board[i][j] == num and (i,j) != (x,y):
                    return False
                
        '''print(x, y, "valid", num)'''
        return True
    
    def solve(self):
        spot = self.next_empty()
        if not spot:
            return True
        else:
            x, y = spot

        for i in range(self.w * self.h):
            if self.valid(x, y, i+1):
                self.board[x][y] = i+1

                if self.solve():        # Check if it can be solved with self.board[x][y] = i+1
                    return True
                '''print("messed up with ({}, {}) as {}".format(x, y, i+1))'''
                self.board[x][y] = 0    # Cannot be solved with self.board[x][y] = i+1

        return False        # Not possible to solve

    def printBoard(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i][j], end=" ")
                if (j+1)//self.w == (j+1)/self.w and j != self.size-1: print("| ", end="")
            print("")
            if (i+1)//self.h == (i+1)/self.h and i != self.size-1:
                print("--"*(self.size+1))
                i -= 1

                
if __name__ == "__main__":
    sample_board = [ [0, 0, 0, 1, 0, 0],
                     [0, 4, 0, 0, 0, 5],
                     [0, 0, 3, 0, 6, 0],
                     [0, 2, 0, 3, 0, 0],
                     [5, 0, 0, 0, 2, 0],
                     [0, 0, 6, 0, 0, 0]
    ]

    sample2x2 = [ [4, 0, 1, 0],
                  [0, 2, 0, 0],
                  [0, 0, 3, 0],
                  [0, 0, 0, 1]
    ]

    x = Solver(sample2x2, (2, 2))
    x.printBoard()
    print("")
    x.solve()
    print("\nSolution:")
    x.printBoard()