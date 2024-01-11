from email.errors import StartBoundaryNotFoundDefect
from pickle import FALSE, TRUE
from tkinter import HORIZONTAL, Y
import pygame
import os
import random
from random import randint
pygame.init()
pygame.mixer.init()


# Variables
WIDTH = 1024
HEIGHT = 700
FPS = 60
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
running = True
game_over = True
counter = 60
direction = 0
global score
score = 0
skin1lock = False
skin2lock = False
skin3lock = True  # Set True if 4.99$ donated
skin = 0

# Main colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 204, 255)
YELLOW = (255, 255, 0)

# Screen settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Noel")


# Sound folder settings
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
snd_dir = os.path.join(os.path.dirname(__file__), 'snd')
click_sound1 = pygame.mixer.Sound(os.path.join(snd_dir, 'click_1.wav'))
click_sound1.set_volume(0.3)
click_sound2 = pygame.mixer.Sound(os.path.join(snd_dir, 'click_2.wav'))
click_sound2.set_volume(0.3)
click_sounds = [click_sound1, click_sound2]
equip_sound = pygame.mixer.Sound(os.path.join(snd_dir, 'gold.wav'))
equip_sound.set_volume(0.3)
deny_sound = pygame.mixer.Sound(os.path.join(snd_dir, 'hit_2.wav'))
deny_sound.set_volume(0.3)
fire_sound1 = pygame.mixer.Sound(os.path.join(snd_dir, 'pew.wav'))
fire_sound1.set_volume(0.4)
fire_sound2 = pygame.mixer.Sound(os.path.join(snd_dir, 'pew2.wav'))
fire_sound2.set_volume(0.4)
fire_sound3 = pygame.mixer.Sound(os.path.join(snd_dir, 'pew3.wav'))
fire_sound3.set_volume(0.05)
fire_sounds = [fire_sound1, fire_sound2, fire_sound3]
healing_sound = pygame.mixer.Sound(os.path.join(snd_dir, 'Heal.wav'))
healing_sound.set_volume(0.5)
breack_sound1 = pygame.mixer.Sound(os.path.join(snd_dir, 'door_ripped_1.wav'))
breack_sound1.set_volume(0.5)
breack_sound2 = pygame.mixer.Sound(os.path.join(snd_dir, 'door_ripped_2.wav'))
breack_sound2.set_volume(0.5)
breack_sounds = [breack_sound1, breack_sound2]
splash_sound1 = pygame.mixer.Sound(os.path.join(snd_dir, 'splash.wav'))
splash_sound1.set_volume(0.3)
splash_sound = pygame.mixer.Sound(os.path.join(snd_dir, 'splash.wav'))
splash_sound.set_volume(0.02)
splash_sound2 = pygame.mixer.Sound(os.path.join(snd_dir, 'fall.wav'))
splash_sound2.set_volume(0.3)
splash_sound3 = pygame.mixer.Sound(os.path.join(snd_dir, 'bonk.wav'))
splash_sound3.set_volume(0.3)
splash_sounds = [splash_sound1, splash_sound2, splash_sound3]
pygame.mixer.music.load(os.path.join(snd_dir, 'xeon6.wav'))
pygame.mixer.music.set_volume(0.1)


# Texture folder settings
fball_images = []
fball_sprites_list = ['1fball1.png', '1fball2.png', '1fball3.png', '1fball4.png', '1fball5.png',
                      '1fball6.png', '1fball7.png', '1fball8.png', '1fball9.png']
for img in fball_sprites_list:
    fball_images.append(pygame.image.load(os.path.join(img_folder, img)))
fball_anim = ['1fball0.png']
for i in range(8):
    filename = '1fball{}.png'.format(i+1)
    fball_anim.append(filename)
    img = pygame.image.load(os.path.join(img_folder, filename))
    img.set_colorkey(BLACK)
fball2_images = []
fball2_sprites_list = ['2fball1.png', '2fball2.png', '2fball3.png', '2fball4.png', '2fball5.png',
                       '2fball6.png', '2fball7.png', '2fball8.png', '2fball9.png']
for img in fball2_sprites_list:
    fball2_images.append(pygame.image.load(os.path.join(img_folder, img)))
fball2_anim = ['2fball0.png']
for i in range(8):
    filename = '2fball{}.png'.format(i+1)
    fball2_anim.append(filename)
    img = pygame.image.load(os.path.join(img_folder, filename))
    img.set_colorkey(BLACK)
fball3_images = []
fball3_sprites_list = ['3fball1.png', '3fball2.png', '3fball3.png', '3fball4.png', '3fball5.png',
                       '3fball6.png', '3fball7.png', '3fball8.png', '3fball9.png']
for img in fball3_sprites_list:
    fball3_images.append(pygame.image.load(os.path.join(img_folder, img)))
fball3_anim = ['3fball0.png']
for i in range(8):
    filename = '3fball{}.png'.format(i+1)
    fball3_anim.append(filename)
    img = pygame.image.load(os.path.join(img_folder, filename))
    img.set_colorkey(BLACK)
