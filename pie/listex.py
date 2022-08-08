# PROBLEM 1 : Python program to interchange first and last elements in a list :

#Given a list, write a Python program to swap first and last element of the list

#1: Find the length of the list and simply swap the first element with (n-1)th element.


# Python3 program to swap first
# and last element of a list
 
# Swap function

'''def swaplist(newlist):
    size = len(newlist)
    
 #Swapping
    temp = newlist[0]
    newlist[0] = newlist[size -1]
    newlist[size -1] = temp
    return newlist

newlist = [1,2.3,4,5]
print(swaplist(newlist))'''

'''def swapname(newname):
    name = len(newname)
    
    temp = newname[0]
    newname[0] = newname[name -1]
    newname[name -1] = temp
    return newname
    
newname = ["vishnu", 'ashsih', 'ani']
print(swapname(newname))'''


'''    
def swapclass(newclas):
 clas = len(newclas)
 
 temp = newclas[0]
 newclas[0] = newclas[clas -1]
 newclas[clas -1] = temp
 return newclas

newclas = ['XI','VII', 'VI']
print(swapclass(newclas)'''


#Approach 2: The last element of the list can be referred as list[-1]. Therefore, we can simply swap list[0] with list[-1].

'''def swaplist(newlist):
    
    newlist[0], newlist[-1] =  newlist[-1], newlist[0]
    return newlist

newlist =[5,2,3,4,1]
print(swaplist(newlist))'''

'''def swapname(newname):

    
    newname[0], newname[-1] = newname[-1], newname[0]
    return newname

n = ('vishnu', 'darsi','ashish')
newname = list(n)
print(swapname(newname))
'''
# Python3 program to swap first
# and last element of a list

'''def swapname(list):
    
     # Storing the first and last element
    # as a pair in a tuple variable get
    get = list[-1], list[0]
    
    # unpacking those elements
    list[0], list[-1] = get
    return get

m = ['ashish','darsi','vish']
print(swapname(m))
'''

# Using insert() and append()

def swapnumber(n):
    first = n.pop(0)
    last = n.pop(-1)
    
    n.insert(0 ,last)
    n.append(first)
    return n

n = [1,2,3]
print(swapnumber(n))
    
    
# PROBLEM 2 : Python program to swap two elements in a list

#Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list




    
