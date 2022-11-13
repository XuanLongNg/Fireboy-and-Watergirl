import pygame

path = "C:\\Users\\ADMIN\\Documents\\Fireboy-and-Watergirl\\IMG\\"
img_back_ground = pygame.image.load(path + "TempleHallForest.jpg")
img_icon = pygame.image.load(path + "icon.jpeg")
title_background = pygame.image.load(path + "GameNameForest.png")
beam_background = pygame.image.load(path + "Beam.png")
map1_background = pygame.image.load(path + "map1.png")
actor = pygame.image.load(path + "a.png")
diamond = pygame.image.load(path+"diamond.jpg")
L1 = pygame.image.load(path+"L1.png")
M1 = pygame.image.load(path+"M1.png")
R1 = pygame.image.load(path+"R1.png")
L2 = pygame.image.load(path+"L2.png")
M2 = pygame.image.load(path+"M2.png")
R2 = pygame.image.load(path+"R2.png")
press = pygame.image.load(path+"press.png")
brick = pygame.image.load(path + "Bricks.png")
beam_background = pygame.transform.scale(beam_background, (159, 600))
