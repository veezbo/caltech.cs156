from numpy import *
from numpy.linalg import *
from sklearn import svm
# from sklearn import 

N = 100

def sign(x):
	if x <= 0.:
		return -1.
	else:
		return 1.

def sqrnorm(p):
	return [2.*(p[0]-0.5), 2.*(p[1]-0.5)]
def genPoint():
	return sqrnorm([random.random(), random.random()])
def genPoints(n):
	p = [None]*n
	for x in range(0, n):
		p[x] = genPoint()
	
	return p


def lineTwoPoints(a, b):
	slope = (b[1]-a[1])/(b[0]-a[0])
	return [slope, a[1]-slope*a[0]]
def genLine():
	return lineTwoPoints(genPoint(), genPoint())


def evalFunction(l, p):
	if (l[0]*p[0]+l[1]) > p[1]:
		return 1
	else:
		return -1

def sign(x):
	if x > 0.:
		return 1
	if x == 0.:
		return 0
	return -1;

def f(p):
	return sign(p[1] - p[0] + 0.25*sin(pi*p[0]))

totalcounter = 0
totalerror = 0.
iterations = 10000

p = None
y = None
EPS = 0.000001

SVMWin = 0
SVMSupportVecs = 0
failure = 0

runPLA = False

for runs in range(0, iterations):
	if runs % 1000 == 0:
		print runs #tells us where the program is

	p = genPoints(N)
	#p = [[1, 0], [0, 1], [0, -1], [-1, 0], [0, 2], [0, -2], [-2, 0]]

	y = [None]*N
	for x in range(len(p)):
		y[x] = f(p[x])

	clf = svm.SVC( kernel='rbf', coef0=1, C=inf, gamma=1.5 )
	clf.fit(p, y)

	# print clf.n_support_
	# print clf.coef_

	E_in = abs(clf.score(p, y) - 1.0)

	#print E_in

	if abs(E_in) > EPS:
		failure+=1

	vecs = clf.n_support_
	SVMSupportVecs += sum(vecs)

# print float(SVMWin) / float(iterations)

# print float(SVMSupportVecs) / float(iterations)

print float(failure) / float(iterations)


#print "Eout for PLA:", float(totalerror)/float(iterations)