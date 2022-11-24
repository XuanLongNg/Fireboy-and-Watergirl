import pygame
from setting import *


# class Lava(pygame.sprite.Sprite):
#     def __init__(self, object, x, y, world_data):
#         pygame.sprite.Sprite.__init__(self)
#         self.step = 0
#         self.rect = pygame.Rect(x, y, block*5, block*0.5)
#         # self.background =
#         self.object = [
#             [
#                 object.subsurface(ibs*15 + ibs*0.5, ibs*42, ibs, ibs),  # 0
#                 object.subsurface(ibs*15 + ibs*0.5, ibs*42, ibs, ibs),
#                 object.subsurface(ibs*15 + ibs*0.5, ibs*42, ibs, ibs),
#                 object.subsurface(ibs*20 + ibs*0.5, ibs*42, ibs, ibs),
#                 object.subsurface(ibs*20 + ibs*0.5, ibs*42, ibs, ibs),
#                 object.subsurface(ibs*20 + ibs*0.5, ibs*42, ibs, ibs),  # 5
#                 object.subsurface(ibs*25 + ibs*0.6, ibs*42, ibs, ibs),
#                 object.subsurface(ibs*25 + ibs*0.6, ibs*42, ibs, ibs),
#                 object.subsurface(ibs*25 + ibs*0.6, ibs*42, ibs, ibs),
#                 object.subsurface(ibs*30 + ibs*0.7, ibs*42, ibs, ibs),
#                 object.subsurface(ibs*2, ibs*44 - ibs*0.3, ibs, ibs),  # 10
#                 object.subsurface(ibs*2, ibs*44 - ibs*0.3, ibs, ibs),
#                 object.subsurface(ibs*3 + ibs*0.7, ibs*44 - ibs*0.3, ibs, ibs),
#                 object.subsurface(ibs*3 + ibs*0.7, ibs*44 - ibs*0.3, ibs, ibs),
#                 object.subsurface(ibs*3 + ibs*0.7, ibs*44 - \
#                                   ibs*0.3, ibs, ibs)  # 14
#             ],
#             [
#                 object.subsurface(ibs*2 - ibs/30, ibs*43 -
#                                   ibs*0.82, ibs, ibs),  # 0
#                 object.subsurface(ibs*2 - ibs/30, ibs*43-ibs*0.82, ibs, ibs),
#                 object.subsurface(ibs*2 - ibs/30, ibs*43-ibs*0.82, ibs, ibs),
#                 object.subsurface(ibs*5 + ibs*0.33, ibs*43-ibs*0.82, ibs, ibs),
#                 object.subsurface(ibs*5 + ibs*0.33, ibs*43-ibs*0.82, ibs, ibs),
#                 object.subsurface(ibs*5 + ibs*0.33, ibs*43 - \
#                                   ibs*0.82, ibs, ibs),  # 5
#                 object.subsurface(ibs*10 + ibs*0.4, ibs*43-ibs*0.82, ibs, ibs),
#                 object.subsurface(ibs*10 + ibs*0.4, ibs*43-ibs*0.82, ibs, ibs),
#                 object.subsurface(ibs*10 + ibs*0.4, ibs*43-ibs*0.82, ibs, ibs),
#                 object.subsurface(ibs*22 + ibs*0.2, ibs*40-ibs*1.05, ibs, ibs),
#                 object.subsurface(ibs*22 + ibs*0.2, ibs*40 - \
#                                   ibs*1.05, ibs, ibs),  # 10
#                 object.subsurface(ibs*22 + ibs*0.2, ibs*40-ibs*1.05, ibs, ibs),
#                 object.subsurface(ibs*27+ibs*0.3, ibs*40-ibs*1.05, ibs, ibs),
#                 object.subsurface(ibs*27+ibs*0.3, ibs*40-ibs*1.05, ibs, ibs),
#                 object.subsurface(ibs*27+ibs*0.3, ibs*40 - \
#                                   ibs*1.05, ibs, ibs)  # 14
#             ],
#             [
#                 object.subsurface(ibs*8 + ibs*0.7, ibs*44 - \
#                                   ibs*0.3, ibs, ibs),  # 0
#                 object.subsurface(ibs*8 + ibs*0.7, ibs*44 - ibs*0.3, ibs, ibs),
#                 object.subsurface(ibs*8 + ibs*0.7, ibs*44 - ibs*0.3, ibs, ibs),
#                 object.subsurface(ibs*13 + ibs*0.75, ibs * \
#                                   44 - ibs*0.3, ibs, ibs),
#                 object.subsurface(ibs*13 + ibs*0.75, ibs * \
#                                   44 - ibs*0.3, ibs, ibs),
#                 object.subsurface(ibs*13 + ibs*0.75, ibs * \
#                                   44 - ibs*0.3, ibs, ibs),  # 5
#                 object.subsurface(ibs*18 + ibs*0.84, ibs * \
#                                   44 - ibs*0.3, ibs, ibs),
#                 object.subsurface(ibs*18 + ibs*0.84, ibs * \
#                                   44 - ibs*0.3, ibs, ibs),
#                 object.subsurface(ibs*18 + ibs*0.84, ibs * \
#                                   44 - ibs*0.3, ibs, ibs),
#                 object.subsurface(ibs*23 + ibs*0.9, ibs * \
#                                   44 - ibs*0.3, ibs, ibs),
#                 object.subsurface(ibs*23 + ibs*0.9, ibs * \
#                                   44 - ibs*0.3, ibs, ibs),  # 10
#                 object.subsurface(ibs*23 + ibs*0.9, ibs * \
#                                   44 - ibs*0.3, ibs, ibs),
#                 object.subsurface(ibs*29 - ibs*0.05, ibs * \
#                                   44 - ibs*0.3, ibs, ibs),
#                 object.subsurface(ibs*29 - ibs*0.05, ibs * \
#                                   44 - ibs*0.3, ibs, ibs),
#                 object.subsurface(ibs*29 - ibs*0.05, ibs * \
#                                   44 - ibs*0.3, ibs, ibs),  # 14
#             ]
#         ]

