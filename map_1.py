import pygame
import img
from color import *
from character import *
from setting import *

source = pygame.image.load(
    "D:\Project\Fire_boy_and_water_girl\IMG\CharAssets.png")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

pygame.draw.rect(screen, white, pygame.Rect(0, 700, 1366, 68))
map = []
for i in range(0, width, 20):
    map.append((i, True))
map.append((map[-1][0]+20, True))
# for i in map:
#     print(i)

animation = 0
animation_dia = 0
step = 0.2
game_over = False

while not game_over:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    char = Character(source)
    diamond = Diamond(source)
    animation = char.update_animation(0, 0, screen, 150, 150, animation)
    animation_dia, step = diamond.update_animation(
        screen, 250, 250, animation_dia, step)
    pygame.display.update()
    clock.tick(50)
pygame.quit()
