from locator.Solver import Solver
from locator.models.Point import Point

imagePath = 'examples/concentration2.tif'

if __name__ == "__main__":
	solver = Solver(imagePath)
	c = solver.getAllCell()
	