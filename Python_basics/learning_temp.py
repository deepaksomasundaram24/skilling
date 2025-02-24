name = "Deepak"
print(isinstance(name,str))
age = 2
print(isinstance(age,int))

print(0 or 1)
print(12 or False)
print(False or 'Hey')
print('Hi' or 'Hey')
print([] or False)
print(False or [])

'''& binary AND, | binary OR, ^ binary XOR, ~ binary NOT, << shift left operation, >> shift right operation'''

'is - identity operator - returns True if both objects are the same'
'in - instance operator, checks if the left hand side value is present in the right hand side'

#ternary operator
a = 19
print(True if a > 18 else False) 

name = "Deepak"
name += " is my name."
print(name)
print(name.upper())
#Title names the first letter of the string capital and the rest small
name2 = ""
print(name2.isalpha())

#The methods below give a new and modified string, they do not alter a string
#isalpha() - checks if a string has alphabets and not empty
#come to this later...

# any() method returns True if any values in the list is True
# all() reuturns true 

#complex 
comp_var1 = 2 + 3j
comp_var2 = 4 + 5j 
print(comp_var1.real)
print(comp_var1.imag)

#enum for creating constants
from enum import Enum
class state(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(state.ACTIVE.value)
print(state['ACTIVE'])

#appending a list using + 
dogs = ["Quincy",2,"Game"]
dogs += ["Asia",4]
print(dogs)

'''#pop method removes and returns the last element in the list 
for i in range(3):
    print(dogs.pop())'''

#inserting values in the list at the particular index
dogs.insert(1,"Play")
print(dogs)
dogs[1:1] = ["Cambodia", "Disney"]
print(dogs)

#Sorting with lower case
items = ["Game","Basketball","Foodball", "Cricket","Handball","Tennis"]
print(items)
sorted(items,key = str.lower)
print(items)
#items.sort(key = str.lower) #this also does not modify the original list
#print(items)
itemscopy = items[:]


#Dictionaries
new_dict = {"name":"Roger","age":10}
print(new_dict.get("name"))
print(new_dict.get("breed"))
