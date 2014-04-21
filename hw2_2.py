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

def calculateFracDiff(y, e):
	size = len(y)
	diff = 0
	eps = .001
	for i in range(size):
		# if (abs(y[i] - e[i])) > eps:
		# 	diff += 1
		if y[i] != e[i]:
			diff += 1
	return float(diff) / float(size)

#Start Program

E = 100
ran = 0
diff = 0.
totalerror = 0.
for x in range(E):

	N = 10

	#Geneate Points
	p = genPoints(N)
	#add the extra zero coordinate
	for i in range(N):
		p[i] = [1] + p[i]

	f = genLine()
	s = [f[1], f[0], -1]

	#Generate the matrix X
	X = matrix(p)

	#print matrix(s).shape
	#print matrix(p[0]).shape

	#Generate the vector y
	y = [None] * N
	for i in range(N):
		#y[i] = evalFunction(f, p[i])
		y[i] = sign((matrix(s) * transpose(matrix(p[i]))).item())
	#print y
	y = matrix(y)
	#print y.shape

	# if x == 0:
	# 	#print p
	# 	# print X
	# 	print pinv(X)
	# 	print y
	# 	print sum(y)
	# 	# print X.shape
	# 	# print y.shape
	# 	# print pinv(X).shape

	#w = inv(transpose(X) * X) * transpose(X) * transpose(y)
	w = pinv(X) * transpose(y)

	w = tolist(w)

	# if x == 0:
	# 	print w
	# 	print s
	# print w
	# print s

	if w[2] == 0.0: #avoid degeneracy case
		continue

	g = [-1.*w[1]/w[2], -1.*w[0]/w[2]]
	ran+=1

	# if x == 0:
	# 	print f
	# 	print g

	# print f
	# print g

	evalf = [None] * N
	evalg = [None] * N
	for i in range(N):
		#evalg[i] = evalFunction(g, p[i])
		evalf[i] = above(matrix(s), matrix(p[i]))
		evalg[i] = above(matrix(w), matrix(p[i]))

	#Calculating Ein
	#fracdiff = calculateFracDiff(tolist(y), evalg)
	fracdiff = calculateFracDiff(evalf, evalg)
	#print "fracdiff: " + str(x) + " " + str(fracdiff)
	diff += fracdiff

	# if x == 0:
	# 	print evalf
	# 	print evalg

	#Estimating Eout
	failed = 0
	gen = 1000
	for i in range(0, gen):
		point = genPoint()
		# if evalFunction(f, point) != evalFunction(g, point):
		# 	failed += 1
		# print matrix(s).shape
		# print matrix(point).shape
		if sign((matrix(s) * transpose(matrix([1]+point))).item()) != sign((matrix(w) * transpose(matrix([1]+point))).item()):
			failed += 1
	error = float(failed)/float(gen)

	totalerror += error


print ran
print diff
print totalerror
print "diff: " + str(float(diff) / float(E))
print "totalerror: " + str(float(totalerror) / float(E))