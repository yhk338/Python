'''
Yang Hwi Kim
Oct.5, 2017
CSCI-UA 2-002(6162)
'''

#ask the user the number to choose
#Lead the user to choose number between 10 and 100
#Indicate that the number user chose is too small or big
while True:
    sticks=int(input('How many sticks (10-100)?'))
    if 10>sticks:
        print("Sorry, that's too few sticks. Try again.")
    elif sticks>100:
        print("Sorry, that's too many sticks. Try again.")
    else:
        print("Great, let's play...")
        break
    
#ask the user how many sticks he or she wants to take
#use while loop to repeat the question until the end
#set two players
while True:
    turn=1
    while turn==1:
        print('Turn: player', turn) 
        print('There are', sticks, 'sticks on the table.')
        numbers=int(input('How many sticks do you want to take (1, 2 or 3)?'))
        print('')
       
    #if the user choose too big number, lead the user to choose smaller number
    #if the user choose other than 1, 2, or 3, ask the user to choose one of them
    #finish the game once the sticks reaches 0
        if numbers>sticks:
            print("Sorry, that's not a valid number.")
        elif numbers ==1 or numbers ==2 or numbers==3:
            sticks-=numbers
            turn+=1
        else: 
            print("Sorry, that's not a valid number.")
    #let the user know player 1 won
    if sticks==0:
            print("There are no sticks left on the table!  Game over.")
            print('Player 1 wins!')
            break
    #put player 2 while looping
    while turn==2:
        print('Turn: player', turn) 
        print('There are', sticks, 'sticks on the table.')
        numbers=int(input('How many sticks do you want to take (1, 2 or 3)?'))
        print('')
       
    #if the user choose too big number, lead the user to choose smaller number
    #if the user choose other than 1, 2, or 3, ask the user to choose one of them
    #finish the game once the sticks reaches 0
        if numbers>sticks:
            print("Sorry, that would bring the total # of sticks below 0. Try again.")
        elif numbers ==1 or numbers ==2 or numbers==3:
            sticks-=numbers
            turn-=1
        else: 
            print("Sorry, that's not a valid number.")
    #let the user know player 2 won
    if sticks==0:
            print("There are no sticks left on the table!  Game over.")
            print('Player 2 wins!')
            break

    
    
