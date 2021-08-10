'''
Yang Hwi Kim
Nov. 28, 2017
CSCI-UA 2-002(6162)
'''
# product lists
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_stock= [10, 5, 20]

while True:
    name=input('(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ')
    if name=='q':
        print('See you soon!')
        break
    elif name=='s':
        product=input('Enter the product name: ')
        if product in product_names:
            location=product_names.index(product)
            cost=product_costs[location]
            stock=product_stock[location]
            print(product, 'at', cost, 'per unit')
            print('We currently have', stock, 'in stock')
        else:
            print('Sorry, not valid')
    elif name=='l':
        print(format('product','<15'),format('price','<7'),format('quality','<10'))
        for i in product_names:
            nal=product_names.index(i)
            print(format(i, '<15'), format(product_costs[nal],'<7'), format(product_stock[nal], '<10'))
    elif name=='a':
        
        newproduct=input('Enter the new product name: ')
        if newproduct in product_names:
            print('Sorry, you already sell that product. Try again')
        else:
            product_names+=[newproduct]
            while True:
                newcost=float(input('Enter a product cost: '))
                if newcost>0:
                    product_costs+=[newcost]
                    break
                else:
                    print('Invalid cost. Try again')
            while True:
                productnum=int(input('How many of these products do we have?'))
                if productnum<=0:
                    print('Invalid quantity. Try again.')
                else:
                    product_stock+=[productnum]
                    print('Product added!')
                    break
    elif name=='r':
        
        while True:
            name=input('Enter the product name: ')
            if name not in product_names:
                print("Product doesn't exist. Can't remove")
            else:
                product_names.remove(name)
                break
    elif name=='u':
        prod = input("Enter a product name: ")
        if prod not in product_names:
            print("Product doesn't exist. Can't update")
            print()
        # If the name is in the list, use index to find which index in the list
        
        else:
            prod_index = product_names.index(prod)
        
            print("What would you like to update?")
            answer = input("(n)ame, (c)ost or (q)uantity: ")

            # If user wants to update name, ask or new name.
            # If name is duplilcate, tell "duplicate.
            # Otherwise, use replace index with a new name. 
            if answer == "n":
                while True:
                    
                    name = input("Enter a new name: ")
                    if name in product_names:
                      print("Duplicate name!")
                    else:
                        print("Product name has been updated")
                        product_names[prod_index] = name
                        print()
                        break
            if answer == "c":
                while True:
                    newcost = float(input("Enter a new cost: "))
                    if newcost <= 0:
                        print("Invalid cost!")
                    else:
                        del product_costs[prod_index]
                        product_costs.insert(prod_index, str(newcost))
                        print("Product cost has been updated")
                        print()
                        break

            # If the user wants to update quantity, ask for new quantity
            # If the new quantity is invalid, tell "invalid"
            # Otherwise, delete the original cost and insert a new quantity
            if answer == "q":
                while True:
                    newquan = int(input("Enter a new quantity: "))
                    if newquan <= 0:
                        print("Invalid quantity!")
                    else:
                        print("Product quantity has been updated")
                        print()
                        del product_stock[prod_index]
                        product_stock.insert(prod_index, str(newquan))
                        break
    elif name == "e":
        maxcost = max(product_costs)
        mincost = min(product_costs)
        maxx = product_costs.index(maxcost)
        minn = product_costs.index(mincost)
        total = 0
        # Use for loop to calculate the total value of all products
        for i in range (0, len(product_costs)):
            x = product_costs[i]
            y = product_stock[i]
            totalcost = x * y
            total += totalcost

        # Format the list in same order
        print(format("Most expensive product:",'<30s'), maxcost, "("+product_names[maxx]+")")
        print(format("Least expensive product:",'<30s'),mincost,"("+product_names[minn]+")")
        print(format("Total value of all products:",'<30s'), format(total, '.2f'))
        print()

                
                    
    

           
                
    else:
        print('Invalid option, try again')
        

