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
        self.world_data = data

    def get_data(self):
        return self.world_data

    def update_data(self, data):
        self.world_data = data

    def draw_map(self):
        for row in range(rows):
            for col in range(cols):
                if self.world_data[row][col] > 0:
                    if self.world_data[row][col] == 1:
                        # background
                        screen.blit(background, (col * block, row * block))
                    if self.world_data[row][col] == 2:
                        # topographic
                        screen.blit(topographic, (col * block, row * block))
                    if self.world_data[row][col] == 3:
                        # fern
                        screen.blit(fern, (col * block, row * block))
                    if self.world_data[row][col] == 4:
                        # mossTree1
                        screen.blit(mossTree1, (col * block, row * block))
                    if self.world_data[row][col] == 5:
                        # grass1
                        screen.blit(grass1, (col * block, row * block))
                    if self.world_data[row][col] == 6:
                        # grass2
                        screen.blit(grass2, (col * block, row * block))
                    if self.world_data[row][col] == 7:
                        # tree
                        screen.blit(tree, (col * block, row * block))
                    if self.world_data[row][col] == 8:
                        # bush
                        screen.blit(bush, (col * block, row * block))
                    if self.world_data[row][col] == 9:
                        # mossTree2
                        screen.blit(mossTree2, (col * block, row * block))
                    if self.world_data[row][col] > 9:
                        # topographic
                        index = self.world_data[row][col] - 10
                        screen.blit(
                            sub_topographic[index//8][index % 8], (col * block, row * block))
                    # pygame.draw.rect(
                    #     screen, white, (col * block, row * block, block, block), 2)
