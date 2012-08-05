import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize


#list chunks[][] = set of chunks
#list q[][]-> the previous running instance's of p

# list of all patterns n(noun),nn(noun noun),an(adjective noun),npn(noun preposition noun),a(adjective),aa(adjective adjective)
our_p=["n","nn","an","npn","a","aa"]

# 2-D list with the pattern as -> [pattern,chunk,chunk....],[pattern,chunk,chunk....],.....
chunks=[["n"],["nn"],["an"],["npn"],["a"],["aa"]]

# list containing all the reg expressions of the patterns 
patterns=["n:{<NN>}","nn:{<NN><NN>}","an:{<JJ><NN>}","npn:{<NN><PRP><NN>}","a:{<JJ>}","aa:{<JJ><JJ>}"]


# For now the program is only for a sentence....not for the corpus
sen="He is driving a red car";

# list with all words along with their pos tags
pos_tags=pos_tag(word_tokenize(sen))


# iterate over all patterns
for i in patterns:
  patt=i
  par=nltk.RegexpParser(patt)
  result=par.parse(pos_tags)
  for n in result:
    if isinstance(n, nltk.tree.Tree):   # checking if the leaves of root(S) are trees or not
      for i in range(len(our_p)):       # if a subtree is found we iterate over the number of patterns 
	if n.node == our_p[i]:          # matching a node with our pattern...we gave name to each regular expression
	  c=""                          # initializing a temp. variable with NULL string 
          for j in range(len(n)):       # iterating over the number of leaves of the subtree
	    c=c + " " + n[j][0]         # concatinating the words ex. (red,JJ),(car,NN) -> red car
	  chunks[i].append(c)
	  
#    else:
 #     print "No Chunks"

  

print chunks         # pattern of result -> (pattern,chunk,chunk..),(pattern,chunk,chunk..)
  
  
  #extraction of chunks
 # p[i].append(#chunks)
  
#save to an external file
#for i in p:
#  for j in p[i]:
 #   for k in q[i]:
  #    for l in q[j]:
#	if(p[i][j] != q[k][l]):
#	  new.append(p[i][j])

  