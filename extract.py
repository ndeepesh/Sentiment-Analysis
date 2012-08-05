
def extract_score(emotion_word,synset_to_match):    #actual implementation of emotion extraction
     import nltk
     from nltk.corpus import wordnet as wn
     from simplenlp import get_nl

    #emotions=["happy","sad","anger","fear","disgust","surprise"]
     result_score=[]
     
     temp_score=-1
    # temp_emotion=""
     
     our_word_synsets=wn.synsets(emotion_word)
     
     if (len(our_word_synsets)==0):
       temp_score=-100
       #return temp_score
  #   for i in emotions:
   #    syn=wn.synsets(i)
       
     else:
       for our_word_synset in our_word_synsets:
	 if (our_word_synset.pos!=synset_to_match.pos):
	   continue;
	 score=our_word_synset.wup_similarity(synset_to_match)   # have to use better heuristics to find similarity between synsets
         if (score>temp_score):
           temp_score=score
        #   return temp_score
	#   temp_emotion=emotion
         #else:
	 #  return temp_score
       
     return temp_score

     
     
#def test_result(emotion_word):
 #    e=extract(emotion_word)
  #   print emotion_word + " -> (closely related to emotion) -> " + e 
    
        

     

     
     

       
     
     
  
#test_result("fear");