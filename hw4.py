from numpy import *
from numpy.linalg import *

def sqrnorm(p):
	return [2.*(p[0]-0.5), 2.*(p[1]-0.5)]
def genPoint():
	return sqrnorm([random.random(), random.random()])
def genPoints(n):
	p = [None]*n
	for x in range(0, n):
		p[x] = genPoint()
	
	return p

ahat = 0.
var = 0.
for x in range(0, 10000):
	[p1, p2] = [genPoint(), genPoint()]
	p1[1] = sin(3.14*p1[0])
	p2[1] = sin(3.14*p2[0])
	a = (p1[0]*p1[1]+p2[0]*p2[1])/(p1[0]**2+p2[0]**2)
	ahat += a
	var += ((1.43 - a)*p1[0])**2
	var += ((1.43 - a)*p2[0])**2

print "average hypothesis:", ahat / 10000.

bias = 0.
for x in range(-100, 100):
	x /= 100.
	#print x
	bias += (sin(3.14 * x) - 1.43*x)**2

print "bias:", bias / (2/.01)

print "variance:", var / 20000.