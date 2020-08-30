from cube import Cube
from time import perf_counter

# my_cube = Cube()
# # print(my_cube)
# my_cube.upset()  # print_out=True)
# print([my_cube.sides["white"].content, my_cube.sides["red"].content, my_cube.sides["blue"].content,
#        my_cube.sides["green"].content, my_cube.sides["orange"].content, my_cube.sides["yellow"].content])


# print(my_cube)
# print(my_cube.sides)
PRINT_OUT = False


def step1_0(my_cube):
	"""
	恢复底面白色小块
	:param my_cube:
	:return:
	"""

	def step1_0_0(color: str):
		if my_cube.sides[color].content[2][1] == my_cube.sides[color].content[1][1]:
			my_cube.rotation(my_cube.sides[color], 'r', PRINT_OUT)
			my_cube.rotation(my_cube.sides[color], 'r', PRINT_OUT)
		elif my_cube.sides[color].content[2][1] == my_cube.sides[color].right.content[1][1]:
			my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
			my_cube.rotation(my_cube.sides[color].right, 'r', PRINT_OUT)
			my_cube.rotation(my_cube.sides[color].right, 'r', PRINT_OUT)
		elif my_cube.sides[color].content[2][1] == my_cube.sides[color].right.right.content[1][1]:
			my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
			my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
			my_cube.rotation(my_cube.sides[color].right.right, 'r', PRINT_OUT)
			my_cube.rotation(my_cube.sides[color].right.right, 'r', PRINT_OUT)
		elif my_cube.sides[color].content[2][1] == my_cube.sides[color].left.content[1][1]:
			my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
			my_cube.rotation(my_cube.sides[color].left, 'r', PRINT_OUT)
			my_cube.rotation(my_cube.sides[color].left, 'r', PRINT_OUT)
		else:
			raise ValueError("不正确的魔方")

	while True:
		if my_cube.sides['yellow'].content[0][1] == 0:
			step1_0_0('blue')
		# if my_cube.sides['blue'].content[2][1]==my_cube.sides['blue'].content[1][1]:
		# 	my_cube.rotation(my_cube.sides['blue'],'r')
		# 	my_cube.rotation(my_cube.sides['blue'],'r')
		# elif my_cube.sides['blue'].content[2][1]==my_cube.sides['orange'].content[1][1]:
		# 	my_cube.rotation(my_cube.sides['yellow'],'r')
		# 	my_cube.rotation(my_cube.sides['orange'],'r')
		# 	my_cube.rotation(my_cube.sides['orange'],'r')
		# elif my_cube.sides['blue'].content[2][1]==my_cube.sides['green'].content[1][1]:
		# 	my_cube.rotation(my_cube.sides['yellow'],'r')
		# 	my_cube.rotation(my_cube.sides['yellow'],'r')
		# 	my_cube.rotation(my_cube.sides['green'],'r')
		# 	my_cube.rotation(my_cube.sides['green'],'r')
		# elif my_cube.sides['blue'].content[2][1]==my_cube.sides['red'].content[1][1]:
		# 	my_cube.rotation(my_cube.sides['yellow'],'l')
		# 	my_cube.rotation(my_cube.sides['red'],'r')
		# 	my_cube.rotation(my_cube.sides['red'],'r')
		# else:
		# 	raise ValueError("不正确的魔方")

		elif my_cube.sides['yellow'].content[1][0] == 0:
			step1_0_0('red')

		elif my_cube.sides['yellow'].content[1][2] == 0:
			step1_0_0('orange')
		elif my_cube.sides['yellow'].content[2][1] == 0:
			step1_0_0('green')
		else:
			break
	pass


