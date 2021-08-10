'''
Yang Hwi Kim
Sep.21, 2017
CSCI-UA 2-002(6162)
'''
#set two numbers by asking each value
num1=int(input("Enter value 1: "))
num2=int(input("Enter value 2: "))
print("")

#print the statement about value totals
print("Place Value Totals: ")
print("")

#ones digit is by dividing the value by 10
ones1= num1%10
ones2=num2%10

#tens digit is by getting the remaining number by dividing it by 100 and then dividing the rest by 10
tens1=(num1%100)//10
tens2=(num2%100)//10

'''
hundreds digit is by diving the number by 1000 and get the remainder, and then divide by 100
agian and get the integered result
'''
hunds1=(num1%1000)//100
hunds2=(num2%1000)//100

#thousands digit is by dividing the number by 1000 and get the integer without the remainder
thous1=(num1//1000)
thous2=(num2//1000)

#If each digit is set, add same digits together
oness=ones1+ones2
tenss=tens1+tens2
hundss=hunds1+hunds2
thouss=thous1+thous2

#print each digit and the added value
print(ones1, "+", ones2, "=", oness, "one(s)")
print(tens1, "+", tens2, "=", tenss, "ten(s)")
print(hunds1, "+", hunds2, "=", hundss, "hundred(s)")
print(thous1, "+", thous2, "=", thouss, "thousand(s)")




           
