'''
Yang Hwi Kim
Oct.24, 2017
CSCI-UA 2-002(6162)
'''
#ask the users costs, budget, and number of people coming
budget= float(input('Enter budget for your party: '))
slices= float(input('Cost per slice of pizza: '))
pie= float(input('Cost per whole pizza pie (8 slices): '))
people=int(input('How many people will be attending your party? '))

#ask how many pizza each person wants, using while and for loop
yes=True
total=0
for pizzanumber in range(1, people+1):
    while True:
        slice_person= int(input('Enter number of slices per person #'+ str(pizzanumber)+" "))
        if slice_person>0:
            total+=slice_person
            break
        else:
            print('Not a valid entry, try again!')

#set pie numbers and slice numbers user should get
pienumber= total//8
slicenumber=total%8

#get total cost of pie and slices
total_cost= pienumber*pie + slicenumber*slices

#give total cost, pie and slice number, and leftover budget to the user
if budget>total_cost:
    print('You should purchase', pienumber, 'pies and', slicenumber, 'slices')
    print('Your total cost will be:', total_cost)
    print('You will still have', budget-total_cost, 'lest after your order')
elif budget==total_cost:
    print('You should purchase', pienumber, 'pies and', slicenumber, 'slices')
    print('Your total cost will be:', total_cost)
    print('You will have no money left after your order')
else:
    print('Your order cannot be completed.')
    print('You would need to purchase', pienumber, 'pies and', slicenumber, 'slices') 
    print('This would put you over budget by', total_cost-budget)
        
            
                
            

