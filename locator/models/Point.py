from random import randint

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, p):
		return Point(self.x + p.x, self.y + p.y)

	def __lt__(self, value):
		if self.x == value.x:
			return self.y < value.y

		return self.x < value.x

	# return a random point in rectangle with righttop of p
	@staticmethod
	def rand(p):
		return Point(randint(0, p.x - 1), randint(0, p.y - 1))

	# return if current point is in the rectangle p
	def range(self, p):
		return 0 <= self.x and self.x < p.x and \
		       0 <= self.y and self.y < p.y

	def __repr__(self):
		return '<Point>: (%d, %d)' % (self.x, self.y)