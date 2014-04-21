from numpy import *
from numpy.linalg import *

e = 2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596

def E(u, v):
	return (u*e**v - 2*v*e**(-u))**2

def g(u, v):
	return array([2*(e**v + 2*v*e**(-u))*(u*e**v - 2*v*e**(-u)), 2*(u*e**v - 2*e**(-u))*(u*e**v - 2*v*e**(-u))])\

def gdu(u, v):
	return 2*(e**v + 2*v*e**(-u))*(u*e**v - 2*v*e**(-u))

def gdv(u, v):
	return 2*(u*e**v - 2*e**(-u))*(u*e**v - 2*v*e**(-u))

start = array([1, 1])
n = 0.1
lt = 2*10**(-14)
count = 0

#Gradient Descent
# while ((E(start[0], start[1])) > lt):
# 	old = start
# 	start = old - n*g(old[0], old[1])
# 	count+=1
# 	print count
# 	print start

#Coordinate Descent
for x in range(15):
	old = start
	valx = old[0] - n * gdu(start[0], start[1])
	valy = old[1] - n * gdv(valx, start[1])
	start = array([valx, valy])
	count += 1
	print count
	print start
	print E(start[0], start[1])