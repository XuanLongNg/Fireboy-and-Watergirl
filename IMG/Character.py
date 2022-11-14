import pygame
from setting import *
from color import *
from map_1 import *
my_char = []
screen = pygame.display.set_mode((width,height))
def dis_char(my_char):
    pygame.draw.rect(screen, red,[my_char[0],my_char[1],block,block])
    pygame.draw.rect(screen, red, [my_char[2], my_char[3], block,block])
    pygame.display.update()
def gravity(my_char,map):
    a,b,c,d=my_char[0],my_char[1],my_char[2],my_char[3]
    while map[0]==False and map[1]==False and map[2]==False and map[3]==False:
        dis_char(my_char)
        my_char[0]-=1
        my_char[2]-=1
def action(my_char,map):
    gravity(my_char,map)
action(my_char,)