# routh's stability criterion 
# input: denominator, numerator(optional) ; the transfer function will be in laplace domain.
# output: boolean; True if stable
# logic: calculates the routh array, using routh stability criterion, which consists of row arrays. If 
#        the first element of each array has the same sign, then the system is stable, else not.
# author: K. Srikar Siddarth

import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

def generateRouthArray(den):
	#	an array initially consisting of 2 rows
	r = [[],[]]
	# distributing alternate numbers of the array to row1 and row2 
	for i in range(len(den)):
		r[i%2].append(den[i])

	i=0
	while True:

		if len(r[i])>len(r[i+1]) and r[i][len(r[i])-1]!=0:
			r[i+1].append(0)
		if r[i][len(r[i])-1] == 0:
			r[i].pop()
		if len(r[i])>1:
			r.append([])
		if r[i+1][0]==0:
			den= [a + b for a, b in zip(den + [0], [0]+den)]
			# print(den)
			# break
			return generateRouthArray(den)
		for j in range(len(r[i])-1):
			r[i+2].append((r[i+1][0]*r[i][j+1] - r[i][0]*r[i+1][j+1])/r[i+1][0])
		# print(r[i+1][0], len(r[i+1]))
		if len(r[i])==1:
			break
		i += 1
	return r



def checkStability(den):
	flag = 0
	if den[len(den)-2]==0 and den[len(den)-1]==0:
		print('System Unstable due to multiple poles at origin! Get back to work!')
		return False

	rowArray = generateRouthArray(den)
	print(rowArray)
	for i in range(len(rowArray)-1):
		if rowArray[i][0]*rowArray[i+1][0]<0:
			flag = 1
	if flag ==0:
		print('Stable System! CoolControlEngineer!')
		return True
	else :
		print('System Unstable! Get back to work!')
		return False

# numerator and denominator may be given as input here
num = [1]
# open loop
# den = [1, 12, 49, 78, 40]
# closed loop
# den = [1, 6, 11, 6, 10.1]

#example1
# den = [1, 1, 10, 72, 152, 240]
#example2
# den = [1, 1, 2, 2, 5]
#example3
# den = [1, 2, 11, 18, 18]
def tellme(s):
        print(s)
        plt.title(s, fontsize=16)
        plt.draw()

plt.clf()
# plt.setp(plt.gca(), autoscale_on=False)
# tellme('click to begin')

# plt.waitforbuttonpress()
plt.ion()
plt.show(block=False)
# the output can be collected by this variable result
for i in range(-80 , 80):
	den = [1, 6, 11, 6, i*0.25]
	# result = checkStability(den)

	# confirmation by plotting pole-zero graph on s-plane
	p, z = ctrl.pzmap(ctrl.TransferFunction(num, den), Plot = False, title="when k=10.1" )
	if i==-80:
		t1=plt.plot(p[0].real, p[0].imag, 'k*')
		plt.setp(t1, markersize=24.0, markeredgewidth=2.0)
		t1=plt.plot(p[1].real, p[1].imag, 'k*')
		plt.setp(t1, markersize=24.0, markeredgewidth=2.0)
		t1=plt.plot(p[2].real, p[2].imag, 'k*')
		plt.setp(t1, markersize=24.0, markeredgewidth=2.0)
		t1=plt.plot(p[3].real, p[3].imag, 'k*')
		plt.setp(t1, markersize=24.0, markeredgewidth=2.0)
	if i == 79:
		t1=plt.plot(p[0].real, p[0].imag, 'kx')
		plt.setp(t1, markersize=24.0, markeredgewidth=2.0)
		t1=plt.plot(p[1].real, p[1].imag, 'kx')
		plt.setp(t1, markersize=24.0, markeredgewidth=2.0)
		t1=plt.plot(p[2].real, p[2].imag, 'kx')
		plt.setp(t1, markersize=24.0, markeredgewidth=2.0)
		t1=plt.plot(p[3].real, p[3].imag, 'kx')
		plt.setp(t1, markersize=24.0, markeredgewidth=2.0)
	# print(p)
	t1=plt.plot(p[0].real, p[0].imag, 'bo')
	plt.setp(t1, markersize=12.0, markeredgewidth=2.0)
	t1=plt.plot(p[1].real, p[1].imag, 'ro')
	plt.setp(t1, markersize=12.0, markeredgewidth=2.0)
	t1=plt.plot(p[2].real, p[2].imag, 'go')
	plt.setp(t1, markersize=12.0, markeredgewidth=2.0)
	t1=plt.plot(p[3].real, p[3].imag, 'yo')
	plt.setp(t1, markersize=12.0, markeredgewidth=2.0)
	# plt.draw()

	# plt.pause(0.16)
	# plt.clf()
plt.grid()
plt.savefig('assgn2.png')





