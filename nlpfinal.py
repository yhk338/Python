'''
Created on 2020. 4. 28

@author: Tracy Kim
Citing from https://towardsdatascience.com/basic-binary-sentiment-analysis-using-nltk-c94ba17ae386

'''
import nltk
from nltk.corpus import stopwords, words
from nltk.text import Text
from nltk import sent_tokenize, word_tokenize, pos_tag
import string, re
import csv
import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify.scikitlearn import SklearnClassifier

all_words = []
documents = []

stop_words = list(set(stopwords.words('english')))

#  j is adjective
allowed_word_types = ["J"]

f = open("positive.txt", "r")
for p in f:
    #print(x)
    
    # create a list of tuples
    documents.append( (p, "pos") )
    # remove punctuations
    cleaned = re.sub(r'[^(a-zA-Z)\s]','', p)
    
    # tokenize 
    tokenized = word_tokenize(cleaned)
    
    # remove stopwords 
    stopped = [w for w in tokenized if not w in stop_words]
    
    # parts of speech tagging for each word 
    postag = nltk.pos_tag(stopped)
    # make a list of  all adjectives 
    for w in postag:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

f = open("negative.txt", "r")   
for p in f:
    # create a list of tuples where the first element of each tuple is a review
    # the second element is the label
    documents.append( (p, "neg") )
    
    # remove punctuations
    cleaned = re.sub(r'[^(a-zA-Z)\s]','', p)
    
    # tokenize 
    tokenized = word_tokenize(cleaned)
    
    # remove stopwords 
    stopped = [w for w in tokenized if not w in stop_words]
    
    # parts of speech tagging for each word 
    neg = nltk.pos_tag(stopped)
    
    # make a list of  all adjectives identified by the allowed word types list above
    for w in neg:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())


all_words = nltk.FreqDist(all_words)

# listing the 1500 most frequent words
freq = list(all_words.keys())[:1500]
print(freq[2:15])
# function to create a dictionary of features
def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in freq:
        features[w] = (w in words)
    return features

# Creating features for each review
featuresets = [(find_features(rev), category) for (rev, category) in documents]
import random

random.shuffle(featuresets)
print("lenght", len(featuresets))
testing_set = featuresets[0:300]
training_set = featuresets[301:]

classifier = nltk.NaiveBayesClassifier.train(training_set)

print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)


classifier.show_most_informative_features(15)

'''
csvfile = open("dev.csv", errors = 'ignore')
reader = csvfile.read()
import string
from textblob import TextBlob
with open('dev.csv', errors='ignore') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    data1 =[]
    data3=[]
    for row in readCSV:
        
        data1.append(row)
        #blob = TextBlob(data3)
        
        #data.remove(data[0][-1])
        
        #tokenized_sents = [word_tokenize(i) for i in data]
data2=[]
for i in data1:
    data2.append(i[-1])
    del i[-1]

#print (data1)
result = np.vstack((data1, data2)).T
#print(result[0])
#from nltk.corpora import wordnet as wn
nouns = set()
for j in range(len(result)):
    tokenized_sents = [word_tokenize(i) for i in result[j][0]]
    result[j][0] = tokenized_sents
    
#print(result[0][1])

from nltk.corpus import brown
jj = {word for word, pos in brown.tagged_words() if pos.startswith('JJ')}
#print(jj)
document =[]

if result[0][1]== 'positive':
    for p in result:
        for i in p[0]:
            for s in i:
                document.append((s, "pos"))
if result[0][1]== 'negative':
    for p in result:
        for i in p[0]:
            for s in i:
                document.append((s, "neg"))      
        
print(document)
import random 
random.shuffle(document)
all_wordsss = nltk.FreqDist(jj)
all_words = nltk.FreqDist(document)

word_features = list(all_words.keys())[:700]


def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

featuresets = [(find_features(rev), category) for (rev, category) in document]

random.shuffle(featuresets)
#print(find_features(document))

testing_set = featuresets[1500:]
training_set = featuresets[:1501]

classifier = nltk.NaiveBayesClassifier.train(training_set)

print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set)))

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)
classifier.show_most_informative_features(15)


with open('positive.txt', errors='ignore') as csvfile:
    readCSV = txt.reader(csvfile, delimiter=',')
    data1 =[]
    data3=[]
    for row in readCSV:
'''