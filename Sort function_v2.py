'''
Yang Hwi Kim
Oct. 31, 2017
CSCI-UA 2-002(6162)
'''

def simple_sort_version2(a,b,c):
    if a<b and a<c and b<c:
        return (a,b,c)
    elif a<b and a<c and c<b:
        return (a,c,b)
    elif b<a and b<c and a<c:
        return (b,a,c)
    elif b<a and b<c and c<a:
        return (b,c,a)
    elif c<a and c<b and a<b:
        return (c,a,b)
    else:
        return(c,b,a)



a,b,c = simple_sort_version2(10,20,30)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(10,30,20)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(30,20,10)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(30,20,20)
print (a,b,c) # 20 20 30
