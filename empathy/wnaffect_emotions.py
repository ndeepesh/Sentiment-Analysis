#! /usr/bin/env python
 
#import easy to use xml parser called minidom:
from xml.dom.minidom import parseString
#all these imports are standard on most modern python implementations
 
#download the file:
f = open('wnaffect/a-hierarchy.xml','r')
#convert to string:
data = f.readlines()
#close file because we dont need it anymore:
f.close()
#parse the xml you downloaded

'''
dom = parseString(data)
#retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
xmlTag = dom.getElementsByTagName('tagName')[0].toxml()
#strip off the tag (<tag>data</tag>  --->   data):
xmlData=xmlTag.replace('<tagName>','').replace('</tagName>','')
#print out the xml tag and data in this format: <tag>data</tag>
print xmlTag
#just print the data
print xmlData
'''

#print data

tuples = []

for i in data:
	myString = i 
	mySubString = myString[ myString.find("=")+1: myString.find("/>")]
	tuples.append(mySubString)

for i in range(len(tuples)):
	tuples[i] = tuples[i].replace("="," ")
	tuples[i] = tuples[i].replace('"'," ")
	
# print tuples

f = open('hierarchy.tuples','w')


for i in tuples:
	print >> f, i 
	f.flush()

f.close()
