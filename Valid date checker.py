'''
Yang Hwi Kim
Oct. 31, 2017
CSCI-UA 2-002(6162)
'''

# a is for month and b is for the date
def valid_date(a,b):
    #The first thing to validate, if month is negative or bigger than 12, it's false
    if a<=0 or a>12:
        return False
    #rest of them goes to else
    else:
        #if month is filtered, go to date. If date is negative or larger than 31, it's false
        if b<=0 or b>31:
            return False
        #rest of them goes to else
        else:
            #Last day of February is 28th, so larger than 28 is false.
            if a==2:
                if b>28:
                    return False
                else:
                    return True
            #Also, last day of April, June, September, and November is 30th, so bigger than 30 is false
            else:           
                if a==4 or a==6 or a==9 or a==11:
                    if b>30:
                        return False
                    else:
                        return True
                #rest after filtering is all true
                else:
                    return True
                
                    
            

print (valid_date(99,1)) # False
print (valid_date(1,99)) # False
print (valid_date(99,99)) # False

print (valid_date(-99,1)) # False
print (valid_date(1,-99)) # False
print (valid_date(-99,-99)) # False

print (valid_date(9,25)) #True
print (valid_date(10,15)) # True
print (valid_date(11,31)) # False
print (valid_date(2,28)) # True
print (valid_date(2,29)) # False
