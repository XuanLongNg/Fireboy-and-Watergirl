import pygame
import img
from setting import *
clock=pygame.time.Clock()

pygame.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Fireboy & Watergirl")
playButton = "Play"

pygame.display.set_icon(img.img_icon)
pygame.display.update()

def disBeam(degree):
    screen.blit(img.img_back_ground,(0,0))
    tmp = img.beam_background
    tmp = pygame.transform.rotate(tmp,degree)
    screen.blit(tmp, (width/2, -600))
    screen.blit(img.title_background, (255, 80))

    pygame.display.update()
game_over = False
degree = 0
adding = 0.01
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    degree+=adding

    if degree == 15 or degree ==-15:
        adding = -adding
    disBeam(degree)
    pygame.display.update()
    clock.tick(1000)
pygame.quit()
quit()