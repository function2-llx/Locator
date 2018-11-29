from PIL import Image
from .models.Point import Point
from .mathUtils.statistics import sigma, average
from copy import copy

class Solver:
	neighborSize = 5

	@classmethod
	def setNeighborSize(cls, d: int):
		cls.neighborSize = d

	def __init__(self, imagePath):
		self.image = Image.open(imagePath).convert('L')
		self.pix = self.image.load()
		self.r, self.c = self.image.size
	
	def getNeighborGaryScale(self, p):
		d = Solver.neighborSize
		v = []
		for i in range(-d, d + 1):
			for j in range(-d, d + 1):
				r, c = p.x + i, p.y + j
				if Point(r, c).range(self.r, self.c):
					v.append(self.pix[r, c])
				else:
					v.append(0)

		return v
		

	def _neighborAverage(self, p):
		return average(self.getNeighborGaryScale())

	def _neighborSigma(self, p):
		return sigma(self.getNeighborGaryScale(p))

	def _getSomeCenter(self):
		r, c = self.r >> 1, self.c >> 1
		d = 10
		pos = Point(r, c)
		val = self._neighborSigma(pos)
		for i in range(-d, d + 1):
			for j in range(-d, d + 1):
				cur = Point(r + i, r + j)
				if cur.range(self.r, self.c):
					curVal = self._neighborSigma(cur)
					# print(cur, curVal)
					if curVal < val:
						pos, val = cur, curVal

		return pos

		

	
