from locator.Solver import Solver
from locator.models.Point import Point
from sharpener.sharpener import Sharpener
import cv2

# image_path = 'examples/con2-2.jpg'

if __name__ == "__main__":

	# sharpener = Sharpener()
	# sharpener.sharpen(image_path)
    for i in [1]:
        image_path = 'examples/concentration{}.tif'.format(i)
        solver = Solver(image_path)
        solver.getAllCell()
	