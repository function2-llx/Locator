from random import randint

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	# return a random point in rectangle(r, c)
	def rand(r, c):
		return Point(randint(0, r - 1), randint(0, c - 1))

	def range(self, r, c):
		return 0 <= self.x and self.x < r and \
		       0 <= self.y and self.y < c

	def __repr__(self):
		return '<Point>: (%d, %d)' % (self.x, self.y)