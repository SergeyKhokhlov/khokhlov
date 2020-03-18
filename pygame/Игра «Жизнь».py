import pygame
import copy
import time


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for i in range(height)]
        self.left = 20
        self.top = 20
        self.cell_size = 28

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for x in range(self.height):
            for y in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255), (self.left + y * self.cell_size,
                                                           self.top + x * self.cell_size,
                                                           self.cell_size, self.cell_size),
                                 1 - self.board[x][y])
                if self.board[x][y]:
                    pygame.draw.rect(screen, (pygame.Color('green')), (self.left + y * self.cell_size,
                                                                       self.top + x * self.cell_size,
                                                                       self.cell_size, self.cell_size),
                                     1 - self.board[x][y])

    def get_cell(self, mouse_pos):  # координаты мыши
        cell = ((mouse_pos[0] - self.left) // self.cell_size,
                (mouse_pos[1] - self.top) // self.cell_size)
        if cell[0] < self.width and cell[1] < self.height and cell[0] >= 0 and cell[1] >= 0:
            return cell
        else:
            return None

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def on_click(self, cell_coords):
        if cell_coords:
            for i in range(7):
                for j in range(5):
                    self.board[cell_coords[1]][cell_coords[0]] \
                        = 1 - self.board[cell_coords[1]][cell_coords[0]]


class Life(Board):
    def next_move(self):
        board2 = [[0] * self.width for i in range(self.height)]
        for x in range(self.height):
            for y in range(self.width):
                count = self.board[x - 1][y] + self.board[x][(y + 1) % self.width] + self.board[x][y - 1] + \
                        self.board[(x + 1) % self.height][y] + \
                        self.board[x - 1][y - 1] + self.board[(x + 1) % self.height][(y + 1) % self.width] + \
                        self.board[(x + 1) % self.height][y - 1] + self.board[x - 1][(y + 1) % self.width]
                if count == 3:
                    board2[x][y] = 1
                elif count == 2 and self.board[x][y] == 1:
                    board2[x][y] = 1
        self.board = copy.deepcopy(board2)


pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
life = Life(20, 20)
running = True
fl = False
fps = 100
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                life.get_click(event.pos)
            if event.button == 3:
                fl = not fl
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fl = not fl
        if event.type == pygame.BUTTON_WHEELDOWN:
            if event.button == 4:
                fps += 10
            elif event.button == 5:
                if fps != 0:
                    fps -= 10

    if fl:
        life.next_move()
    screen.fill((0, 0, 0))
    life.render()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
