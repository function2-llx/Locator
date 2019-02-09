from math import sqrt
from .basic import sqr

def average(l):
	if not l:
		return 0

	ret = 0
	for x in l:
		ret += x
	return ret / len(l)

def sigma(l):
	if not l:
		return 0

	a = average(l)
	ret = 0
	for x in l:
		ret += sqr(x - a)

	return sqrt(ret / len(l))

def max_min(v):
	return max(v) - min(v)