#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Iron_man module '

__author__ = 'Kevin Ma'

import turtle
import time
import math
import os 

t = turtle.Turtle()




def go_to(x,y):
	t.up()
	t.goto(x,y)
	t.down()


def draw_sjx():

	#设置画笔
	t.speed(10)
	t.pensize(10)
	t.pencolor('Brown')

	go_to(-200,5*1.732)
	t.fillcolor("#CD7F32")
	t.begin_fill()
	for i in range(3):
		t.forward(400)
		t.right(120)
	t.end_fill()

	n = 200 / 1.732
	t.right(30)
	t.forward(n)
	t.left(30)
	t.forward(200)

	t.left(30)
	t.forward(n)
	t.backward(n)
	t.right(150)
	t.forward(200)

	t.left(30)
	t.forward(n)
	t.backward(n)
	t.right(150)
	t.forward(200)

	t.right(120)

def draw_line():
	s1 = 400/3  #三角形边上前进的距离
	s2 = 400/1.732 - 400/3	#外接圆的半径上前进的距离

	t.forward(s1)
	t.left(120)
	t.forward(s2)
	t.backward(s2)
	t.right(120)
	t.forward(s1)
	t.left(60)
	t.forward(s2)
	t.backward(s2)
	t.right(60)
	t.forward(s1)


def draw_round():

	#设置画笔
	t.speed(10)
	t.pensize(20)
	t.pencolor('Brown')
	go_to(-200,5*1.732)
	t.fillcolor("#CD7F32")

	t.begin_fill()
	t.forward(400)
	t.left(120)
	t.circle(400/1.732,120)
	t.end_fill()
	
	t.begin_fill()
	t.circle(400/1.732,120)
	t.left(120)
	t.forward(400)
	t.end_fill()
	t.backward(400)

	t.begin_fill()
	t.right(120)
	t.circle(400/1.732,120)
	t.left(120)
	t.end_fill()
	t.forward(400)
	t.backward(400)

	draw_line()
	t.right(120)
	draw_line()
	t.right(120)
	draw_line()

def write_zh():

	#设置窗口
	turtle.screensize(800,800,'#8B0000')

	#设置画笔
	t.speed(10)
	t.pensize(3)
	t.pencolor('#CD7F32')

	t.write("你好，我是IRON MAN\n\n我就是计划!",move = True,align="center",font=("Arial",50,"normal"))
	t.up()


def main():

	#设置窗口
	turtle.screensize(800,800,'#8B0000')
	
	draw_sjx()
	draw_round()
	time.sleep(3)
	t.clear()
	go_to(0,0)
	write_zh()
	time.sleep(5)
	t.reset()

if __name__ == "__main__":

	main()


