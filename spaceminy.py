#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 11:45:01 2018

@author: nov35102
"""

import pyglet
import random
from math import sin, cos, radians, pi
from pyglet.window.key import DOWN, UP, LEFT, RIGHT




window = pyglet.window.Window(1000, 900)
batch = pyglet.graphics.Batch()   
image = pyglet.image.load("space.png")


        
class Stone(object):

    def __init__(self,x=None, y=None,direction=None,speed=None, rspeed=None):
       
        
        num = random.choice(range(0, 10))
        self.image = pyglet.image.load('meteor3.png'.format(num))

        
        # sprite
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)

   
        self.x = x if x is not None else random.randint(400, window.width)
        self.y = y if y is not None else random.randint(400, window.height)
  
    
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.direction = direction if direction is not None else random.randint(0, 400)
        # rychlost pohybu
        self.speed = speed if speed is not None else random.randint(30, 100)
        
        
        # rychlost otáčení
        
        self.rspeed = rspeed if rspeed is not None else random.randint(-2, 10)

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
            self.direction = random.randint(15, 40)
            return
        if self.y + rozmer >= window.height:
            self.direction = random.randint(100, 300)
            return
        if self.y - rozmer <= 0:
            self.direction = random.randint(-100, 100)
            return
    


class Lodka(object):
    
    def __init__(self):
        #lod
        self.obrazek = pyglet.image.load("rocket-512.png")
        
        #střed otáčení
        self.obrazek.anchor_x = self.obrazek.width // 4
        self.obrazek.anchor_y = self.obrazek.height // 4
        
    
        self.sprite =pyglet.sprite.Sprite(self.obrazek, batch=batch)
        
        self.sprite.rotation=50
        self.speed= 250
        self.x=300
        self.y=250
        self.sprite.x = self.x
        self.sprite.y = self.y
        
        
    def tiktak(self,t):
        global klavesy
        self.okraj()
        
        
        #ovládání 
        for data in klavesy:
            if data == LEFT:
                self.sprite.rotation -= 5
                
            if data == RIGHT:
                self.sprite.rotation += 5
                
            if data == UP:
                self.x = self.sprite.x + self.speed*t*sin(pi*self.sprite.rotation/180)
                self.sprite.x=self.x
                self.y = self.sprite.y + self.speed*t*cos(pi*self.sprite.rotation/180)
                self.sprite.y=self.y
                
            if data == DOWN:
                self.x = self.sprite.x + self.speed*t*-sin(pi*self.sprite.rotation/180)
                self.sprite.x = self.x
                self.y = self.sprite.y + self.speed*t*-cos(pi*self.sprite.rotation/180)
                self.sprite.y = self.y
                
                
                
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






klavesy=set()        
for o in range(1):
    lod=Lodka()
    pyglet.clock.schedule_interval(lod.tiktak, 1/ 50 )

for x in range(15):
    stone=Stone()
    pyglet.clock.schedule_interval(stone.tick, 1/ 50 )





@window.event
def on_key_press(data, mod):
    global klavesy
    klavesy.add(data)
    



@window.event
def on_key_release(data, mod):
    global klavesy
    klavesy.remove(data)




@window.event
def on_draw():
    window.clear()
    image.blit(0,0)
    batch.draw()
    
    


pyglet.app.run()
