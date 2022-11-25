import pygame
from setting import *


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        object = groundAssets
        self.step = 0
        self.rect = pygame.Rect(
            x+block*0.8, y+0.5*block, block*4-block*0.8, block*0.5)
        self.object = [
            [
                object.subsurface(ibs*15 + ibs*0.5, ibs*42, ibs, ibs),  # 0
                object.subsurface(ibs*15 + ibs*0.5, ibs*42, ibs, ibs),
                object.subsurface(ibs*15 + ibs*0.5, ibs*42, ibs, ibs),
                object.subsurface(ibs*20 + ibs*0.5, ibs*42, ibs, ibs),
                object.subsurface(ibs*20 + ibs*0.5, ibs*42, ibs, ibs),
                object.subsurface(ibs*20 + ibs*0.5, ibs*42, ibs, ibs),  # 5
                object.subsurface(ibs*25 + ibs*0.6, ibs*42, ibs, ibs),
                object.subsurface(ibs*25 + ibs*0.6, ibs*42, ibs, ibs),
                object.subsurface(ibs*25 + ibs*0.6, ibs*42, ibs, ibs),
                object.subsurface(ibs*30 + ibs*0.7, ibs*42, ibs, ibs),
                object.subsurface(ibs*2, ibs*44 - ibs*0.3, ibs, ibs),  # 10
                object.subsurface(ibs*2, ibs*44 - ibs*0.3, ibs, ibs),
                object.subsurface(ibs*3 + ibs*0.7, ibs*44 - ibs*0.3, ibs, ibs),
                object.subsurface(ibs*3 + ibs*0.7, ibs*44 - ibs*0.3, ibs, ibs),
                object.subsurface(ibs*3 + ibs*0.7, ibs*44 - \
                                  ibs*0.3, ibs, ibs)  # 14
            ],
            [
                object.subsurface(ibs*2 - ibs/30, ibs*43 -
                                  ibs*0.82, ibs, ibs),  # 0
                object.subsurface(ibs*2 - ibs/30, ibs*43-ibs*0.82, ibs, ibs),
                object.subsurface(ibs*2 - ibs/30, ibs*43-ibs*0.82, ibs, ibs),
                object.subsurface(ibs*5 + ibs*0.33, ibs*43-ibs*0.82, ibs, ibs),
                object.subsurface(ibs*5 + ibs*0.33, ibs*43-ibs*0.82, ibs, ibs),
                object.subsurface(ibs*5 + ibs*0.33, ibs*43 - \
                                  ibs*0.82, ibs, ibs),  # 5
                object.subsurface(ibs*10 + ibs*0.4, ibs*43-ibs*0.82, ibs, ibs),
                object.subsurface(ibs*10 + ibs*0.4, ibs*43-ibs*0.82, ibs, ibs),
                object.subsurface(ibs*10 + ibs*0.4, ibs*43-ibs*0.82, ibs, ibs),
                object.subsurface(ibs*22 + ibs*0.2, ibs*40-ibs*1.05, ibs, ibs),
                object.subsurface(ibs*22 + ibs*0.2, ibs*40 - \
                                  ibs*1.05, ibs, ibs),  # 10
                object.subsurface(ibs*22 + ibs*0.2, ibs*40-ibs*1.05, ibs, ibs),
                object.subsurface(ibs*27+ibs*0.3, ibs*40-ibs*1.05, ibs, ibs),
                object.subsurface(ibs*27+ibs*0.3, ibs*40-ibs*1.05, ibs, ibs),
                object.subsurface(ibs*27+ibs*0.3, ibs*40 - \
                                  ibs*1.05, ibs, ibs)  # 14
            ],
            [
                object.subsurface(ibs*8 + ibs*0.7, ibs*44 - \
                                  ibs*0.3, ibs, ibs),  # 0
                object.subsurface(ibs*8 + ibs*0.7, ibs*44 - ibs*0.3, ibs, ibs),
                object.subsurface(ibs*8 + ibs*0.7, ibs*44 - ibs*0.3, ibs, ibs),
                object.subsurface(ibs*13 + ibs*0.75, ibs * \
                                  44 - ibs*0.3, ibs, ibs),
                object.subsurface(ibs*13 + ibs*0.75, ibs * \
                                  44 - ibs*0.3, ibs, ibs),
                object.subsurface(ibs*13 + ibs*0.75, ibs * \
                                  44 - ibs*0.3, ibs, ibs),  # 5
                object.subsurface(ibs*18 + ibs*0.84, ibs * \
                                  44 - ibs*0.3, ibs, ibs),
                object.subsurface(ibs*18 + ibs*0.84, ibs * \
                                  44 - ibs*0.3, ibs, ibs),
                object.subsurface(ibs*18 + ibs*0.84, ibs * \
                                  44 - ibs*0.3, ibs, ibs),
                object.subsurface(ibs*23 + ibs*0.9, ibs * \
                                  44 - ibs*0.3, ibs, ibs),
                object.subsurface(ibs*23 + ibs*0.9, ibs * \
                                  44 - ibs*0.3, ibs, ibs),  # 10
                object.subsurface(ibs*23 + ibs*0.9, ibs * \
                                  44 - ibs*0.3, ibs, ibs),
                object.subsurface(ibs*29 - ibs*0.05, ibs * \
                                  44 - ibs*0.3, ibs, ibs),
                object.subsurface(ibs*29 - ibs*0.05, ibs * \
                                  44 - ibs*0.3, ibs, ibs),
                object.subsurface(ibs*29 - ibs*0.05, ibs * \
                                  44 - ibs*0.3, ibs, ibs),  # 14
            ]
        ]

        # update character's animation
    def update_animation(self, screen):
        if self.step > 13:
            self.step = -1
        self.step += 1

        screen.blit(pygame.transform.scale(
            self.object[0][self.step], (block, block)), (self.rect.x - block*0.8, self.rect.y - block*0.5))
        screen.blit(pygame.transform.scale(self.object[1][self.step], (block, block)),
                    (self.rect.x - block*0.8 + block, self.rect.y - block*0.5))
        screen.blit(pygame.transform.scale(self.object[1][self.step], (block, block)),
                    (self.rect.x - block*0.8 + block*2, self.rect.y - block*0.5))
        screen.blit(pygame.transform.scale(self.object[1][self.step], (block, block)),
                    (self.rect.x - block*0.8 + block*3, self.rect.y - block*0.5))
        screen.blit(pygame.transform.scale(self.object[2][self.step], (block, block)),
                    (self.rect.x - block*0.8 + block*4, self.rect.y - block*0.5))


