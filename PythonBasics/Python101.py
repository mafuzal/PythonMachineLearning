#%% List 

listOfNumbers = [1, 2, 3, 4, 5, 6]
for number in listOfNumbers:
    if (number % 2 == 0):
        print(number, "is even")
    else:
        print(number, "is odd")
        
print("All done.")

#%% Importing Modules 
import numpy as np
A = np.random.normal(25.0, 5.0, 10)
print(A)

#%% Lists 
x = [1, 2, 3, 4, 5, 6]
print(len(x))

print('Slice, ask for first 3 elements of the list') 
print(x[:3])

print('Slice after the 3rd element') 
print(x[3:])

print('Slice, to ask for last two elements of the list') 
print(x[-2:])

print('Append a list to list') 
print(x.extend([7,8]))

print('Append a single value') 
x.append(9)
print(x)

y = [10, 11, 12]
listOfLists = [x, y]
listOfLists

y[1]

z = [3, 2, 1]
z.sort()

z.sort(reverse = True)

#%% Tuples 
#Tuples are just immutable lists. Use () instead of []
x = (1, 2, 3)
print(len(x))

y = (4, 5, 6)
print(y[2])

listOfTuples = [x, y]
listOfTuples
(age, income) = "32,12000".split(',')
print(age)
print(income)

#%%Dictionaries 
#Like a map or hash table in other Languages 

captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Matthew"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janeway"

print(captains["Voyager"])
print(captains.get("Enterprise"))
print(captains.get("YALE"))

for ship in captains:
    print(ship + ": " + captains[ship])


#%%Functions 
def SquareIt(x):
    return x * x
print(SquareIt(2))

#You can pass function around as a parameters 
def DoSomething(f, x):
    return f(x)

print(DoSomething(SquareIt, 3))

#Lambda functions let you inline simple functions 
print(DoSomething(lambda x: x * x * x  , 3))

#%% Boolean Function 
print(1 == 3)
print (True or False)
print(1 == 3)

if 1 == 3:
    print("How did that happen?")
elif 1 >3:
    print("Yikes")
else:
    print("All is well with the world")
    
#%% Looping 
for x in range(10):
    print(x)
    
for x in range(10):
    if ( x == 1):
        continue 
    if (x > 5):
        break
    print(x)
    
X = 0
while ( X < 10):
    print(X)
    X += 1
    
#%% Activity 
myList = [0, 1, 2, 5, 8, 3]
for number in myList:
    if number %2 == 0:
        print(number)