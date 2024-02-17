from pygame import *
from random import randint
import sys

mixer.init()
font.init()

clock = time.Clock()
FPS = 60
w = 700
h = 500
speed = 5
window = display.set_mode((w, h))
display.set_caption("Ping-pong")
background = (255, 255, 255)
window.fill(background)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update (self):
        if key_pressed[K_d] and self.rect.x < 625:
            self.rect.x += self.speed
        if key_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[K_w] and self.rect.y > 250:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 425:
            self.rect.y += self.speed

running = True
while running:
    for e in event.get(): 
        if e.type == QUIT:
                running = False
    key_pressed = key.get_pressed()
    
    display.update()    
    clock.tick(FPS)