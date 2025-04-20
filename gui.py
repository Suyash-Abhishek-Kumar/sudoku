import pygame #type: ignore
from solver import Solver
from generator import Generator
from buttons import Button
import colors

class Sudoku:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("Sudoku")
        self.base_font = pygame.font.Font(None, 36)
        self.heading_font = pygame.font.Font(".\\fonts\\ka1.ttf", 56)
        self.size = 9
        self.holes = 40
        self.block_size = (3, 3)
        self.board = Generator(size=self.size, block_size=self.block_size).generate(num_holes=self.holes)

        copy_board = [row[:] for row in self.board]  # Ensure a deep copy of the board
        solver = Solver(copy_board, self.block_size)
        solver.solve()
        self.solved_board = solver.board
        
        self.buttons = { Button(self.screen, (280, 600), 3, "Solve", self.solve_board, text_color= colors.WHITE, button_color=colors.update_brightness(colors.GRAY, 30), hover="darken"),
                         Button(self.screen, (280, 650), 3, "Generate", self.generate_board, text_color= colors.WHITE, button_color=colors.update_brightness(colors.GRAY, 30), hover="darken"),
                         Button(self.screen, (280, 700), 3, "Reset", self.reset_board, text_color= colors.WHITE, button_color=colors.update_brightness(colors.GRAY, 30), hover="darken")
        }
        self.solve = False
        self.clock = pygame.time.Clock()

    def solve_board(self): self.solve = True
    def reset_board(self): self.solve = False
    def generate_board(self):
        self.board = Generator(size=self.size, block_size=self.block_size).generate(num_holes=self.holes)
        copy_board = [row[:] for row in self.board]  # Ensure a deep copy of the board
        solver = Solver(copy_board, self.block_size)
        solver.solve()
        self.solved_board = solver.board

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for j in self.buttons:
                            if j.collision_check():
                                j.function()
                                continue

            self.screen.fill((255, 255, 255))
            self.draw_board()
            for i in self.buttons:
                i.run()
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

    def draw_board(self):       # Draw the Sudoku board
        # Draw the heading
        heading_text = self.heading_font.render("Sudoku", True, (0, 0, 0))
        heading_rect = heading_text.get_rect(center=(300, 50))
        self.screen.blit(heading_text, heading_rect)

        # Draw the outer border of the Sudoku board
        board_width = self.size * 40
        board_height = self.size * 40
        offset_x = (600 - board_width) // 2
        offset_y = 100
        pygame.draw.rect(self.screen, (240, 240, 240), (offset_x, offset_y, board_width, board_height), 0)
        pygame.draw.rect(self.screen, (0, 0, 0), (offset_x, offset_y, board_width, board_height), 2)

        # Draw the grid lines
        for i in range(self.size + 1):
            line_width = 3 if i % self.block_size[0] == 0 else 1
            # Horizontal lines
            pygame.draw.line(self.screen, (0, 0, 0), (offset_x, offset_y + i * 40), (offset_x + board_width, offset_y + i * 40), line_width)
            # Vertical lines
            pygame.draw.line(self.screen, (0, 0, 0), (offset_x + i * 40, offset_y), (offset_x + i * 40, offset_y + board_height), line_width)

        # Draw the numbers
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != 0:
                    text = self.base_font.render(str(self.board[i][j]), True, (0, 0, 0))
                    self.screen.blit(text, (offset_x + j * 40 + 15, offset_y + i * 40 + 10))
                elif self.solve:
                    text = self.base_font.render(str(self.solved_board[i][j]), True, (255, 0, 0))
                    self.screen.blit(text, (offset_x + j * 40 + 15, offset_y + i * 40 + 10))

x = Sudoku()
x.run()