def step1_1(my_cube):
	"""
	恢复底棱侧面白色小块
	:param my_cube:
	:return:
	"""

	def step1_1_0(color: str, a, b):
		if my_cube.sides[color].content[1][1] == my_cube.sides['yellow'].content[a][b]:
			my_cube.rotation(my_cube.sides["yellow"], "r", PRINT_OUT)
			my_cube.rotation(my_cube.sides[color].right, "r", PRINT_OUT)
			my_cube.rotation(my_cube.sides[color], "l", PRINT_OUT)
			my_cube.rotation(my_cube.sides[color].right, "l", PRINT_OUT)
		elif my_cube.sides[color].right.content[1][1] == my_cube.sides['yellow'].content[a][b]:
			my_cube.rotation(my_cube.sides[color], 'l', PRINT_OUT)
			my_cube.rotation(my_cube.sides[color].right, "r", PRINT_OUT)
			my_cube.rotation(my_cube.sides[color], 'r', PRINT_OUT)
		elif my_cube.sides[color].right.right.content[1][1] == my_cube.sides['yellow'].content[a][b]:
			my_cube.rotation(my_cube.sides["yellow"], "r", PRINT_OUT)
			my_cube.rotation(my_cube.sides[color].right, 'l', PRINT_OUT)
			my_cube.rotation(my_cube.sides[color].right.right, "r", PRINT_OUT)
			my_cube.rotation(my_cube.sides[color].right, 'r', PRINT_OUT)
		elif my_cube.sides[color].left.content[1][1] == my_cube.sides['yellow'].content[a][b]:
			my_cube.rotation(my_cube.sides[color], 'r', PRINT_OUT)
			my_cube.rotation(my_cube.sides[color].left, "l", PRINT_OUT)
			my_cube.rotation(my_cube.sides[color], 'l', PRINT_OUT)
			pass
		else:
			raise ValueError("不正确的魔方")

	while True:
		if my_cube.sides["red"].content[2][1] == 0:
			step1_1_0("red", 1, 0)
		elif my_cube.sides["blue"].content[2][1] == 0:
			step1_1_0("blue", 0, 1)
		elif my_cube.sides["orange"].content[2][1] == 0:
			step1_1_0("orange", 1, 2)
		elif my_cube.sides["green"].content[2][1] == 0:
			step1_1_0("green", 2, 1)
		else:
			break


def step1_2(my_cube):
	"""
	恢复侧棱白色小块
	:param my_cube:
	:return:
	"""
	side_colors = ["red", "blue", "green", "orange"]
	flag = True

	def step1_2_0(color: str, direction):
		my_cube.rotation(my_cube.sides[color], direction, PRINT_OUT)
		step1_1(my_cube)
		pass

	while flag:
		flag = False
		for color in side_colors:
			if my_cube.sides[color].content[1][0] == 0:
				my_cube.rotation(my_cube.sides[color], 'l')
				my_cube.rotation(my_cube.sides["yellow"], 'l')
				my_cube.rotation(my_cube.sides[color], 'r')
				step1_2_0(color, 'l')
				flag = True
			elif my_cube.sides[color].content[1][2] == 0:
				my_cube.rotation(my_cube.sides[color], 'r')
				my_cube.rotation(my_cube.sides["yellow"], 'r')
				my_cube.rotation(my_cube.sides[color], 'l')
				step1_2_0(color, 'r')
				flag = True


def step1_3(my_cube):
	"""
	顶棱侧面白色小块
	:param my_cube: 
	:return: 
	"""
	top_side_colors = ["red", "blue", "green", "orange"]
	flag = True
	while flag:
		flag = False
		for color in top_side_colors:
			if my_cube.sides[color].content[0][1] == 0:
				flag = True
				my_cube.rotation(my_cube.sides[color], 'r')
				my_cube.rotation(my_cube.sides[color], 'r')
				step1_1(my_cube)


def step1_4(my_cube):
	"""
	顶面十字错位
	:param my_cube:
	:return:
	"""
	flag = True
	while flag:
		flag = False
		if my_cube.sides["white"].content[0][1] == 0 and my_cube.sides["green"].content[0][1] != \
				my_cube.sides["green"].content[1][1]:
			my_cube.rotation(my_cube.sides["green"], "r")
			my_cube.rotation(my_cube.sides["green"], "r")
		elif my_cube.sides["white"].content[1][0] == 0 and my_cube.sides["red"].content[0][1] != \
				my_cube.sides["red"].content[1][1]:
			my_cube.rotation(my_cube.sides["red"], "r")
			my_cube.rotation(my_cube.sides["red"], "r")
		elif my_cube.sides["white"].content[1][2] == 0 and my_cube.sides["orange"].content[0][1] != \
				my_cube.sides["orange"].content[1][1]:
			my_cube.rotation(my_cube.sides["orange"], "r")
			my_cube.rotation(my_cube.sides["orange"], "r")
		elif my_cube.sides["white"].content[2][1] == 0 and my_cube.sides["blue"].content[0][1] != \
				my_cube.sides["blue"].content[1][1]:
			my_cube.rotation(my_cube.sides["blue"], "r")
			my_cube.rotation(my_cube.sides["blue"], "r")
		else:
			continue
		flag = True
		step1_0(my_cube)


