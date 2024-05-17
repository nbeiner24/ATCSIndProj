#!/usr/bin/env python3
"""
mario.py
The main program for my ATCS independent project. Runs a recreation of World 1-1 of the original
Super Mario game.
"""

__author__ = "Nicolas Beiner"
__version__ = "2024-05-15"

import pygame
import sys
import math
import time
import random

# pygame setup
pygame.init()
# load and set the logo
logo = pygame.image.load("star_icon.png")    
pygame.display.set_icon(logo)
pygame.display.set_caption("Super Mario 1-1")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

class My_Sprite(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.dy = 0
        self.dx = 0
        self.width = width
        self.height = height
        self.color = (0, 0, 0)
        self.friction = 0.8

    def goto(self, x, y):
        self.x = x
        self.y = y

    def render(self):
        pygame.draw.rect(screen , self.color, pygame.Rect(int(self.x-self.width/2.0), int(self.y-self.height/2.0), self.width, self.height))

    def is_AABB_collision(self, other):
        # Axis Aligned Bounding Box Collision
        pass

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER GAME HERE

    # flip() the display to put work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()