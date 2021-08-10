'''
Yang Hwi Kim
Oct. 31, 2017
CSCI-UA 2-002(6162)
'''

def simple_sort_version1(a,b):
    if a<b:
        return (a,b)
    else:
        return (b,a)
    
    
a,b = simple_sort_version1(10,20)
print (a,b) # 10 20

a,b = simple_sort_version1(20,10)
print (a,b) # 10 20

a,b = simple_sort_version1(30,30)
print (a,b) # 30 30
