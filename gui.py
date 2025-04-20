import pygame #type: ignore
from generator import Generator
from buttons import Button
import colors
import random

class Sudoku:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((450, 600))
        pygame.display.set_caption("Sudoku")
        pygame.display.set_icon(pygame.image.load(".\\sudoku_icon.png"))
        self.base_font = pygame.font.Font(None, 36)
        self.tiny_font = pygame.font.Font(None, 16)
        self.heading_font = pygame.font.Font(".\\fonts\\ka1.ttf", 56)
        self.size = 9
        self.holes = random.randint(40, 60)
        self.block_size = (3, 3)
        self.board, self.solved_board = Generator(size=self.size, block_size=self.block_size).generate(num_holes=self.holes)
        self.buttons = { Button(self.screen, (125, 500), 3, "Solve", self.solve_board, text_color= colors.WHITE, button_color=colors.update_brightness(colors.GRAY, 30), fixed_size=(100, 30)),
                         Button(self.screen, (125, 550), 3, "Check", self.check_board, text_color= colors.WHITE, button_color=colors.update_brightness(colors.GRAY, 30), fixed_size=(100, 30)),
                         Button(self.screen, (325, 500), 3, "Generate", self.generate_board, text_color= colors.WHITE, button_color=colors.update_brightness(colors.GRAY, 30), fixed_size=(100, 30)),
                         Button(self.screen, (325, 550), 3, "Reset", self.reset_board, text_color= colors.WHITE, button_color=colors.update_brightness(colors.GRAY, 30), fixed_size=(100, 30))
        }
        self.input_board = [[0 for _ in range(self.size)] for _ in range(self.size)]

        board_width = self.size * 40
        offset_x = (450 - board_width) // 2
        offset_y = 100
        self.coords = [[(j * 40 + offset_x, i * 40 + offset_y, j * 40 + offset_x + 40, i * 40 + offset_y + 40) for i in range(self.size)] for j in range(self.size)]
        self.selected = None
        self.check = False
        self.solve = False
        self.i, self.j = 0, 0
        self.last_click = pygame.time.get_ticks()
        self.click_wait = 500
        self.can_click = True
        self.clock = pygame.time.Clock()

    def solve_board(self): self.solve = True
    def check_board(self): self.check = True

    def reset_board(self):
        self.solve = False
        self.check = False
        self.input_board = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def generate_board(self):
        self.solve = False
        self.check = False
        self.board, self.solved_board = Generator(size=self.size, block_size=self.block_size).generate(num_holes=self.holes)
        self.input_board = [[0 for _ in range(self.size)] for _ in range(self.size)]

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
                                break
                    self.selected = self.find_selected(pygame.mouse.get_pos())  # Find the selected cell based on mouse position

            self.screen.fill((255, 255, 255))
            if self.selected and self.can_click: self.input()
            self.draw_board()
            for i in self.buttons:
                i.run()
            self.cooldown()
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

    def find_selected(self, mouse):  # Find the selected cell based on mouse position
        for i in range(self.size):
            for j in range(self.size):
                if self.coords[i][j][0] < mouse[0] < self.coords[i][j][2] and self.coords[i][j][1] < mouse[1] < self.coords[i][j][3]:
                    return (i, j)
        return None

    def draw_board(self):       # Draw the Sudoku board
        # Draw the heading
        heading_text = self.heading_font.render("Sudoku", True, (0, 0, 0))
        heading_rect = heading_text.get_rect(center=(225, 50))
        self.screen.blit(heading_text, heading_rect)

        # Draw the outer border of the Sudoku board
        board_width = self.size * 40
        board_height = self.size * 40
        offset_x = (450 - board_width) // 2
        offset_y = 100
        pygame.draw.rect(self.screen, (240, 240, 240), (offset_x, offset_y, board_width, board_height), 0)
        pygame.draw.rect(self.screen, (0, 0, 0), (offset_x, offset_y, board_width, board_height), 2)

        # Draw the grid lines
        # Horizontal lines
        for i in range(self.size + 1):
            line_width = 3 if i % self.block_size[0] == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0), (offset_x, offset_y + i * 40), (offset_x + board_width, offset_y + i * 40), line_width)
        
        # Vertical lines
        for i in range(self.size + 1):
            line_width = 3 if i % self.block_size[1] == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0), (offset_x + i * 40, offset_y), (offset_x + i * 40, offset_y + board_height), line_width)

        if self.selected:
            pygame.draw.rect(self.screen, colors.RED, (*self.coords[self.selected[0]][self.selected[1]][:2], 40, 40), 3)
        '''if self.i < 8*4 or self.j < 8:
            if self.i < 8*4:
                self.i += 1
            else:
                self.i = 0
                self.j += 1
        else:
            self.i, self.j = 0, 0'''

        # Draw the numbers
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != 0:
                    text = self.base_font.render(str(self.board[i][j]), True, (0, 0, 0))
                    self.screen.blit(text, (offset_x + j * 40 + 15, offset_y + i * 40 + 10))

                elif self.solve:
                    text = self.base_font.render(str(self.solved_board[i][j]), True, colors.update_brightness(colors.GREEN, -50))
                    self.screen.blit(text, (offset_x + j * 40 + 15, offset_y + i * 40 + 10))

                elif self.check:
                    if self.input_board[i][j] != self.solved_board[i][j]:
                        text = self.base_font.render(str(self.solved_board[i][j]), True, colors.update_brightness(colors.RED, -50))
                        self.screen.blit(text, (offset_x + j * 40 + 15, offset_y + i * 40 + 10))
                    elif self.input_board[i][j] != 0 and self.input_board[i][j] == self.solved_board[i][j]:
                        text = self.base_font.render(str(self.solved_board[i][j]), True, colors.update_brightness(colors.GREEN, -50))
                        self.screen.blit(text, (offset_x + j * 40 + 15, offset_y + i * 40 + 10))
                    else:
                        print(self.solved_board[i][j], self.input_board[i][j])
                        text = self.base_font.render(str(self.solved_board[i][j]), True,colors.GRAY)
                        self.screen.blit(text, (offset_x + j * 40 + 15, offset_y + i * 40 + 10))
                
                if self.input_board[i][j] != 0:
                    guess = self.tiny_font.render(str(self.input_board[i][j]), True, colors.GRAY)
                    self.screen.blit(guess, (offset_x + j * 40 + 5, offset_y + i * 40 + 5))

    def input(self):
        keys = pygame.key.get_pressed()
        key = None
        if keys[pygame.K_1] or keys[pygame.K_KP1]:
            key = 1
        elif keys[pygame.K_2] or keys[pygame.K_KP2]:
            key = 2
        elif keys[pygame.K_3] or keys[pygame.K_KP3]:
            key = 3
        elif keys[pygame.K_4] or keys[pygame.K_KP4]:
            key = 4
        elif keys[pygame.K_5] or keys[pygame.K_KP5]:
            key = 5
        elif keys[pygame.K_6] or keys[pygame.K_KP6]:
            key = 6
        elif keys[pygame.K_7] or keys[pygame.K_KP7]:
            key = 7
        elif keys[pygame.K_8] or keys[pygame.K_KP8]:
            key = 8
        elif keys[pygame.K_9] or keys[pygame.K_KP9]:
            key = 9
        elif keys[pygame.K_DELETE]:
            key = None
                
        if key is not None and self.board[self.selected[1]][self.selected[0]] == 0:
            self.input_board[self.selected[1]][self.selected[0]] = key
            self.can_click = False
            key = None
            self.last_click = pygame.time.get_ticks()
        
                # if event.key == pygame.K_RETURN:
                #     i, j = board.selected
                #     if board.cubes[i][j].temp != 0:
                #         if board.place(board.cubes[i][j].temp):
                #             print("Success")
                #         else:
                #             print("Wrong")
                #             strikes += 1
                #         key = None

                #         if board.is_finished():
                #             print("Game over")
    
    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_click >= self.click_wait:
            self.can_click = True

x = Sudoku()
x.run()