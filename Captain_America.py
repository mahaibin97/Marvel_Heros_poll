#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Captain_America module '

__author__ = 'Kevin Ma'

import turtle
import time
import math
import os 

t = turtle.Turtle()

#设置窗口



def go_to(x,y):
	t.up()
	t.goto(x,y)
	t.down()

def draw_star():
	go_to(-165,55)
	t.fillcolor('white')
	t.begin_fill()
	r = 130

	for i in range(5):
		t.forward(r)
		t.left(72)
		t.forward(r)
		t.right(144)

	t.end_fill()


def draw_round1(r,color):
	
	go_to(0,-400)
	t.fillcolor(color)
	t.begin_fill()
	t.circle(r)
	t.end_fill()
	t.up()

def draw_round2(r,color):
	
	go_to(0,-340)
	t.fillcolor(color)
	t.begin_fill()
	t.circle(r)
	t.end_fill()
	t.up()

def draw_round3(r,color):
	
	go_to(0,-280)
	t.fillcolor(color)
	t.begin_fill()
	t.circle(r)
	t.end_fill()
	t.up()

def draw_round4(r,color):
	
	go_to(0,-180)
	t.fillcolor(color)
	t.begin_fill()
	t.circle(r)
	t.end_fill()
	t.up()

def write_zh():
	#设置窗口
	turtle.screensize(800,800,'black')

	#设置画笔
	t.speed(10)
	t.pensize(3)
	t.pencolor('white')
	t.write("下午好，我是Captain\n\n我可以一直打下去!",move = True,align="center",font=("Arial",30,"normal"))

def main():

	count = []

	turtle.screensize(900,900,'white')

	#设置画笔
	t.speed(10)
	t.pensize(3)
	t.pencolor('black')


	draw_round1(400,'#8B0000')
	draw_round2(340,'#F0FFF0')
	draw_round3(280,'#8B0000')
	draw_round4(180,'#0000CD')
	draw_star()
	time.sleep(3)
	t.clear()
	go_to(0,0)
	write_zh()

	count.append(1)

	t.hideturtle()
	time.sleep(5)
	t.reset()

	return count.append(1)


if __name__ == "__main__":
	main()

