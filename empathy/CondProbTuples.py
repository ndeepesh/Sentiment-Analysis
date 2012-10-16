#! /usr/bin/env python

import MicrosoftNgram

s = MicrosoftNgram.LookupService(model='urn:ngram:bing-body:apr10:5')
 
f = open('emotion.tuples', 'r')
tuples = f.readlines()
f.close()

for i in range(len(tuples)):
	tuples[i] = tuples[i].replace("\n","")
	tuples[i] = tuples[i].replace("  "," ")

f = open('EmotionTuples.Prob', 'w')

for i in tuples:
	try:
		prob = s.GetConditionalProbability(i)
		print >> f, i , "\t", prob 
		f.flush()
	except:
		continue
f.close()
