from numpy import *
from numpy.linalg import *
from sklearn import svm
from sklearn import cluster

N = 100
e = 2.7182818284590
EPS = 0.000001
gammorg = 1.5



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

def normDiffSquared(a, b):
	return (a[0]-b[0])**2+(a[1]-b[1])**2

def f(p):
	return sign(p[1] - p[0] + 0.25*sin(pi*p[0]))

def rbf(p, w, XK):
	total = 0.
	for x in range(len(XK)):
		total += w[x] * e**(-gammorg * normDiffSquared(p, XK[x]))
	return sign(total)

totalcounter = 0
totalerror = 0.
iterations = 100

p = None
y = None
K = 9

SVMWin = 0
SVMSupportVecs = 0
beaten = 0.

E_totinkm = 0.
E_totoutkm = 0.

for runs in range(0, iterations):
	if runs % 10 == 0:
		print runs #tells us where the program is

	p = genPoints(N)

	y = [None]*N
	for x in range(len(p)):
		y[x] = f(p[x])

	pout = genPoints(N)
	yout = [None]*N
	for x in range(len(pout)):
		yout[x] = f(pout[x])


	#Kernel RBF
	clf = svm.SVC( kernel='rbf', coef0=1, C=inf, gamma=gammorg )
	clf.fit(p, y)

	E_inclf = abs(clf.score(p, y) - 1.)
	E_outclf = abs(clf.score(pout, yout) - 1.)

	#Regular RBF
	km = cluster.KMeans( k=K, n_init=1 )
	km.fit(p, y)
	XK = km.cluster_centers_

	phi = [x[:] for x in [[0]*(K+1)]*N]

	for i in range(N):
		phi[i][0] = 1.

	for i in range(N):
		for j in range(0, K):
			phi[i][j+1] = e**(-1*gammorg*(normDiffSquared(p[i], XK[j])))

	#Now calculate the weights
	phi = matrix(phi)
	w = pinv(phi) * transpose(matrix(y))
	
	#And now calculate in and out of sample error
	kmincount = 0.
	kmoutcount = 0.
	for x in range(len(p)):
		if rbf(p[x], w, XK) != y[x]:
			kmincount+=1.
		if rbf(pout[x], w, XK) != yout[x]:
			kmoutcount+=1.

	E_inclf = abs(clf.score(p, y) - 1.)
	E_outclf = abs(clf.score(pout, yout) - 1.)
	E_inkm = kmincount / float(len(p))
	E_outkm = kmoutcount / float(len(p))

	if E_outclf < E_outkm:
		beaten += 1.

	E_totinkm += E_inkm
	E_totoutkm += E_outkm

	# print E_inclf
	# print E_outclf
	# print E_inkm
	# print E_outkm

print float(beaten) / float(iterations)
print "E_inkm:", float(E_totinkm) / float(iterations)
print "E_outkm:", float(E_totoutkm) / float(iterations)


#print "Eout for PLA:", float(totalerror)/float(iterations)