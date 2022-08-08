'''x = 14
y = 45
sum = x + y
#print("sum of 2 numbers x and y:",sum)
print("sum of {} and {} is {}".format(x,y,sum))'''



'''x = input("Enter 1st number: ")
y = input("Enter 2nd numb: ")
sum = int(x) + int(y)
print("sum of {} and {} is {}" .format(x,y,sum))
'''



#Maximum of two numbers in Python
'''x = input("Enter 1st number: ")
y = input("Enter 2nd number: ")

maximum = max(x,y)
print("result:",maximum)'''

'''x = input("Enter 1st number: ")
y = input("Enter 2nd number: ")

if(x<y):
    print(y)
else:
    print(x)
'''

#Python Program for factorial of a number

num = int(input("Enter any integer: "))

if num<0:
    print("Factorial doesnt exist for negative numbers")
elif num==0 or num<1:
    print("The factorial of number 0 and 1 is 1")
else:
    factorial = 1
    for i in range (2, num+1):
        factorial = factorial * i
    print("the factorial of {} is {}".format(num, factorial))
    
    

'''def factorial(n):
    return 1 if(n==1) or (n==0) else n * factorial(n-1)

n = int(input("enter the number: "))
print("factorial of", n, "is",factorial(n))'''

'''import math
def factorial(n):
    return(math.factorial(n))

num = 5
print("factorial of", num, 'is',factorial(num))
'''

#Python Program for simple interest

'''def simple_interest(p,t,r):
  print('the principle is',p)
  print('the time period is',t)
  print('the rate of interest is',r)
  si = p * t * r/100
  print("Simple interest: ",si)

simple_interest(10000,5,5)
'''


#Python Program for compound interest
'''def compund_interest(p,r,t):
    amount = p*(pow((1+r/100),t))
    ci = amount-p
    print("Compound interest: ",ci)
    
compund_interest(1200,5.4,2)'''


# Python Program for Program to find area of a circle

#print("area of cricle is ",3.14*(int(input("enter the radius value:")))**2)


# python program to find the sqaure root

'''import math
from math import sqrt
num = int(input("Enter a number: "))
print("Square root of {} is {}".format(num, sqrt(num))) #math.sqrt'''


'''num = 5
square_root = num ** 0.5
print("the square root of num {} is {:.3f}".format(num,square_root))
'''

#Python Program for Sum of first n natural numbers

# using for loop

'''num = int(input("enter the number:"))
sum = 0
for i in range (1,num+1):
    sum += i

print("sum of num is : ",sum)'''
    
'''num = int(input("enter the number:"))
sum = 0
i = 1
while i<=num:
    sum = sum + i
    i = i + 1
    print("sum is : ",sum)'''
    


#Python Program for Sum of square of first n natural numbers

'''n =  int(input("enter the value: "))
sum = 0
for i in range (1, n+1):
    sum = sum + i*i
    print("result: ",sum)'''
    

'''n =  int(input("enter the value: "))
sum = 0
i = 1
while i<=n:
    sum = sum + i*i
    i = i+1
    print("Result: ",sum)'''
    
# python program to calculate the area of a triangle:
#if 3 sides :a,b,c
 
 #s = (a+b+c)/2
 #area = (s*(s-a)*(s-b)*(s-c))**0.5
 
 # If base and height are given:
 # area = 0.5*b*h
 
'''a = int(input("enter side one : "))
b = int(input("enter side: "))
c = int(input("enter side: "))

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)**0.5)
print("area of triangle with sides{},{} and {} is {:.2f}".format(a, b, c, area))'''



'''b = int(input("enter value for b: "))
h = int(input("enter value for h: "))
area = 0.5*b*h
print("area of base {} and {} is {}".format(b, h, area))'''

# pyhton program to convert kilometers to miles:

'''km = float(input('enter in kilometers: '))
conv_fact = 0.621371
miles = km * conv_fact
print("there are {:.2f} miles in {} kilometers".format(miles, km))'''

# pyhton program to convert miles to kilometers:
'''miles = float(input('enter in kilometers: '))
conv_fact = 0.621371
km = miles / conv_fact
print("there are {:.2f} kilometers in {}  miles".format(km, miles))'''


# Python program to check if a number is +,- or 0:


'''num = int(input("enter the number : "))
if num > 0:
    print("positive")
elif num==0:
    print("zero")
else:
    print("negative")'''
    
    
