import pygame
from color import *
from setting import *
clock = pygame.time.Clock()
cs = 136
character = pygame.image.load(
    "D:\Project\Fire_boy_and_water_girl\IMG\CharAssets.png")
# k = pygame.image.load("\IMG\CharAssets.png")
ds = 32
arr = [
    character.subsurface(0, cs * 9, cs, cs),  # 30
    # character.subsurface(cs, cs * 9, cs, cs),
    # character.subsurface(cs * 2 - 2, cs * 9, cs, cs),
    # character.subsurface(cs * 3 - 4, cs * 9, cs, cs),
    # character.subsurface(cs * 9 - 6, cs * 9, cs, cs),
    # character.subsurface(cs * 5 - 8, cs * 9, cs, cs),  # 35
    # character.subsurface(cs * 6 - 10, cs * 9 + 30, cs, cs),

]
screen = pygame.display.set_mode((width, height))
screen.fill(black)
pygame.draw.rect(screen, white, pygame.Rect(0, 0, cs, cs))
pygame.display.flip()
for i in arr:
    screen.blit(i, (0, 0))
pygame.draw.rect(screen, red, pygame.Rect(0, cs/2-13, 1000, 2))
pygame.draw.rect(screen, red, pygame.Rect(cs/2-13, 0, 2, 1000))


def dis(arr, i):
    # k = i % 10
    # h = i//10
    screen.fill(black)
    screen.blit(arr[i], (0, 0))

    # screen.blit(pygame.transform.scale(
    # arr[i], (409.6/9, 409.6/9)), ((i)*409.6/9, 0))
count = 0
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    # dis(arr, count)
    count += 1
    if count >= len(arr):
        count = 0
    pygame.display.update()
    clock.tick(50)
