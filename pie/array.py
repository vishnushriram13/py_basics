# inserting elements in an empty array
from array import *

'''n_arr = array('i',[])
n = int(input("enter the length: "))
for i in range (n):
    c = int(input("enter the elements: "))
    n_arr.append(c)
print("Entered elements:",n_arr)'''
    

#Program to find largest(maximum) and smallest(minimum) number in array:

'''a = array('i',[1,30,50,5,9])
max = a[0]
n = len(a)
for i in range(1,n):
    if a[i]>max:
        max = a[i]
print("largest number in array :",max)

# With user inputs:
n = array('i',[])
c = int(input("enter the length:"))
for i in range(c):
    v = int(input("enter the elements: "))
    n.append(v)
print(n)
max = n[0]
for i in range(1,c):
 if n[i]>max:
    max = n[i]
print("largest number is : ",max)
        
        
m = array('i',[50,80,41,25])
min = m[0]
q = len(m)
for i in range(1,q):
    if m[i]<min:
        min = m[i]
print("Minimum number in array :",min)'''

#Find Second Smallest Element in an list using Python
'''a = [1,20,30,31,40,50]
a.sort()
print(a[1])
'''

'''n = []
c = int(input("enter the length of list:"))
for i in range(c):
    v = int(input("enter the values:"))
    n.append(v)
print("the entered values as list are: ",n)
n.sort()
print("After sorting the given list: ",n)
print("the second largest number in the list is: ",n[0])'''

    

#Find Second largest Element in an list also removing duplicate elements using sort in Python

'''a =[]
b = int(input("enter the length:"))
for i in range (b):
    c = int(input("enter the number: "))
    a.append(c)
print("Entered values in list:",a)
d = list(set(a))
print(d)
d.sort()
print("after sorting:",d)
print("the 2nd largest element in array is:",(d[-2]))
'''

#without using set
'''a =[]
b = int(input("enter the length:"))
for i in range (b):
    c = int(input("enter the number: "))
    a.append(c)
print("Entered values in list:",a)
r = []
if i in a:
    if i not in r:
        r.append(i)
r.sort()
print("after sorting:",r)
print("the 2nd largest element in array is:",(r[2]))    '''












