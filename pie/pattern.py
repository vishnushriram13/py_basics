#right angle triangle star pattern:
'''ros = int(input("enter the value: "))
for i in range(1,ros+1):
  print("* " * i)'''


#inverse right angle triangle pattern:

'''totalrows = int(input("enter the values: "))
for row in range(1, totalrows+1):
  
#logic for space :
  for space in range(1, (totalrows - row) + 1):
   print(" ", end ="")
  
#logic for star:
  for star in range(1, row+1):
   print("*", end ="")
    
  print()
  '''

'''#Printing numbers in X shape :
n = int(input("Enter the values:"))
for row in range(n):
  for column in range(n):
    if(row == column) or ((row+column)==n-1):  
      print("{0}".format(column), end="")
    else:
      print("  ", end="")
  print()'''
  
#printing chars in x shape:
name = input("Enter the name: ")
target = len(name)
for row in range(target):
  for col in range(target):
    if (row == col) or ((row+col == target -1)):
     print("{}".format(name[row]), end="")
    else:
     print("  ", end="")
  print()

  

