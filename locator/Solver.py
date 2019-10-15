from PIL import Image
from locator.models.Point import Point
from locator.mathUtils.statistics import sigma, average
from locator.mathUtils.basic import sqr
from copy import copy
from queue import Queue

gridWidth = 16
gridDis = 25

class Solver:
    _neighborSize = gridWidth >> 1

    @classmethod
    def setNeighborSize(cls, d: int):
        cls._neighborSize = d
    
    @classmethod
    def getNeighborSize(cls, d: int):
        return cls._neighborSize

    @classmethod
    def getNeighborArea(cls):
        return sqr(2 * cls._neighborSize + 1)

    def __init__(self, imagePath):
        self.image = Image.open(imagePath).convert('L')
        self.pix = self.image.load()
        x, y = self.image.size
        self.p = Point(x, y)

    def _getNeighbor(self, p, d):
        n = []
        for i in range(-d, d + 1):
            for j in range(-d, d + 1):
                cur = p + Point(i, j)
                if (cur.range(self.p)):
                    n.append(p + Point(i, j))

        return n

    
    def getNeighborGaryScale(self, p):
        n = self._getNeighbor(p, self._neighborSize)
        v = [0] * (self.getNeighborArea() - len(n))
        for x in n:
            assert x.range(self.p)
            v.append(self.pix[x.x, x.y])

        return v		

    def _neighborAverage(self, p):
        return average(self.getNeighborGaryScale(p))

    def _neighborSigma(self, p):
        return sigma(self.getNeighborGaryScale(p))

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

    _adjustSize = 2

    # return a point that is closer to a center in the neighbor of p
    def _adjust(self, p):
        n = self._getNeighbor(p, self._adjustSize)
        return self.chooseLowestSigma(n)

    def _getSomeCenter(self):
        r, c = self.p.x >> 1, self.p.y >> 1
        pos = Point(r, c)
        n = self._getNeighbor(pos, gridDis >> 1)
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

                if len(self._getNeighbor(v, self._neighborSize)) < self.getNeighborArea():
                    continue

                if not v.pointTuple() in pointSet:
                    pointSet.add(v.pointTuple())
                    centers.append(v)
                    queue.put(v)

        minVal = self._neighborSigma(min(centers, key=lambda p: self._neighborSigma(p)))
        maxVal = self._neighborSigma(max(centers, key=lambda p: self._neighborSigma(p)))
        
        piv = (minVal + maxVal) / 2

        print('potential positions:')

        for x in centers:
            if self._neighborSigma(x) > piv:
                print(x)

        self.image.show()
