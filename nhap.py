import pygame
from setting import *
clock = pygame.time.Clock()
ibs = 32
character = pygame.image.load('IMG/CharAssets.png')
topographic = pygame.transform.scale(templeAssets.subsurface(
    ibs*16+8, ibs * 16+8, ibs*8, ibs*8), (block*8, block*8))
# k = pygame.image.load("\IMGCharAssets.png")
cs = 136
arr = [
    character.subsurface(cs*11-11.1, 15, cs, cs),  # 11
    character.subsurface(cs*12+30, 15, cs, cs),
    character.subsurface(cs*13+72, 15, cs, cs),
    character.subsurface(cs*11-11.1, 161, cs, cs),
    character.subsurface(cs*12+30, 161, cs, cs),  # 15
    character.subsurface(cs*13+72, 161, cs, cs),
    character.subsurface(10.1, 223, cs, cs),
    character.subsurface(cs+52, 223, cs, cs),
    character.subsurface(cs*2+94, 223, cs, cs),
    character.subsurface(cs*4, 223, cs, cs),
    character.subsurface(cs*5+42, 223, cs, cs),
]
body = character.subsurface(cs*6+90, cs*2, cs, cs)
screen = pygame.display.set_mode((width, height))


def draw_grid():
    for i in range(rows):
        pygame.draw.line(screen, black, (0, i*block), (width, i*block))
    for i in range(cols):
        pygame.draw.line(screen, black, (i*block, 0), (i*block, width))


screen.fill(white)
draw_grid()
pygame.display.flip()
# for i in range(len(arr)):
#     # for j in range(len(arr[i])):
#     # screen.blit(arr[i][j], (ibs*5+block*i, ibs*5+block*j))
#     screen.blit(pygame.transform.scale(
#         arr[i], (block*3, block*3)), (ibs*5+block, ibs*5+block))


def dis(arr, i):
    # k = i % 10
    # h = i//10
    screen.fill(white)
    draw_grid()
    screen.blit(pygame.transform.scale(
        body, (block*3, block*3)), (block*5-block/2, block*5-block/2))
    screen.blit(pygame.transform.scale(
        arr[i], (block*3, block*3)), (block*5-block*1.2, block*5-block*1.2))


    # screen.blit(pygame.transform.scale(
    # arr[i], (409.6/9, 409.6/9)), ((i)*409.6/9, 0))
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
