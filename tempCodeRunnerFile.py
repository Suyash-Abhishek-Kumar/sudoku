generator = Generator(size=self.size, block_size=self.block_size)
        self.board = generator.generate(num_holes=self.holes)
        new_board = [row[:] for row in self.board]  # Ensure a deep copy of the board
        solver = Solver(new_board, self.block_size)
        if solver.solve():
            self.solved_board = solver.board
        else:
            raise ValueError("The generated Sudoku puzzle could not be solved.")
