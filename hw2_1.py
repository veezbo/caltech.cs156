from numpy import *
from numpy.linalg import *

F = 10
def flipCoin():
	count = 0.
	for x in range(F):
		count += random.randint(2)
	return count / float(F)

E = 10000

v1 = 0
vrand = 0
vmin = 0
for x in range(E):
	if (x % 1000 == 0):
		print x
	C = 1000

	c1 = -198234.
	crand = -112312.
	rindex = int(1000 * random.random())
	cmin = 92849.
	for i in range(C):
		f = flipCoin()
		if i == 0:
			c1 = f
		if i == rindex:
			crand = f
		if f < cmin:
			cmin = f

	v1 += c1
	vrand += crand
	vmin += cmin

print v1 / float(E)
print vrand / float(E)
print vmin / float(E)

#got these values:
#0.50034
#0.49851
#0.03744