# python program to check if a number is ODD or EVEN:

'''num = int(input("enter the number : "))
if num % 2 == 0:
    print("{} is Even number".format (num))
else:
    print("{} number is odd".format(num))'''
    
    
# Program to check leap year:

'''year = int(input("enter the year: "))

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("{} is a leap year".format(year))
        else:
            print("{} is not a leap year".format(year))
    else:
     print("{} is not a leap year".format(year))
else:
 print("{} is not a leap year".format(year))  '''
 
 
 
# program to find out the largest or maximum  value number:

#using logic:
'''num1 = float(input('number1: '))
num2 = float(input('number2: '))
num3 = float(input('number3: '))

if num1<=num2 and num1<=3:
    largest = num1
elif num2<=num1 and num2<=3:
    largest = num2
else:
    largest = num3
    
print("{} largest number".format(largest))'''

#using inbuilt ():
'''num1 = float(input('number1: '))
num2 = float(input('number2: '))
num3 = float(input('number3: '))

maximum = max(num1,num2,num3)
print("{} is the largest number".format(maximum))'''

#program to check prime number:

# Python program to print all Prime numbers in an Interval

# Python program to display the multiplication table:

'''n = int(input("enter the number: "))

for i in range(1,11):
    print(i, 'x', n, '=',i*n)'''
    
# program to print fibonacci sequence

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
        
n = int(input("enter the number:"))
fibonacci(n)

#program to display fibonacci seq using recursion
#program to check armstrong number
#program to find armstrong number in an interval
#program  to add two matrices
#program to multiply two matrices
#program to transpose a matrix


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
    
#program to find sum of natural numbers using recursion:



# program to display powers of 2 using lambda  
# program to find number divisible by another number:

'''n = [10,20,22,56,30,33,48,80]
for i in n:
    if i%15==0:
        print(i)
'''

'''n = [10,20,22,56,30,33,48,80]
result = list(filter(lambda x: (x%5==0),n))
print(result)'''


#program to convert decimal to binary,octaland hexadecimal

'''n = 6

print(bin(n))
print(oct(n))
print(hex(n))'''

#program to convert decimal to binary using recursion


#program to find ASCII value of a number:
#inbuilt ord
'''print(ord('%'))

chr(65)

for i in range(65,91):
 print(chr(i))
'''

#program to find HCF or GCD
#program to find LCM

#program to find the factors of the number:

'''def factor(x):
  for i in range(1,x+1):
      if x%i==0:
          print(i)
        
factor(5)'''

          
      
#simple calculator
#shuffle deck of cards



#program to display calendar:

'''import calendar
year = int(input("enter year: "))
month = int(input("enter month: "))
print(calendar.month(year,month))
'''

'''from unicodedata import name'''


'''class vechile:
    def __init__(self,model,color):
        self.model = model
        self.color = color
        
    def myfunc(self):
        print("my model is " + self.model)
        print("my vechicle color is " + self.color)
        
v1 = vechile("audi","black")
v1.myfunc()
'''

'''class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print("my name is "+self.name)
        print("my age is"+ self.age)
        
p1 = person("vishnu","22")
p1.myfunc()
'''

'''class fruit:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    
    def myfunc(self):
        print("the fruit name is "+ self.name)
        print("my fruit color is "+ self.color)
        
f1 = fruit("mango","yellow")
f1.myfunc()
'''

    
    
'''count = 0
string = str(input("enter the string: "))
word = str(input("enter the occurrence: "))
if string == word:
        count = count+1
print(count)'''

'''count = 0
a =  ['V''i''s''h''n''u' 'S''h''r''i''r''a''m']
word = a
if a == word:
        count = count+1
print(count)'''

'''count = 0
string = str(input("enter the string: "))
word = str(input("enter the occurrence: "))
for i in string:
    if i == word:
        count = count + 1
print("count of occurrence in string: ",count)'''



'''sentence1 =" VISHNU SHRIRIAM "
count = { }
for i in sentence1:
    if i in count:
        count[i.lower()] = count[i.lower()] + 1
    else:
        count[i.lower()] = 1
print(count)'''

'''ab = set("VISHNU SHRIRAM")

test_str = "CLOFUS"

for i in ab:
  counter = test_str.count(i)
  if i == ' ':
    i = 'Space'
  print(counter, i)'''














