def cross(my_cube):
	"""

	:param my_cube:
	:return:
	"""
	a1 = my_cube.sides["white"].content[0][1] == my_cube.sides["white"].content[1][1] and \
		 my_cube.sides["red"].content[0][1] == my_cube.sides["red"].content[1][1]
	a2 = my_cube.sides["white"].content[1][0] == my_cube.sides["white"].content[1][1] and \
		 my_cube.sides["blue"].content[0][1] == my_cube.sides["blue"].content[1][1]
	a3 = my_cube.sides["white"].content[1][2] == my_cube.sides["white"].content[1][1] and \
		 my_cube.sides["orange"].content[0][1] == my_cube.sides["orange"].content[1][1]
	a4 = my_cube.sides["white"].content[2][1] == my_cube.sides["white"].content[1][1] and \
		 my_cube.sides["green"].content[0][1] == my_cube.sides["green"].content[1][1]
	if a1 and a2 and a3 and a4:
		complete = True
	else:
		complete = False
	return complete


def step1(my_cube):
	"""
	顶十字
	:param my_cube:
	:return:
	"""
	i = 0
	while True:
		i += 1
		if i > 5000:
			raise ValueError("不正确的魔方")
		if cross(my_cube):
			break
		step1_0(my_cube)
		# print("1111111111111111111")
		step1_1(my_cube)
		# print("2222222222222222222")
		step1_2(my_cube)
		# print("3333333333333333333")
		step1_3(my_cube)
		# print("4444444444444444444")
		step1_4(my_cube)


def up_side(my_cube):
	a = cross(my_cube)
	if not a:
		return False
	a = up_conner_finish(my_cube, 0, 0, "green")
	if not a:
		return False
	b = up_conner_finish(my_cube, 2, 0, "red")
	if not b:
		return False
	c = up_conner_finish(my_cube, 2, 2, "blue")
	if not c:
		return False
	d = up_conner_finish(my_cube, 0, 2, "orange")
	if not d:
		return False
	return True


def up_conner_finish(my_cube, a, b, color1):
	color2 = my_cube.sides[color1].right.color
	a = my_cube.sides['white'].content[a][b] == 0
	if not a:
		return False
	b = my_cube.sides[color1].content[0][2] == my_cube.sides[color1].content[1][1]
	if not b:
		return False
	c = my_cube.sides[color2].content[0][0] == my_cube.sides[color2].content[1][1]
	if not c:
		return False
	return True


def step2_1(my_cube):
	"""
	底角侧面白色小块
	:param my_cube:
	:return:
	"""

	def step2_1_0(my_cube, color):
		my_cube.rotation(my_cube.sides[color], 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides[color], 'r', PRINT_OUT)

	def step2_1_1(my_cube, color):
		my_cube.rotation(my_cube.sides[color], 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides[color], 'l', PRINT_OUT)

	side_colors = ["red", "blue", "green", "orange"]
	flag = True
	i = 0
	while flag:
		i += 1
		if i > 5000:
			raise ValueError("不正确的魔方")
		flag = False
		for color in side_colors:
			if my_cube.sides[color].content[2][0] == 0:
				flag = True
				if my_cube.sides[color].left.content[2][2] == my_cube.sides[color].left.content[1][1]:
					step2_1_0(my_cube, color)
				elif my_cube.sides[color].left.content[2][2] == my_cube.sides[color].content[1][1]:
					my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
					step2_1_0(my_cube, my_cube.sides[color].right.color)
				elif my_cube.sides[color].left.content[2][2] == my_cube.sides[color].right.content[1][1]:
					my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
					my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
					step2_1_0(my_cube, my_cube.sides[color].right.right.color)
				elif my_cube.sides[color].left.content[2][2] == my_cube.sides[color].right.right.content[1][1]:
					my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
					step2_1_0(my_cube, my_cube.sides[color].left.color)
				else:
					raise ValueError("不正确的魔方")
			elif my_cube.sides[color].content[2][2] == 0:
				flag = True
				if my_cube.sides[color].right.content[2][0] == my_cube.sides[color].right.content[1][1]:
					step2_1_1(my_cube, color)
				elif my_cube.sides[color].right.content[2][0] == my_cube.sides[color].right.right.content[1][1]:
					my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
					step2_1_1(my_cube, my_cube.sides[color].right.color)
				elif my_cube.sides[color].right.content[2][0] == my_cube.sides[color].left.content[1][1]:
					my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
					my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
					step2_1_1(my_cube, my_cube.sides[color].right.right.color)
				elif my_cube.sides[color].right.content[2][0] == my_cube.sides[color].content[1][1]:
					my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
					step2_1_1(my_cube, my_cube.sides[color].left.color)
				else:
					raise ValueError("不正确的魔方")


