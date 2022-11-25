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
player1 = Character1(block*2, height - block*6)
player2 = Character2(block*2, height - block*2)
world = Map(world_data)
diamond_ground = pygame.sprite.Group()
lava_ground = pygame.sprite.Group()
box = []
linked = []
# Add object

diamond_ground.add(Diamond(block * 29, height - block*4))
diamond_ground.add(Diamond(block * 23, block*3))
diamond_ground.add(Diamond(block * 2, block*4))
diamond_ground.add(Diamond(block * 23, block*13))

lava_ground.add(Lava(block * 18, height - block*1.5))

linked.append(Linked([Button(block*8, height - block*10, blue)],
                     [TransportBar(block, block*15, 4, red, 0, 4)]))
linked.append(Linked([Button(block*10, height - block*15, red),
                     Button(block*29, height - block*19, red)],
                     [TransportBar(width-5*block, block*11, 4, blue, 0, 4)]))

box.append(Box(block*22, height - block*22))
run = True
game_over = False
change1, change2 = [], []
for i in range(len(linked)):
    tmp1 = []
    tmp2 = []
    for j in range(len(linked[i].impact)):
        tmp1.append(False)
        tmp2.append(False)
    change1.append(tmp1)
    change2.append(tmp2)
while run:
    draw_background()
    for i in range(len(linked)):
        check = False
        for j in range(len(linked[i].impact)):
            check = check or change1[i][j] or change2[i][j]
            linked[i].impact[j].run(change1[i][j] or change2[i][j])
            linked[i].impact[j].update_animation(screen)
        for j in range(len(linked[i].bar)):
            linked[i].bar[j].run(check)
            linked[i].bar[j].update_animation(screen)
    world.draw_map()
    for i in lava_ground:
        i.update_animation(screen)
    for i in diamond_ground:
        i.update_animation(screen, 2)
    for i in box:
        i.update_animation(screen)
    moveX, moveY, game_over, change1 = player1.update(
        moveX, moveY, world, game_over, lava_ground, diamond_ground, linked, change1)
    player1.update_animation(moveX, moveY, screen)
    moveX, moveY, game_over, change2 = player2.update(
        moveX, moveY, world, game_over, lava_ground, diamond_ground, linked, change2)
    player2.update_animation(moveX, moveY, screen)
    if game_over:
        run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(fps)
pygame.quit()
