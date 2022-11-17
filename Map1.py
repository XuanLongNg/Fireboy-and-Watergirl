import pygame
from pygame.locals import *
import pickle
import img
import matrix

clock = pygame.time.Clock()
pygame.init()

width = 1020
height = 563

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Map 1")

game_over = 0
tile_size = 20
score = 0
isPress1 = False
isPress2 = False
animation_dia = 0
step = 0.2


class Player:
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.transform.scale(pygame.image.load(img.path + f'character{num}.jpg'), (tile_size, 30))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.dead_image = pygame.transform.scale(img.dead, (tile_size, tile_size))
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0

    def update(self, game_over):
        dx = 0
        dy = 0
        walk_cooldown = 5
        if game_over == 0:
            # get keypress
            key = pygame.key.get_pressed()
            if key[pygame.K_UP] and not self.jumped:
                self.jumped = True
                self.vel_y = -12
            if not key[pygame.K_UP]:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1

            if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # handle animation
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # add gravity
            self.vel_y += 1.2
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            # check for collision
            for tile in world.tile_list:

                if len(tile) == 3 and tile[2] == 1:
                    if tile[1].colliderect(self.rect.x, self.rect.y, self.width, self.height):

                        dx = -5

                # check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height) and len(tile) == 2:
                    dx = 0
                # check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height) and len(tile) == 2:
                    # check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # check if above the ground i.e. jumping
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0

            # check for collision with diamond
            if pygame.sprite.spritecollide(self, LavaL_group, False) or pygame.sprite.spritecollide(self, LavaM_group, False) or pygame.sprite.spritecollide(
                    self, LavaR_group, False) or pygame.sprite.spritecollide(self, ToxicL_group, False) or pygame.sprite.spritecollide(self, ToxicM_group,
                                                                                                                                       False) or pygame.sprite.spritecollide(
                self, ToxicR_group, False):
                game_over = -1
                print(game_over)

            # update player coordinates
            self.rect.x += dx
            self.rect.y += dy
        elif game_over == -1:
            self.image = self.dead_image
            if self.rect.y > 450 or self.rect.y > 380:
                self.rect.y -= 5
            # if self.rect.y >=377:
            #     self.image = pygame.transform.scale(img.brick, (tile_size, tile_size))

        # draw player onto screen
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        return game_over


class World:
    def __init__(self, data):
        self.tile_list = []
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 0:
                    image = pygame.transform.scale(img.brick, (tile_size, tile_size))
                    img_rect = image.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (image, img_rect, 0)
                    self.tile_list.append(tile)
                if tile == 1:
                    image = pygame.transform.scale(img.brick1, (tile_size, tile_size))
                    img_rect = image.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (image, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    image = pygame.transform.scale(img.grass1, (tile_size, tile_size))
                    img_rect = image.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (image, img_rect)
                    self.tile_list.append(tile)
                if tile == 2.1:
                    image = pygame.transform.scale(img.grass21, (tile_size, tile_size))
                    img_rect = image.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (image, img_rect, 0)
                    self.tile_list.append(tile)
                if tile == 2.11:
                    image = pygame.transform.scale(img.grass211, (tile_size, tile_size))
                    img_rect = image.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (image, img_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    regi = Box(col_count * tile_size, row_count * tile_size, self.tile_list)
                    box_group.add(regi)
                if tile == 4.1:
                    regi = ToxicL(col_count * tile_size, row_count * tile_size)
                    ToxicL_group.add(regi)
                if tile == 4.2:
                    regi = ToxicM(col_count * tile_size, row_count * tile_size)
                    ToxicM_group.add(regi)
                if tile == 4.3:
                    regi = ToxicR(col_count * tile_size, row_count * tile_size)
                    ToxicR_group.add(regi)
                if tile == 5:
                    diamond = Diamond(col_count * tile_size, row_count * tile_size)
                    diamond_group.add(diamond)
                if tile == 6.1:
                    regi = L(col_count * tile_size, row_count * tile_size)
                    L_group.add(regi)
                if tile == 6:
                    regi = M(col_count * tile_size, row_count * tile_size)
                    M_group.add(regi)
                if tile == 6.2:
                    regi = R(col_count * tile_size, row_count * tile_size)
                    R_group.add(regi)
                if tile == 7.1:
                    regi = L2(col_count * tile_size, row_count * tile_size)
                    L2_group.add(regi)
                if tile == 7:
                    regi = M2(col_count * tile_size, row_count * tile_size)
                    M2_group.add(regi)
                if tile == 7.2:
                    regi = R2(col_count * tile_size, row_count * tile_size)
                    R2_group.add(regi)
                if tile == 8:
                    regi = Press(col_count * tile_size, row_count * tile_size)
                    press1_group.add(regi)
                if tile == 9:
                    regi = Press(col_count * tile_size, row_count * tile_size)
                    press2_group.add(regi)
                if tile == 10.1:
                    regi = LavaL(col_count * tile_size, row_count * tile_size, self.tile_list)
                    LavaL_group.add(regi)
                if tile == 10.2:
                    regi = LavaM(col_count * tile_size, row_count * tile_size, self.tile_list)
                    LavaM_group.add(regi)
                if tile == 10.3:
                    regi = LavaR(col_count * tile_size, row_count * tile_size, self.tile_list)
                    LavaR_group.add(regi)

                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            # pygame.draw.rect(screen, (0, 0, 0), tile[1], 1)


class Diamond(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img.diamond1, (tile_size + 5, tile_size + 5))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0


class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, lis):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img.box, (tile_size * 1.5, tile_size * 1.5))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 10
        tile = (self.image, self.rect, 1)
        lis.append(tile)


