import pygame

path = "C:\\Users\\ADMIN\\Documents\\Fireboy-and-Watergirl\\IMG\\"
img_back_ground = pygame.image.load(path + "TempleHallForest.jpg")
img_icon = pygame.image.load(path + "icon.jpeg")
title_background = pygame.image.load(path + "GameNameForest.png")
beam_background = pygame.image.load(path + "Beam.png")
map1_background = pygame.image.load(path + "bg_map1.png")

diamond = pygame.image.load(path + "diamond.png")
diamondBlue = pygame.image.load(path + "diamond1.jpg")
diamondRed = pygame.image.load(path + "diamond2.png")

source = pygame.image.load(path + "CharAssets.png")
L1 = pygame.image.load(path + "L1.png")
M1 = pygame.image.load(path + "M1.png")
R1 = pygame.image.load(path + "R1.png")
L2 = pygame.image.load(path + "L2.png")
M2 = pygame.image.load(path + "M2.png")
R2 = pygame.image.load(path + "R2.png")

grass1 = pygame.image.load(path + "grass1.png")
grass21 = pygame.image.load(path + "grass21.png")
grass211 = pygame.image.load(path + "grass211.png")
press = pygame.image.load(path + "press.jpg")
brick = pygame.image.load(path + "Bricks.png")
brick1 = pygame.image.load(path + "brick1.png")

lavaBlueL = pygame.image.load(path + "lava1.png")
lavaBlueM = pygame.image.load(path + "lava2.png")
lavaBlueR = pygame.image.load(path + "lava3.png")

lavaRedL = pygame.image.load(path + "lavaRed1.png")
lavaRedM = pygame.image.load(path + "lavaRed2.png")
lavaRedR = pygame.image.load(path + "lavaRed3.png")

toxicL = pygame.image.load(path + "toxic1.png")
toxicM = pygame.image.load(path + "toxic2.png")
toxicR = pygame.image.load(path + "toxic3.png")

drownBlue = pygame.image.load(path + "drown.jpg")
drownRed = pygame.image.load(path + "drownRed.jpg")

box = pygame.image.load(path + "box.png")
dead = pygame.image.load(path + "dead.jpg")
character1 = pygame.image.load(path + "character1.jpg")

beam_background = pygame.transform.scale(beam_background, (159, 600))
