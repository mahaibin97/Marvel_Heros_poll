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


def draw_ct():


	go_to(-150,200)
	t.fillcolor("white")
	t.begin_fill()
	for i in range(2):
		t.forward(300)
		t.right(90)
		t.forward(200)
		t.right(90)
	t.end_fill() 

	for i in range(2):
		t.begin_fill()
		t.left(60)
		t.forward(20)
		t.right(60)
		t.forward(280)
		t.right(60)
		t.forward(20)
		t.end_fill()

		t.begin_fill()
		t.left(30)
		t.forward(40)
		t.right(60)
		t.forward(160)
		t.right(60)
		t.forward(40)
		t.right(30)
		t.end_fill()

	#绘制四个角的三角形
	t.begin_fill()
	t.right(150)
	t.forward(40)
	t.right(120)
	t.goto(-140,217)
	t.end_fill()

	go_to(140,217)
	t.begin_fill()
	t.goto(184,180)
	t.goto(150,200)
	t.end_fill()

	go_to(150,0)
	t.begin_fill()
	t.goto(140,-17)
	t.goto(184,20)
	t.goto(150,0)
	t.end_fill()

	go_to(-150,0)
	t.begin_fill()
	t.goto(-140,-17)
	t.goto(-184,20)
	t.goto(-150,0)
	t.end_fill()

def draw_cb():
	
	t.fillcolor("white")
	go_to(-30,230)
	t.begin_fill()
	t.goto(30,230)
	t.goto(30,220)
	t.goto(-30,220)
	t.goto(-30,230)
	t.end_fill()

	go_to(-20,-14)
	t.fillcolor("#8B4500")
	t.begin_fill()
	t.goto(20,-14)
	t.goto(20,-214)
	t.goto(-20,-214)
	t.goto(-20,-14)
	t.end_fill()

	go_to(-20,-54)
	t.goto(20,-14)

	go_to(-20,-94)
	t.goto(20,-54)

	go_to(-20,-134)
	t.goto(20,-94)

	go_to(-20,-174)
	t.goto(20,-134)

	go_to(-20,-214)
	t.goto(20,-174)


def draw_cz():
	#设置画笔
	t.speed(10)
	t.pensize(6)
	t.pencolor('black')

	draw_ct()
	draw_cb()

def write_zh():

	#设置窗口
	turtle.screensize(800,800,'#363636')

	#设置画笔
	t.speed(10)
	t.pensize(3)
	t.pencolor('#CD7F32')

	t.write("I'm 雷神，Thor.\n再也没有什么可以失去了",move = True,align="center",font=("Arial",50,"normal"))
	t.up()


def main():

	#设置窗口
	turtle.screensize(800,800,'#363636')

	draw_cz()
	time.sleep(5)
	t.clear()
	go_to(0,0)
	write_zh()
	time.sleep(5)
	t.reset()


if __name__ == '__main__':
	main()
