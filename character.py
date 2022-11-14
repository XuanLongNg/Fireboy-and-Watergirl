import pygame
from math import *


class Character():
    def __init__(self, character):
        cs = 136
        self.characters = [
            # head fall
            character.subsurface(0, 15, cs, cs),  # 0
            character.subsurface(cs-2, 15, cs, cs),
            character.subsurface(cs*2-4, 15, cs, cs),
            character.subsurface(cs*3-6, 15, cs, cs),
            character.subsurface(cs*4-8, 15, cs, cs),
            character.subsurface(cs*5-10, 15, cs, cs),  # 5
            character.subsurface(cs*6-12, 15, cs, cs),
            character.subsurface(cs*7-14, 15, cs, cs),
            character.subsurface(cs*8-16, 15, cs, cs),
            character.subsurface(cs*9-18, 15, cs, cs),
            character.subsurface(cs*10-20, 15, cs, cs),  # 10
            # head move
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
            character.subsurface(cs*5+42, 223, cs, cs),  # 21
            # body move
            character.subsurface(cs*2+10, cs*3, cs, cs),  # 22
            character.subsurface(cs*3+10, cs*3, cs, cs),
            character.subsurface(cs*4+10, cs*3, cs, cs),
            character.subsurface(cs*5+10, cs*3, cs, cs),
            character.subsurface(cs*6+3, cs*3+30, cs, cs),  # 26
            character.subsurface(cs*7+3, cs*3+30, cs, cs),
            character.subsurface(cs*8+3, cs*3+30, cs, cs),
            character.subsurface(cs*9+3, cs*3+30, cs, cs),  # 29
            # head stay
            character.subsurface(0 + 2, cs * 4, cs, cs),  # 30
            character.subsurface(cs, cs * 4, cs, cs),
            character.subsurface(cs * 2 - 2, cs * 4, cs, cs),
            character.subsurface(cs * 3 - 4, cs * 4, cs, cs),
            character.subsurface(cs * 4 - 6, cs * 4, cs, cs),
            character.subsurface(cs * 5 - 8, cs * 4, cs, cs),  # 35
            character.subsurface(cs * 6 - 10, cs * 4 + 30, cs, cs),
            character.subsurface(cs * 7 - 12, cs * 4 + 30, cs, cs),
            character.subsurface(cs * 8 - 14, cs * 4 + 30, cs, cs),
            character.subsurface(cs * 9 - 16, cs * 4 + 30, cs, cs),
            character.subsurface(cs * 10 - 18, cs * 4.77, cs, cs),  # 40
            character.subsurface(cs * 11 - 20, cs * 4.77, cs, cs),
            character.subsurface(cs * 12 - 22, cs * 4.77, cs, cs),
            character.subsurface(cs * 13 - 24, cs * 4.77, cs, cs),
            character.subsurface(cs * 14 - 26, cs * 4.77, cs, cs),
            character.subsurface(0 + 2, cs * 5 + 30, cs, cs),  # 45
            character.subsurface(cs, cs * 5 + 30, cs, cs),
            character.subsurface(cs * 2 - 2, cs * 5 + 30, cs, cs),
            character.subsurface(cs * 3 - 4, cs * 5 + 30, cs, cs),
            character.subsurface(cs * 4 - 6, cs * 5 + 30, cs, cs),
            character.subsurface(cs * 5 - 8, cs * 5 + 30, cs, cs),  # 50
            character.subsurface(cs * 6 - 10, cs * 5.442, cs, cs),
            character.subsurface(cs * 7 - 12, cs * 5.442, cs, cs),
            character.subsurface(cs * 8 - 14, cs * 5.442, cs, cs),
            character.subsurface(cs * 9 - 16, cs * 5.442, cs, cs),
            character.subsurface(cs * 10 - 18, cs * 3.55, cs, cs),  # 55
            character.subsurface(cs * 11 - 20, cs * 3.55, cs, cs),
            character.subsurface(cs * 12 - 22, cs * 3.55, cs, cs),
            character.subsurface(cs * 13 - 24, cs * 3.55, cs, cs),
            character.subsurface(cs * 14 - 26, cs * 3.55, cs, cs),  # 59

            # body stay
            character.subsurface(cs*6+90, cs*2, cs, cs)  # 60
        ]
        self.character_index = 0

    # update character's animation
    def update_animation(self, x, y, screen, lct_x, lcx_y, k):
        if x == 0 and y == 0:
            if k > 58 or k <= 29:
                k = 29
        else:
            if abs(x) > 0 and y == 0:
                if k:
                    pass
            elif x == 0 and abs(y) > 0:
                if y < 0:
                    if k > 9:
                        k = -1
                if y > 0:
                    if k:
                        pass
        k += 1
        screen.blit(self.characters[60], (lct_x+13, lcx_y+45))
        screen.blit(self.characters[k], (lct_x, lcx_y))
        self.character_index = k
        return self.character_index


class Diamond:
    def __init__(self, object):
        cs = 136
        self.object = [
            object.subsurface(0, cs*10-20, cs-26, cs-26),  # red blue
            object.subsurface(cs*6+33, cs*10-20, cs-26, cs-26),  # white
            object.subsurface(cs*7+17, cs*10-20, cs-26, cs-26),  # blue
            object.subsurface(cs*8-2, cs*10-20, cs-26, cs-26),  # red
        ]
    # update character's animation

    def update_animation(self, screen, lct_x, lcx_y, k, step):
        if round(abs(k)) == 5:
            step *= -1
        k += step
        screen.blit(self.object[2], (lct_x, lcx_y+k))
        print(step, k)
        return k, step
