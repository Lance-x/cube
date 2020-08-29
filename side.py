from copy import deepcopy

class Side(object):
    color = None
    forward = None
    back = None
    left = None
    right = None
    content = []
    dic_DC = {"white":None, "red":None, "blue":None, "green":None, "orange":None, "yellow":None}
    def __init__(self, n, color):
        self.color = color
        self.content = deepcopy([[], [], []])
        for i in range(3):
            for j in range(3):
                self.content[i].append(deepcopy(n))

if __name__ == '__main__':
    a=Side(2,"red")
    print(type(a.content))