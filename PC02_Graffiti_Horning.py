#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:30:21 2020

@author: Clayton
"""

from turtle import *

panel = Screen()
w = 750 
h = 750 
panel.setup(width=w, height=h) 

image = ("Bezos.gif")
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

up()
goto(125, -93)
right(10)
down()
color("red")
pensize(8)
forward(200)
up()

goto(30,48)
down()
color("white")
pensize(15)
right(70)
forward(20)

up()
goto(10, 45)
down()
forward(20)
up()

goto(-80, 200)
left(115)
pensize(10)
color("black")
down()
forward(20)
up()

left(90)
forward(10)
right(90)
down()
pensize(30)
forward(10)
up()

right(90)
forward(10)
pensize(10)
down()
left(90)
forward(20)
up()

goto(-12,100)
down()
fillcolor("teal")
color("teal")
begin_fill()
circle(15)
end_fill()
