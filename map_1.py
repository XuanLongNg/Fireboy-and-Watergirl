import pygame
import pickle
from pygame.locals import *
from setting import *
from Character import *
from Map import *
from os import path

pygame.init()
pygame.display.set_caption('Platformer')

# define game variables
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 20
ani_head, ani_body = 0, 0
moveX, moveY, bottom = 0, 0, 0
x, y = 0, 0
level = 1
world_data = []
if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')
    world_data = pickle.load(pickle_in)


player = Character(charAssets, block*2, height - block*6)
world = Map(world_data)

game_over = True
while game_over:
    draw_background()
    world.draw_map()
    # bottom = world.world_data[int(player.rect_body[1] //
    #                           block)+1][int(player.rect_body[0]//block)]
    moveX, moveY = player.update(moveX, moveY, world.world_data)
    ani_head, ani_body = player.update_animation(
        moveX, moveY, screen, ani_head, ani_body)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False

    pygame.display.update()
    clock.tick(fps)
pygame.quit()
