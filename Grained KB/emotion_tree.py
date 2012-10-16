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

#print d["leaf"]


'''
values = list(set(values))

f = open('wn.emotions', 'w')

for i in values:
	print >> f, i 
	f.flush()

f.close()

'''
for i in values:
  if (d.has_key(i)):
     d["root"].search_nodes(name=i)[0].add_child(d[i])


     

f = open('wn.emotions','r')
concept2 = f.readlines()
f.close()

for i in range(len(concept2)):
	concept2[i] = concept2[i].replace("\n","")

  
concept2_grained_path=[]
   
for i in concept2:   
 desired_node=d["root"].search_nodes(name=i)[0]
 path=[]


 while desired_node.up.up:
   path.append(desired_node.name)
   desired_node=desired_node.up.up
 concept2_grained_path.append(path) 
 
print concept2_grained_path