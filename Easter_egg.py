#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author : ma haibin
# Github : https://github.com/mahaibin97
# Date   : 2018-05-26
# Version: V1.0.0


import sys
import os
import re
import turtle
import time



def openFile():

	with open("/Users/mahaibin/python/marvel/marvel_10_years.txt",'r') as file:
		for line in file:
			print(line)
			write_zh(line)
			time.sleep(2)
			turtle.reset()

	solgn = "致敬漫威！"
	write_zh2(solgn)
	time.sleep(5)

def write_zh(line):
	#设置窗口
	turtle.screensize(800,800,'black')

	turtle.hideturtle()
	#设置画笔
	turtle.speed(10)
	turtle.pensize(3)
	turtle.pencolor('white')
	turtle.write(line,move = True,align="left",font=("Arial",30,"normal"))

def write_zh2(line):
	#设置窗口
	turtle.screensize(800,800,'black')

	turtle.hideturtle()
	#设置画笔
	turtle.speed(10)
	turtle.pensize(4)
	turtle.pencolor('orange')
	turtle.write(line,move = True,align="left",font=("Arial",90,"normal"))

def caidan():
	string1 = "最后，送你一个真正的python彩蛋！！！"
	string2 = "请确保你的电脑已经连接到Internet！"
	string3 = "3"
	string4 = "2"
	string5 = "1"

	write_zh(string1)
	time.sleep(3)
	turtle.reset()

	write_zh(string2)
	time.sleep(3)
	turtle.reset()

	write_zh2(string3)
	time.sleep(1)
	turtle.reset()

	write_zh2(string4)
	time.sleep(1)
	turtle.reset()

	write_zh2(string5)
	time.sleep(1)
	turtle.reset()

	import antigravity

def main():

	print("你要打开彩蛋吗(Y(y) or N(n))?\n")

	s = input()
	if s == "Y" or s == "y":
		print("\n\n##### MARVEL 10年所有电影 #####\n\n")
		openFile()
	elif s == "N" or s == "n":
		print("Over...")
	else:
		print("Error!")


	time.sleep(3)
	turtle.reset()

	caidan()

	time.sleep(10)
	thanks = "感谢您的体验！"
	write_zh2(thanks)
	time.sleep(10)
	print("\n\n\n感谢您的体验！\n\n")

if __name__ == '__main__':
	main()

