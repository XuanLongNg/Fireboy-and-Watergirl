import pygame
from pygame.mixer_music import play

import img
import matrix

clock = pygame.time.Clock()
pygame.init()

width = 1020
height = 563

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Map 1")

tile_size = 20
score = 0
isPress1 = False
isPress2 = False


def draw_grid():
    for line in range(0, 52):
        pygame.draw.line(screen, (0, 0, 0), (0, line * tile_size), (width, line * tile_size))
        pygame.draw.line(screen, (0, 0, 0), (line * tile_size, 0), (line * tile_size, height))


class Player:
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.transform.scale(img.actor, (20, 30))
            img_left = pygame.transform.flip(img.actor, False, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0

    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 30
        print(self.image.get_rect())

        # get keypress
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.jumped == False:
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
            # check for collision in x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0

            # check for collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if below the ground i.e. jumping
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                # check if above the ground i.e. jumping
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0

        # check for collision with diamond
        if pygame.sprite.spritecollide(self, blob_group, False):
            game_over = 0

        # update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        # draw player onto screen
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)


class World:
    def __init__(self, data):
        self.tile_list = []
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    image = pygame.transform.scale(img.brick, (tile_size, tile_size))
                    img_rect = image.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (image, img_rect)
                    self.tile_list.append(tile)
                # if tile == 2:
                #     img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                #     img_rect = img.get_rect()
                #     img_rect.x = col_count * tile_size
                #     img_rect.y = row_count * tile_size
                #     tile = (img, img_rect)
                #     self.tile_list.append(tile)
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

                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (0, 0, 0), tile[1], 2)


class Diamond(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img.diamond, (tile_size, tile_size))
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
press1_group = pygame.sprite.Group()
press2_group = pygame.sprite.Group()

L_group = pygame.sprite.Group()
M_group = pygame.sprite.Group()
R_group = pygame.sprite.Group()
L2_group = pygame.sprite.Group()
M2_group = pygame.sprite.Group()
R2_group = pygame.sprite.Group()

world = World(matrix.world_data)

run = True
while run:
    screen.blit(img.map1_background, (0, 0))

    draw_grid()
    world.draw()

    if pygame.sprite.spritecollide(player, diamond_group, True):
        score += 1

    if pygame.sprite.spritecollide(player, press1_group, True):
        print(pygame.sprite.spritecollideany(player, press1_group, True))
        isPress1 = False
        isPress2 = True
        pygame.sprite.spritecollide(player, press2_group, False)
    if pygame.sprite.spritecollide(player, press2_group, True):
        isPress1 = True
        isPress2 = False
        pygame.sprite.spritecollide(player, press1_group, False)

    blob_group.draw(screen)
    diamond_group.draw(screen)
    press1_group.draw(screen)
    press2_group.draw(screen)
    L_group.draw(screen)
    M_group.draw(screen)
    R_group.draw(screen)
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

    player.update()
    pygame.time.delay(22)
    pygame.display.update()

pygame.quit()
quit()
