#! /usr/bin/env python

import nltk

f = open('patterns.emotions','r')
patterns = f.readlines()
f.close()

for i in range(len(patterns)):
	patterns[i] = patterns[i].replace("\n","")

print patterns

patterns_final = []



for i in range(len(patterns)):
	b = nltk.word_tokenize(patterns[i])
	print b
	print len(b)
	if( len(nltk.word_tokenize(patterns[i]) )  == 8 or len(nltk.word_tokenize(patterns[i]) )  == 9 ) :
		patterns_final.append(patterns[i])

#print patterns_final

f = open('patterns.final','w')

for i in patterns_final:
	print >> f, i 
	f.flush()

f.close() 

