import wx
from restore import *


class MyPanel(wx.Panel):
	result = ''

	def __init__(self, parent, id):
		wx.Panel.__init__(self, parent, id)
		image_file = 'cube1.png'
		try:
			to_bmp_image = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
			self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0))
			image_width = to_bmp_image.GetWidth()
			image_height = to_bmp_image.GetHeight()
			set_title = "魔方计算器"  # '%s %d x %d' % (image_file, to_bmp_image.GetWidth(), to_bmp_image.GetHeight())
			parent.SetTitle(set_title)
		except IOError:
			print('Image file %s not found'.format(image_file))
			raise SystemExit
		# 创建一个按钮
		# self.button = wx.Button(self.bitmap, -1, label='Test', pos=(10, 10))
		self.content = []
		for k in range(6):
			if k == 0:
				x, y = 220, 25
			elif 1 <= k <= 4:
				x, y = 192 * k - 164, 190
			else:
				x, y = 220, 355
			for j in range(3):
				for i in range(3):
					if i == 1 and j == 1:
						continue
					self.content.append(
						wx.TextCtrl(self.bitmap, -1, pos=(x + 65 * i, y + 55 * j), size=(50, 45), style=wx.TE_CENTER))
					self.content[-1].SetMaxLength(1)
					font1 = wx.Font(30, wx.MODERN, wx.BOLD, wx.NORMAL, False, 'Calibri')
					self.content[-1].SetFont(font1)

		self.button1 = wx.Button(self.bitmap, 1, label='随机生成', pos=(450, 450))
		self.button1.Bind(wx.EVT_BUTTON, self.load)
		self.button2 = wx.Button(self.bitmap, 2, label='开始计算', pos=(550, 450))
		self.button2.Bind(wx.EVT_BUTTON, self.calculate)
		self.button3 = wx.Button(self.bitmap, 3, label='关闭', pos=(650, 450))
		self.button3.Bind(wx.EVT_BUTTON, self.colse)
		self.result = wx.TextCtrl(self.bitmap, -1, pos=(410, 25), size=(380, 155),
								  style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)

	def load(self, event):
		self.cube = gen_cube()
		# print(self.cube)
		self.result.SetValue("")
		self.cube_to_gui()

	def colse(self, event):
		exit(0)

	def calculate(self, event):
		input_cub = self.gui_to_cube()
		if not input_cub:
			return
		try:
			re_steps = restore(self.cube)
		except ValueError as e:
			wx.MessageBox("不正确的魔方")
			return
		# result.SetStyle(0,0,wx.MULTILINE)
		out_put = "计算成功，共用 {} 步,还原步骤如下：\n".format(self.cube.step_count)
		for key in re_steps:
			out_put = out_put + re_steps[key][0] + " "
		self.result.SetValue(out_put)
		# print(out_put)

	# self.result.SetValue("")
	def cube_to_gui(self):
		side_colors = ["white", "red", "blue", "orange", "green", "yellow"]
		k = 0
		for color in side_colors:
			for i in range(3):
				for j in range(3):
					if i == j == 1:
						continue
					self.content[k].SetValue(str(self.cube.sides[color].content[i][j]))
					k += 1

	def gui_to_cube(self):
		side_colors = {"white": 0, "red": 1, "blue": 2, "orange": 4, "green": 3, "yellow": 5}
		k = 0
		for color in side_colors:
			for i in range(3):
				for j in range(3):
					if i == j == 1:
						self.cube.sides[color].content[i][j] = side_colors.get(color)
						continue
					if self.content[k].GetValue()=="":
						wx.MessageBox("输入不完整")
						return False
					if ord("0") <= ord(self.content[k].GetValue()) <= ord("6"):
						self.cube.sides[color].content[i][j] = eval(self.content[k].GetValue())
						k += 1
					else:
						self.cube = Cube()
						wx.MessageBox("输入错误")
						return False
		return True
		# print(self.cube)


if __name__ == '__main__':
	app = wx.App()
	frame = wx.Frame(None, -1, 'Image', size=(820, 570))
	my_panel = MyPanel(frame, -1)
	frame.Show()
	app.MainLoop()
