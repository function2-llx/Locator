from PIL import Image, ImageDraw
from locator.models.Point import Point
from locator.mathUtils.statistics import sigma, average
from locator.mathUtils.basic import sqr
from copy import copy
from queue import Queue
import numpy as np
from math import sqrt

gridWidth = 14
gridDis = 20

# nbr = neighbor
# gs = gray scale

class Solver:
    nbr_size = 5

    @classmethod
    def setNeighborSize(cls, d: int):
        cls.nbr_size = d
    
    @classmethod
    def getNeighborSize(cls, d: int):
        return cls.nbr_size

    @classmethod
    def getNeighborArea(cls):
        return sqr(2 * cls.nbr_size + 1)

    def __init__(self, imagePath):
        self.image = Image.open(imagePath).convert('L')
        self.pix = self.image.load()
        x, y = self.image.size
        self.p = Point(x, y)
        # self.neigobor_sigma = np.array([[np.var(self.get_nbr_gs(Point(i, j))) for j in range(y)] for i in range(x)])
        tmp = []
        for i in range(x):
            print(i)
            tmp.append([sqrt(np.var(self.get_nbr_gs(Point(i, j)))) for j in range(y)])

        self.sigma = np.array(tmp)
        self.adjust_size = 2

        print("sigma initialized")

    def get_neighbor(self, p, d):
        n = []
        for i in range(-d, d + 1):
            for j in range(-d, d + 1):
                cur = p + Point(i, j)
                if (cur.range(self.p)):
                    n.append(p + Point(i, j))

        return n
    
    def get_nbr_gs(self, p):
        n = self.get_neighbor(p, self.nbr_size)
        v = [0] * (self.getNeighborArea() - len(n))
        for x in n:
            assert x.range(self.p)
            v.append(self.pix[x.x, x.y])

        return v		

    # def _neighborAverage(self, p):
    #     return average(self.get_nbr_gs(p))

    def _neighborSigma(self, p):
        # return sigma(self.get_nbr_gs(p))
        return self.sigma[p.x, p.y]

    def _contains(self, p):
        return p.range(self.p)

    # return the point with lowest 
    def chooseLowestSigma(self, n):
        ret = copy(n[0])
        val = self._neighborSigma(ret)
        for x in n:
            cur = self._neighborSigma(x)
            if cur < val:
                ret, val = x, cur

        return ret


    # return a point that is closer to a center in the neighbor of p
    def _adjust(self, p):
        # n = self.get_neighbor(p, self.adjust_size)
        # return self.chooseLowestSigma(n)
        print('ajust')
        while True:
            q = self.chooseLowestSigma(self.get_neighbor(p, self.adjust_size))
            if p == q: return p
            print(p, q)
            p = q
        # while p != self.chooseLowestSigma(self.get_neighbor(p, self.adjust_size)):


    def _getSomeCenter(self):
        r, c = self.p.x >> 1, self.p.y >> 1
        pos = Point(r, c)
        n = self.get_neighbor(pos, gridDis >> 1)
        return self.chooseLowestSigma(n)

    def getAllCell(self):
        p = self._getSomeCenter()
        queue = Queue()
        pointSet = set()
        pointSet.add(p.pointTuple())
        queue.put(p)
        d = gridDis
        mx, my = (d, 0, -d, 0), (0, d, 0, -d)
        centers = [p]
        
        cnt = 0

        while not queue.empty():
            cnt = cnt + 1
            u = queue.get()
            print(u, self._neighborSigma(u), cnt)
            for x, y in zip(mx, my):
                v = u + Point(x, y)
                if not self._contains(v):
                    continue
                v = self._adjust(v)

                if len(self.get_neighbor(v, self.nbr_size)) < self.getNeighborArea():
                    continue

                if not v.pointTuple() in pointSet:
                    pointSet.add(v.pointTuple())
                    centers.append(v)
                    queue.put(v)

        minVal = self._neighborSigma(min(centers, key=lambda p: self._neighborSigma(p)))
        maxVal = self._neighborSigma(max(centers, key=lambda p: self._neighborSigma(p)))
        
        piv = (minVal + maxVal) / 2

        print('potential positions:')

        draw = ImageDraw.Draw(self.image)

        for x in centers:
            if self._neighborSigma(x) > piv:
                print(x)
                draw.rectangle([x.x - 3, x.y - 3, x.x + 3, x.y + 3])

        
        # for i in range(30):
        #     for j in range(30):
        #         self.pix[i, j] = 0

        

        self.image.save('test.jpg', quality=95)
