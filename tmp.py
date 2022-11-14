import pygame
import tmx
import sys

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

tilemap = tmx.load("D:\Project\Fire_boy_and_water_girl\IMG\map.tmx", screen.get_size())

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    screen.fill((95, 183, 229)) # sky color
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("Hello World !", 1, (255, 0, 0))
        textpos = text.get_rect(centerx=width/2)
        screen.blit(text, textpos)

    tilemap.set_focus(0, 480)
    tilemap.draw(screen)

    pygame.display.flip()