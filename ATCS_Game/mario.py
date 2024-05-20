#!/usr/bin/env python3
"""
mario.py
The main program for my ATCS independent project. Runs a demo of a mario level that I wanted to make (what could have been ); ). I realized partway through that this task is far more complicated than I originally made it out to be, so the program is honestly far more rudimentary and inefficient than I wanted it to be, in terms of both visuals and the code itself. I think that if I had a whole month I could actually recreate a 1:1 replica of the first level of the original Super Mario. I also was pretty busy during the week and weekend with AP's, prom, and my weekend job, but I still appreciate what I could do for the program :).
"""

__author__ = "Nicolas Beiner"
__version__ = "2024-05-15"

import pygame
import math

# pygame setup
pygame.init()
# load and set the logo
logo = pygame.image.load("ATCS_Game\star_icon.png")
bg = pygame.image.load(r"ATCS_Game\background.png")    
pygame.display.set_icon(logo)
pygame.display.set_caption("Super Mario Demo")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
GRAVITY = 0.5
MAX_SPEED = 12
MAX_SPEED_Y = MAX_SPEED + 5

# My own rudimentary sprite class
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

    # teleports the sprite to a given coordinate
    def goto(self, x, y):
        self.x = x
        self.y = y

    # renders the sprite onto the screen
    def render(self):
        pygame.draw.rect(screen , self.color, pygame.Rect(int(self.x-self.width/2.0), int(self.y-self.height/2.0), self.width, self.height))

    # Fundamental collision method that is used throughout the program
    def is_AABB_collision(self, other):
        # Axis Aligned Bounding Box Collision
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)

# class for the player's sprite
class Player(My_Sprite):
    def __init__(self, x, y, width, height):
        My_Sprite.__init__(self, x, y, width, height)
        self.mushroom_status = 0
        if self.mushroom_status == 0:
            self.mario = pygame.image.load("ATCS_Game\small_mario.gif")
        elif self.mushroom_status == 1:
            self.mario = pygame.image.load(r"ATCS_Game\big_mario.gif")
        self.image = pygame.transform.scale(self.mario, (int(self.mario.get_width()*0.2), int(self.mario.get_height()*0.2)))
        self.direction = 1
        self.flip = False
        
    # changes position values of the sprite based on dy, dx, and whatever influences them
    def move(self):
        if self.dy > MAX_SPEED_Y:
            self.dy = MAX_SPEED_Y
        if self.dx > MAX_SPEED:
            self.dx = MAX_SPEED
        if self.dx < -1*MAX_SPEED:
            self.dx = -1*MAX_SPEED
        self.x += self.dx
        self.y += self.dy
        self.dy += GRAVITY

    def jump(self):
        self.dy -= 15

    def left(self):
        self.dx -= 1
        self.flip = True
        self.direction = -1

    def right(self):
        self.dx += 1
        self.flip = False
        self.direction = 1

    def render(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.x - int(self.mario.get_width()*0.2)/2, self.y - int(self.mario.get_height()*0.2)/2))

# class for the goomba
class Enemy(My_Sprite):
    def __init__(self, x, y, width, height):
        My_Sprite.__init__(self, x, y, width, height)
        self.goomba = pygame.image.load("ATCS_Game\goomba.png")
        self.image = pygame.transform.scale(self.goomba, (int(self.goomba.get_width()*0.025), int(self.goomba.get_height()*0.025)))
        self.dx = 2
        self.dead = False

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += GRAVITY

    def render(self):
        # i only rendered the goomba when it was alive (before the player stomps on it)
        if self.dead == False:
            screen.blit(self.image, (self.x - int(self.goomba.get_width()*0.025)/2, self.y - int(self.goomba.get_height()*0.025)/2))
        else:
            pass

# class for the question mark block
class Block(My_Sprite):
    def __init__(self, x, y, width, height):
        My_Sprite.__init__(self, x, y, width, height)
        self.block = pygame.image.load("ATCS_Game\q_block.png")
        self.image = pygame.transform.scale(self.block, (int(self.block.get_width()*0.1), int(self.block.get_height()*0.1)))
        self.used = False
    
    def render(self):
        screen.blit(self.image, (self.x - int(self.block.get_width()*0.1)/2, self.y - int(self.block.get_height()*0.1)/2))