class LavaL(pygame.sprite.Sprite):
    def __init__(self, x, y, lis):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img.lavaL, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class LavaM(pygame.sprite.Sprite):
    def __init__(self, x, y, lis):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img.lavaM, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class LavaR(pygame.sprite.Sprite):
    def __init__(self, x, y, lis):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img.lavaR, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class ToxicL(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img.toxicL, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class ToxicM(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img.toxicM, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class ToxicR(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img.toxicR, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Press(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img.press, (30, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class L(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img.L1, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.y += self.move_direction
        self.move_counter += 1
        world.tile_list.append((self.image, self.rect))
        if self.move_counter > 60:
            self.move_direction *= -1
            self.move_counter = 0


class M(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img.M1, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.y += self.move_direction
        world.tile_list.append((self.image, self.rect))
        self.move_counter += 1
        if self.move_counter > 60:
            self.move_direction *= -1
            self.move_counter = 0


class R(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img.R1, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.y += self.move_direction
        world.tile_list.append((self.image, self.rect))
        self.move_counter += 1
        if self.move_counter > 60:
            self.move_direction *= -1
            self.move_counter = 0


class L2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img.L2, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.y += self.move_direction
        self.move_counter += 1
        world.tile_list.append((self.image, self.rect))
        if self.move_counter > 60:
            self.move_direction *= -1
            self.move_counter = 0


class M2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img.M2, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.y += self.move_direction
        world.tile_list.append((self.image, self.rect))
        self.move_counter += 1
        if self.move_counter > 60:
            self.move_direction *= -1
            self.move_counter = 0


class R2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img.R2, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.y += self.move_direction
        world.tile_list.append((self.image, self.rect))
        self.move_counter += 1
        if self.move_counter > 60:
            self.move_direction *= -1
            self.move_counter = 0


player = Player(40, height - 80)
blob_group = pygame.sprite.Group()
diamond_group = pygame.sprite.Group()
box_group = pygame.sprite.Group()

press1_group = pygame.sprite.Group()
press2_group = pygame.sprite.Group()

L_group = pygame.sprite.Group()
M_group = pygame.sprite.Group()
R_group = pygame.sprite.Group()
L2_group = pygame.sprite.Group()
M2_group = pygame.sprite.Group()
R2_group = pygame.sprite.Group()

LavaL_group = pygame.sprite.Group()
LavaM_group = pygame.sprite.Group()
LavaR_group = pygame.sprite.Group()

ToxicL_group = pygame.sprite.Group()
ToxicM_group = pygame.sprite.Group()
ToxicR_group = pygame.sprite.Group()

world = World(matrix.world_data)

run = True
while run:
    screen.blit(img.map1_background, (0, 0))

    world.draw()

    if pygame.sprite.spritecollide(player, diamond_group, True):
        score += 1
    if pygame.sprite.spritecollide(player, press1_group, True):
        isPress1 = False
        isPress2 = True
        pygame.sprite.spritecollide(player, press2_group, False)
    if pygame.sprite.spritecollide(player, press2_group, True):
        isPress1 = True
        isPress2 = False
        pygame.sprite.spritecollide(player, press1_group, False)

    blob_group.draw(screen)
    diamond_group.draw(screen)
    box_group.draw(screen)

    LavaL_group.draw(screen)
    LavaM_group.draw(screen)
    LavaR_group.draw(screen)

    ToxicL_group.draw(screen)
    ToxicM_group.draw(screen)
    ToxicR_group.draw(screen)

    press1_group.draw(screen)
    press2_group.draw(screen)
    L_group.draw(screen)
    M_group.draw(screen)
    R_group.draw(screen)
    if game_over == 0:
        if isPress1:
            L_group.update()
            M_group.update()
            R_group.update()
        L2_group.draw(screen)
        M2_group.draw(screen)
        R2_group.draw(screen)
        if isPress2:
            L2_group.update()
            M2_group.update()
            R2_group.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    game_over = player.update(game_over)
    pygame.time.delay(22)
    pygame.display.update()

pygame.quit()
quit()
