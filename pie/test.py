from array import array
'''a = array('i',[])
b = int(input("enter the length:"))
for i in range(b):
    c = int(input("enter the number:"))
    a.append(c)
print("entered values in array:",a)'''

#finding largest and smallest in array

'''a = array('i',[])
b = int(input("enter the length:"))
for i in range(b):
    c = int(input("enter the values:"))
    a.append(c)
print("values in array: ",a)
max = a[0]
for i in range(1,b):
    if a[i]>max:       #logic 
        max = a[i]     #logic
print("the largest number: ", max))'''

#to find smallest in array
'''a = array('i',[])
b = int(input("enter the length:"))
for i in range(b):
    c = int(input("enter the array value:"))
    a.append(c)
print("entered arrray:", a)
max = a[0]
for i in range (b):
    if a[i]<max:
        max = a[i]
print("Smallest number in array: ",max)
'''

#find the second largest number in list with removing dups:
'''a = []
b  = int(input("Enter the length: "))
for i in range(b):
    c = int(input("enter the values: "))
    a.append(c)
print("Entered values in [] : ",a)
d = list(set(a))
print("For removing dups: ",d)
d.sort()
print("After sorting values: ",d)
print("the second largest number in []: ",(d[-2]))
'''
#reverse a number:
'''a = int(input("enter the values:"))
b = 0
print("entered ele: ",a)
while a > 0:
    b = (a % 10) + b * 10  #logic 
    a //= 10
print("Reversed sum is : ",b)'''

#positive or negative:
'''a = int(input("enter the value:"))
if a > 0:
    print("positive")
if a == 0:
    print("zero")

else :
    print("negative")'''
    
#Even or odd :
'''a = int(input('Enter the number:'))
if a % 2 == 0:
    print("Even")
else:
    print("odd")'''
    
#sum of first n natural numbers:
'''a = int(input('Enter the number:'))
b = 0
for i in range(1, a+1):
    b = b + i
print(b)'''

#Greatest of three numbers:
'''a = int(input('Enter the number:'))
b = int(input('Enter the number:'))
c = int(input('Enter the number:'))
if a >= b and a>=c:
    largest = a
elif b>=a and b >=c:
    largest = b
else:
    largest = c
    
print("largest num is ",largest)'''

#to find leap year
'''year = int(input("enter the year: "))
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("leap year")
        else:
            print("not a leap year")
    else: 
        print("not a leap year")
else:
    print("not a leap year")'''
    
#Program to count the occurrence of char in a string:
#DYnamic:jm
'''count = 0
string = str(input("enter the string: "))
word = str(input("enter the occurrence: "))
for i in string:
    if i == word:
        count = count + 1
print("count of occurrence in string: ",count)'''

#Using in built:
'''string = str(input("enter the string: "))
word = str(input("enter the occurrence: "))
print("Ocuurence: ",(string.count(word)))'''


# remove duplicates from array/list:

# dynamic :


'''def remove_dups(data):
 non_dup = []
 for e in data:           #logic 
    if e not in non_dup:
        non_dup.append(e)
 return non_dup
    
data = []
a = int(input("Enter the length: "))
for i in range(a):
    b = int(input("enter the values: "))
    data.append(b)
print("Original data: ",data)
print("After removing dup data:", remove_dups(data))'''


'''data = []
a = int(input("Enter the length: "))
for i in range(a):
    b = int(input("enter the values: "))
    data.append(b)
non = []
for i in (data):
    if i not in  non:
        non.append(i)
print(non)
'''

#static:
'''def remove_dup(data):
    nodup = []
    for i in data:
        if i not in nodup:
            nodup.append(i)
    return nodup

data = [1,22,1,22,3,4,5] 
print("OG data: ",data)
print("After removing dups: ",remove_dup(data))'''

#program to find the sum of natural numbers:

'''n = int(input("enter the number:"))
if n<0:
    print("enter the positive number")
else:
    sum = 0
    while n>0:
        sum+=n
        n-=1
    print("the sum is :",sum)'''


# to find the missing number in array/list:

'''def missing_num(arr,b):
    expected_sum = b * (b + 1)/2 #formula for finding missing number in dynamic
    actual_sum = sum(arr)
    return expected_sum - actual_sum

arr = []
b = int(input("Enter the length of the array: "))

for i in range(b-1):
    c = int(input("Enter the values: "))
    arr.append(c)
print("actual array: ", arr)
    
print("the missing number is : ",(missing_num(arr,b)))'''

'''def find_missing(a):
    actual_sum = sum(a)
    b = len(a)
    expected_sum = (b + 1)*(b + 2)/2 # formula for finding missing number in static
    return expected_sum - actual_sum

a = [1, 2, 3, 5]
print("missing number is : ", find_missing(a))'''

#Python Program for factorial of a number

'''num = int(input("Enter any integer: "))

if num<0:
    print("Factorial doesnt exist for negative numbers")
elif num==0 or num<1:
    print("The factorial of number 0 and 1 is 1")
else:
    factorial = 1
    for i in range (2, num+1):
        factorial = factorial * i
    print("the factorial of {} is {}".format(num, factorial))'''
    


# Program to check prime or not:
'''a  = int(input("enter the num: "))
c = 0
for i in range(1, a+1) :
    if a % i == 0:
        c += 1
if c == 2:
    print("Entered number is prime:",a)
else:
    print("is not a prime")'''
    
 
 
#difference between yield and list   
'''def double_numbers(iterable):
    for i in iterable:
        print("[] {}".format(i))
        yield(i*2)
        
def datagen():
    l = []
    for i in range(10):
        print("[]")
        l.append(i)
    return l
    
for i in double_numbers(range(10)):
    print(i)
    
for i in datagen():
    print(i)
    '''
#for printing range in list 
'''print(list(range(100)))'''


'''#fibonacci
def fibonacci(n):
  a = 0
  b = 1
  print(a)
  print(b)
  for i in range(n):
     c = a + b
     a = b
     b = c
     print(c)
n = int(input("Enter the values: "))
fibonacci(n)'''



    
    
    
    


        
    



        
    


    





    

    

    

    


        
    
