"""
穷举法计算20步以内的解法，计算量太大，不可行
"""
from cube import Cube
from copy import deepcopy

steps = [('white', 'r'), ('white', 'l'), ('yellow', 'r'), ('yellow', 'l'), ('red', 'r'), ('red', 'l'),
		 ('orange', 'r'), ('orange', 'l'), ('green', 'r'), ('green', 'l'), ('blue', 'r'), ('blue', 'l')]


def judge_finished(my_cube):
	side_colors = ["white", "red", "blue", "green", "orange", "yellow"]
	for color in side_colors:
		a = my_cube.sides[color].content[0][0]
		b = my_cube.sides[color].content[0][1]
		c = my_cube.sides[color].content[0][2]
		d = my_cube.sides[color].content[1][0]
		e = my_cube.sides[color].content[1][1]
		f = my_cube.sides[color].content[1][2]
		g = my_cube.sides[color].content[2][0]
		h = my_cube.sides[color].content[2][1]
		i = my_cube.sides[color].content[2][2]
		if a == b == c == d == e == f == g == h == i:
			continue
		else:
			return False
	return True


def jinzhi12(list: list):
	# list.reverse()
	if list[-1] == 11:
		list1 = list[:-1]
		list = jinzhi12(list1)
		list.append(0)
		return list
	else:
		list[-1] = list[-1] + 1
	# list.reverse()
	return list


def restor2():
	a = []
	for i in range(20):
		a.append(deepcopy(0))
	my_cube = Cube()
	my_cube.upset()
	my_cube_bak = deepcopy(my_cube)
	while True:
		if judge_finished(my_cube):
			print(my_cube_bak)
			print(a)
			break
		my_cube = deepcopy(my_cube_bak)
		a = jinzhi12(a)
		print(a)
		rotation(my_cube, a)


def rotation(my_cube, a: list):
	for st in a:
		color = steps[st][0]
		direction = steps[st][1]
		my_cube.rotation(my_cube.sides[color], direction, False)


restor2()
