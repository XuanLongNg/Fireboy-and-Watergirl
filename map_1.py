import pygame
import pickle
from pygame.locals import *
from setting import *
from character import *
from Map import *
from Object import *
from os import path

pygame.init()
pygame.display.set_caption('Platformer')

# define game variables
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 20
moveX, moveY = 0, 0
x, y = 0, 0
level = 1
world_data = []
if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')
    world_data = pickle.load(pickle_in)


# object initialization
player = Character(charAssets, block*2, height - block*6)
world = Map(world_data)
# lava = [Lava(groundAssets, block * 18, height - block*1.5)]
diamond = [Diamond(charAssets, block * 29, height - block*3),
           Diamond(charAssets, block * 23, block*4),
           Diamond(charAssets, block * 2, block*5),
           Diamond(charAssets, block * 23, block*14)]
run = True
game_over = False
while run:
    draw_background()
    world.draw_map()
    # lava[0].update_animation(screen)
    for i in diamond:
        i.update_animation(screen, 2, True)
    moveX, moveY = player.update(moveX, moveY, world, game_over, 0, diamond)
    player.update_animation(moveX, moveY, screen)
    # print(game_over)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(fps)
pygame.quit()
