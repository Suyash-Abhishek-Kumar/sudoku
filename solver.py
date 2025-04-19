class Solver:
    def __init__ (self, board, block_size):
        self.board = board
        self.block_size = block_size
        self.w = self.block_size[0]
        self.h = self.block_size[1]
    
    def next_empty(self):
        # Find empty spot in the board
        for i in range(self.w):
            for j in range(self.h):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def valid(self, x, y, num):
        # check if num can be placed at (x, y)
        for i in range(self.w):         # Check the Row
            if self.board[i][y] == num: return False

        for i in range(self.h):         # Check the Column
            if self.board[x][i] == num: return False

        block_x = x//self.w             # Check the Block
        block_y = y//self.h
        for i in range(block_y*3, block_y*3 + self.h):
            for j in range(block_x*3, block_x*3 + self.w):
                if self.board[i][j] == num and (i,j) != (x,y):
                    return False
                
x = Solver([[0, 0, 0], [0, 0, 0], [0, 0, 0]], (1, 1))
# x.valid(0, 0, 2)