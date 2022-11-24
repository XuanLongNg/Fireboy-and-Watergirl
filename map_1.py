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
diamond_ground = pygame.sprite.Group()
lava_ground = pygame.sprite.Group()


# Add object

diamond_ground.add(Diamond(charAssets, block * 29, height - block*3))
diamond_ground.add(Diamond(charAssets, block * 23, block*4))
diamond_ground.add(Diamond(charAssets, block * 2, block*5))
diamond_ground.add(Diamond(charAssets, block * 23, block*14))

lava_ground.add(Lava(groundAssets, block * 18, height - block*1.5))
run = True
game_over = False
while run:
    draw_background()
    world.draw_map()
    for i in lava_ground:
        i.update_animation(screen)
    for i in diamond_ground:
        i.update_animation(screen, 2, True)
    moveX, moveY, game_over = player.update(
        moveX, moveY, world, game_over, lava_ground, diamond_ground)
    player.update_animation(moveX, moveY, screen)
    if game_over:
        run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(fps)
pygame.quit()
