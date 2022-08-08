a = input("Enter the name: ")
rev = a[::-1]
for i in a:
  if (i==rev):
    print("its a palindrome")
  else:
    print("not palindrome")