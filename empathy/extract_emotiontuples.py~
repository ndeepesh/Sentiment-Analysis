#! /usr/bin/env python


f = open('X.emotions','r')
X_score = f.readlines()
f.close()

X = []

for i in X_score:
	a = i.split("\t")
	X.append(a[0])

print X 

f = open('patterns.final','r')
patterns = f.readlines()
f.close()

for i in range(len(patterns)):
	patterns[i] = patterns[i].replace("\n", "")

f = open('wn.emotions','r')
Y = f.readlines()
f.close()

for i in range(len(Y)):
	Y[i] = Y[i].replace("\n","")
	
f = open('emotion.tuples', 'w')


for i in range(len(X)):
	for k in range(len(Y)):
		for j in range(len(patterns)):
			SIP = patterns[j].replace("{1}",X[i])
			tup = SIP.replace("{2}",Y[k])
			print >> f, tup
			f.flush()


					

