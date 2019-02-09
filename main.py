from locator.Solver import Solver
from locator.models.Point import Point

imagePath = 'examples/test.jpg'

if __name__ == "__main__":
	solver = Solver(imagePath)
	solver.getAllCell()
	