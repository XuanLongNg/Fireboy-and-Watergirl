import pygame
from math import *
from setting import *


class Character():
    def __init__(self, character, x, y):
        # logic game
        self.rect = pygame.Rect(x, y, block, block*2)
        self.vel_y = 0
        self.jumped = False
        self.step_head = 0  # step animation head
        self.step_body = 0  # step animation body
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
    def update(self, x, y, map, game_over, lava_ground, diamond_ground):
        if game_over == True:
            0, 0, game_over
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
            dx -= block/3
            x = -1
        if key[pygame.K_d]:
            dx += block/3
            x = 1
        # add gravity
        self.vel_y += 1
        if self.vel_y == 0:
            y = -1
        if self.vel_y >= block/2:
            self.vel_y = block/2

        dy += self.vel_y

        # check for collision
        for i in map.world_data:
            for j in i:
                # check for collision in x direction
                if j[1].colliderect(self.rect.x + dx, self.rect.y - block, block, block*2):
                    dx = 0
                # check for collision in y direction
                if j[1].colliderect(self.rect.x, self.rect.y + dy - block, block, block*2):
                    # check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = j[1].bottom - self.rect.top + block
                        self.vel_y = 0
                    # check if above the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = j[1].top - self.rect.bottom + block
                        self.vel_y = 0
                        self.jumped = False
                        y = 0

        # check for collision with lava
        if pygame.sprite.spritecollide(self, lava_ground, False):
            game_over = True
            # print("cham")
        # check for collision with diamond
        if pygame.sprite.spritecollide(self, diamond_ground, True):
            pass
        # update player coordinates
        if dy > 0:
            y = -1
            self.jumped = True
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.y > height-block:
            self.rect.y = height-block
            dy = 0
        return x, y, game_over

    # update character's animation
    def update_animation(self, x, y, screen):
        # pygame.draw.rect(
        # screen, white, (self.rect.x, self.rect.y-block, block, block*2), 2)

        mergex, mergey, degree, move, lctFlip = 0, 0, 0, 0, 0
        flip = False
        if x == 0 and y == 0:  # stay
            if self.step_head > 58 or self.step_head <= 29:
                self.step_head = 29
            self.step_body = 59
            mergex = - block * 0.8
            mergey = - block * 1.5
        else:
            if abs(x) > 0 and y == 0:  # move
                if self.step_head > 20 or self.step_head < 11:
                    self.step_head = 10
                if self.step_body < 22 or self.step_body > 28:
                    self.step_body = 21
                mergex = - block * 1.2
                mergey = - block * 1.1
                move = - 0.2
                if x < 0:
                    flip = True   # flip
                    lctFlip = - block
                    mergex = block * 0.2
            elif x == 0 and abs(y) > 0:  # jump and fall
                if y < 0:
                    if self.step_head > 9:
                        self.step_head = -1
                    mergex = - block * 0.8
                    mergey = - block * 2
                if y > 0:
                    if self.step_head <= 60 or self.step_head > 69:
                        self.step_head = 60
                    mergex = - block * 0.8
                    mergey = - block * 1.5
                self.step_body = 59
            else:  # jump and move
                if self.step_head > 20 or self.step_head < 11:
                    self.step_head = 10
                if self.step_body < 22 or self.step_body > 28:
                    self.step_body = 21
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
        self.step_head += 1
        self.step_body += 1
        degree = 0
        img = pygame.transform.scale(pygame.transform.rotate(
            self.characters[self.step_head], degree), (block*3, block*3))
        imgBody = pygame.transform.scale(
            self.characters[self.step_body], (block*3, block*3))
        if flip:
            img = pygame.transform.flip(img, True, False)
            imgBody = pygame.transform.flip(imgBody, True, False)

        if x == 0 and y > 0:
            screen.blit(
                img, (self.rect.x + mergex + lctFlip, self.rect.y + mergey))
            screen.blit(
                imgBody, (self.rect.x - block/2 + lctFlip, self.rect.y - block/2 + move))
        else:
            screen.blit(
                imgBody, (self.rect.x - block/2 + lctFlip, self.rect.y - block/2 + move))
            screen.blit(
                img, (self.rect.x + mergex + lctFlip, self.rect.y + mergey))
