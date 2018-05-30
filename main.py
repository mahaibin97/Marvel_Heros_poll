#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author : ma haibin
# Github : https://github.com/mahaibin97
# e-mail : mahaibin20@163.com
# Date   : 2018-05-26
# Version: V1.1.0


import turtle
import time
import sys
import os
import Captain_America as Captain_America
import Iron_Man as Iron_Man
import Spider_Man as Spider_Man
import Thor as Thor
import Hulk as Hulk
import test as test
import Easter_egg as Easter_egg

sys.path.append("~/Captain_America.py")
sys.path.append("~/Iron_Man.py")
sys.path.append("~/Spider_Man.py")
sys.path.append("~/Thor.py")
sys.path.append("~/Hulk.py")
sys.path.append("~/test.py")
sys.path.append("~/Easter_egg.py")


t = turtle.Turtle()

def window():
	print(
		"""

			#####################################################

				请浏览以下漫威英雄，选出你最喜欢的英雄。
				（你的选择，将会影响到最终的投票结果)

					1. 美国队长 Captain America

					2. 钢铁侠 Iron Man

					3. 蜘蛛侠 Spider Man

					4. 雷神 Thor

					5. 绿巨人 Hulk


					最后送你一个彩蛋！！！

			#####################################################

	""")


def select_hero(hero_number):


	if hero_number == 1:
		Captain_America.main()
		print("\n我选择支持队长！\n")

	elif hero_number == 2:
		Iron_Man.main()
		print("\n钢钢...\n")

	elif hero_number == 3:
		Spider_Man.main()
		print("\n最爱的小蜘蛛...\n")

	elif hero_number == 4:
		Thor.main()
		print("\n雷神锤...\n")

	elif hero_number == 5:
		Hulk.main()
		print("\n浩克!!!浩克!!!\n")

	else:
		print("请检查你的输入！\n")

def hero_count():
	pass


def main():
	
	hero_name = ["Captain America","Iron Man","Spider Man","Thor","Hulk"]
	hero_count = [0,0,0,0,0]
	
	#显示界面菜单
	window()

	#选择人物
	for i in range(3):
		print("请把您的第{}票投给以上最喜欢的英雄(共有3票)：(1-5)\n".format(i+1))
		hero_number = input("hero_number=")
		hero_number = int(hero_number)
		if hero_number < 5:
			hero_count[hero_number-1] += 1
		select_hero(hero_number)
		t.reset()
		#print(hero_count)

	#输出
	hero_dict = dict(zip(hero_name,hero_count))
	#print(hero_dict)

	print("#####################################################\n")
	print("		排行榜									")

	for key,value in hero_dict.items():
		print("\n		恭喜{}获得{}票".format(key,value))

	print("\n#####################################################")

	No1 = max(hero_dict,key=hero_dict.get)
	print("\n最后赢家是{},恭喜！\n\n".format(No1))
	#test.main()

	#彩蛋
	Easter_egg.main()


if __name__ == "__main__":
	main()

	