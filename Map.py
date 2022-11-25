import pygame
from pygame.locals import *
from setting import *

screen = pygame.display.set_mode((width, height))


# background
def draw_background():
    for i in range(1, rows, 8):
        for j in range(1, cols, 8):
            screen.blit(background, (j * block, i * block))


class Map():
    def __init__(self, data):
        self.world_data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                if data[row][col] > 0:
                    if data[row][col] == 1:
                        # background
                        rect = background.get_rect()
                        rect.topleft = (col * block, row * block)
                        tmp.append((background, rect, data[row][col]))
                        # screen.blit(background, (col * block, row * block))
                    if data[row][col] == 2:
                        # topographic
                        rect = topographic.get_rect()
                        rect.topleft = (col * block, row * block)
                        tmp.append((topographic, rect, data[row][col]))
                        # screen.blit(topographic, (col * block, row * block))
                    if data[row][col] == 3:
                        # fern
                        rect = fern.get_rect()
                        rect.topleft = (col * block, row * block)
                        tmp.append((fern, rect, data[row][col]))
                        # screen.blit(fern, (col * block, row * block))
                    if data[row][col] == 4:
                        # mossTree1
                        rect = mossTree1.get_rect()
                        rect.topleft = (col * block, row * block)
                        tmp.append((mossTree1, rect, data[row][col]))
                        # screen.blit(mossTree1, (col * block, row * block))
                    if data[row][col] == 5:
                        # grass1
                        rect = grass1.get_rect()
                        rect.topleft = (col * block, row * block)
                        tmp.append((grass1, rect, data[row][col]))
                        # screen.blit(grass1, (col * block, row * block))
                    if data[row][col] == 6:
                        # grass2
                        rect = grass2.get_rect()
                        rect.topleft = (col * block, row * block)
                        tmp.append((grass2, rect, data[row][col]))
                        # screen.blit(grass2, (col * block, row * block))
                    if data[row][col] == 7:
                        # tree
                        rect = tree.get_rect()
                        rect.topleft = (col * block, row * block)
                        tmp.append((tree, rect, data[row][col]))
                        # screen.blit(tree, (col * block, row * block))
                    if data[row][col] == 8:
                        # bush
                        rect = bush.get_rect()
                        rect.topleft = (col * block, row * block)
                        tmp.append((bush, rect, data[row][col]))
                        # screen.blit(bush, (col * block, row * block))
                    if data[row][col] == 9:
                        # mossTree2
                        rect = mossTree2.get_rect()
                        rect.topleft = (col * block, row * block)
                        tmp.append((mossTree2, rect, data[row][col]))
                        # screen.blit(mossTree2, (col * block, row * block))
                    if data[row][col] > 9:
                        # topographic
                        index = data[row][col] - 10
                        rect = sub_topographic[index//8][index % 8].get_rect()
                        rect.topleft = (col * block, row * block)
                        tmp.append(
                            (sub_topographic[index//8][index % 8], rect, data[row][col]))
                        # screen.blit(
                        # sub_topographic[index//8][index % 8], (col * block, row * block))
            self.world_data.append(tmp)

    def draw_map(self):
        for row in self.world_data:
            for col in row:
                screen.blit(col[0], col[1])
                # pygame.draw.rect(
                #     screen, white, col[1], 2)
