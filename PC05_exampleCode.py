#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:00:12 2020

@author: Dr. Z

A generative art piece that uses 5 turtles to make random walk patterns in 
different colors. One turtle draws a wiggly spiral in the middle of the 
screen. 
"""
from turtle import *
import math, random

# create palette
COLORS = ['aquamarine','pink','white','orange','yellow']

# create screen, and set size
panel = Screen()
w = 500
h = 500
panel.setup(width=w,height=h)
tracer(0) # turn off the animation or it will take forEVER

# set background color
panel.bgcolor('purple')

# define variables for turtle movement
step = 2  # amount of straightness in paths


# create turtles
turtle1 = Turtle(visible=False)
turtle2 = Turtle(visible=False)
turtle3 = Turtle(visible=False)
turtle4 = Turtle(visible=False)
spiral = Turtle(visible=False)
# assign colors
turtle1.color(COLORS[0])
turtle2.color(COLORS[1])
turtle3.color(COLORS[2])
turtle4.color(COLORS[3])
spiral.color(COLORS[4])#random.choice(COLORS))
thicc = 20  # pen width
turtle1.penup()
turtle1.width(20)
turtle2.penup()
turtle2.width(20)
turtle3.penup()
turtle3.width(20)
turtle4.penup()
turtle4.width(20)
spiral.penup()
spiral.width(20)
rot = 90  # amount of bend in paths
# place randomly around edge screen
X = random.randint(w/2-100,w/2)
Y = random.randint(w/2-100,w/2)
turtle1.goto(X,Y)
turtle1.seth(turtle1.towards(0,0))
# place randomly around edge screen
X = random.randint(-w/2,-w/2+100)
Y = random.randint(-w/2,-w/2+100)
turtle2.goto(X,Y)
turtle2.seth(turtle1.towards(spiral))
# place randomly around edge screen
X = random.randint(w/2-100,w/2)
Y = random.randint(w/2-100,w/2)
turtle3.goto(X,Y)
turtle3.seth(turtle1.towards(0,0))
# place randomly around edge screen
X = random.randint(-w/2,-w/2+100)
Y = random.randint(-w/2,-w/2+100)
turtle4.goto(X,Y)
turtle4.seth(turtle1.towards(0,0))

# set down pens
turtle1.pendown()
turtle2.pendown()
turtle3.pendown()
turtle4.pendown()
spiral.pendown()

# walk forward (iterate 10000 times or use a while loop) with random turns
for i in range(2):
    spiral = Turtle()
    forward(step) # move each turtle forward
    turtle1.left(random.randint(-rot,rot))
    turtle2.forward(step)
    turtle2.left(random.randint(-rot,rot))
    turtle3.forward(step)
    turtle3.left(random.randint(-rot,rot))
        turtle4.forward(step)
        turtle4.left(random.randint(-rot,rot))
    spiral.left(random.randint(-rot,rot))
    # TODO: spin in circles??
    spiral.forward(random.randint(-step*2,step*2))
    spiral.left(rot)


done()