from solver import Solver
import random

class Generator(Solver):
    def __init__(self, size, block_size):
        # Initialize an empty board
        board = [[0 for _ in range(size)] for _ in range(size)]
        super().__init__(board, block_size)
        self.printBoard()

    def fill_diagonal_blocks(self):
        # Fill the diagonal blocks with random numbers
        for block in range(min(self.w, self.h)):
            i = block * self.h  # Row index for the top-left corner of the block
            j = block * self.w  # Column index for the top-left corner of the block
            nums = list(range(1, self.size + 1))
            random.shuffle(nums)
            for x in range(self.h):
                for y in range(self.w):
                    print(i + x, j + y)
                    self.board[i + x][j + y] = nums.pop()
    
    def bruteforce_fill(self):
        for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] == 0:
                        nums = list(range(1, self.size + 1))
                        random.shuffle(nums)
                        for num in nums:
                            if self.valid(i, j, num):
                                self.board[i][j] = num
                                break

    def remove_numbers(self, num_holes):
        # Remove numbers randomly to create the puzzle
        count = num_holes
        while count > 0:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.board[x][y] != 0:
                self.board[x][y] = 0
                count -= 1

    def generate(self, num_holes):
        # Generate a Sudoku puzzle
        if self.w != self.h:        # If the block size is not square, fill the board using brute force
            self.bruteforce_fill()
        else:
            self.fill_diagonal_blocks()
            self.solve()            # Solve the board to ensure it's valid
        self.remove_numbers(num_holes)
        return self.board

if __name__ == "__main__":
    generator = Generator(size=8, block_size=(2, 4))
    generator.generate(num_holes=10)
    generator.printBoard()