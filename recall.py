#!/usr/bin/python

import re

new1=[];
new2=[];

    

d1={};d2={};
temp='';

h=open('newoutput2.HasProperty');                        #reading the database
m=h.readlines();
h.close();
m.sort();                            # sorting them as relations were not ordered
new3=[];

for a in range(len(m)):
    start=m[a].index('(');                  # geting the index of '(',',',')'......ex from HasProperty(apple,red).....extrated result in new3 will be apple,red
    mid=m[a].index(',');
    end=m[a].index(')');
    new3.append(m[a][start+1:end]);
    if (m[a][start+1:mid] != temp):                     #the building phase of Hash Join....where we compare first element (ex: apple) with a temp var
      d1[m[a][start+1:mid]]=1;                 # if not found in temp...we mark it (apple) in d1 dictionary (we dothis because...we have tuples like - (apple,red) and (apple,sweet))
      d2[m[a][mid+1:end]]=1;                   # similarly we mark next element (ex. red) in d2 dictionary  (second element is unique)
      temp=m[a][start+1:mid];
    else:
       d2[m[a][mid+1:end]]=1;
    
#print new3; 
 
 
op=[];



h=open('sorted-conceptnet.txt');
m=h.readlines();
h.close();
m.sort();


#for i in range(len(m)):
 # if new2[0] == new3[0]:
 #print "y";
#else:
 #print "n";
  
for i in range(len(m)):
 match=re.match('HasProperty',m[i]);               # matching with RE.....WE WILL UPDATE THIS TO simple STRING MATCHING
 if match:
  new1.append(m[i]);
    
    
for a in range(len(new1)):
    start=new1[a].index('(');
    mid=new1[a].index(',');
    end=new1[a].index(')');
    new2.append(new1[a][start+1:end]);
    if (d1.has_key(new1[a][start+1:mid])):                      # to match if the tuple matches...we check for entries of both elementsi.e apple and red in our d1 and d2 dictionaries
      if (d2.has_key(new1[a][mid+1:end])):
	op.append(new2[a]);
   
    


#print new2[0];


print len(op);






	









   




 #for a in range(len(m)):
   # start=m[a].index('(');
    #end=m[a].index(')');
   # new.append(m[a][start+1:end]);
   # a=a+1;
  
  

#start=m[0].index('(');
#end=m[0].index(')');
  
#new.append(m[0][start:end+1]);

 
 #print new;


#new.append('HasProperty(chicken,allowed)');
#new.append('HasProperty(chicken,bought)');