fball4_images = []
fball4_sprites_list = ['4fball1.png', '4fball2.png', '4fball3.png', '4fball4.png', '4fball5.png',
                       '4fball6.png', '4fball7.png', '4fball8.png', '4fball9.png']
for img in fball4_sprites_list:
    fball4_images.append(pygame.image.load(os.path.join(img_folder, img)))
fball4_anim = ['4fball0.png']
for i in range(8):
    filename = '4fball{}.png'.format(i+1)
    fball4_anim.append(filename)
    img = pygame.image.load(os.path.join(img_folder, filename))
    img.set_colorkey(BLACK)
wallbr_images = []
wallbr_sprites_list = ['1wallbr1.png', '1wallbr2.png', '1wallbr3.png', '1wallbr4.png', '1wallbr5.png',
                       '1wallbr6.png', '1wallbr7.png']
for img in wallbr_sprites_list:
    wallbr_images.append(pygame.image.load(os.path.join(img_folder, img)))
wallbr_anim = ['1wallbr0.png']
for i in range(6):
    filename = '1wallbr{}.png'.format(i+1)
    wallbr_anim.append(filename)
    img = pygame.image.load(os.path.join(img_folder, filename))
    img.set_colorkey(BLACK)
player_images = []
player_sprites_list = ['player_front1.png', 'player_front2.png', 'player_front3.png', 'player_right1.png', 'player_right2.png',
                       'player_right3.png', 'player_left1.png', 'player_left2.png', 'player_left3.png', 'player_back1.png', 'player_back2.png', 'player_back3.png']
for img in player_sprites_list:
    player_images.append(pygame.image.load(os.path.join(img_folder, img)))
skin0sprite = pygame.image.load(os.path.join(img_folder, 'skin0.png'))
skin1sprite = pygame.image.load(os.path.join(img_folder, 'skin1.png'))
skin1lsprite = pygame.image.load(os.path.join(img_folder, 'skin1l.png'))
skin2sprite = pygame.image.load(os.path.join(img_folder, 'skin2.png'))
skin2lsprite = pygame.image.load(os.path.join(img_folder, 'skin2l.png'))
skin3sprite = pygame.image.load(os.path.join(img_folder, 'skin3.png'))
skin3lsprite = pygame.image.load(os.path.join(img_folder, 'skin3l.png'))
skin4sprite = pygame.image.load(os.path.join(img_folder, 'skin4.png'))
background1 = pygame.image.load(os.path.join(img_folder, 'background1.png'))
background = pygame.image.load(os.path.join(img_folder, 'background.png'))
background2 = pygame.image.load(os.path.join(img_folder, 'background2.png'))
ground_img = pygame.image.load(os.path.join(img_folder, 'Ground.png'))
ground_x_img = pygame.image.load(os.path.join(img_folder, 'Ground_x.png'))
ground_y_img = pygame.image.load(os.path.join(img_folder, 'Ground_y.png'))
ground_xy_img = pygame.image.load(os.path.join(img_folder, 'Ground_xy.png'))
wall1_img = pygame.image.load(os.path.join(img_folder, 'wall1.png'))
wall2_img = pygame.image.load(os.path.join(img_folder, 'wall2.png'))
wall3_img = pygame.image.load(os.path.join(img_folder, 'wall3.png'))
game_over_1 = pygame.image.load(os.path.join(img_folder, 'Game_over_1.png'))
game_over_2 = pygame.image.load(os.path.join(img_folder, 'Game_over_2.png'))
#wall1_img = pygame.image.load(os.path.join(img_folder, 'wall1.png'))
heal_img = pygame.image.load(os.path.join(img_folder, 'heal.png'))
health_line_img = pygame.image.load(
    os.path.join(img_folder, 'health_line.png'))
score_img = pygame.image.load(os.path.join(img_folder, 'score.png'))
slime_images = []  # random choice for slime sprites
slime_list = ['slime_red_s.png',
              'slime_green_s.png', 'slime_blue_s.png', 'slime_blue_b.png', 'slime_blue_m.png', 'slime_red_b.png', 'slime_red_m.png', 'slime_green_m.png', 'slime_green_b.png']
for img in slime_list:
    slime_images.append(pygame.image.load(os.path.join(img_folder, img)))
splash_images = []
splash_list = ['splash0.png', 'splash1.png', 'splash2.png',
               'splash3.png', 'splash4.png', 'splash5.png', 'splash6.png', 'splash7.png']
for img in splash_list:
    splash_images.append(pygame.image.load(os.path.join(img_folder, img)))
splash_anim = ['splash0.png']
for i in range(7):
    filename = 'splash{}.png'.format(i+1)
    splash_anim.append(filename)
    img = pygame.image.load(os.path.join(img_folder, filename))
    img.set_colorkey(BLACK)
heal_images = []
heal_list = ['heal0.png', 'heal1.png', 'heal2.png',
             'heal3.png', 'heal4.png', 'heal5.png', 'heal6.png', 'heal7.png', 'heal8.png', 'heal9.png']
for img in heal_list:
    heal_images.append(pygame.image.load(os.path.join(img_folder, img)))
