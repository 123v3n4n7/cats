import pygame
import random
import time
import sys

max_x = 1920
max_y = 1080

max_figures = 50
figure_size = 100

class Figures():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 3)
        self.img_num = random.randint(1, 5)
        self.fileName = "smiley" + str(self.img_num) + ".png"
        self.image = pygame.image.load(self.fileName).convert_alpha()
        self.image = pygame.transform.scale(self.image, (figure_size, figure_size))

    def moving(self):
        self.y = self.y + self.speed
        if self.y > max_y:
            self.y = (0 - figure_size)

        i = random.randint(1, 3)
        if i == 1:
            self.x += 1
            if self.x > max_x:
                self.x = (0 - figure_size)
        if i == 2:
            self.x -= 1
            if self.x < (0 - figure_size):
                self.x = figure_size

    def draw_image(self):
        screen.blit(self.image, (self.x, self.y))


def falling(max_figures, figuresfall):
    for i in range(0, max_figures):
        xx = random.randint(0, max_x)
        yy = random.randint(0, max_y)
        figuresfall.append(Figures(xx, yy))


def exit_check():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()


pygame.init()
screen = pygame.display.set_mode((max_x, max_y))
bg_color = (0, 0, 0)
figuresfall = []

falling(max_figures, figuresfall)

while True:
    screen.fill(bg_color)
    exit_check()
    for i in figuresfall:
        i.moving()
        i.draw_image()
    pygame.display.flip()