def step2_2(my_cube):
	"""
	底面角白色小块
	:param my_cube:
	:return:
	"""

	def step2_2_0(my_cube, color):
		my_cube.rotation(my_cube.sides[color], 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides[color], 'l', PRINT_OUT)

	flag = True
	i = 0
	while flag:
		i += 1
		if i > 5000:
			raise ValueError("不正确的魔方")
		flag = False
		n = 0
		if my_cube.sides['yellow'].content[0][0] == 0:
			flag = True
			color = 'red'
			if up_conner_finish(my_cube, 2, 0, 'red'):
				n = 1
				if up_conner_finish(my_cube, 2, 2, 'blue'):
					n = 2
					if up_conner_finish(my_cube, 0, 2, 'orange'):
						n = 3
						if up_conner_finish(my_cube, 0, 0, 'green'):
							raise ValueError("不正确的魔方")
			if n == 1:
				my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
				color = my_cube.sides[color].right.color
			elif n == 2:
				my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
				my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
				color = my_cube.sides['red'].right.right.color
			elif n == 3:
				my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
				color = my_cube.sides['red'].left.color
			step2_2_0(my_cube, color)
			step2_1(my_cube)
		elif my_cube.sides['yellow'].content[0][2] == 0:
			flag = True
			color = 'blue'
			if up_conner_finish(my_cube, 2, 2, 'blue'):
				n = 1
				if up_conner_finish(my_cube, 0, 2, 'orange'):
					n = 2
					if up_conner_finish(my_cube, 0, 0, 'green'):
						n = 3
						if up_conner_finish(my_cube, 2, 0, 'red'):
							raise ValueError("不正确的魔方")
			if n == 1:
				my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
				color = my_cube.sides[color].right.color
			elif n == 2:
				my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
				my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
				color = my_cube.sides[color].right.right.color
			elif n == 3:
				my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
				color = my_cube.sides[color].left.color
			step2_2_0(my_cube, color)
			step2_1(my_cube)
		elif my_cube.sides['yellow'].content[2][2] == 0:
			flag = True
			color = 'orange'
			if up_conner_finish(my_cube, 0, 2, 'orange'):
				n = 1
				if up_conner_finish(my_cube, 0, 0, 'green'):
					n = 2
					if up_conner_finish(my_cube, 2, 0, 'red'):
						n = 3
						if up_conner_finish(my_cube, 2, 2, 'blue'):
							raise ValueError("不正确的魔方")
			if n == 1:
				my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
				color = my_cube.sides[color].right.color
			elif n == 2:
				my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
				my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
				color = my_cube.sides[color].right.right.color
			elif n == 3:
				my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
				color = my_cube.sides[color].left.color
			step2_2_0(my_cube, color)
			step2_1(my_cube)
		elif my_cube.sides['yellow'].content[2][0] == 0:
			flag = True
			color = 'green'
			if up_conner_finish(my_cube, 0, 0, 'green'):
				n = 1
				if up_conner_finish(my_cube, 2, 0, 'red'):
					n = 2
					if up_conner_finish(my_cube, 2, 2, 'blue'):
						n = 3
						if up_conner_finish(my_cube, 0, 2, 'orange'):
							raise ValueError("不正确的魔方")
			if n == 1:
				my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
				color = my_cube.sides[color].right.color
			elif n == 2:
				my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
				my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
				color = my_cube.sides[color].right.right.color
			elif n == 3:
				my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
				color = my_cube.sides[color].left.color
			step2_2_0(my_cube, color)
			step2_1(my_cube)
			pass


def step2_3(my_cube):
	flag = True
	i = 0
	while flag:
		i += 1
		if i > 5000:
			raise ValueError("不正确的魔方")
		a = up_conner_finish(my_cube, 0, 0, 'green')
		b = up_conner_finish(my_cube, 0, 2, 'orange')
		c = up_conner_finish(my_cube, 2, 2, 'blue')
		d = up_conner_finish(my_cube, 2, 0, 'red')
		flag = False
		if not a:
			flag = True
			my_cube.rotation(my_cube.sides['green'], 'r', PRINT_OUT)
			my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
			my_cube.rotation(my_cube.sides['green'], 'l', PRINT_OUT)
		elif not b:
			flag = True
			my_cube.rotation(my_cube.sides['orange'], 'r', PRINT_OUT)
			my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
			my_cube.rotation(my_cube.sides['orange'], 'l', PRINT_OUT)
		elif not c:
			flag = True
			my_cube.rotation(my_cube.sides['blue'], 'r', PRINT_OUT)
			my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
			my_cube.rotation(my_cube.sides['blue'], 'l', PRINT_OUT)
		elif not d:
			flag = True
			my_cube.rotation(my_cube.sides['red'], 'r', PRINT_OUT)
			my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
			my_cube.rotation(my_cube.sides['red'], 'l', PRINT_OUT)
		else:
			continue
		step2_1(my_cube)
		step2_2(my_cube)


