

'''a = []
b = int(input("Enter the length : "))
for i in range(b):
    c = int(input("Enter the elements : "))
    a.append(c)
print("Entered number in array: ",a) 
a.sort()
print("after sorting: ",a)
print("the largest ele: ",a[-1])
print("the smallest ele: ",a[0])
print("the second larg ele: ",a[-2])
print("the second smallest: ",a[1])
print("reversing the ele: ",a[::-1])
'''



'''a = [10,20,30,40]
sum = 0
for i in a:
  print(i)
  print(a)
  sum = sum + i
print(sum)'''

'''a = [10,1,2,55,64,87,74]
a.sort()
print("Enter the values after sorting: ",a)
print("First half in ascending: ",a[0:4])
print("Second half in descending: ",a[:-4:-1])'''

'''a = [10,20,20,10,30,45]
dup = []
for i in a:
  if i not in dup:
   dup.append(i)
print("after removing dups: ",dup)
      '''
#Positive or negative  and their occurance    
'''a = [-2,-1,20,30,0]
elepos = []
eleneg = []
pos = 0
neg = 0
for i in a:
  if (i > 0):
    elepos.append(i)
    pos = pos + 1
    
  elif (i < 0):
    eleneg.append(i)
    neg = neg + 1
  
  elif (i == 0):
    print("netural num : ",i)
    
print("Positive numbers : {} and total + num is : {}".format(elepos, pos))
print("Negative numbers : {} and total - nums are : {}".format(eleneg,neg))
'''


'''a = [10,-20,30,0]
for i in a:
 if (i > 0):
  print("postive number : ",i)
  
 elif (i < 0):
  print("negative number : ",i)
  
 else:
  print("netural :", i)'''
  


'''x = int(input("Enter the elements: "))
v = int(input("Enter the elements: "))
n = int(input("Enter the elements: "))
m = int(input("Enter the elements: "))
if x > v and x > n and x > m :
  print(x)
elif v > x and v > n and x > m:
  print(v)
elif n > x and n > v and n > m:
  print(n)
else :
  print(m)'''
  
#find the ocuurence :
'''occ = ['vishnu', 'darshi', 'ashish']
n = str(input("Enter the target char: "))
c = 0 
for i in occ :
    if n in i :
      c = c + 1
print("The target occurence {} in array occured {} times ".format(n, c))'''


#missing number in an array
#prime or not :

'''a = int(input("Enter the number : "))
for i in range(2,a):
  if a % i == 0:
    print("Not Prime")
    break
else :
  print("Prime")
'''
#factorial 
'''d = int(input("Enter the input: "))
factorial = 1
if d < 0:
  print("Negative numbers cant be computed")
elif d < 2:
  print("{} ! is : {}".format(d, factorial))
else:
  for i in range(d,1,-1):
    factorial = factorial * i
  print("{} ! is : {}".format(d, factorial))'''
  

#palindrome
'''n = input("Enter the values: ")
reverse = n[::-1]
if n == reverse:
  print("The value {} is a palindrome ".format(n))
else:
  print("Its not a palindrome")'''
  
#fibonacci


'''def fibonacci(n):
 
 if n < 0:
  print("- numbers cant be computed")
  
 elif n == 1:
  print()
  
 else:
  a = 0
  b = 1
  print(a)
  print(b)
  for i in range(n):
   c = a+b
   a = b
   b = c
   print(c)

n = int(input("enter the number: "))
fibonacci(n)'''
  

#Sum of arrays:
'''a = []
n = int(input("Enter the length: "))
b = 0
for i in range(1, n+1):
  c = int(input("Enter the values: "))
  a.append(c)
for i in a:
  b = b + i
print("sum of arrays: ",b)'''
  

'''a = [10,20,30,40]
sum = 0
for i in a:
  print(i)
  print(a)
  sum = sum + i
print(sum)

occ = ['vishnu', 'darshi', 'ashish']
n = str(input("Enter the target char: "))
c = 0 
for i in occ :
    if n in i :
      c = c + 1
print("The target occurence {} in array occured {} times ".format(n, c))'''


'''a = int(input("ENter the value : "))
if(a%2==0):
  print("Even")
else:
  print("Odd")
'''
        
        
#prime or not :
'''a = int(input("Enter the value: "))
for i in range(2,a):
  if(i % a == 0):
   print("Not prime")
   break
else:
  print("Prime")'''
  
  
a = 11
for i in range(2,a):
  if (i%2==0):
    print("Not a prime")
    break
else:
    print("not prime")
  
'''#factorial of number:
def fac(n):
  f = 1
  for i in range(1,n+1):
   f = f*n
  return f
  

x = 4

n = fac(x)
print(n)'''






'''a = [10,20,50,70,5]
a.sort()
print("first half in ascending: ",a[1:4])
print("second half in descending: ",a[:-3:-1])'''

'''a = [10,50,10,20]
dup = []
for i in a:
 if i not in dup:
  dup.append(i)
print("after removing dup in arrray: ",dup)'''


'''a = [10,-2,0,20]
for i in a:
  if i < 0:
    print("the number {} is negative".format(i))  
    
  elif i > 0:
    print("the number {} is postive:".format(i))
    
  else :
    print("Netural")'''
    
'''a = [10,11,12,0,13]
for i in a:
  if (i%2==0):
    print("the number {} is even".format(i))
  elif(i%2!=0):
    print("the number {} is odd".format(i))'''
    
'''a = ["vishnu", "ashish", "darshi"]
c = input("ENter the traget occ: ")
occ = 0
for i in a:
  if c in i:
    occ = occ + 1
print(occ)'''

'''def fac(n):
 fact = 1
 for i in range(1, n+1):
  fact = fact*n
 return fact
    
x = 4
n = fac(x)
print(n)'''

#palindrome
'''a = input("Enter the name: ")
rev = a[::-1]
if (a==rev):
    print("its a palindrome")
else:
    print("not palindrome")
    '''
#prime oe not 


    
    
    


  
  






      
        


      









