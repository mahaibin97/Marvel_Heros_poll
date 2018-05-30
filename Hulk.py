#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Thor module '

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

def draw_s():
	#设置画笔
	t.speed(3)
	t.pensize(8)
	t.pencolor('#1C1C1C')

	t.fillcolor("#228B22")
	t.begin_fill()
	t.right(30)
	for i in range(4):
		t.left(60)
		t.forward(40)
		t.right(60)
		t.forward(40)
	t.right(60)
	t.forward(200)

	for i in range(4):
		t.right(60)
		t.forward(40)
		t.right(60)
		t.forward(40)
		t.right(60)
		t.forward(150)
		t.backward(150)
		t.right(180)

	t.right(180)
	t.forward(200)
	t.end_fill()

def draw_f():

	go_to(242,-220)
	t.left(120)
	t.forward(30)
	t.right(30)
	t.forward(140)
	t.right(90)
	t.forward(30)


def write_zh():
	#设置窗口
	turtle.screensize(800,800,'DarkGreen')

	#设置画笔
	t.speed(10)
	t.pensize(3)
	t.pencolor('white')
	t.write("你好，我是浩克",move = True,align="center",font=("Arial",30,"normal"))


def main():
	#设置窗口
	turtle.screensize(800,800,'DarkGreen')

	draw_s()
	draw_f()
	time.sleep(5)
	t.clear()
	go_to(0,0)
	write_zh()
	time.sleep(5)
	t.reset()

if __name__ == '__main__':
	main()