heal_anim = ['heal0.png']
for i in range(8):
    filename = 'heal{}.png'.format(i+1)
    heal_anim.append(filename)
    img = pygame.image.load(os.path.join(img_folder, filename))
    img.set_colorkey(BLACK)

blood_images = []
blood_list = ['blood0.png', 'blood1.png',
              'blood2.png', 'blood3.png', 'blood4.png']
for img in blood_list:
    blood_images.append(pygame.image.load(os.path.join(img_folder, img)))
blood_anim = ['blood0.png']
for i in range(0):
    filename = 'blood{}.png'.format(i+1)
    blood_anim.append(filename)
    img = pygame.image.load(os.path.join(img_folder, filename))
    img.set_colorkey(BLACK)


# Score file settings
file = open('text.txt', 'r')
best_score = file.read()
best_score = int(best_score)
file.close()
file = open('text.txt', 'w')


# Player sprite
class Player (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_images[0]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.hp = 100
        self.time_in_sec = 0
        self.shoot_delay = 450
        self.last_step = pygame.time.get_ticks()
        self.last_shot = pygame.time.get_ticks()
        self.radius = 25  # hitbox settings
        pygame.draw.circle(self.image, RED, self.rect.center, self.radius)

    def update(self):
        self.speedy = 0
        self.speedx = 0
        resistancex = 0
        resistancey = 0
        global direction
        self.time_in_sec += 1
        if self.time_in_sec >= 30:
            self.time_in_sec = 0
        keystate = pygame.key.get_pressed()  # player movement
        if keystate[pygame.K_a]:
            self.speedx = -6
            direction = 1
            if self.time_in_sec >= 0 and self.time_in_sec < 10:
                self.image = player_images[6]
            if self.time_in_sec >= 10 and self.time_in_sec < 20:
                self.image = player_images[7]
            if self.time_in_sec >= 20 and self.time_in_sec < 31:
                self.image = player_images[8]

        if keystate[pygame.K_d]:
            self.speedx = 6
            direction = 2
            if self.time_in_sec >= 0 and self.time_in_sec < 10:
                self.image = player_images[3]
            if self.time_in_sec >= 10 and self.time_in_sec < 20:
                self.image = player_images[4]
            if self.time_in_sec >= 20 and self.time_in_sec < 31:
                self.image = player_images[5]

        if keystate[pygame.K_w]:
            self.speedy = -6
            direction = 3
            if self.time_in_sec >= 0 and self.time_in_sec < 10:
                self.image = player_images[9]
            if self.time_in_sec >= 10 and self.time_in_sec < 20:
                self.image = player_images[10]
            if self.time_in_sec >= 20 and self.time_in_sec < 31:
                self.image = player_images[11]

        if keystate[pygame.K_s]:
            self.speedy = 6
            direction = 4
            if self.time_in_sec >= 0 and self.time_in_sec < 10:
                self.image = player_images[0]
            if self.time_in_sec >= 10 and self.time_in_sec < 20:
                self.image = player_images[1]
            if self.time_in_sec >= 20 and self.time_in_sec < 31:
                self.image = player_images[2]

        if keystate[pygame.K_SPACE]:
            self.shoot()
        if self.rect.right > WIDTH - 400:  # movement resistance
            resistancex = -round((self.rect.right - (WIDTH - 400))/10)
        if self.rect.left < 400:
            resistancex = -round((self.rect.left - 400)/10)
        if self.rect.top < 280:
            resistancey = -round((self.rect.top - 280)/10)
        if self.rect.bottom > HEIGHT - 280:
            resistancey = -round((self.rect.bottom - (HEIGHT - 280))/10)
        self.rect.x += self.speedx + resistancex
        self.rect.y += self.speedy + resistancey
        if self.hp < 0:
            self.hp = 0

    def shoot(self):  # Shooting
        sword = Sword()
        object = Object()
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            all_sprites.add(object)
            objects.add(object)
            all_sprites.add(sword)
            swords.add(sword)


# Main ground part sprite
class ground (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.speedx = 0
        self.speedy = 0
        self.resistancex = 0
        self.resistancey = 0
        if player.rect.right > WIDTH - 400:  # movement resistance
            self.resistancex = -round((player.rect.right - (WIDTH - 400))/10)
        if player.rect.left < 400:
            self.resistancex = -round((player.rect.left - 400)/10)
        if player.rect.top < 280:
            self.resistancey = -round((player.rect.top - 280)/10)
        if player.rect.bottom > HEIGHT - 280:
            self.resistancey = -round((player.rect.bottom - (HEIGHT - 280))/10)
        self.rect.x += self.speedx + self.resistancex
        self.rect.y += self.speedy + self.resistancey


# Ground helping part №1 sprite (x axis)
class ground_help_1 (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_x_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += Ground.speedx + Ground.resistancex
        self.rect.y += Ground.speedy + Ground.resistancey
        if Ground.rect.left >= 0 and Ground.rect.bottom > 0 and Ground.rect.top < HEIGHT:
            self.rect.right = Ground.rect.left
            self.rect.y = Ground.rect.y
        if Ground_help_1.rect.left >= 0 and Ground_help_1.rect.bottom > 0 and Ground_help_1.rect.top < HEIGHT:
            Ground.rect.right = Ground_help_1.rect.left
            Ground.rect.y = Ground_help_1.rect.y
        if Ground.rect.right <= WIDTH and Ground.rect.bottom > 0 and Ground.rect.top < HEIGHT:
            self.rect.left = Ground.rect.right
            self.rect.y = Ground.rect.y
        if Ground_help_1.rect.right <= WIDTH and Ground_help_1.rect.bottom > 0 and Ground_help_1.rect.top < HEIGHT:
            Ground.rect.left = Ground_help_1.rect.right
            Ground.rect.y = Ground_help_1.rect.y


# Ground helping part №3 sprite (y axis)
class ground_help_2 (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_y_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += Ground.speedx + Ground.resistancex
        self.rect.y += Ground.speedy + Ground.resistancey
        if Ground.rect.top >= 0:
            self.rect.bottom = Ground.rect.top
            self.rect.x = Ground.rect.x
        else:
            self.rect.top = Ground.rect.bottom
            self.rect.x = Ground.rect.x
        if self.rect.top >= 0:
            Ground.rect.bottom = self.rect.top
            Ground.rect.x = self.rect.x
        if self.rect.bottom <= HEIGHT:
            Ground.rect.top = self.rect.bottom
            Ground.rect.x = self.rect.x


# Ground helping part №3 sprite (both axis)
class ground_help_3 (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_xy_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += Ground.speedx + Ground.resistancex
        self.rect.y += Ground.speedy + Ground.resistancey
        if Ground_help_1.rect.top >= 0 and Ground_help_2.rect.left >= 0:
            self.rect.x = Ground_help_1.rect.x
            self.rect.y = Ground_help_2.rect.y
        if Ground_help_1.rect.bottom <= HEIGHT and Ground_help_2.rect.left >= 0:
            self.rect.x = Ground_help_1.rect.x
            self.rect.y = Ground_help_2.rect.y
        if Ground_help_1.rect.top >= 0 and Ground_help_2.rect.right <= WIDTH:
            self.rect.x = Ground_help_1.rect.x
            self.rect.y = Ground_help_2.rect.y
        if Ground_help_1.rect.bottom <= HEIGHT and Ground_help_2.rect.right <= WIDTH:
            self.rect.x = Ground_help_1.rect.x
            self.rect.y = Ground_help_2.rect.y


# Walls sprites
class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        wall = randint(1, 3)
        if wall == 1:  # random choice of sptites (with different hitboxes)
            self.image = wall1_img
            self.radius = 55
        elif wall == 2:
            self.image = wall2_img
            self.radius = 45
        else:
            self.image = wall3_img
            self.radius = 55
        self.rect = self.image.get_rect()
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius) #uncomment to check hitboxes
        self.image.set_colorkey(BLACK)
        r = randint(1, 4)  # walls spawn on the edges of screen
        if r == 1:  # Top spawn
            self.rect.x = random.uniform(
                0 - self.rect.width, WIDTH + self.rect.width)
            self.rect.y = random.uniform(-100, -200)
        elif r == 2:  # Bottom spawn
            self.rect.x = random.uniform(
                0 - self.rect.width, WIDTH + self.rect.width)
            self.rect.y = random.uniform(HEIGHT + 100, HEIGHT + 200)
        elif r == 3:  # Left spawn
            self.rect.x = random.uniform(-100, -200)
            self.rect.y = random.uniform(
                0 - self.rect.height, HEIGHT + self.rect.height)
        else:  # Right spawn
            self.rect.x = random.uniform(WIDTH + 100, WIDTH + 200)
            self.rect.y = random.uniform(
                0 - self.rect.height, HEIGHT + self.rect.height)

    def update(self):
        # Respawn when too far away from Player
        if (self.rect.right > WIDTH + 400) or (self.rect.left < -400) or (self.rect.top > HEIGHT + 200) or (self.rect.bottom < -200):
            r = randint(1, 4)
            if r == 1:
                self.rect.x = random.uniform(
                    0 - self.rect.width, WIDTH + self.rect.width)
                self.rect.y = random.uniform(-150, -200)
            elif r == 2:
                self.rect.x = random.uniform(
                    0 - self.rect.width, WIDTH + self.rect.width)
                self.rect.y = random.uniform(HEIGHT + 100, HEIGHT + 200)
            elif r == 3:
                self.rect.x = random.uniform(-300, -400)
                self.rect.y = random.uniform(
                    0 - self.rect.height, HEIGHT + self.rect.height)
            else:
                self.rect.x = random.uniform(WIDTH + 300, WIDTH + 400)
                self.rect.y = random.uniform(
                    0 - self.rect.height, HEIGHT + self.rect.height)
        self.rect.x += Ground.speedx + Ground.resistancex
        self.rect.y += Ground.speedy + Ground.resistancey


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(slime_images)
        self.rect = self.image.get_rect()
        self.flipimage = pygame.transform.flip(self.image, True, False)
        self.normalimage = self.image
        self.radius = round(self.rect.width / 2)
        r = randint(1, 4)  # mobs spawn on the edges of screen
        if r == 1:  # Top spawn
            self.rect.x = random.uniform(
                0 - self.rect.width, WIDTH + self.rect.width)
            self.rect.y = random.uniform(-100, -200)
        elif r == 2:  # Bottom spawn
            self.rect.x = random.uniform(
                0 - self.rect.width, WIDTH + self.rect.width)
            self.rect.y = random.uniform(HEIGHT + 100, HEIGHT + 200)
        elif r == 3:  # Left spawn
            self.rect.x = random.uniform(-100, -200)
            self.rect.y = random.uniform(
                0 - self.rect.height, HEIGHT + self.rect.height)
        else:  # Right spawn
            self.rect.x = random.uniform(WIDTH + 100, WIDTH + 200)
            self.rect.y = random.uniform(
                0 - self.rect.height, HEIGHT + self.rect.height)

    def update(self):
        if self.rect.x <= player.rect.x:
            self.image = self.flipimage
        else:
            self.image = self.normalimage

        # Respawn when too far away from Player
        if (self.rect.right > WIDTH + 200) or (self.rect.left < -200) or (self.rect.top > HEIGHT + 200) or (self.rect.bottom < -200):
            r = randint(1, 4)
            if r == 1:
                self.rect.x = random.uniform(
                    0 - self.rect.width, WIDTH + self.rect.width)
                self.rect.y = random.uniform(-100, -200)
            elif r == 2:
                self.rect.x = random.uniform(
                    0 - self.rect.width, WIDTH + self.rect.width)
                self.rect.y = random.uniform(HEIGHT + 100, HEIGHT + 200)
            elif r == 3:
                self.rect.x = random.uniform(-100, -200)
                self.rect.y = random.uniform(
                    0 - self.rect.height, HEIGHT + self.rect.height)
            else:
                self.rect.x = random.uniform(WIDTH + 100, WIDTH + 200)
                self.rect.y = random.uniform(
                    0 - self.rect.height, HEIGHT + self.rect.height)
        resistancex = 0
        resistancey = 0
        if player.rect.right > WIDTH - 400:  # Moving resistance
            resistancex = -round((player.rect.right - (WIDTH - 400))/10)
        if player.rect.left < 400:
            resistancex = -round((player.rect.left - 400)/10)
        if player.rect.top < 280:
            resistancey = -round((player.rect.top - 280)/10)
        if player.rect.bottom > HEIGHT - 280:
            resistancey = -round((player.rect.bottom - (HEIGHT - 280))/10)

        # Difficulty settings
        speedboost = 1
        global level
        level = 1
        if (score > 1000) and (score <= 3000):
            speedboost = 1.4
            level = 2
        elif (score > 3000) and (score <= 5000):
            speedboost = 1.8
            level = 3
        elif (score > 5000) and (score <= 8000):
            speedboost = 2.4
            level = 4
        elif score > 8000:
            speedboost = 3
            level = 5

        # Moving to Player
        if self.rect.x <= player.rect.x:
            self.speedx = speedboost
        if self.rect.x >= player.rect.x:
            self.speedx = -speedboost
        if self.rect.y <= player.rect.y:
            self.speedy = speedboost
        if self.rect.y >= player.rect.y:
            self.speedy = -speedboost
        if (self.rect.x < player.rect.x + 5) and (self.rect.x > player.rect.x - 5):
            self.speedx = 0
        if (self.rect.y < player.rect.y + 5) and (self.rect.y > player.rect.y - 5):
            self.speedy = 0
        self.rect.x += self.speedx + resistancex
        self.rect.y += self.speedy + resistancey

    def rotate(self):
        if self.rect.x <= player.rect.x:
            self.image = pygame.transform.flip(self.image, True, False)


# Helping object sprite settings
class Object(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((71, 100))
        self.rect = self.image.get_rect()
        self.rect.center = player.rect.center
        if direction == 1:
            self.rect.right = player.rect.left - 30
            self.rect.y = player.rect.y + 30
            self.image = pygame.transform.rotate(self.image, -90)
        if direction == 2:
            self.rect.left = player.rect.right
            self.rect.y = player.rect.y + 30
            self.image = pygame.transform.rotate(self.image, 90)
        if direction == 4:
            self.rect.top = player.rect.bottom
            self.rect.x = player.rect.x
            self.image = pygame.transform.rotate(self.image, 0)
        if direction == 3:
            self.rect.bottom = player.rect.top
            self.rect.x = player.rect.x
            self.image = pygame.transform.rotate(self.image, 180)
        self.image.set_colorkey(BLACK)

    def update(self):
        self.deadth_delay = 400
        now = pygame.time.get_ticks()
        if now - player.last_shot > self.deadth_delay:
            self.kill()


# Sword sprite settings
class Sword(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((71, 100))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.center = player.rect.center
        global direction  # Direction where the Player is looking
        if direction == 1:
            self.rect.right = player.rect.left - 30
            self.rect.y = player.rect.y + 30
            self.image = pygame.transform.rotate(self.image, -90)
        if direction == 2:
            self.rect.left = player.rect.right
            self.rect.y = player.rect.y + 30
            self.image = pygame.transform.rotate(self.image, 90)
        if direction == 4:
            self.rect.top = player.rect.bottom
            self.rect.x = player.rect.x
            self.image = pygame.transform.rotate(self.image, 0)
        if direction == 3:
            self.rect.bottom = player.rect.top
            self.rect.x = player.rect.x
            self.image = pygame.transform.rotate(self.image, 180)

    def update(self):
        self.deadth_delay = 400
        now = pygame.time.get_ticks()
        if now - player.last_shot > self.deadth_delay:
            self.kill()


# Heal sprite settings
class HPboost(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = heal_img
        self.image = pygame.transform.scale(heal_img, (55, 55))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        r = randint(1, 4)
        if r == 1:  # Top spawn
            self.rect.x = random.uniform(
                0 - self.rect.width, WIDTH + self.rect.width)
            self.rect.y = random.uniform(-100, -200)
        elif r == 2:  # Bottom sprite
            self.rect.x = random.uniform(
                0 - self.rect.width, WIDTH + self.rect.width)
            self.rect.y = random.uniform(HEIGHT + 100, HEIGHT + 200)
        elif r == 3:  # Left spawn
            self.rect.x = random.uniform(-100, -200)
            self.rect.y = random.uniform(
                0 - self.rect.height, HEIGHT + self.rect.height)
        else:  # Right spawn
            self.rect.x = random.uniform(WIDTH + 100, WIDTH + 200)
            self.rect.y = random.uniform(
                0 - self.rect.height, HEIGHT + self.rect.height)

    def update(self):
        # Respawn when the Player too far away
        if (self.rect.right > WIDTH + 200) or (self.rect.left < -200) or (self.rect.top > HEIGHT + 200) or (self.rect.bottom < -200):
            r = randint(1, 4)
            if r == 1:
                self.rect.x = random.uniform(
                    0 - self.rect.width, WIDTH + self.rect.width)
                self.rect.y = random.uniform(-100, -200)
            elif r == 2:
                self.rect.x = random.uniform(
                    0 - self.rect.width, WIDTH + self.rect.width)
                self.rect.y = random.uniform(HEIGHT + 100, HEIGHT + 200)
            elif r == 3:
                self.rect.x = random.uniform(-100, -200)
                self.rect.y = random.uniform(
                    0 - self.rect.height, HEIGHT + self.rect.height)
            else:
                self.rect.x = random.uniform(WIDTH + 100, WIDTH + 200)
                self.rect.y = random.uniform(
                    0 - self.rect.height, HEIGHT + self.rect.height)
        self.rect.x += Ground.speedx + Ground.resistancex
        self.rect.y += Ground.speedy + Ground.resistancey


# HP bar sprite settings
class HPs(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((200, 40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (145, 45)

    def update(self):
        if player.hp >= 1:
            self.image = pygame.Surface((player.hp * 2, 40))
        self.image.fill(RED)


# Body of HP bar sprite
class HPbody(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = health_line_img
        self.rect = self.image.get_rect()
        self.rect.center = (150, 45)


# Body of score counter
class SCOREbody(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = score_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - 75, 50)


# Top part of "Game over" notification
class Game_over1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = game_over_1
        self.image = pygame.transform.scale(game_over_1, (WIDTH + 100, 250))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.center = (WIDTH + 1000, HEIGHT / 2 - 250)
        self.speedx = 0
        self.stat = 1

    def update(self):
        self.rect.x += self.speedx
        if counter > 0:
            player.speedx = 0
            player.speedy = 0
            player.resistancex = 0
            player.resistancey = 0
            self.speedx = -counter * 0.1
            if self.rect.right < 0:
                self.speedx = 0
                self.stat = 0
                pygame.time.delay(0)
                self.kill()


# Bottom part of "Game over" notification
class Game_over2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = game_over_2
        self.image = pygame.transform.scale(game_over_2, (WIDTH + 100, 250))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.center = (-1000, HEIGHT / 2 + 250)
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx
        if counter > 0:
            self.speedx = counter * 0.1
            if self.rect.left > WIDTH:
                self.speedx = 0


# main menu screen
def show_go_screen():
    screen.blit(background, (0, 0))
    text(screen, str(best_score), 40, WIDTH - 73, 27)  # Text on the screen
    pygame.display.update()
    waiting = True
    while waiting == True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file.write(str(best_score))
                print(best_score)
                file.close()
                pygame.quit()
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_TAB]:
                random.choice(click_sounds).play()
                waiting = False
            if keystate[pygame.K_ESCAPE]:
                random.choice(click_sounds).play()
                file.write(str(best_score))
                file.close()
                pygame.quit()
            if keystate[pygame.K_e]:
                random.choice(click_sounds).play()
                hints_screen()
            if keystate[pygame.K_q]:
                random.choice(click_sounds).play()
                skins_screen()


# Screen with controls
def hints_screen():
    screen.blit(background1, (0, 0))
    text(screen, str(best_score), 40, WIDTH - 73, 27)  # Text on the screen
    pygame.display.update()
    waiting = True
    while waiting == True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file.write(str(best_score))
                file.close()
                pygame.quit()
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_TAB]:
                waiting = False
            if keystate[pygame.K_ESCAPE]:
                random.choice(click_sounds).play()
                file.write(str(best_score))
                file.close()
                pygame.quit()
            if keystate[pygame.K_e]:
                random.choice(click_sounds).play()
                show_go_screen()


# Screen with skin settings
def skins_screen():
    global skin
    screen.blit(background2, (0, 0))
    screen.blit(skin0sprite, (245, 105))
    if skin1lock == True:
        screen.blit(skin1sprite, (590, 105))
    if skin1lock == False:
        screen.blit(skin1lsprite, (590, 105))
        text(screen, 'Reach 2000 points to unlock', 18, 705, 215)
    if skin2lock == True:
        screen.blit(skin2sprite, (245, 252))
    if skin2lock == False:
        text(screen, 'Reach 4000 points to unlock', 18, 350, 361)
        screen.blit(skin2lsprite, (245, 252))
    if skin3lock == True:
        screen.blit(skin3sprite, (570, 245))
    if skin3lock == False:
        screen.blit(skin3lsprite, (570, 245))
        text(screen, '4.99$', 18, 705, 361)
    screen.blit(skin4sprite, (570, 418))
    screen.blit(skin4sprite, (225, 418))
    global skin_description
    skin_description = ''
    text(screen, skin_description, 32, 280, 550)
    pygame.display.update()
    waiting = True
    while waiting == True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file.write(str(best_score))
                file.close()
                pygame.quit()
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_TAB]:
                random.choice(click_sounds).play()
                waiting = False
            if keystate[pygame.K_ESCAPE]:
                random.choice(click_sounds).play()
                file.write(str(best_score))
                file.close()
                pygame.quit()
            if keystate[pygame.K_q]:
                random.choice(click_sounds).play()
                show_go_screen()
            if keystate[pygame.K_1]:
                equip_sound.play()
                skin = 0
                skin_description = 'Skin 1 set'
            if keystate[pygame.K_2]:
                if skin1lock == True:
                    equip_sound.play()
                    skin = 1
                    skin_description = 'Skin 2 set'
                else:
                    deny_sound.play()
            if keystate[pygame.K_3]:
                if skin2lock == True:
                    equip_sound.play()
                    skin = 2
                else:
                    deny_sound.play()
            if keystate[pygame.K_4]:
                if skin3lock == True:
                    equip_sound.play()
                    skin = 3
                else:
                    deny_sound.play()


# splash animation
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = splash_images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(splash_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = splash_images[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


# Wall breach animation
class Wallbr(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = wallbr_images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(wallbr_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = wallbr_images[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


# Healing animation
class Healing(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = heal_images[0]
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y + 30
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(heal_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = heal_images[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


# Blood animation
class Blood(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = blood_images[0]
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y + 30
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(blood_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = blood_images[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


# Attack fireball animation
class Fball(pygame.sprite.Sprite):
    def __init__(self, x, y, rot):
        pygame.sprite.Sprite.__init__(self)
        if skin == 1:
            self.image = fball2_images[0]
        elif skin == 2:
            self.image = fball3_images[0]
        elif skin == 3:
            self.image = fball4_images[0]
        else:
            self.image = fball_images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rot = rot
        self.image = pygame.transform.rotate(self.image, rot)
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if skin == 1:
                if self.frame == len(fball2_anim):
                    self.kill()
                else:
                    center = self.rect.center
                    self.image = fball2_images[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center
                    self.image = pygame.transform.rotate(self.image, self.rot)
            elif skin == 2:
                if self.frame == len(fball3_anim):
                    self.kill()
                else:
                    center = self.rect.center
                    self.image = fball3_images[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center
                    self.image = pygame.transform.rotate(self.image, self.rot)
            elif skin == 3:
                if self.frame == len(fball4_anim):
                    self.kill()
                else:
                    center = self.rect.center
                    self.image = fball4_images[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center
                    self.image = pygame.transform.rotate(self.image, self.rot)
            else:
                if self.frame == len(fball_anim):
                    self.kill()
                else:
                    center = self.rect.center
                    self.image = fball_images[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center
                    self.image = pygame.transform.rotate(self.image, self.rot)


# Drawing text
font_name = pygame.font.match_font('arial')


# Text settings
def text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, YELLOW)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def text_left(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, YELLOW)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surf.blit(text_surface, text_rect)


# Moving sprites in group "all_sprites" + Drawing all sprites
while running:  # main loop of a game
    clock.tick(FPS)  # Speed of a game
    for event in pygame.event.get():  # Stopping if the game is closed
        if event.type == pygame.QUIT:
            running = False

    if game_over == True:
        game_over = False
        if best_score >= 2000:
            skin1lock = True
        if best_score >= 4000:
            skin2lock = True
        show_go_screen()
        pygame.mixer.music.play(loops=-1)
        score = 0
        all_sprites = pygame.sprite.Group()
        Grounds = pygame.sprite.Group()
        Ground = ground()
        all_sprites.add(Ground)
        Grounds.add(Ground)
        Ground_help_1 = ground_help_1()
        all_sprites.add(Ground_help_1)
        Grounds.add(Ground_help_1)
        Ground_help_2 = ground_help_2()
        all_sprites.add(Ground_help_2)
        Grounds.add(Ground_help_2)
        Ground_help_3 = ground_help_3()
        all_sprites.add(Ground_help_3)
        Grounds.add(Ground_help_3)
        swords = pygame.sprite.Group()
        objects = pygame.sprite.Group()
        hpboosts = pygame.sprite.Group()
        walls = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        player = Player()
        for j in range(8):  # Number of walls
            w = Wall()
            all_sprites.add(w)
            walls.add(w)
        for i in range(8):  # Number of enemies
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)
        hpboost = HPboost()
        all_sprites.add(hpboost)
        hpboosts.add(hpboost)
        all_sprites.add(player)

        # Drawing GUI sprites
        hps = HPs()
        all_sprites.add(hps)
        hpbody = HPbody()
        scorebody = SCOREbody()
        game_over1 = Game_over1()
        game_over2 = Game_over2()

    if game_over1.stat == 0:
        game_over = True

    # Collision check
    all_sprites.update()
    playerisongroung = False
    objhit = pygame.sprite.groupcollide(objects, swords, True, False)
    for objhits in objhit:
        random.choice(fire_sounds).play()
        if direction == 1:
            fball = Fball(objhits.rect.x, objhits.rect.y, -90)
            all_sprites.add(fball)
        if direction == 2:
            fball = Fball(objhits.rect.x, objhits.rect.y, 90)
            all_sprites.add(fball)
        if direction == 3:
            fball = Fball(objhits.rect.x, objhits.rect.y, 180)
            all_sprites.add(fball)
        if direction == 4:
            fball = Fball(objhits.rect.x, objhits.rect.y, 0)
            all_sprites.add(fball)
    playerongroung = pygame.sprite.spritecollide(player, Grounds, False)
    for playerongroung in playerongroung:
        playerisongroung = True
    if playerisongroung == False:
        player.hp -= 4
    playerhit = pygame.sprite.spritecollide(player, mobs, False)
    for playerhits in playerhit:
        player.hp -= 2
        blood = Blood()
        all_sprites.add(blood)
    mobhit = pygame.sprite.groupcollide(mobs, swords, True, False)
    for mobhits in mobhit:
        random.choice(splash_sounds).play()
        score += mobhits.radius + 10
        m = Mob()
        all_sprites.add(m)
        expl = Explosion(mobhits.rect.x, mobhits.rect.y)
        all_sprites.add(expl)
        mobs.add(m)
    mobwallhit = pygame.sprite.groupcollide(mobs, walls, True, False)
    for mobwallhits in mobwallhit:
        splash_sound.play()
        m = Mob()
        all_sprites.add(m)
        expl = Explosion(mobwallhits.rect.x, mobwallhits.rect.y)
        all_sprites.add(expl)
        mobs.add(m)
    playerwallhit = pygame.sprite.spritecollide(
        player, walls, True, pygame.sprite.collide_circle)
    for playerwallhits in playerwallhit:
        random.choice(breack_sounds).play()
        player.hp -= 20
        w = Wall()
        all_sprites.add(w)
        walls.add(w)
        wallbr = Wallbr(playerwallhits.rect.x, playerwallhits.rect.y)
        all_sprites.add(wallbr)
    swordwallhit = pygame.sprite.groupcollide(
        swords, walls, False, True, pygame.sprite.collide_circle)
    for swordwallhits in swordwallhit:
        random.choice(breack_sounds).play()
        w = Wall()
        all_sprites.add(w)
        walls.add(w)
        player.hp -= 5
        pygame.time.delay(80)
        wallbr = Wallbr(swordwallhits.rect.x, swordwallhits.rect.y)
        all_sprites.add(wallbr)
    if player.hp <= 0:
        if score > best_score:
            best_score = score
        all_sprites.add(game_over1)
        all_sprites.add(game_over2)
        counter += 1
        if counter >= 400:
            score = 0
    playerHPboosthit = pygame.sprite.spritecollide(player, hpboosts, True)
    for playerHPboosthits in playerHPboosthit:
        healing_sound.play()
        player.hp += randint(10, 20)
        if player.hp > 100:
            player.hp = 100
        hpboost = HPboost()
        all_sprites.add(hpboost)
        hpboosts.add(hpboost)
        healing = Healing()
        all_sprites.add(healing)

    # Rendering
    screen.fill(BLACK)
    all_sprites.draw(screen)
    screen.blit(hps.image, hps.rect)
    hps.update()
    screen.blit(hpbody.image, hpbody.rect)
    hpbody.update()
    screen.blit(scorebody.image, scorebody.rect)
    scorebody.update()
    text(screen, str(score), 26, WIDTH - 73, 52)  # Text on the screen
    text(screen, str(player.hp), 24, 70, 25)
    text(screen, str(level), 24, WIDTH - 20, 100)
    # Final rendering
    pygame.display.flip()

# Quit if closed
file.write(str(best_score))
file.close()
pygame.quit()
