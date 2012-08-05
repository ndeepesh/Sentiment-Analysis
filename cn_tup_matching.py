
# MAIN file where all main logic behind keyword spotting to find some emotive ConceptNet Tuples
import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from conceptnet.models import *

from actual import get_synsets_for_matching
from get_correct_pos import matching_pos
from extract import extract_score

en=Language.get('en')
cn_tuples=Assertion.objects.filter(language=en)  # getting all conceptnet tuples

base_synsets={}
base_synsets=get_synsets_for_matching()   # all synsets with which we map our conceptnet tuples

emotions={'happy','sad','anger','disgust','surprise','fear'}

result_list={}   # contains the result indexed by emotion
h=[];sa=[];a=[];d=[];s=[];f=[];n=[]
result_list['happy']=h
result_list['sad']=sa
result_list['anger']=a
result_list['disgust']=d
result_list['surprise']=s
result_list['fear']=f
result_list['neutral']=n


for cn_tuple in cn_tuples:          # looping over all tuples
  concept1_text=Concept.objects.filter(language=en,id=cn_tuple.concept1_id)[0].text  # getting concept1 text
  concept2_text=Concept.objects.filter(language=en,id=cn_tuple.concept2_id)[0].text  # getting concept2 text
# getting concept1 tokenized and assiging to each word POS  ...???? COULD WE USE A BETTER POS Tagger
  con1_pos_tags=pos_tag(word_tokenize(concept1_text))   
  con2_pos_tags=pos_tag(word_tokenize(concept2_text))
  
  # looping with each word 
  for i in range(len(con2_pos_tags)):
    pos=matching_pos(con2_pos_tags[i][1])  # correcting POS ..example 'NN' to 'n'....
    if (pos == ""):
      continue;
    score=0;temp_emo="neutral"
    for emo in emotions:              # looping over each emotion
      for syn in base_synsets[emo][pos]:   #looping over every synset with specifed emotion and POS....
	temp_score=extract_score(con2_pos_tags[i][0],syn)   # get score
	# just getting the higest score for that word and the corresponding emotion
	if (temp_score>score):
	  score=temp_score
	  temp_emo=emo
	  main_syn=syn
	  word=con2_pos_tags[i][0]
	  
	  # for now limit is 0.13.....??? FURTHUR IMPROVEMENT
    if (score>0.13):
     result_list[temp_emo].append(cn_tuple)
     print main_syn
     print 'word->' + ' ' + word + '  ' + 'emotion' + '->  ' + temp_emo + '  ' + 'concept->' + ' ' + concept2_text + '\n'
     break;

    
	  
	
    
#print result_list

    	
    

