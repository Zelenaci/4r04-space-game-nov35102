#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 11:45:01 2018

@author: nov35102
"""

import pyglet
import random
from math import sin, cos, radians, pi



window = pyglet.window.Window(1000, 1000)
batch = pyglet.graphics.Batch()   
image = pyglet.image.load("space.png")


        
class Stone(object):

    def __init__(self,x=None, y=None,direction=None,speed=None, rspeed=None):
       
        
        num = random.choice(range(0, 5))
        self.image = pyglet.image.load('meteor3.png'.format(num))

        
        # sprite
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)

   
        self.x = x if x is not None else random.randint(400, window.width)
        self.y = y if y is not None else random.randint(400, window.height)
  
    
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.direction = direction if direction is not None else random.randint(0, 40)
        
        
        # rychlost pohybu
        self.speed = speed if speed is not None else random.randint(30, 50)
        
        
        # rychlost otáčení
        
        self.rspeed = rspeed if rspeed is not None else random.randint(0, 0)

    def tick(self, dt):
        self.bounce()
        
        self.x += dt * self.speed * cos(pi / 2 - radians(self.direction))
        self.sprite.x = self.x
        self.y += dt * self.speed * sin(pi / 2 - radians(self.direction))
        self.sprite.y = self.y
        self.sprite.rotation +=self.rspeed
        
        
   
         # kraj a stred
    def bounce(self):
        
        rozmer = min(self.image.width, self.image.height)/2

        if self.x + rozmer >= window.width:
            self.direction = random.randint(150, 300)
            return
        if self.x - rozmer <= 0:
            self.direction = random.randint(150, 40)
            return
        if self.y + rozmer >= window.height:
            self.direction = random.randint(100, 250)
            return
        if self.y - rozmer <= 0:
            self.direction = random.randint(-100, 100)
            return
    




                
                
           # okraj stred
    def okraj(self):
        
    
        rozmer = min(self.obrazek.width, self.obrazek.height)/2
        if self.x + rozmer >= window.width+40:
            self.sprite.x=-30
        if self.x - rozmer < -40:
            self.sprite.x=window.width+30
        if self.y + rozmer >= window.height + 40:
            self.sprite.y=-30
        if self.y - rozmer < -40:
            self.sprite.y=window.height+30  





for x in range(15):
    stone=Stone()
    pyglet.clock.schedule_interval(stone.tick, 1/ 50 )











@window.event
def on_draw():
    window.clear()
    image.blit(0,0)
    batch.draw()
    
    


pyglet.app.run()