def step2(my_cube):
	if up_side(my_cube):
		return
	step2_1(my_cube)
	step2_2(my_cube)
	step2_3(my_cube)


def algorithm3(my_cube, side_color, direction):
	if direction == "r":
		my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides[side_color].right, 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides[side_color].right, 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides[side_color], 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides[side_color], 'l', PRINT_OUT)
	elif direction == "l":
		my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides[side_color].left, 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides[side_color].left, 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides[side_color], 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides[side_color], 'r', PRINT_OUT)


def step3_1(my_cube):
	side_colors = ["red", "blue", "green", "orange"]
	i = 0
	while True:
		i += 1
		if i > 5000:
			raise ValueError("不正确的魔方")
		block_color2 = ""
		for side_color in side_colors:
			if my_cube.sides[side_color].content[2][1] == my_cube.sides[side_color].content[1][1]:
				n = 0
				block_color = side_color
			elif my_cube.sides[side_color].content[2][1] == my_cube.sides[side_color].right.content[1][1]:
				n = 1
				block_color = my_cube.sides[side_color].right.color
			elif my_cube.sides[side_color].content[2][1] == my_cube.sides[side_color].right.right.content[1][1]:
				n = 2
				block_color = my_cube.sides[side_color].right.right.color
			elif my_cube.sides[side_color].content[2][1] == my_cube.sides[side_color].left.content[1][1]:
				n = 3
				block_color = my_cube.sides[side_color].left.color
			else:
				continue

			if my_cube.sides["yellow"].forward.color == side_color:
				if my_cube.sides["yellow"].content[0][1] == my_cube.sides["yellow"].content[1][1]:
					continue
				else:
					block_color2 = side_colors[my_cube.sides["yellow"].content[0][1] - 1]
			elif my_cube.sides["yellow"].right.color == side_color:
				if my_cube.sides["yellow"].content[1][2] == my_cube.sides["yellow"].content[1][1]:
					continue
				else:
					block_color2 = side_colors[my_cube.sides["yellow"].content[1][2] - 1]
			elif my_cube.sides["yellow"].back.color == side_color:
				if my_cube.sides["yellow"].content[2][1] == my_cube.sides["yellow"].content[1][1]:
					continue
				else:
					block_color2 = side_colors[my_cube.sides["yellow"].content[2][1] - 1]
			elif my_cube.sides["yellow"].left.color == side_color:
				if my_cube.sides["yellow"].content[1][0] == my_cube.sides["yellow"].content[1][1]:
					continue
				else:
					block_color2 = side_colors[my_cube.sides["yellow"].content[1][0] - 1]
			else:
				raise ValueError("不正确的魔方")

			if n == 1:
				my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
			elif n == 2:
				my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
				my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
			elif n == 3:
				my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)

			if my_cube.sides[block_color].right.color == block_color2:
				direction = "r"
			elif my_cube.sides[block_color].left.color == block_color2:
				direction = "l"
			else:
				raise ValueError("不正确的魔方")

			algorithm3(my_cube, block_color, direction)

		if block_color2 == "":
			break
	pass


def step3_2(my_cube):
	side_colors = ["red", "blue", "green", "orange"]
	for side_color in side_colors:
		if my_cube.sides[side_color].content[1][0] != my_cube.sides[side_color].content[1][1]:
			algorithm3(my_cube, side_color, 'l')
		elif my_cube.sides[side_color].content[1][2] != my_cube.sides[side_color].content[1][1]:
			algorithm3(my_cube, side_color, 'r')
		else:
			continue
		step3_1(my_cube)
	pass


def step3(my_cube):
	step3_1(my_cube)
	step3_2(my_cube)


