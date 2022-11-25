import pygame
import pickle
import time
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
font = pygame.font.SysFont('Futura', 24)
clock = pygame.time.Clock()
fps = 20
moveX, moveY = 0, 0
x, y = 0, 0
level = 1
world_data = []
if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')
    world_data = pickle.load(pickle_in)
win1 = False
win2 = False
text = "Game Over"
# object initialization
desPlay1 = Destination(width - block*5, block*3, 1)
desPlay2 = Destination(width - block*9, block*3, 0)
world = Map(world_data)
player1 = Character1(block*3, height - block*6, desPlay1)
player2 = Character2(block*3, height - block*2, desPlay2)
diamond_blue_ground = pygame.sprite.Group()
diamond_red_ground = pygame.sprite.Group()
lava_ground = pygame.sprite.Group()
water_ground = pygame.sprite.Group()
toxic_ground = pygame.sprite.Group()
box = []
linked = []
# Add object

diamond_blue_ground.add(Diamond(block * 29, height - block*4))
diamond_blue_ground.add(Diamond(block * 23, block*3))
diamond_blue_ground.add(Diamond(block * 2, block*4))
diamond_blue_ground.add(Diamond(block * 23, block*13))

diamond_red_ground.add(Diamond(block * 20, height - block*4))
diamond_red_ground.add(Diamond(block * 8, block*13))
diamond_red_ground.add(Diamond(block * 12, block*2))

lava_ground.add(Lava(block * 18, height - block*1.5))
toxic_ground.add(Toxic(block * 24, height - block*7.5))

linked.append(Linked([Button(block*8, height - block*10, blue)],
                     [TransportBar(block, block*15, 4, red, 0, 4)]))
linked.append(Linked([Button(block*10, height - block*15, red),
                     Button(block*29, height - block*19, red)],
                     [TransportBar(width-5*block, block*11, 4, blue, 0, 4)]))

box.append(Box(block*23, block*8))
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
    desPlay1.update_animation(screen)
    desPlay2.update_animation(screen)
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
    for i in toxic_ground:
        i.update_animation(screen)
    for i in diamond_blue_ground:
        i.update_animation(screen, 2)
    for i in diamond_red_ground:
        i.update_animation(screen, 3)
    for i in box:
        i.update(0, world.world_data)
        i.update_animation(screen)
    moveX, moveY, game_over, change1, box, win1 = player1.update(
        moveX, moveY, world, game_over, lava_ground, toxic_ground, diamond_blue_ground, linked, change1, box, win1)
    player1.update_animation(moveX, moveY, screen)
    moveX, moveY, game_over, change2, box, win2 = player2.update(
        moveX, moveY, world, game_over, water_ground, toxic_ground, diamond_red_ground, linked, change2, box, win2)
    player2.update_animation(moveX, moveY, screen)
    if win1 and win2:
        text = "You win!"
        run = False
    if game_over:
        run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(fps)

pygame.draw.rect(screen, black, (15*block, 10*block, block*10, block*7))
draw_text(text, font, white, 18*block, 13*block)
pygame.display.update()

time.sleep(5)
pygame.quit()
