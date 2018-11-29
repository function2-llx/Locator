from locator.Solver import Solver

imagePath = 'examples/concentration2.tif'

if __name__ == "__main__":
	solver = Solver(imagePath)
	print(solver._getSomeCenter())