def algorithm4_1(my_cube, color, direction):
	if direction == "r":
		my_cube.rotation(my_cube.sides[color], 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides[color].right, 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides[color].right, 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides[color], 'r', PRINT_OUT)
	elif direction == 'l':
		my_cube.rotation(my_cube.sides[color], 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides[color].left, 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides[color].left, 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides[color], 'l', PRINT_OUT)


def algorithm4_2(my_cube, color, direction):
	if direction == 'r':
		my_cube.rotation(my_cube.sides[color], 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides[color], 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides[color], 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides[color], 'r', PRINT_OUT)
	elif direction == 'l':
		my_cube.rotation(my_cube.sides[color], 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides[color], 'l', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides[color], 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
		my_cube.rotation(my_cube.sides[color], 'l', PRINT_OUT)
	else:
		raise ValueError("方向错误")


def judge_center_point(my_cube):
	a = my_cube.sides['yellow'].content[0][1] == my_cube.sides['yellow'].content[1][1]
	if a:
		return False
	a = my_cube.sides['yellow'].content[1][0] == my_cube.sides['yellow'].content[1][1]
	if a:
		return False
	a = my_cube.sides['yellow'].content[1][2] == my_cube.sides['yellow'].content[1][1]
	if a:
		return False
	a = my_cube.sides['yellow'].content[2][1] == my_cube.sides['yellow'].content[1][1]
	if a:
		return False
	return True


def judge_v(my_cube):
	a = my_cube.sides['yellow'].content[0][1]
	b = my_cube.sides['yellow'].content[1][0]
	c = my_cube.sides['yellow'].content[1][1]
	d = my_cube.sides['yellow'].content[1][2]
	e = my_cube.sides['yellow'].content[2][1]
	if a == c and b == c and d != c and e != c:
		return 'orange'
	elif a == c and d == c and b != c and e != c:
		return 'green'
	elif e == c and b == c and a != c and d != c:
		return 'blue'
	elif e == c and d == c and a != c and b != c:
		return 'red'
	return False


def judge_line(my_cube):
	a = my_cube.sides['yellow'].content[0][1]
	b = my_cube.sides['yellow'].content[1][0]
	c = my_cube.sides['yellow'].content[1][1]
	d = my_cube.sides['yellow'].content[1][2]
	e = my_cube.sides['yellow'].content[2][1]
	if a == c and e == c and b != c and d != c:
		return 'orange'
	elif b == c and d == c and a != c and e != c:
		return 'blue'
	return False


def judge_cross(my_cube):
	a = my_cube.sides['yellow'].content[0][1]
	b = my_cube.sides['yellow'].content[1][0]
	c = my_cube.sides['yellow'].content[1][1]
	d = my_cube.sides['yellow'].content[1][2]
	e = my_cube.sides['yellow'].content[2][1]
	side_colors = ["red", "blue", "green", "orange"]
	if a == b == c == d == e:
		for color in side_colors:
			if my_cube.sides[color].content[2][0] == my_cube.sides['yellow'].content[1][1]:
				return color, 'l'
			elif my_cube.sides[color].content[2][2] == my_cube.sides['yellow'].content[1][1]:
				return color, 'r'
		return True
	return False


def judge_cross_plus(my_cube):
	a = my_cube.sides['yellow'].content[0][1]
	b = my_cube.sides['yellow'].content[1][0]
	c = my_cube.sides['yellow'].content[1][1]
	d = my_cube.sides['yellow'].content[1][2]
	e = my_cube.sides['yellow'].content[2][1]

	j = my_cube.sides['yellow'].content[0][0]
	k = my_cube.sides['yellow'].content[0][2]
	m = my_cube.sides['yellow'].content[2][2]
	n = my_cube.sides['yellow'].content[2][0]
	if a == b == c == d == e:
		if j == c and k != c and m != c and n != c:
			if my_cube.sides['orange'].content[2][2] == my_cube.sides['yellow'].content[1][1]:
				return "orange", 'r'
			elif my_cube.sides['orange'].right.content[2][0] == my_cube.sides['yellow'].content[1][1]:
				return my_cube.sides['orange'].right.color, 'l'
		elif k == c and j != c and m != c and n != c:
			if my_cube.sides['green'].content[2][2] == my_cube.sides['yellow'].content[1][1]:
				return "green", 'r'
			elif my_cube.sides['green'].right.content[2][0] == my_cube.sides['yellow'].content[1][1]:
				return my_cube.sides['green'].right.color, 'l'
		elif m == c and k != c and j != c and n != c:
			if my_cube.sides['red'].content[2][2] == my_cube.sides['yellow'].content[1][1]:
				return "red", 'r'
			elif my_cube.sides['red'].right.content[2][0] == my_cube.sides['yellow'].content[1][1]:
				return my_cube.sides['red'].right.color, 'l'
		elif n == c and k != c and m != c and j != c:
			if my_cube.sides['blue'].content[2][2] == my_cube.sides['yellow'].content[1][1]:
				return "blue", 'r'
			elif my_cube.sides['blue'].right.content[2][0] == my_cube.sides['yellow'].content[1][1]:
				return my_cube.sides['blue'].right.color, 'l'
	return False


def judge_top_finished(my_cube):
	a = my_cube.sides['yellow'].content[0][1]
	b = my_cube.sides['yellow'].content[1][0]
	c = my_cube.sides['yellow'].content[1][1]
	d = my_cube.sides['yellow'].content[1][2]
	e = my_cube.sides['yellow'].content[2][1]

	j = my_cube.sides['yellow'].content[0][0]
	k = my_cube.sides['yellow'].content[0][2]
	m = my_cube.sides['yellow'].content[2][0]
	n = my_cube.sides['yellow'].content[2][2]
	if a == b == c == d == e == j == k == m == n:
		return True
	return False


def step4(my_cube):
	"""
	判断上面是否完成
	如果已完成

	如果未完成
		判断是不是十字多一点
		如果是十字多一点

		如果不是十字多一点
		判断是不是十字
			如果是十字

			如果不是十字
			判断是不是V字
			如果是V字

			如果不是V字
			判断是不是一字
			如果是一字

			如果不是一字
				按点处理
	"""
	i = 0
	while True:
		i += 1
		if i > 5000:
			raise ValueError("不正确的魔方")
		if judge_top_finished(my_cube):
			break
		is_cross_plus = judge_cross_plus(my_cube)
		if type(is_cross_plus) is tuple:
			algorithm4_2(my_cube, is_cross_plus[0], is_cross_plus[1])
			continue
		is_cross = judge_cross(my_cube)
		if type(is_cross) is tuple:
			algorithm4_2(my_cube, is_cross[0], is_cross[1])
			continue
		is_v = judge_v(my_cube)
		if is_v:
			algorithm4_1(my_cube, is_v, 'r')
			continue
		is_line = judge_line(my_cube)
		if is_line:
			algorithm4_1(my_cube, is_line, 'r')
			continue
		if judge_center_point(my_cube):
			algorithm4_1(my_cube, 'red', 'r')


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


def judge_bottom_conner(my_cube):
	"""
	如果四面，返回 color,direction
	如果一面，返回 color
	如果没有，返回 False

	:param my_cube:
	:return:
	"""
	side_colors = ["red", "blue", "green", "orange"]
	n = 0
	c = ""
	for color in side_colors:
		if my_cube.sides[color].content[2][0] == my_cube.sides[color].content[2][2]:
			c = my_cube.sides[color].right.right.color
			n += 1
	if n == 0:
		return False
	elif n == 1:
		return c
	elif n == 4:
		for color in side_colors:
			if my_cube.sides[color].content[2][0] == my_cube.sides[color].content[2][1]:
				if my_cube.sides[color].right.content[2][1] == my_cube.sides[color].right.right.content[2][0]:
					return my_cube.sides[color].right.color, 'l'
				else:
					return my_cube.sides[color].left.color, 'r'
		return 'red', 'l'
	else:
		raise ValueError("不正确的魔方")


def algorithm5_1(my_cube, color, direction):
	algorithm4_2(my_cube, color, direction)
	if direction == "r":
		color = my_cube.sides[color].left.color
		direction = "l"
	elif direction == "l":
		color = my_cube.sides[color].right.color
		direction = "r"
	else:
		raise ValueError("方向错误")
	algorithm4_2(my_cube, color, direction)


def algorithm5_2(my_cube, color):
	my_cube.rotation(my_cube.sides[color].right, 'r', PRINT_OUT)
	my_cube.rotation(my_cube.sides[color], 'l', PRINT_OUT)
	my_cube.rotation(my_cube.sides[color].right, 'r', PRINT_OUT)
	my_cube.rotation(my_cube.sides[color].right.right, 'l', PRINT_OUT)
	my_cube.rotation(my_cube.sides[color].right.right, 'l', PRINT_OUT)
	my_cube.rotation(my_cube.sides[color].right, 'l', PRINT_OUT)
	my_cube.rotation(my_cube.sides[color], 'r', PRINT_OUT)
	my_cube.rotation(my_cube.sides[color].right, 'r', PRINT_OUT)
	my_cube.rotation(my_cube.sides[color].right.right, 'l', PRINT_OUT)
	my_cube.rotation(my_cube.sides[color].right.right, 'l', PRINT_OUT)
	my_cube.rotation(my_cube.sides[color].right, 'l', PRINT_OUT)
	my_cube.rotation(my_cube.sides[color].right, 'l', PRINT_OUT)


def judge_bottom_side(my_cube):
	side_colors = ["red", "blue", "green", "orange"]
	finish = 0
	for color in side_colors:
		a = my_cube.sides[color].content[2][0]
		b = my_cube.sides[color].content[2][1]
		c = my_cube.sides[color].content[2][2]
		if a == b == c:
			finish += 1
	if finish == 4:
		if my_cube.sides["red"].right.content[2][0] == my_cube.sides["red"].content[1][1]:
			return 3
		elif my_cube.sides["red"].right.right.content[2][0] == my_cube.sides["red"].content[1][1]:
			return 2
		elif my_cube.sides["red"].left.content[2][0] == my_cube.sides["red"].content[1][1]:
			return 1
		return True
	else:
		return False


def step5(my_cube):
	"""
	如果已完成
		结束
	如果底四面完成
		旋转底面至完成
	如果底角四
		调用 algorithm5_1
	如果底角一
		调用 algorithm5_2
	如果底角零
		调用 algorithm5_2
	:param my_cube:
	:return:
	"""
	i = 0
	while True:
		i += 1
		if i > 5000:
			raise ValueError("不正确的魔方")
		a = judge_finished(my_cube)
		if a:
			break
		# a=judge_bottom_side()
		a = judge_bottom_side(my_cube)
		if a:
			if a == 3:
				my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
			elif a == 2:
				my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
				my_cube.rotation(my_cube.sides['yellow'], 'l', PRINT_OUT)
			elif a == 1:
				my_cube.rotation(my_cube.sides['yellow'], 'r', PRINT_OUT)
		a = judge_bottom_conner(my_cube)
		if a:
			if type(a) is str:
				algorithm5_2(my_cube, a)
			elif type(a) is tuple:
				algorithm5_1(my_cube, a[0], a[1])
		else:
			algorithm5_2(my_cube, 'red')
			continue

	pass


def restore(my_cube):
	# list2 = [[[3, 0, 0], [0, 0, 3], [3, 1, 2]], [[4, 1, 5], [5, 1, 5], [0, 5, 4]], [[1, 3, 5], [4, 2, 0], [3, 4, 2]],
	#          [[4, 2, 0], [4, 3, 2], [0, 5, 1]], [[4, 0, 2], [4, 4, 2], [5, 2, 3]], [[5, 3, 1], [3, 5, 1], [2, 1, 1]]]
	# list2 = [[[1, 1, 4], [3, 0, 5], [5, 5, 0]], [[0, 0, 1], [4, 1, 4], [3, 2, 5]], [[3, 3, 2], [5, 2, 0], [1, 4, 5]],
	# 		 [[5, 2, 2], [3, 3, 2], [0, 0, 1]], [[4, 1, 2], [1, 4, 1], [4, 5, 4]], [[2, 3, 3], [0, 5, 2], [0, 4, 3]]]
	# my_cube = Cube(list2)
	# my_cube = Cube()
	# my_cube.upset()  # print_out=True)
	# print(my_cube)
	my_cube.steps={}
	my_cube.step_count=0
	step1(my_cube)
	# print(my_cube)
	step2(my_cube)
	# print(my_cube)
	step3(my_cube)
	# print(my_cube)
	step4(my_cube)
	# print(my_cube)
	step5(my_cube)
	# print(my_cube)
	# print(my_cube.steps.keys())
	return my_cube.steps


def gen_cube():
	my_cube = Cube()
	my_cube.upset()
	return my_cube


if __name__ == '__main__':
	my_cube = Cube()
	my_cube.upset()
	steps = restore(my_cube)
	while True:
		a = input("1、查看总步数\n2、查看步骤\n3、查看每步详情\n4、查看初始状态\n\n请选择：")
		if a == '1':
			print(len(steps) - 1)
		elif a == '2':
			for key in steps.keys():
				print(steps[key][0], end=",")
			print("\n\n")
		elif a == '3':
			for key in steps.keys():
				print(steps[key][0])
				print(steps[key][1])
			print("\n\n")
		elif a == "4":
			print(steps[0][1])
		else:
			break
