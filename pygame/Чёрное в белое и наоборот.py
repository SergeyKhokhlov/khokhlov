import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for i in range(height)]
        self.left = 60
        self.top = 40
        self.cell_size = 30

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
                    self.board[i][cell_coords[0]] = \
                        1 - self.board[i][cell_coords[0]]
                    self.board[cell_coords[1]][j] = \
                        1 - self.board[cell_coords[1]][j]
                    self.board[cell_coords[1]][cell_coords[0]] \
                        = 1 - self.board[cell_coords[1]][cell_coords[0]]


pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
board = Board(5, 7)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
pygame.quit()
