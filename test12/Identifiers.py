from idna.core import unichr


#Standard Datatypes - Numbers, String , List, Tuple, Dictionary

#Usage of Numbers

#when you assign numbers to a variable Number Objects are created
a = 10
b = 20.1

print(a);print(b)

#Number Objects can be deleted too

del a,b

#print(a);print(b)

#Numbers supports 4 types -  int,long(octal, hexal are also allowed),float,complex(x+yj - x,y are real nums and J is imaginary unit)

# *******************************************************************************************************
#Strings

stringVar = "sairam"

print(stringVar)

# [:] operator substrings

print (stringVar[3])
print (stringVar[0:3])
print (stringVar[3:])
print (stringVar[3:-1])

# + concatinates, * is operator

print (stringVar[0:3] + "ram") 
print (stringVar[3:] *2) 


# *******************************************************************************************************

# Lists

#unlike other languages list can have different datatypes here

simpleList = ['a', "sai", 2.1, 112]

print(simpleList)
print(simpleList[0])

# [:] operator substrings
print(simpleList[0:3])
print(simpleList[3])

# + concatinates, * is operator

print(simpleList*2)
print(simpleList+[1])


# *******************************************************************************************************

# Tuples

# A Tuple can be treated as a read only list
# a tuple defines in () 

simpleTuple = ('a', "sai", 2.1, 112)

print(simpleList)
print(simpleList[0])

# [:] operator substrings
print(simpleList[0:3])
print(simpleList[3])

# + concatinates, * is operator

print(simpleList*2)
print(simpleList+[1])

# *******************************************************************************************************

# Dictionary

# kind of hash table

simpleDict = {}
simpleDict["one"] = "one"
simpleDict[2] = "two"

print(simpleDict)

simpleDict2 = {'one': 'one', 2: 'two'}
print(simpleDict2)


print(simpleDict[2])
print(simpleDict2["one"])

print(simpleDict.keys())
print(simpleDict2.values())

# *******************************************************************************************************

aString = "12121"

aInt = int(aString)

print(aInt)

aFloat = float(aInt)
print(aFloat)

aTuple = tuple(simpleList)
print(aTuple)

aList = list(simpleTuple)
print(aList)

aTuple = tuple(simpleDict)
print(aTuple)

#ord converts the single char to its integer value
print(ord("s"))
#unichr converts integer to unicode char
print(unichr(115))

print(hex(aInt))
print(oct(aInt))


