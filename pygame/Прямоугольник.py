import pygame


def draw():
    pygame.draw.rect(screen, (255, 0, 0), (1, 1, coord_x - 2, coord_y - 2), 0)


pygame.init()
coords = input().split()
coord_x = int(coords[0])
coord_y = int(coords[-1])
size = width, height = coord_x, coord_y
screen = pygame.display.set_mode(size)
draw()
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
