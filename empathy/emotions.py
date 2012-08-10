#! /usr/bin/env python

f = open('emotionlists_wordnet.txt','r')
all_emo = f.read()
f.close()

emotions = []

split_comma = all_emo.split(",")

#print split_comma

emotion = []

for i in split_comma:
	myString = i
	mySubString = myString[ myString.find("('")+1 : myString.find(".") ]
	if  '[' not in mySubString :
		emotion.append( mySubString[1:] )
	

print emotion

emotion = list(set(emotion))

emotion.sort()

f = open('emotions.list','w')

for i in emotion:
	print >>f, i 
	f.flush()

f.close()
