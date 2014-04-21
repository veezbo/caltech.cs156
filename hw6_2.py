import urllib
from numpy import *
from numpy.linalg import *

fpin = urllib.urlopen("http://work.caltech.edu/data/in.dta")
fpout = urllib.urlopen("http://work.caltech.edu/data/out.dta")

#Gives us Triples of Data
input = ([map(float,(line.strip('\n').split('\r')[0].split())) for line in fpin])
output = ([map(float,(line.strip('\n').split('\r')[0].split())) for line in fpout])

N = len(input)
p = [None] * N
y = [None] * N

for x in range(N):
	[x1, x2] = [input[x][0], input[x][1]]
	p[x] = [1, x1, x2, x1**2, x2**2, x1*x2, abs(x1 - x2), abs(x1 + x2)]
	y[x] = input[x][2]

X = matrix(p)
k = -1
lamb = 10**k

#Apply Linear Regression (without modified weights)
w = inv(transpose(X)*X + lamb*identity(8)) * transpose(X) * transpose(matrix(y))

print w

#Calculating Ein
diff = 0
for x in range(N):
	first = y[x]
	second = sign((transpose(w) * transpose(matrix(p[x]))).item())
	#print first
	#print second
	if (first != second):
		diff += 1

print "E_in =", float(diff)/float(N)

#Calculating Eout
Nout = len(output)
diffout = 0
for x in range(Nout):
	[x1, x2] = [output[x][0], output[x][1]]
	pout = [1, x1, x2, x1**2, x2**2, x1*x2, abs(x1 - x2), abs(x1 + x2)]
	y = output[x][2]
	ycalc = sign((transpose(w) * transpose(matrix(pout))).item())

	if (ycalc != y):
		diffout += 1

print "E_out =", float(diffout)/float(Nout)