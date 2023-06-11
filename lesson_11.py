#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:39:37 2023

@author: rasuljon
"""

from turtle import Turtle,Screen

oyna = Screen()
oyna.title("Mening oynam")
chiziq = Turtle()
chiziq.color('red')
chiziq.pensize(5)
chiziq.speed(0)
chiziq.hideturtle()
chiziq.up()
chiziq.goto(250,250)
chiziq.down()
chiziq.goto(250,-250)
chiziq.goto(-250,-250)
chiziq.goto(-250,250)
chiziq.goto(250,250)
chegara = Turtle()
chegara.color('green')
chegara.pensize(5)
chegara.up()
chegara.goto(-210,-250)
chegara.down()
chegara.goto(-80,-250)
chegara.goto(-80,-220)
chegara.goto(-210,-220)
chegara.goto(-210,-250)
chegara.hideturtle()
chegara.speed()

koptok = Turtle()
koptok.shape('circle')
koptok.color("blue")
koptok.up()
koptok.goto(0,0)

step_x = 3
step_y = 2
while True :
    
    x,y =koptok.position()
    
    if x + step_x >= 250 or x + step_x <=-250:
        step_x= -step_x
    if y + step_y >= 250 or y+step_y <=-250:
        step_y = -step_y 
    if x<= -80 and y<=-220:  
    
         break  
    
        
    koptok.goto(x+step_x,y+step_y)


    
    

oyna.mainloop()

