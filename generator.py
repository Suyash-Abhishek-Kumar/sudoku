from solver import Solver
import random

class Generator(Solver):
    def __init__(self, size, block_size):
        # Initialize an empty board
        board = [[0 for _ in range(size)] for _ in range(size)]
        super().__init__(board, block_size)

    def fill_diagonal_blocks(self):
        # Fill the diagonal blocks with random numbers
        for i in range(0, self.size, self.w):
            nums = list(range(1, self.size + 1))
            random.shuffle(nums)
            for x in range(self.w):
                for y in range(self.h):
                    self.board[i + x][i + y] = nums.pop()

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
        self.fill_diagonal_blocks()
        self.solve()  # Solve the board to ensure it's valid
        self.remove_numbers(num_holes)
        return self.board

if __name__ == "__main__":
    generator = Generator(size=9, block_size=(3, 3))
    generator.generate(num_holes=40)
    generator.printBoard()