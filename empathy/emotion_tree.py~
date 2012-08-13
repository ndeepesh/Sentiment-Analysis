#! /usr/bin/env python

#from collections import defaultdict
from ete2 import Tree


f = open('hierarchy1.tuples','r')
tuples_list = f.readlines()
f.close()

tuples = []

for i in tuples_list:
	if( i != "\n"):
		tuples.append(i[1:-2])

for i in range(len(tuples)):
	tuples[i] = tuples[i].replace("\n","")

#print tuples



keys = []
values = []


for i in tuples:
	a = i.split("  ")
	keys.append(a[2])
	values.append(a[0])	


#print keys
#print values

keys_set = list(set(keys))

d = {}

for i in keys_set:
	d[i] = Tree()
'''	
for i in d:
	print i 
'''

for i in range(len(keys)):
	a = keys[i]
	d[a].add_child( name=values[i])

print d["root"]


