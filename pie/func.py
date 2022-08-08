'''def basic_math(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d

a = int(input("enter the 1st number:"))
b = int(input("enter the 2nd number:"))
i, j, k, l = basic_math(a, b)

print("Addition of {} and {} = {}".format(a, b, i))
print("sub of {} and {} = {}".format(a, b, j))
print("* of {} and {} = {}".format(a, b, k))
print("/ of {} and {} = {}".format(a, b, l))   
'''
# the above and below both are same #

'''def basic_math(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d

a = int(input("enter the 1st number:"))
b = int(input("enter the 2nd number:"))
i, j, k, l = basic_math(a, b)

print("Basic math of {} and {} :".format(a, b))
print("Addition : {}".format(i))
print("sub : {}".format(j))
print("* : {}".format(k))
print("/ : {}".format(l))''' 


'''def basic_math(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return {
        "add" : a,
        "sub" : b,
        "multi" : c,
        "div" : d
    }

a = int(input("enter the 1st number:"))
b = int(input("enter the 2nd number:"))
d = basic_math(a, b)

print("Basic math of {} and {} :".format(a, b))
for i in d.keys():
   print("{} : {}".format(i, d[i])) '''

#Concept: Packing and Unpacking 
# Functions processing multiple values within the given arguments:


'''def add(x, *y):
    print(x)
    print(y)
    r = 0
    r = r + x 
    for i in y:
      r = r + i
    return r

print("addition result : {}".format(add(1,2,3,4,89,5,6,7)))'''

# Without x  as arg: 
'''def add(*y):
    x = 0
    print(x)
    print(y)
    r = 0
    r = r + x 
    for i in y:
      r = r + i
    return r

print("addition result : {}".format(add(1,2,3,4,89,5,6,7)))'''



   
