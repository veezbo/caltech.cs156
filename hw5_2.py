from numpy import *
from numpy.linalg import *

import random

def sqrnorm(p):
	return [2.*(p[0]-0.5), 2.*(p[1]-0.5)]
def genPoint():
	return sqrnorm([random.random(), random.random()])
def genPoints(n):
	p = [None]*n
	for x in range(0, n):
		p[x] = genPoint()
	
	return p


def tolist(y):
	return array(y).reshape(-1,).tolist()


def lineTwoPoints(a, b):
	slope = (b[1]-a[1])/(b[0]-a[0])
	return [slope, a[1]-slope*a[0]]
def genLine():
	return lineTwoPoints(genPoint(), genPoint())

def evalFunction(l, p):
	if (l[0]*p[0]+l[1]) >= p[1]:
		return 1
	else:
		return -1

def above(w, x):
	if (w * transpose(x)).item() < 0.:
		return 1
	else:
		return -1

N = 100

w = array([0., 0., 0.])
w_start = w
line = genLine()
x_start = genPoints(N)
x = x_start
y_start = [None] * N

for i in range(N):
	if above(line, x[i]):
		y_start[i] = 1
	else:
		y_start[i] = -1

eps = 0.01
while (norm(w_start - w) > eps):
	random.shuffle(x)
	for i in range(N):
		g = (x[1]*x[0])/(1.+e**(x[1]*))