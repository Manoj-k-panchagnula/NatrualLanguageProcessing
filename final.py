'''
Created on Nov 20, 2016

@author: manoj
'''
import re 
import nltk
from collections import Counter
def create_model(path):
    token = re.sub('[^a-zA-Z0-9]',' ',path)
    token = token.lower()
    token = token.split()
    return token

def pos_tagger(token):
    a = nltk.pos_tag(token)
    counts = Counter(tag for word,tag in a )
    return counts

path1 =raw_input('Enter the first text:')
path2 =raw_input('Enter the second text:')
Text1 = create_model(path1)
Text2 = create_model(path2)
Text_similarity = set(Text1) & set(Text2)

print 'The similar words in the given sentences are:', Text_similarity
a = len(Text1)
b = len(Text2)
c = len(Text_similarity)*2
x = float(c) / float(a + b)
y = x * 5.0
print "Similarity of texts w.r.to common words in the given texts is: %f " % y
t1 = pos_tagger(Text1)
t2 = pos_tagger(Text2)

noun_1 = t1['NN'] + t1['NNS'] + t1['NNP'] + t1['NNPS']
noun_2 = t2['NN'] + t2['NNS'] + t2['NNP'] + t2['NNPS']
verb_1 = t1['VB'] + t1['VBZ'] + t1['VBP'] + t1['VBN']
verb_2  = t2['VB'] + t2['VBZ'] + t2['VBP'] + t2['VBN']
adj_1 = t1['JJ'] + t1['JJR'] + t1['JJS'] + t1['NN'] + t1['NNS'] + t1['NNP'] + t1['NNPS'] + t1['VB'] + t1['VBZ'] + t1['VBP'] + t1['VBN']
adj_2 = t2['JJ'] + t2['JJR'] + t2['JJS'] + t2['VB'] + t2['VBZ'] + t2['VBP'] + t2['VBN'] + t2['NN'] + t2['NNS'] + t2['NNP'] + t2['NNPS']
number_1 = t1['CD']
number_2 = t2['CD']
c1 = noun_1+noun_2
c2 = verb_1+verb_2
c3 = adj_1+adj_2
c4 = number_1+number_2

def Similarity(pos1,pos2):
    if pos1 > pos2:
        result = float(pos2)/float(pos1) * 5.0
    else:
        result = float(pos1)/float(pos2) * 5.0
    return result

if c1>0:
    noun_sim = Similarity(noun_1,noun_2)
    print "Similarity of texts w.r.to nouns is: %f" % noun_sim 
if c2>0:
    verb_sim = Similarity(verb_1,verb_2)
    print "Similarity of the texts w.r.to verbs is: %f"% verb_sim
if c3>0:
    adj_sim = Similarity(adj_1, adj_2) 
    print "Similarity of the texts w.r.to verbs,nouns and adjectives is: %f"% adj_sim 
if c4>0:
    number_sim = Similarity(number_1, number_2)
    print "Similarity of numbers present in the given text is: %f" %number_sim   