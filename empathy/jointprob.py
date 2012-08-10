#! /usr/bin/env python

import MicrosoftNgram
#from conceptnet.models import *
from simplenlp import get_nl

en_nl = get_nl('en')


s = MicrosoftNgram.LookupService(model='urn:ngram:bing-body:apr10:5')


sent = "I have had a pretty crazy weekend"
ans = en_nl.lemma_split(sent)


print ans
