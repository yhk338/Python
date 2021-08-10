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

#split up the file based on line break
split_file=data.split('\n')

#split reviews
before=time.time()
phrase=str.lower(input('Enter the phrase: '))
words=phrase.split(' ')

#set up a sentiment dictionary
sentiment={}
#examine every line in file
for line in split_file:
    #cut up the string for the line
    split_line=line.split(' ')
    #for this record, grab the score
    score=int(split_line[0])
    #examine every word in this review
    for i in range(1, len(split_line)):
        #grab this word
        #word should be lower case#####
        word=str.lower(split_line[i])
        #is this word a new one?
        if word not in sentiment:
            #add it!
            sentiment[word]=[score, 1]
        else:
            sentiment[word][0]+=score
            sentiment[word][1]+=1
after=time.time()
print('Initializing sentiment database')
print('Sentiment database initilization complete')
print('Total unique words analyzed:', len(sentiment))
print('Analysis took', after-before, 'seconds to complete') 
print()           

scores=0
for i in words:
    if i not in sentiment:
        print(i, 'does not appear in any moview reviews')
        print('Not enough words to determine sentiment.')
    else:
        average=sentiment[i][0]/sentiment[i][1]
        print(i, 'appears', sentiment[i][1], 'times with average score of', average)
        scores+=average
aver_score=scores/len(words)

print('Average score for this phrase is:', aver_score)
if aver_score==2:
        classif='neutral'
elif aver_score>=0 and aver_score<2:
        classif='negative'
elif aver_score>2 and aver_score<=4:
        classif='positive'
print('This is', classif)

