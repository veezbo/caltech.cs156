from numpy import *
from numpy.linalg import *
from sklearn import svm

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

totalcounter = 0
totalerror = 0.
iterations = 100

p = None
f = None
y = None

SVMWin = 0
SVMSupportVecs = 0

runPLA = False

for runs in range(0, iterations):
	if runs % 10 == 0:
		print runs #tells us where the program is
	p = genPoints(N)
	f = genLine()

	y = [None]*N
	for i in range(0, N):
		y[i] = evalFunction(f, p[i])

	w = array([0, 0, 0])

	counter = 0
	while True:

		yn = [None]*N
		missed = []
		for i in range(0, N):

			yn[i] = sign(dot(w, array([1]+p[i])))
			
			if yn[i] != y[i]:
				missed.append(i)
		#Breaks when there are no misclassified points
		if len(missed) == 0:
			break

		counter+=1
		ind = missed[random.randint(0, len(missed))]

		xn = array([1]+p[ind])
		w = w + y[ind]*xn


	totalcounter += counter

	#Now generate the function g from the weights
	g = [-1.*w[1]/w[2], -1*w[0]/w[2]]

	failed = 0.
	gen = 2000
	for i in range(0, gen):
		point = genPoint()
		if evalFunction(f, point) != evalFunction(g, point):
			failed+=1.
	error = failed/gen

	totalerror += error

	# print "PLA error:", error

	clf = svm.SVC( kernel='linear', C=1.0E6 )
	clf.fit(p, y)

	# print clf.n_support_
	# print clf.coef_

	pout = genPoints(1000)
	yout = [None] * 1000
	for x in range(1000):
		yout[x] = evalFunction(f, pout[x])

	score = clf.score( pout, yout )
	e_out = abs(score - 1.0)

	# print "SVM error:", e_out, "\n"
	if e_out < error:
		SVMWin += 1

	vecs = clf.n_support_
	SVMSupportVecs += sum(vecs)

print float(SVMWin) / float(iterations)

print float(SVMSupportVecs) / float(iterations) 


#print "Eout for PLA:", float(totalerror)/float(iterations)