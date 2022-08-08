'''#find largest element in array:
from array import array 
a = []
b = int(input("Enter the len : "))
for i in range(b):
    c = int(input("Enter the values : "))
    a.append(c)
#removing dups with logic:
d = []
for i in a:
    if i not in d:
        d.append(i)
print("after removing dups :", d)
#Sorting with inbuilt function to index the Largest or Smallest element in array :
d.sort()
print("After sorting values : ", d)
print("Largest element in array :", d[-1])
print("Smallest element in array is :", d[0])'''
#Calculating sum of elements:
'''e= [10, 20, 30, 10, 50]
sum = 0
for i in e:
    sum  = sum + i
print(sum)'''
#Reversing array :
'''f = [10, 20, 30, 40]
print (f[::-1]) #Slicing 

#Using Function : 
def reverse(g):
    print (g[::-1])

g = [20, 0, 50, 60]
reverse(g)'''
#Sorting in Ascending and Descending Order :
'''h = [90, 10, 30, 50, 20]
h.sort()
print(h)
h.sort(reverse=True)
print(h)
'''
# program to Sort first half in ascending order and second half in descending order in an array
#Dynamic
'''arr=[]
size=int(input("Enter the length : "))
for i in range(size):
 element = int(input("Enter the values : "))
 arr.append(element)
arr.sort()
rev = arr[::-1] 
print("first half in ascending order",arr[:3])
print("second half in descending order",rev[:3])'''

#Static
'''arr=[90, 10, 30, 50, 20]
arr.sort()
rev = arr[::-1] 
print("first half in ascending order",arr[:3])
print("second half in descending order",rev[:2])
'''
#Finding the  Frequency of elements in an array using Python
'''arr=[2,2,2,2,2,2,2,2,45,7,8,9,6,3,666]
n=int(input("enter a number from the list : "))
freq=0
for i in arr:
 if n ==i:
  freq+=1
else:
 pass
print("the number of times {} occurred is {}".format(n,freq))'''

#to find palindrome:
'''li = (input("Enter the values: "))
reverse = li[::-1]
if li == reverse:
    print("palindrome")
else:
    print("not palindrome")
'''















    

    
    