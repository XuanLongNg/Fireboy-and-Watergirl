import pygame
from math import *
from setting import *


class Character():
    def __init__(self, character, x, y):
        # logic game
        self.rect_body = pygame.Rect(x, y-block, block, block*2)
        # self.rect_body = [0, 0]
        # self.rect_body.x = x
        # self.rect_body.y = y
        self.vel_y = 0
        self.jumped = False

        # animation
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
            character.subsurface(cs*6+90, cs*2, cs, cs),  # 60

            # head jump
            character.subsurface(0, cs * 9-27, cs, cs),  # 61
            character.subsurface(cs, cs * 9-27, cs, cs),
            character.subsurface(cs * 2, cs * 9-27, cs, cs),
            character.subsurface(cs * 9 + 40, cs * 9+45, cs, cs),
            character.subsurface(cs * 10 + 40, cs * 9+45, cs, cs),
            character.subsurface(cs * 11 + 40, cs * 9+45, cs, cs),  # 66
            character.subsurface(cs * 12 + 40, cs * 9+45, cs, cs),
            character.subsurface(cs * 13 + 40, cs * 9+45, cs, cs),
            character.subsurface(cs * 7 + 40, cs * 9-29, cs, cs),
            character.subsurface(cs * 8 + 40, cs * 9-29, cs, cs)  # 70
        ]

    # logic game
    def update(self, x, y, map):
        dx = 0
        dy = 0
        x = 0
        # get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.jumped == False:
            self.vel_y = -block*0.6
            self.jumped = True
            y = 1
        if key[pygame.K_a]:
            dx -= block/2
            x = -1
        if key[pygame.K_d]:
            dx += block/2
            x = 1
        # if bottom > 0:
        #     self.jumped = False
        #     y = 0
        # add gravity
        self.vel_y += 1
        if self.vel_y == 0:
            y = -1
        if self.vel_y >= block/2:
            self.vel_y = block/2

        dy += self.vel_y

        # check for collision
        # for i in world:
        # if i[]

        # update player coordinates
        self.rect_body.x += dx
        self.rect_body.y += dy

        if self.rect_body.y > height-block:
            self.rect_body.y = height-block
            dy = 0
        return x, y

    # update character's animation
    def update_animation(self, x, y, screen, k, h):
        pygame.draw.rect(
            screen, white, (self.rect_body.x, self.rect_body.y-block, block, block*2), 2)

        mergex, mergey, degree, move, lctFlip = 0, 0, 0, 0, 0
        flip = False
        if x == 0 and y == 0:  # stay
            if k > 58 or k <= 29:
                k = 29
            h = 59
            mergex = - block * 0.8
            mergey = - block * 1.5
        else:
            if abs(x) > 0 and y == 0:  # move
                if k > 20 or k < 11:
                    k = 10
                if h < 22 or h > 28:
                    h = 21
                mergex = - block * 1.2
                mergey = - block * 1.1
                move = - 0.2
                if x < 0:
                    flip = True   # flip
                    lctFlip = - block
                    mergex = block * 0.2
            elif x == 0 and abs(y) > 0:  # jump and fall
                if y < 0:
                    if k > 9:
                        k = -1
                    mergex = - block * 0.8
                    mergey = - block * 2
                if y > 0:
                    if k <= 60 or k > 69:
                        k = 60
                    mergex = - block * 0.8
                    mergey = - block * 1.5
                h = 59
            else:  # jump and move
                if k > 20 or k < 11:
                    k = 10
                if h < 22 or h > 28:
                    h = 21
                # degree = 45
                # mergex = - block * 1
                # mergey = - block * 1
                mergex = - block * 1.2
                mergey = - block * 1.1
                if x < 0:
                    flip = True   # flip
                    lctFlip = - block
                    mergex = block * 0.2
                # if x > 0 and y < 0:
                #     degree = -45
                #     mergex = - block * 1.2
                #     mergey = - block * 1.3
                # if x < 0 and y < 0:
                #     degree = -45
                #     mergex = 0
                #     mergey = - block * 1.2
        k += 1
        h += 1
        degree = 0
        img = pygame.transform.scale(pygame.transform.rotate(
            self.characters[k], degree), (block*3, block*3))
        imgBody = pygame.transform.scale(
            self.characters[h], (block*3, block*3))
        if flip:
            img = pygame.transform.flip(img, True, False)
            imgBody = pygame.transform.flip(imgBody, True, False)

        if x == 0 and y > 0:
            screen.blit(
                img, (self.rect_body.x + mergex + lctFlip, self.rect_body.y + mergey))
            screen.blit(
                imgBody, (self.rect_body.x - block/2 + lctFlip, self.rect_body.y - block/2 + move))
        else:
            screen.blit(
                imgBody, (self.rect_body.x - block/2 + lctFlip, self.rect_body.y - block/2 + move))
            screen.blit(
                img, (self.rect_body.x + mergex + lctFlip, self.rect_body.y + mergey))

        return k, h


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
        return k, step
