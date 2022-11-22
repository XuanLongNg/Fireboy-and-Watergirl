import pygame
import pickle
from setting import *
from Map import *
from os import path

pygame.init()

clock = pygame.time.Clock()
fps = 60

# game window
margin = 100
width = block * cols
height = (block * rows) + margin
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Level Editor')


# define game variables
clicked = False
level = 1
font = pygame.font.SysFont('Futura', 24)

# create empty tile list
world_data = []
for row in range(rows):
    r = [0] * cols
    world_data.append(r)

# create boundary
draw_background()
for i in range(0, cols):
    world_data[rows-1][i] = 10+i % 8
    world_data[0][i] = 10+i % 8
for i in range(0, rows):
    world_data[i][0] = 10
    world_data[i][cols-1] = 10

# function for outputting text onto the screen


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def draw_grid():
    for i in range(rows):
        pygame.draw.line(screen, white, (0, i*block), (width, i*block))
    for i in range(cols):
        pygame.draw.line(screen, white, (i*block, 0), (i*block, width))


def draw_world():
    for row in range(rows):
        for col in range(cols):
            if world_data[row][col] > 0:
                if world_data[row][col] == 1:
                    # background
                    screen.blit(background, (col * block, row * block))
                if world_data[row][col] == 2:
                    # topographic
                    screen.blit(topographic, (col * block, row * block))
                if world_data[row][col] == 3:
                    # fern
                    screen.blit(fern, (col * block, row * block))
                if world_data[row][col] == 4:
                    # mossTree1
                    screen.blit(mossTree1, (col * block, row * block))
                if world_data[row][col] == 5:
                    # grass1
                    screen.blit(grass1, (col * block, row * block))
                if world_data[row][col] == 6:
                    # grass2
                    screen.blit(grass2, (col * block, row * block))
                if world_data[row][col] == 7:
                    # tree
                    screen.blit(tree, (col * block, row * block))
                if world_data[row][col] == 8:
                    # bush
                    screen.blit(bush, (col * block, row * block))
                if world_data[row][col] == 9:
                    # mossTree2
                    screen.blit(mossTree2, (col * block, row * block))
                if world_data[row][col] > 9:
                    # topographic
                    index = world_data[row][col] - 10
                    screen.blit(
                        sub_topographic[index//8][index % 8], (col * block, row * block))


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


# create load and save buttons
save_button = Button(width // 2 - 150, height - 80, save_img)
load_button = Button(width // 2 + 50, height - 80, load_img)

# main game loop
run = True
while run:

    clock.tick(fps)

    # draw background
    draw_background()
    # show the grid and draw the level tiles
    draw_world()
    # draw_grid()
    pygame.draw.rect(screen, black, pygame.Rect(0, ibs*18, 39*ibs, 110))

    # load and save level
    if save_button.draw():
        # save level data
        pickle_out = open(f'level{level}_data', 'wb')
        pickle.dump(world_data, pickle_out)
        pickle_out.close()
    if load_button.draw():
        # load in level data
        if path.exists(f'level{level}_data'):
            pickle_in = open(f'level{level}_data', 'rb')
            world_data = pickle.load(pickle_in)
    # text showing current level
    draw_text(f'Level: {level}', font, white, block, height - 60)
    draw_text('Press UP or DOWN to change level', font,
              white, block, height - 40)

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
        # mouseclicks to change tiles
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
            pos = pygame.mouse.get_pos()
            x = pos[0] // block
            y = pos[1] // block
            # check that the coordinates are within the tile area
            if x < cols and y < rows:
                # update tile value
                if pygame.mouse.get_pressed()[0] == 1:
                    world_data[y][x] += 1
                    if world_data[y][x] > 73:
                        world_data[y][x] = 0
                elif pygame.mouse.get_pressed()[2] == 1:
                    world_data[y][x] -= 1
                    if world_data[y][x] < 0:
                        world_data[y][x] = 73
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        # up and down key presses to change level number
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                level += 1
            elif event.key == pygame.K_DOWN and level > 1:
                level -= 1

    # update game display window
    pygame.display.update()

pygame.quit()