class Mushroom(Enemy):
    def __init__(self, x, y, width, height):
        Enemy.__init__(self, x, y, width, height)
        self.mushroom = pygame.image.load("ATCS_Game\mushroom.png")
        self.image = pygame.transform.scale(self.mushroom, (int(self.mushroom.get_width()*0.2), int(self.mushroom.get_height()*0.2)))
        self.dx = 0
        self.spawned = False

    def render(self):
        # I wanted the mushroom to only render before being used and after hitting the ?-block
        if self.spawned == True:
            screen.blit(self.image, (self.x - int(self.mushroom.get_width()*0.2)/2, self.y - int(self.mushroom.get_height()*0.2)/2))
        else:
            pass

# creating all the objects to be used in the main game loop
# very inefficient, but didn't have much time to work on the project this week or weekend :(
player = Player(600, 0, pygame.image.load("ATCS_Game\small_mario.gif").get_width()*0.2, pygame.image.load("ATCS_Game\small_mario.gif").get_height()*0.2)
goomba = Enemy(400, 500, pygame.image.load("ATCS_Game\goomba.png").get_width()*0.025, pygame.image.load("ATCS_Game\goomba.png").get_height()*0.025)
q = Block(700, 75, pygame.image.load("ATCS_Game\q_block.png").get_width()*0.1, pygame.image.load("ATCS_Game\q_block.png").get_height()*0.1)
m = Mushroom(700, 50, pygame.image.load("ATCS_Game\mushroom.png").get_width()*0.2, pygame.image.load("ATCS_Game\mushroom.png").get_height()*0.2)
blocks = []
blocks.append(My_Sprite(600, 200, 400, 20))
blocks.append(My_Sprite(600, 400, 600, 20))
blocks.append(My_Sprite(600, 600, 1000, 20))
blocks.append(My_Sprite(1000, 500, 100, 200))
blocks.append(My_Sprite(200, 500, 100, 200))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keyboard events, with names for each key
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.left()
        elif event.key == pygame.K_RIGHT:
            player.right()
        elif event.key == pygame.K_UP:
            for block in blocks:
                # makes it so you can only jump when standing on a platform
                if player.is_AABB_collision(block):
                    player.jump()
                    break

    #player movement and collision
    player.move()
    if player.is_AABB_collision(goomba) and goomba.dead == False:
        # player is to the left
        if player.x < goomba.x - goomba.width/2.0 and player.dx > 0:
            player.dx = 0
            player.x = goomba.x - goomba.width/2.0 - player.width/2.0
            # resets the player to the beginning if they hit the goomba from the side
            player.goto(600, 0)
        # player is to the right
        elif player.x > goomba.x + goomba.width/2.0 and player.dx < 0:
            player.dx = 0
            player.x = goomba.x + goomba.width/2.0 + player.width/2.0
            player.goto(600, 0)
        # player is above
        elif player.y < goomba.y:
            player.dy = 0
            player.y = goomba.y - goomba.height/2.0 - player.height/2.0 + 1
            goomba.dead = True
            # kills the goomba if the player hits it from above

    # for this part, I tried to make it so tht if the player hit a mushroom, their sprite would change
    # to the bigger mario, but I couldn't figure out how to get the images to change since
    # once a player object is created, the image that is rendered cant be edited (at least i dont think it can)
    if player.is_AABB_collision(m) and m.spawned == True:
        # player is to the left
        if player.x < m.x - m.width/2.0 and player.dx > 0:
            player.mushroom_status = 1
            m.spawned = False
        # player is to the right
        elif player.x > m.x + m.width/2.0 and player.dx < 0:
            player.mushroom_status = 1
            m.spawned = False
        # player is above
        elif player.y < m.y:
            player.mushroom_status = 1
            m.spawned = False

    if player.is_AABB_collision(q):
        # player is to the left
        if player.x < q.x - q.width/2.0 and player.dx > 0:
            player.dx = 0
            player.x = q.x - q.width/2.0 - player.width/2.0
        # player is to the right
        elif player.x > q.x + q.width/2.0 and player.dx < 0:
            player.dx = 0
            player.x = q.x + q.width/2.0 + player.width/2.0
        # player is above a platform
        elif player.y < q.y:
            player.dy = 0
            player.y = q.y - q.height/2.0 - player.height/2.0 + 1
            player.dx *= q.friction
        # player is below a platform
        elif player.y > q.y:
            player.dy = 0
            player.y = q.y + q.height/2.0 + player.height/2.0
            if q.used == False:
                #if the player hits the ?-block from underneath, it spawns the mushroom and goes inactive
                m.spawned = True
                m.dx = 1
                q.used = True

    #basic collision
    for block in blocks:
        if player.is_AABB_collision(block):
            # player is to the left
            if player.x < block.x - block.width/2.0 and player.dx > 0:
                player.dx = 0
                player.x = block.x - block.width/2.0 - player.width/2.0
            # player is to the right
            elif player.x > block.x + block.width/2.0 and player.dx < 0:
                player.dx = 0
                player.x = block.x + block.width/2.0 + player.width/2.0
            # player is above a platform
            elif player.y < block.y:
                player.dy = 0
                player.y = block.y - block.height/2.0 - player.height/2.0 + 1
                player.dx *= block.friction
            # player is below a platform
            elif player.y > block.y:
                player.dy = 0
                player.y = block.y + block.height/2.0 + player.height/2.0

    # mushromom movement and collision
    m.move()
    for block in blocks:
        if m.is_AABB_collision(block):
            # player is to the left
            if m.x < block.x - block.width/2.0 and m.dx > 0:
                m.dx *= -1
                m.x = block.x - block.width/2.0 - m.width/2.0
            # m is to the right
            elif m.x > block.x + block.width/2.0 and m.dx < 0:
                m.dx *= -1
                m.x = block.x + block.width/2.0 + m.width/2.0
            # m is above a platform
            elif m.y < block.y:
                m.dy = 0
                m.y = block.y - block.height/2.0 - m.height/2.0 + 1
            # m is below a platform
            elif m.y > block.y:
                m.dy = 0
                m.y = block.y + block.height/2.0 + m.height/2.0
    if m.is_AABB_collision(q):
        # m is to the left
        if m.x < q.x - q.width/2.0 and m.dx > 0:
            m.dx = 0
            m.x = q.x - q.width/2.0 - m.width/2.0
        # m is to the right
        elif m.x > q.x + q.width/2.0 and m.dx < 0:
            m.dx = 0
            m.x = q.x + q.width/2.0 + m.width/2.0
        # m is above a platform
        elif m.y < q.y:
            m.dy = 0
            m.y = q.y - q.height/2.0 - m.height/2.0 + 1
        # m is below a platform
        elif m.y > q.y:
            m.dy = 0
            m.y = q.y + q.height/2.0 + m.height/2.0

    # enemy movement and collision
    goomba.move()
    for block in blocks:
        if goomba.is_AABB_collision(block):
            # player is to the left
            if goomba.x < block.x - block.width/2.0 and goomba.dx > 0:
                goomba.dx *= -1
                goomba.x = block.x - block.width/2.0 - goomba.width/2.0
            # goomba is to the right
            elif goomba.x > block.x + block.width/2.0 and goomba.dx < 0:
                goomba.dx *= -1
                goomba.x = block.x + block.width/2.0 + goomba.width/2.0
            # goomba is above a platform
            elif goomba.y < block.y:
                goomba.dy = 0
                goomba.y = block.y - block.height/2.0 - goomba.height/2.0 + 1
            # goomba is below a platform
            elif goomba.y > block.y:
                goomba.dy = 0
                goomba.y = block.y + block.height/2.0 + goomba.height/2.0
            
    # resets the players position if they go below the boundaries of the map
    if player.y > 720:
        player.goto(600, 0)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    screen.blit(bg, bg.get_rect())

    # RENDER GAME HERE
    player.render()
    goomba.render()
    q.render()
    m.render()
    for block in blocks:
        block.render()

    # flip() the display to put work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()