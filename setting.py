import pygame

# menu setting
height_menu = 768
width_menu = 1366

# map setting
block = 25
cols = 39
rows = 29
height = block * rows
width = block * cols
ibs = 32  # image box size
# funtion settings


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    pygame.display.set_mode((width, height)).blit(img, (x, y))


# character setting
speed = block/3
# color
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 128, 0)
red = (255, 0, 0)
violet = (255, 192, 203)
rose = (255, 0, 127)
green = (144, 201, 120)

# load image
img_back_ground = pygame.image.load("IMG/TempleHallForest.jpg")
img_icon = pygame.image.load("IMG/icon.jpeg")
title_background = pygame.image.load("IMG/GameNameForest.png")
beam_background = pygame.transform.scale(
    pygame.image.load("IMG/Beam.png"), (159, 1200))
templeAssets = pygame.image.load('IMG/TempleAssets.png')
menuAssets = pygame.image.load('IMG/MenuAssets.png')
mechAssets = pygame.image.load('IMG/MechAssets.png')
charAssets = pygame.image.load("IMG/CharAssets.png")
groundAssets = pygame.image.load('IMG/GroundAssets.png')

background = pygame.transform.scale(templeAssets.subsurface(
    ibs*8+4, ibs * 16+8, ibs*8, ibs*8), (block*8, block*8))  # 1
topographic = pygame.transform.scale(templeAssets.subsurface(
    ibs*16+8, ibs * 16+8, ibs*8, ibs*8), (block*8, block*8))  # 2
fern = pygame.transform.scale(templeAssets.subsurface(
    ibs*29, 6, ibs*2, ibs*2), (block*2, block*2))  # 3
mossTree1 = pygame.transform.scale(templeAssets.subsurface(
    ibs*29+15, ibs*3, ibs*2, ibs*2), (block*2, block*2))  # 4
grass1 = pygame.transform.scale(templeAssets.subsurface(
    ibs*29+15, ibs*5, ibs*2, ibs*2), (block*2, block*2))  # 5
grass2 = pygame.transform.scale(templeAssets.subsurface(
    ibs*29+15, ibs*8, ibs*2, ibs), (block*2, block))  # 6
tree = pygame.transform.scale(templeAssets.subsurface(
    ibs*29+15, ibs*9, ibs*2, ibs*2), (block*2, block*2))  # 7
bush = pygame.transform.scale(templeAssets.subsurface(
    ibs*29+15, ibs*11, ibs*2, ibs*2), (block*2, block*2))  # 8
mossTree2 = pygame.transform.scale(templeAssets.subsurface(
    ibs*29+15, ibs*13, ibs*2, ibs*2), (block*2, block*2))  # 9
sub_topographic = [
    [
        topographic.subsurface(0, 0, block, block),  # 10
        topographic.subsurface(0, block, block, block),  # 11
        topographic.subsurface(0, block * 2, block, block),  # 12
        topographic.subsurface(0, block * 3, block, block),  # 13
        topographic.subsurface(0, block * 4, block, block),  # 14
        topographic.subsurface(0, block * 5, block, block),  # 15
        topographic.subsurface(0, block * 6, block, block),  # 16
        topographic.subsurface(0, block * 7, block, block)  # 17
    ],
    [
        topographic.subsurface(block, 0, block, block),  # 18
        topographic.subsurface(block, block, block, block),  # 19
        topographic.subsurface(block, block * 2, block, block),  # 20
        topographic.subsurface(block, block * 3, block, block),  # 21
        topographic.subsurface(block, block * 4, block, block),  # 22
        topographic.subsurface(block, block * 5, block, block),  # 23
        topographic.subsurface(block, block * 6, block, block),  # 24
        topographic.subsurface(block, block * 7, block, block)  # 25
    ],
    [
        topographic.subsurface(block * 2, 0, block, block),  # 26
        topographic.subsurface(block * 2, block, block, block),  # 27
        topographic.subsurface(block * 2, block * 2, block, block),  # 28
        topographic.subsurface(block * 2, block * 3, block, block),  # 29
        topographic.subsurface(block * 2, block * 4, block, block),  # 30
        topographic.subsurface(block * 2, block * 5, block, block),  # 31
        topographic.subsurface(block * 2, block * 6, block, block),  # 32
        topographic.subsurface(block * 2, block * 7, block, block)  # 33
    ],
    [
        topographic.subsurface(block * 3, 0, block, block),  # 34
        topographic.subsurface(block * 3, block, block, block),  # 35
        topographic.subsurface(block * 3, block * 2, block, block),  # 36
        topographic.subsurface(block * 3, block * 3, block, block),  # 37
        topographic.subsurface(block * 3, block * 4, block, block),  # 38
        topographic.subsurface(block * 3, block * 5, block, block),  # 39
        topographic.subsurface(block * 3, block * 6, block, block),  # 40
        topographic.subsurface(block * 3, block * 7, block, block)  # 41
    ],
    [
        topographic.subsurface(block * 4, 0, block, block),  # 42
        topographic.subsurface(block * 4, block, block, block),  # 43
        topographic.subsurface(block * 4, block * 2, block, block),  # 44
        topographic.subsurface(block * 4, block * 3, block, block),  # 45
        topographic.subsurface(block * 4, block * 4, block, block),  # 46
        topographic.subsurface(block * 4, block * 5, block, block),  # 47
        topographic.subsurface(block * 4, block * 6, block, block),  # 48
        topographic.subsurface(block * 4, block * 7, block, block)  # 49
    ],
    [
        topographic.subsurface(block * 5, 0, block, block),  # 50
        topographic.subsurface(block * 5, block, block, block),  # 51
        topographic.subsurface(block * 5, block * 2, block, block),  # 52
        topographic.subsurface(block * 5, block * 3, block, block),  # 53
        topographic.subsurface(block * 5, block * 4, block, block),  # 54
        topographic.subsurface(block * 5, block * 5, block, block),  # 55
        topographic.subsurface(block * 5, block * 6, block, block),  # 56
        topographic.subsurface(block * 5, block * 7, block, block)  # 57
    ],
    [
        topographic.subsurface(block * 6, 0, block, block),  # 58
        topographic.subsurface(block * 6, block, block, block),  # 59
        topographic.subsurface(block * 6, block * 2, block, block),  # 60
        topographic.subsurface(block * 6, block * 3, block, block),  # 61
        topographic.subsurface(block * 6, block * 4, block, block),  # 62
        topographic.subsurface(block * 6, block * 5, block, block),  # 63
        topographic.subsurface(block * 6, block * 6, block, block),  # 64
        topographic.subsurface(block * 6, block * 7, block, block)  # 65
    ],
    [
        topographic.subsurface(block * 7, 0, block, block),  # 66
        topographic.subsurface(block * 7, block, block, block),  # 67
        topographic.subsurface(block * 7, block * 2, block, block),  # 68
        topographic.subsurface(block * 7, block * 3, block, block),  # 69
        topographic.subsurface(block * 7, block * 4, block, block),  # 70
        topographic.subsurface(block * 7, block * 5, block, block),  # 71
        topographic.subsurface(block * 7, block * 6, block, block),  # 72
        topographic.subsurface(block * 7, block * 7, block, block)  # 73
    ]
]
save_img = pygame.image.load('IMG/save_btn.png')
load_img = pygame.image.load('IMG/load_btn.png')
