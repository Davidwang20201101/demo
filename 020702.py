import pygame
from sys import exit
import random

class Bullet:
    def __init__(self):
        self.x= 0
        self.y= -1
        self.image = pygame.image.load('2.png').convert_alpha()
        self.active = False

    def move(self):
        if self.active:
            self.y -= 3
        if self.y < 0:
            self.active = False

    def restart(self):
        mouseX,mouseY = pygame.mouse.get_pos()
        self.x = mousex = - self.image.get_width()/2
        self.y = mouseY = - self.image.get_width()/2


        if self.y <0:
            mouseX , mouseY =pygame.mouse.get_pos()
            self.x =mouseX - self.image.get_width()/2
            self.y =mouseY - self.image.get_height()/2
            self.active = True

class Enemy:
     def restart(self):
        self.x =random.randint(50,400)
        self.y =random.randint(-200,-50)
        self.speed = random.radom() +0.1
     def __init__(self):
        self.x =200
        self.y= -50
        self.image =pygame.image.load('s.jpg').convert_alpha()

     def move(self):
            if self.y <800:
                self.y += 0.3
            else:
                self.y = -50


pygame.init()
screen = pygame.display.set_mode((500,700),0,32)
pygame.display.set_caption("Welcome,Kamrider MDZ~!")
background = pygame.image.load('MI.jpg')
player = pygame.image.load('hdh.jpeg')
enemies=[]
for i in range(5):
    enemies.append(Enemy())


bullets = []
for i in range(5):
    bullets.append(Bullet())
count_b = len(bullets)
index_b =0
gap_b=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0, 0))
    gap_b -= 1
    if gap_b <0:
        bullets[index_b].restart()
        gap_b = 100
        index_b = (index_b + 1) % count_b
    for b in bullets:
        if b.active:
            b.move()
            screen.blit(b.image,(b.x,b.y))
    for e in enemies:
        e.move()
        screen.blit(e.image,(e.x,e.y))


    # bullet.move()



    x,y = pygame.mouse.get_pos()
    x -= player .get_width()/2
    y -= player .get_height()/2
    screen.blit(player,(x,y))
    pygame.display.update()

