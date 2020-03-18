import pygame


def draw():
    pygame.draw.line(screen, (255, 255, 255), (0, 0), (x, y), 5)
    pygame.draw.line(screen, (255, 255, 255), (x, 0), (0, y), 5)


pygame.init()
coords = input().split()
x = int(coords[0])
y = int(coords[-1])
size = width, height = x, y
screen = pygame.display.set_mode(size)
draw()
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
