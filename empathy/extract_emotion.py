#! /usr/bin/env python

from conceptnet.models import *

en = Language.get('en')


f = open('patterns.emotions','w')
f1 = open('seeds.emotions','w')
f2 = open('relations.emotions','w')

relations = []
patterns = []

raw = []

basic_emotions = ['happy','sad','anger','fear','disgust','surprise']


for i in basic_emotions:
	assertions = Assertion.objects.filter(concept2__text= i , language=en)

	for a in assertions:
		raw.extend(a.rawassertion_set.all())
	for r in raw:
		print >> f1, r.nl_repr()
		f1.flush()
		patterns.append(str(r.frame))
		relation = str(r.assertion)
		relations.append( relation[0: relation.find("(")] ) 

f1.close()

patterns = list(set(patterns))
patterns.sort()

for i in range(len(patterns)):
	patterns[i] = patterns[i].replace("(en)","")
	print >> f, patterns[i]
	f.flush()

f.close()

relations = list(set(relations))
relations.sort()

for i in relations:
	print >> f2, i
	f2.flush()

f2.close()
