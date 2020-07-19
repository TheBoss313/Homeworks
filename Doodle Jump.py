from pygame.locals import *
import pygame
import random
import sys


class DoodleJump:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 25)
        self.green = pygame.image.load('assets/green.png').convert_alpha()
        self.platforms = []
        self.springs = []
        self.cameray = 0
        self.direction = 0
        self.playerx = 400
        self.playery = 400
        self.jump = 0
        self.gravity = 0
        self.xmovement = 0
        self.blue = pygame.image.load('assets/blue.png')
        self.died = pygame.image.load('assets/died.png')
        self.spring = pygame.image.load('assets/spring.png')
        self.spring_1 = pygame.image.load('assets/spring_1.png')
        self.red_1 = pygame.image.load('assets/red_1.png')
        self.red = pygame.image.load('assets/red.png')
        self.playerLeft_1 = pygame.image.load('assets/left_1.png')
        self.playerRight_1 = pygame.image.load('assets/right_1.png')
        self.playerRight = pygame.image.load('assets/right.png')
        self.playerLeft = pygame.image.load('assets/left.png')

    def updatePlayer(self):
        if not self.jump:
            self.playery += self.gravity
            self.gravity += 1
        elif self.jump:
            self.playery -= self.jump
            self.jump -= 1
        key = pygame.key.get_pressed()
        if key[K_RIGHT]:
            if self.xmovement < 10:
                self.xmovement += 1
            self.direction = 0
        elif key[K_LEFT]:
            if self.xmovement > -10:
                self.xmovement -= 1
            self.direction = 1
        else:
            if self.xmovement > 0:
                self.xmovement -= 1
            else:
                self.xmovement += 1
        if self.playerx > 850:
            self.playerx = -50
        elif self.playerx < -50:
            self.playerx = 850
        self.playerx += self.xmovement
        if self.playery - self.cameray <= 200:
            self.cameray -= 5
        image = object
        if self.direction == 0:
            if self.jump:
                image = self.playerRight_1
            else:
                image = self.playerRight
        else:
            if self.jump:
                image = self.playerLeft_1
            else:
                image = self.playerLeft
        self.screen.blit(image, (self.playerx, self.playery - self.cameray))

    def updatePlatforms(self):
        for p in self.platforms:
            rect = pygame.Rect(p[0], p[1], self.green.get_width(), self.green.get_height())
            player = pygame.Rect(self.playerx, self.playery, self.playerRight.get_width(),
                                 self.playerRight.get_height())
            if rect.colliderect(player) and self.gravity and self.playery < p[1]-self.cameray\
                    and p[2] != 2:
                self.jump = 15
                self.gravity = 0
            elif rect.colliderect(player) and self.gravity and self.playery < p[1]-self.cameray:
                p[3] = 1
            if p[2] == 1:
                if p[3] == 1:
                    p[0] += 5
                    if p[0] > 550:
                        p[3] = 0
                else:
                    p[0] -= 5
                    if p[0] <= 0:
                        p[3] = 1

    def drawPlatforms(self):
        for p in self.platforms:
            check = self.platforms[1][1] - self.cameray
            if check > 600:
                platform = random.randint(0, 1000)
                a = 0
                if platform < 800:
                    a = 0
                elif platform < 900:
                    a = 1
                else:
                    a = 2
                self.platforms.append([random.randint(0, 700), self.platforms[-1][1] - 50, a, 0])
                self.platforms.pop(0)
                coords = self.platforms[-1]
                check = random.randint(0, 1000)
                if check > 900 and a == 0:
                    self.springs.append([coords[0], coords[1]-25, 0])
            image = object
            if p[2] == 0:
                image = self.green
            elif p[2] == 1:
                image = self.blue
            elif p[2] == 2:
                if not p[3]:
                    image = self.red
                else:
                    image = self.red_1
            self.screen.blit(image, (p[0], p[1] - self.cameray))
        for s in self.springs:
            image = object
            if s[-1] == 1:
                image = self.spring
            else:
                image = self.spring_1
            self.screen.blit(image, (s[0], s[1] - self.cameray))
            spring1 = pygame.Rect(s[0], s[1], image.get_width(), image.get_height())
            player = pygame.Rect(self.playerx, self.playery, self.playerRight.get_width(),
                                 self.playerRight.get_height())
            if spring1.colliderect(player):
                self.jump = 50
                self.cameray -= -50

    def generatePlatforms(self):
        on = 600
        while on > -100:
            x = random.randint(0, 700)
            platform = random.randint(0, 1000)
            a = 0
            if platform < 800:
                a = 0
            elif platform < 900:
                a = 1
            else:
                a = 2
            self.platforms.append([x, on, a, 0])
            on -= 50

    def drawGrid(self):
        for x in range(80):
            pygame.draw.line(self.screen, (222, 222, 222), (x * 12, 0), (x * 12, 600))
            pygame.draw.line(self.screen, (222, 222, 222), (0, x * 12), (800, x * 12))

    def run(self):
        clock = pygame.time.Clock()
        self.generatePlatforms()
        while True:
            self.screen.fill((255, 255, 255))
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            self.drawGrid()
            self.updatePlatforms()
            self.updatePlayer()
            self.drawPlatforms()
            if self.playery > 600:
                imgRect = self.died.get_rect()
                imgRect.center = (400, 300)
                self.screen.blit(self.died, imgRect)
            pygame.display.flip()
            pygame.event.pump()


DoodleJump().run()
