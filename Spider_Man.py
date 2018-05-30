#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Spider Man module '

__author__ = 'Kevin Ma'

import turtle
import time
import math
import os 

t=turtle.Turtle() #定义画笔实例

turtle.screensize(800,800,'white')



t.fillcolor("red")
t.pensize(3)
t.speed(10)

t.begin_fill()

def go_to(x,y):
	t.up()
	t.goto(x,y)
	t.down()

def draw_face():
	go_to(0,-150)

	a=10
	for i in range(120):
	    if 0<=i<30 or 60<=i<90:
	        a=a+0.2
	        t.lt(3) #向左转3度
	        t.fd(a) #向前走a的步长
	    else:
	        a=a-0.2
	        t.lt(3)
	        t.fd(a)

	t.end_fill()

def draw_eyes():

	t.fillcolor("LightYellow1")
	t.pensize(15)
	t.speed(10)

	t.begin_fill()
	go_to(-120,250)
	t.right(120)
	t.circle(100,100)
	t.goto(-120,250)
	t.end_fill()

	t.begin_fill()
	go_to(60,100)
	t.left(40)
	t.circle(100,100)
	t.goto(60,100)
	t.end_fill()
	time.sleep(3)




def write_zh():

	#设置窗口
	turtle.screensize(800,800,'#363636')

	#设置画笔
	t.speed(10)
	t.pensize(3)
	t.pencolor('black')

	t.write("你好，我是小蜘蛛",move = True,align="center",font=("Arial",50,"normal"))
	time.sleep(5)
	t.clear()

	t.write("我不想死...\n\n\nbut I am an Avenger.",move = True,align="right",font=("Arial",50,"normal"))
	time.sleep(5)

def main():
	#设置窗口
	turtle.screensize(800,800,'white')

	#设置画笔
	t.speed(5)
	t.pensize(6)
	t.pencolor('black')

	draw_face()
	draw_eyes()
	t.reset()
	write_zh()
	t.reset()


if __name__ == '__main__':
	main()
