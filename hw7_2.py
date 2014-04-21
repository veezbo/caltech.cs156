import urllib
from numpy import *
from numpy.linalg import *

fpin = urllib.urlopen("http://work.caltech.edu/data/in.dta")
fpout = urllib.urlopen("http://work.caltech.edu/data/out.dta")

#Gives us Triples of Data
input = ([map(float,(line.strip('\n').split('\r')[0].split())) for line in fpin])
output = ([map(float,(line.strip('\n').split('\r')[0].split())) for line in fpout])

V = 25
N = 10
pV = [None] * V
yV = [None] * V
p = [None] * N
y = [None] * N

for x in range(V+N):
	[x1, x2] = [input[x][0], input[x][1]]
	#pp = [1, x1, x2, x1**2, x2**2, x1*x2, abs(x1 - x2), abs(x1 + x2)]
	pp = [1, x1, x2]
	yy = input[x][2]

	if x < V:
		pV[x] = pp
		yV[x] = yy
	else:
		p[x-V] = pp
		y[x-V] = yy

X = matrix(p)

#Apply Linear Regression
w = pinv(X) * transpose(matrix(y))

#print w

#Check Validation
E_val = 0
for x in range(V):
	first = yV[x]
	second = sign((transpose(w) * transpose(matrix(pV[x]))).item())
	if first != second:
		E_val += 1

print "E_val:", float(E_val) / float(V)


#Calculate E_out
Nout = len(output)
diffout = 0
for x in range(Nout):
	[x1, x2] = [output[x][0], output[x][1]]
	#pout = [1, x1, x2, x1**2, x2**2, x1*x2, abs(x1 - x2), abs(x1 + x2)]
	pout = [1, x1, x2]
	y = output[x][2]
	ycalc = sign((transpose(w) * transpose(matrix(pout))).item())

	if (ycalc != y):
		diffout += 1

print "E_out:", float(diffout) / float(Nout)
