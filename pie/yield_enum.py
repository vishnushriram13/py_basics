'''
# Yield eg 
def yield_eg(iterable):
    for i in iterable:
        print("double data gen {}".format(i))
        yield i*2 #Its also called LazyCoding
        

# Eg without Yeild:        
def yield_eg (iterable):
    l = []
    for i in iterable:
        print("double data gen {}".format(i))
        l.append(i*2)
        return(l)
        
def datagen():
    l = []
    for i in range(10):
        print("[]datagen")
        l.append(i)
    return l 

# Generating data on demand
for i in yield_eg(range(10)):
    print(i)
 
 # Iterating already available data   
for i in datagen():
    print(i)'''
    
    
# Enum eg:
l = ['apple','banana', 'orange']

for i, d in enumerate(l):
    print("{} {}".format(i,d))
    if i==1:
        break;

# Without enum :
c = 0
for i in l:
    print(i)
    c+=1 
    if(c==2):
        break