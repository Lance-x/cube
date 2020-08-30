from copy import deepcopy
from random import randint
from side import Side


class Cube(object):
	sides = {}
	steps = {}
	step_count = 0
	step_dic={('white','r'):"U",('white','l'):"U'",('yellow','r'):"D",('yellow','l'):"D'",
			  ('red','r'):"L",('red','l'):"L'",('orange','r'):"R",('orange','l'):"R'",
			  ('green','r'):"F",('green','l'):"F'",('blue','r'):"B",('blue','l'):"B'"}


	def __init__(self, list2=None):
		self.sides["white"] = Side(0, 'white')
		self.sides["red"] = Side(1, 'red')
		self.sides["blue"] = Side(2, 'blue')
		self.sides["green"] = Side(3, 'green')
		self.sides["orange"] = Side(4, 'orange')
		self.sides["yellow"] = Side(5, 'yellow')

		self.sides["white"].forward = self.sides["green"]
		self.sides["white"].back = self.sides["blue"]
		self.sides["white"].left = self.sides["red"]
		self.sides["white"].right = self.sides["orange"]

		self.sides["yellow"].forward = self.sides["blue"]
		self.sides["yellow"].back = self.sides["green"]
		self.sides["yellow"].left = self.sides["red"]
		self.sides["yellow"].right = self.sides["orange"]

		self.sides["red"].forward = self.sides["white"]
		self.sides["red"].back = self.sides["yellow"]
		self.sides["red"].left = self.sides["green"]
		self.sides["red"].right = self.sides["blue"]

		self.sides["orange"].forward = self.sides["white"]
		self.sides["orange"].back = self.sides["yellow"]
		self.sides["orange"].left = self.sides["blue"]
		self.sides["orange"].right = self.sides["green"]

		self.sides["blue"].forward = self.sides["white"]
		self.sides["blue"].back = self.sides["yellow"]
		self.sides["blue"].left = self.sides["red"]
		self.sides["blue"].right = self.sides["orange"]

		self.sides["green"].forward = self.sides["white"]
		self.sides["green"].back = self.sides["yellow"]
		self.sides["green"].left = self.sides["orange"]
		self.sides["green"].right = self.sides["red"]

		if list2 is not None:
			self.sides["white"].content, self.sides["red"].content, \
			self.sides["blue"].content, self.sides["green"].content, \
			self.sides["orange"].content, self.sides["yellow"].content = \
				list2[0:]

	def __str__(self):
		my_str = ''

		def my_print(*sides):
			nonlocal my_str
			# print(sides)
			if len(sides) == 1:
				# my_str += "         {}\n".format(sides[0].color)
				my_str += "         ---------\n"
				my_str += "         {}\n".format(sides[0].content[0])
				my_str += "         {}\n".format(sides[0].content[1])
				my_str += "         {}\n".format(sides[0].content[2])
				my_str += "         ---------\n"
			# my_str += "\n"
			else:
				# for side in sides:
				#     my_str += "{:<9}".format(side.color)
				# my_str += "\n"

				for i in range(3):
					for side in sides:
						my_str += str(side.content[i])
					my_str += "\n"

		my_print(self.sides["white"])
		my_print(self.sides["red"], self.sides["blue"], self.sides["orange"], self.sides["green"])
		my_print(self.sides["yellow"])
		return my_str

	def rotation(self, color: Side, direction, print_out: bool = False):
		if self.step_count==0:
			self.steps[self.step_count] = ("ini_status", deepcopy(str(self)))
		elif self.step_count>1000:
			raise ValueError("不正确的魔方")
		if direction == 'r':
			color.content = color.content[::-1]
			a = zip(*color.content)
			b = []
			for i in a:
				b.append(list(i))
		elif direction == 'l':
			b = []
			c = []
			for i in color.content:
				c.append(i[::-1])
			c = zip(*c)
			for i in c:
				b.append(list(i))

		else:
			b = color.content
		# color.content = deepcopy(b)
		self.sides[color.color].content = deepcopy(b)
		if color.color == 'white':
			if direction == "r":
				color.left.content[0], color.back.content[0], color.right.content[0], color.forward.content[0] = \
					color.back.content[0], color.right.content[0], color.forward.content[0], color.left.content[0]
			elif direction == 'l':
				color.left.content[0], color.back.content[0], color.right.content[0], color.forward.content[0] = \
					color.forward.content[0], color.left.content[0], color.back.content[0], color.right.content[0]
		elif color.color == 'yellow':
			if direction == "r":
				color.left.content[2], color.back.content[2], color.right.content[2], color.forward.content[2] = \
					color.back.content[2], color.right.content[2], color.forward.content[2], color.left.content[2]
			elif direction == 'l':
				color.left.content[2], color.back.content[2], color.right.content[2], color.forward.content[2] = \
					color.forward.content[2], color.left.content[2], color.back.content[2], color.right.content[2]

		elif color.color == 'red':

			if direction == "r":
				color.left.content[0][2], color.left.content[1][2], color.left.content[2][2], \
				color.forward.content[2][0], color.forward.content[1][0], color.forward.content[0][0], \
				color.right.content[2][0], color.right.content[1][0], color.right.content[0][0], \
				color.back.content[2][0], color.back.content[1][0], color.back.content[0][0] \
					= \
					color.back.content[2][0], color.back.content[1][0], color.back.content[0][0], \
					color.left.content[0][2], color.left.content[1][2], color.left.content[2][2], \
					color.forward.content[2][0], color.forward.content[1][0], color.forward.content[0][0], \
					color.right.content[2][0], color.right.content[1][0], color.right.content[0][0]
			elif direction == 'l':
				color.left.content[0][2], color.left.content[1][2], color.left.content[2][2], \
				color.forward.content[2][0], color.forward.content[1][0], color.forward.content[0][0], \
				color.right.content[2][0], color.right.content[1][0], color.right.content[0][0], \
				color.back.content[2][0], color.back.content[1][0], color.back.content[0][0] \
					= \
					color.forward.content[2][0], color.forward.content[1][0], color.forward.content[0][0], \
					color.right.content[2][0], color.right.content[1][0], color.right.content[0][0], \
					color.back.content[2][0], color.back.content[1][0], color.back.content[0][0], \
					color.left.content[0][2], color.left.content[1][2], color.left.content[2][2]

		elif color.color == 'orange':

			if direction == "r":
				color.left.content[0][2], color.left.content[1][2], color.left.content[2][2], \
				color.forward.content[0][2], color.forward.content[1][2], color.forward.content[2][2], \
				color.right.content[2][0], color.right.content[1][0], color.right.content[0][0], \
				color.back.content[0][2], color.back.content[1][2], color.back.content[2][2] \
					= \
					color.back.content[0][2], color.back.content[1][2], color.back.content[2][2], \
					color.left.content[0][2], color.left.content[1][2], color.left.content[2][2], \
					color.forward.content[0][2], color.forward.content[1][2], color.forward.content[2][2], \
					color.right.content[2][0], color.right.content[1][0], color.right.content[0][0]
			elif direction == 'l':
				color.left.content[0][2], color.left.content[1][2], color.left.content[2][2], \
				color.forward.content[0][2], color.forward.content[1][2], color.forward.content[2][2], \
				color.right.content[2][0], color.right.content[1][0], color.right.content[0][0], \
				color.back.content[0][2], color.back.content[1][2], color.back.content[2][2] \
					= \
					color.forward.content[0][2], color.forward.content[1][2], color.forward.content[2][2], \
					color.right.content[2][0], color.right.content[1][0], color.right.content[0][0], \
					color.back.content[0][2], color.back.content[1][2], color.back.content[2][2], \
					color.left.content[0][2], color.left.content[1][2], color.left.content[2][2]

		elif color.color == 'blue':

			if direction == "r":
				color.left.content[0][2], color.left.content[1][2], color.left.content[2][2], \
				color.forward.content[2][2], color.forward.content[2][1], color.forward.content[2][0], \
				color.right.content[2][0], color.right.content[1][0], color.right.content[0][0], \
				color.back.content[0][0], color.back.content[0][1], color.back.content[0][2] \
					= \
					color.back.content[0][0], color.back.content[0][1], color.back.content[0][2], \
					color.left.content[0][2], color.left.content[1][2], color.left.content[2][2], \
					color.forward.content[2][2], color.forward.content[2][1], color.forward.content[2][0], \
					color.right.content[2][0], color.right.content[1][0], color.right.content[0][0]
			elif direction == 'l':
				color.left.content[0][2], color.left.content[1][2], color.left.content[2][2], \
				color.forward.content[2][2], color.forward.content[2][1], color.forward.content[2][0], \
				color.right.content[2][0], color.right.content[1][0], color.right.content[0][0], \
				color.back.content[0][0], color.back.content[0][1], color.back.content[0][2] \
					= \
					color.forward.content[2][2], color.forward.content[2][1], color.forward.content[2][0], \
					color.right.content[2][0], color.right.content[1][0], color.right.content[0][0], \
					color.back.content[0][0], color.back.content[0][1], color.back.content[0][2], \
					color.left.content[0][2], color.left.content[1][2], color.left.content[2][2]

		elif color.color == 'green':

			if direction == "r":
				color.left.content[0][2], color.left.content[1][2], color.left.content[2][2], \
				color.forward.content[0][0], color.forward.content[0][1], color.forward.content[0][2], \
				color.right.content[2][0], color.right.content[1][0], color.right.content[0][0], \
				color.back.content[2][2], color.back.content[2][1], color.back.content[2][0] \
					= \
					color.back.content[2][2], color.back.content[2][1], color.back.content[2][0], \
					color.left.content[0][2], color.left.content[1][2], color.left.content[2][2], \
					color.forward.content[0][0], color.forward.content[0][1], color.forward.content[0][2], \
					color.right.content[2][0], color.right.content[1][0], color.right.content[0][0]
			elif direction == 'l':
				color.left.content[0][2], color.left.content[1][2], color.left.content[2][2], \
				color.forward.content[0][0], color.forward.content[0][1], color.forward.content[0][2], \
				color.right.content[2][0], color.right.content[1][0], color.right.content[0][0], \
				color.back.content[2][2], color.back.content[2][1], color.back.content[2][0] \
					= \
					color.forward.content[0][0], color.forward.content[0][1], color.forward.content[0][2], \
					color.right.content[2][0], color.right.content[1][0], color.right.content[0][0], \
					color.back.content[2][2], color.back.content[2][1], color.back.content[2][0], \
					color.left.content[0][2], color.left.content[1][2], color.left.content[2][2]
		else:
			print("error!!")
		if self.step_count>=0:
			self.step_count += 1
			self.steps[self.step_count] = (self.step_dic[(color.color, direction)], deepcopy(str(self)))
		if print_out:
			print(color.color, direction)
			print(self)

	def upset(self, times: int = 100, print_out: bool = False):
		colors = ["white", "red", "blue", "green", "orange", "yellow"]
		directions = ["r", "l"]
		self.step_count=-1
		for i in range(times):
			color = colors[randint(0, 5)]
			direction = directions[randint(0, 1)]
			# print(color, direction)
			self.rotation(self.sides[color], direction, print_out)
		self.step_count=0


if __name__ == '__main__':
	my_mo_fang = Cube()
	# my_mo_fang.sides["white"].content[0]=[1,2,4]
	# my_mo_fang.rotation(my_mo_fang.sides["blue"], 'l')
	print(my_mo_fang)
	print("=================================")
	for i in range(100):
		print(i)
		my_mo_fang.upset(1)
		print(my_mo_fang)
# my_mo_fang.upset(100)
# print(my_mo_fang)
# print(my_mo_fang.sides)
