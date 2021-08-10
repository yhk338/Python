'''
Yang Hwi Kim
Oct.5, 2017
CSCI-UA 2-002(6162)
'''

import random

#ask the user for the number of side on their dice
while True:
    sides= int(input("Enter sides - 4, 6, 8, 10, 12, or 20: "))
    if sides== 4 or sides==6 or sides==8 or sides==10 or sides==12 or sides==20:
        break
    else:
        print('Bad user, try again')
               

#keep track of roll
roll=0

#keep track of doubles
double=0

#keep track of total
total_die1=0
total_die2=0

#compare them - are they snakeeyes? if so, stop rolling
while True:
    #once this data is good, we can continue to the rolling phase     
    # roll two dice of this size
    die1= random.randint(1, sides)
    die2= random.randint(1, sides)
    roll+= 1

    #print them out
    print('Die 1 was', die1, 'and die 2 was', die2)
    print()

    total_die1= total_die1+ die1
    total_die2= total_die2+ die2

    #See how many times the user rolled double
    if die1== die2:
        double+=1
    percent= double/roll*100
    average1= total_die1/ roll
    average2= total_die2/ roll
        
    if die1== 1 and die2 ==1:
        #all done, report to user
        print('You got snake eyes! On try number', roll,  '.')
        print ('Along the way, you rolled doubles', double, 'times.(', format(percent, '.2f'), '% of all rolles were double)')
        print('The average roll for die #1 is', format(average1, '.2f'))
        print('The average roll for die #2 is', format(average2, '.2f'))
        break
    
        
 


