# program just takes a word and checks which emotion it matches the closset

import nltk
from nltk.corpus import wordnet as wn
from simplenlp import get_nl

def extract(emotion_word):                                         #actual implementation of emotion extraction
     emotions=["happy","sad","anger","fear","disgust","surprise"]
     result_score=[]
     
     temp_score=-1
     temp_emotion=""
     
     our_word=wn.synsets(emotion_word)
     
     if (len(our_word)==0):
       temp_emotion="Sorry Nothin  found in WN"
       return temp_emotion
     for i in emotions:
       syn=wn.synsets(i)
       s=syn[0].path_similarity(our_word[0])
       if (s>temp_score):
           temp_score=s
	   temp_emotion=i
       if (temp_score==-1):
	temp_emotion="Not Matched"
     return temp_emotion

     
     
def test_result(emotion_word):        # test function
     e=extract(emotion_word)
     print emotion_word + " -> (closely related to emotion) -> " + e 
    
        

     

     
     

       
     
     
  
test_result("fear");