import pygame


def draw():
    couner = 0
    for i in range(count):
        pygame.draw.rect(screen, color, (10, 10, 100, 100), 0)


pygame.init()
coords = input().split()
coord_w = int(coords[0])
count = int(coords[-1])
size = width, height = coord_w, coord_w
screen = pygame.display.set_mode(size)
draw()
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
