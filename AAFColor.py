from collections import namedtuple

X = lambda point: point[0]
Y = lambda point: point[1]
def Z(self):
	return self[2]

Point = namedtuple('Points', ['x', 'y', 'z'], verbose=True)

p = Point(11, 22, 33)

print(Z(p))