class Diamond(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        object = charAssets
        self.rect = pygame.rect.Rect(x, y, block*1.2, block*1.2)
        cs = 136
        self.object = [
            object.subsurface(0, cs*10-20, cs-26, cs-26),  # red blue
            object.subsurface(cs*6+33, cs*10-20, cs-26, cs-26),  # white
            object.subsurface(cs*7+17, cs*10-20, cs-26, cs-26),  # blue
            object.subsurface(cs*8-2, cs*10-20, cs-26, cs-26),  # red
        ]
        self.step = 0
        self.stepAni = 2
    # update character's animation

    def update_animation(self, screen, diamond):
        self.step += 2
        if abs(self.step) > 40:
            self.step *= -1
            self.stepAni *= -1
        self.rect.y += self.stepAni/2
        screen.blit(pygame.transform.scale(
            self.object[2], (block*3, block*3)), (self.rect.x-block, self.rect.y-block))
        # pygame.draw.rect(
        #     screen, white, (self.rect.x, self.rect.y, block*1.2, block*1.2), 2)
        # print(self.step, self.stepAni, self.rect.y)


class TransportBar(pygame.sprite.Sprite):
    def __init__(self, x, y, size, color, newX, newY):
        pygame.sprite.Sprite.__init__(self)
        object = mechAssets
        self.step = 0
        self.rect = pygame.Rect(x, y, block*size, block)
        self.old_rect = pygame.Rect(x, y, block*size, block)
        self.new_rect = pygame.Rect(
            x + newX*block, y+block*newY, block*size, block)
        self.size = size
        self.color = color
        self.object = [
            object.subsurface(ibs*53 + ibs*0.2, ibs*0.23, ibs, ibs+2),  # 0
            object.subsurface(ibs*57, ibs*0.23, ibs, ibs+2),
            object.subsurface(ibs*54 + ibs*0.8, ibs*0.2, ibs, ibs+2)
        ]

    def run(self, run):
        stepX = 0
        stepY = 0
        if run:
            if self.rect == self.new_rect:
                return
            if self.rect.x > self.new_rect.x:
                stepX = -1
            elif self.rect.x < self.new_rect.x:
                stepX = 1
            if self.rect.y > self.new_rect.y:
                stepY = -1
            elif self.rect.y < self.new_rect.y:
                stepY = 1
        else:
            if self.rect == self.old_rect:
                return
            if self.rect.x > self.old_rect.x:
                stepX = -1
            elif self.rect.x > self.old_rect.x:
                stepX = 1
            if self.rect.y > self.old_rect.y:
                stepY = -1
            elif self.rect.y > self.new_rect.y:
                stepY = 1
        self.rect.x += stepX
        self.rect.y += stepY

    def update_animation(self, screen):
        img = pygame.transform.scale(self.object[0], (block, block))
        screen.blit(img, (self.rect.x, self.rect.y))
        for i in range(1, len(self.object)):
            img = pygame.transform.scale(self.object[1], (block, block))
            screen.blit(img, (self.rect.x+block*i, self.rect.y))
        img = pygame.transform.scale(self.object[2], (block, block))
        screen.blit(img, (self.rect.x+block*(self.size-1), self.rect.y))
        pygame.draw.rect(screen, self.color, pygame.Rect(
            self.rect.x + block*0.55, self.rect.y + block*0.4, self.size*block-block*0.9, block*0.28))


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        object = mechAssets
        self.step = 0
        self.rect = pygame.Rect(x, y, block*2.5, block*0.5)
        self.old_rect = pygame.Rect(x, y, block*2.5, block*0.5)
        self.new_rect = pygame.Rect(x, y+block-block*0.1, block*2.5, block*0.5)
        self.color = color
        self.object = [
            object.subsurface(ibs*30 + ibs*0.8, ibs *
                              27+ibs*0.5, ibs*2.5, ibs)  # 0
        ]
        self.stepY = 1

    def run(self, run):
        if run:
            if self.rect == self.new_rect:
                return
            self.stepY = 1
        else:
            if self.rect == self.old_rect:
                return
            self.stepY = -1
        self.rect.y += self.stepY

    def update_animation(self, screen):
        for i in range(len(self.object)):
            img = pygame.transform.scale(
                self.object[i], (block*2.5, block*0.7))
            screen.blit(img, (self.rect.x, self.rect.y+block*0.5))


class Box:
    def __init__(self, x, y):
        object = mechAssets
        self.rect = pygame.Rect(x, y, block*2, block*2)
        self.object = [
            object.subsurface(ibs*48 + ibs*0.4, ibs*0.15, ibs*2.15, ibs*2.15)
        ]
        self.vel_y = 0

    def update(self, moveX, world_data):
        dx = 0
        dy = 0
        self.rect.x += moveX
        # self.rect.y += moveY
        # add gravity
        self.vel_y += 1
        if self.vel_y == 0:
            y = -1
        if self.vel_y >= block/2:
            self.vel_y = block/2

        dy += self.vel_y
        # check for collision
        for i in world_data:
            for j in i:
                # check for collision in x direction
                if j[1].colliderect(self.rect.x + dx, self.rect.y, block*2, block*2):
                    dx = 0
                # check for collision in y direction
                if j[1].colliderect(self.rect.x, self.rect.y + dy-block, block*2, block*2):
                    # check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = j[1].bottom - self.rect.top + block
                        self.vel_y = 0
                    # check if above the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = j[1].top - self.rect.bottom+block
                        self.vel_y = 0
        self.rect.y += dy

    def update_animation(self, screen):
        img = pygame.transform.scale(
            self.object[0], (block*2, block*2))
        screen.blit(img, (self.rect.x, self.rect.y))


class Linked:
    def __init__(self, impact, bar):
        self.impact = impact
        self.bar = bar
