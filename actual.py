# keyword spotting with conceptnet conceptsss....!!

def get_synsets_for_matching():
  from nltk.corpus import wordnet as wn 
  

  
  emotions={'happy','sad','anger','disgust','surprise','fear'}
  p_speech={'n','v','a','r'}

  happy_dict={};sad_dict={};anger_dict={};disgust_dict={};surprise_dict={};fear_dict={}
  emotion_dict={}

  emotion_dict['happy']=happy_dict
  emotion_dict['sad']=sad_dict
  emotion_dict['anger']=anger_dict
  emotion_dict['disgust']=disgust_dict
  emotion_dict['surprise']=surprise_dict
  emotion_dict['fear']=fear_dict


  h_n=[];h_v=[];h_a=[];h_r=[];sa_n=[];sa_v=[];sa_a=[];sa_r=[];a_n=[];a_v=[];a_a=[];a_r=[];d_n=[];d_v=[];d_a=[];d_r=[];s_n=[];s_v=[];s_a=[];s_r=[];f_n=[];f_v=[];f_a=[];f_r=[]

  happy_dict['n']=h_n
  happy_dict['v']=h_v
  happy_dict['a']=h_a
  happy_dict['r']=h_r

  sad_dict['n']=sa_n
  sad_dict['v']=sa_v
  sad_dict['a']=sa_a
  sad_dict['r']=sa_r

  anger_dict['n']=a_n
  anger_dict['v']=a_v
  anger_dict['a']=a_a
  anger_dict['r']=a_r

  disgust_dict['n']=d_n
  disgust_dict['v']=d_v
  disgust_dict['a']=d_a
  disgust_dict['r']=d_r

  surprise_dict['n']=s_n
  surprise_dict['v']=s_v
  surprise_dict['a']=s_a
  surprise_dict['r']=s_r


  fear_dict['n']=f_n
  fear_dict['v']=f_v
  fear_dict['a']=f_a
  fear_dict['r']=f_r


  
  for emo in emotions:
    for pos in p_speech:
      synset=wn.synsets(emo,pos)
      for syn in synset:
        our_pos=syn.pos
        if (our_pos == 's'):
	  our_pos='a'
        emotion_dict[emo][our_pos].append(syn)
        syn_hypernyms=syn.hypernyms()
        for syn_hypernym in syn_hypernyms:
          pos_1=syn_hypernym.pos
          if (pos_1 == 's'):
	    pos_1='a'
          emotion_dict[emo][pos_1].append(syn_hypernym)
        lemmas=syn.lemmas
        for lemma in lemmas:
	  der_rel_forms=lemma.derivationally_related_forms()
	  for form in der_rel_forms:
	    base_synset=form.synset
	    base_pos=base_synset.pos
	    if (base_pos == 's'):
	      base_pos='a'
	    if base_synset in emotion_dict[emo][base_pos]:
	      continue;
	    else:
	      emotion_dict[emo][base_pos].append(base_synset)

  return emotion_dict    
	 
#print emotion_dict['fear']



    
    
  
