from pygame import *
from random import randint
import sys

mixer.init()
font.init()

clock = time.Clock()
FPS = 60
w = 600
h = 600
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
    def update_1 (self):
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 480:
            self.rect.y += self.speed
    
    def update_2 (self):
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 480:
            self.rect.y += self.speed
        
rocket_r = Player("ракетка.png", 30, 200, 10, 45, 120)    
rocket_l = Player("ракетка.png", 520 , 200, 10, 45, 120)  
ball = GameSprite("ball.png", 250, 250, 3, 50, 50 )  

speed_x = 3 
speed_y = 3

blue = (0, 0, 255)
green = (0, 255, 0)

font1 = font.Font(None, 50)
lose1 = font1.render("PLAYER 1 LOST!", True, blue)
lose2= font1.render("PLAYER 2 LOST!", True, blue)

running = True
finish = False
while running:
    window.fill(background)
    for e in event.get(): 
        if e.type == QUIT:
                running = False
    key_pressed = key.get_pressed()
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > w -50 or ball.rect.y< 0:
        speed_y *= -1
    if sprite.collide_rect(rocket_r, ball) or sprite.collide_rect(rocket_l, ball):
        speed_x *= -1
    
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 300))

    if ball.rect.x >= h:
        finish = True
        window.blit(lose2, (200, 300))
    rocket_l.reset()
    rocket_r.reset()
    rocket_r.update_1()
    rocket_l.update_2()
    ball.reset()

    display.update()    
    clock.tick(FPS)