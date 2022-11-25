import pygame
from setting import *
clock = pygame.time.Clock()
ibs = 32
object = templeAssets
block = 50
cs = 136
arr = [
    object.subsurface(ibs*0.7, ibs*37-ibs*0.2, ibs*3+ibs*0.6, ibs*4),  # 0

]
screen = pygame.display.set_mode((width, height))


def draw_grid():
    for i in range(rows):
        pygame.draw.line(screen, black, (0, i*block), (width, i*block))
    for i in range(cols):
        pygame.draw.line(screen, black, (i*block, 0), (i*block, width))


# for i in range(len(arr)):
#     screen.blit(pygame.transform.scale(
#         arr[i], (block*2, block*2)), (block*3, block*5))


def dis(arr, i):
    screen.fill(white)
    # screen.fill(black)
    draw_grid()
    # pygame.draw.rect(screen, white, pygame.Rect(0, 0, cs, cs))
    img = arr[i]
    img = pygame.transform.scale(arr[i], (block*3 + block*0.6, block*4))
    screen.blit(img, (block*2, block*2))
    # pygame.draw.rect(screen, blue, pygame.Rect(0, cs/2-1, cs*4, 2))
    # pygame.draw.rect(screen, blue, pygame.Rect(0, cs*0.75, cs*4, 2))
    # pygame.draw.rect(screen, blue, pygame.Rect(cs/2-1, 0, 2, cs*4))
    # pygame.draw.rect(screen, blue, pygame.Rect(cs*0.25, 0, 2, cs*4))


count = 0
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    dis(arr, count)
    count += 1
    if count >= len(arr):
        count = 0
    pygame.display.update()
    clock.tick(10)
