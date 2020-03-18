import pygame


def draw():
    pass


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('blue'))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
