'''
Yang Hwi Kim
Dec. 07, 2017
CSCI-UA 2-002(6162)
'''
import time
import urllib.request
url='https://cs.nyu.edu/~kapp/courses/cs0002fall2017/assignments/assignment10/movie_reviews.txt'
request=urllib.request.urlopen(url)
data=request.read().decode('utf-8')
#split reviews

#split up the file based on line break
split_file=data.split('\n')
word = str.lower (input ("Enter a word to test: "))    

#set up a sentiment dictionary
sentiment={}
#examine every line in file
for line in split_file:
    lines=line.lower()
    #cut up the string for the line
    split_line=lines.split(' ')
    #for this record, grab the score
    score=int(split_line[0])
    #examine every word in this review
    if word in split_line:
        if word not in sentiment:
            #add it!
            sentiment[word]=[score, 1] 
        if word in sentiment:
            sentiment[word][0]+=score
            sentiment[word][1]+=1
average=sentiment[word][0]/sentiment[word][1] 
if average==2:
    classif='neutral'
elif average>=0 and average<2:
    classif='negative'
elif average>2 and average<=4:
    classif='positive'
                                           

if word not in sentiment:
    print('There is no average score for reviews containing the word', word)
    print('Cannot determine if this word is positive or negative')

else:
    print(word, 'appears', sentiment[word][1], 'times')
    print("The average score for reviews containing the word", "'"+word+"'", "is", average)
    print('This is a', classif, 'word')
 
            