#         # update character's animation
#     def update_animation(self, screen):
#         if self.step > 13:
#             self.step = -1
#         self.step += 1

#         screen.blit(pygame.transform.scale(
#             self.object[0][self.step], (block, block)), (self.rect.x, self.rect.y))
#         screen.blit(pygame.transform.scale(self.object[1][self.step], (block, block)),
#                     (self.rect.x+block, self.rect.y))
#         screen.blit(pygame.transform.scale(self.object[1][self.step], (block, block)),
#                     (self.rect.x+block*2, self.rect.y))
#         screen.blit(pygame.transform.scale(self.object[1][self.step], (block, block)),
#                     (self.rect.x+block*3, self.rect.y))
#         screen.blit(pygame.transform.scale(self.object[2][self.step], (block, block)),
#                     (self.rect.x+block*4, self.rect.y))


class Diamond(pygame.sprite.Sprite):
    def __init__(self, object, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.rect.Rect(x, y, block*1.2, block*1.2)
        cs = 136
        self.object = [
            object.subsurface(0, cs*10-20, cs-26, cs-26),  # red blue
            object.subsurface(cs*6+33, cs*10-20, cs-26, cs-26),  # white
            object.subsurface(cs*7+17, cs*10-20, cs-26, cs-26),  # blue
            object.subsurface(cs*8-2, cs*10-20, cs-26, cs-26),  # red
        ]
        self.step = 0.2
        self.stepAni = 0
    # update character's animation

    def update_animation(self, screen, diamond, display):
        pygame.draw.rect(
            screen, white, (self.rect.x, self.rect.y, block*1.2, block*1.2), 2)
        if display == False:
            return
        # if abs(self.stepAni) == 5:
        #     self.step *= -1
        # self.stepAni = round((self.stepAni+self.step)*10)/10
        # self.rect.y = round((self.rect.y+self.step)*10)/10
        screen.blit(pygame.transform.scale(
            self.object[2], (block*3, block*3)), (self.rect.x-block, self.rect.y-block))
        # print(self.stepAni, self.step, self.rect.y)
