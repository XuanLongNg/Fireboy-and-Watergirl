from os import path
import pickle
from Map import *
from setting import *
screen = pygame.display.set_mode((width, height))
# load in level data
level = 1
world_data = []
if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')
    world_data = pickle.load(pickle_in)
    print("Hello World")
world_data = Map(world_data)
for i in world_data.world_data:
    for j in i:
        screen.blit(j[0], j[1])
        print(j[2], end=" ")
    print()
clock = pygame.time.Clock()
fps = 30
game_over = True
while game_over:
    # world.draw_map()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False

    pygame.display.update()
    clock.tick(fps)
pygame.quit()
