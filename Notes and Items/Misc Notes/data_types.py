#String Data Type

#Literal Assignment
first = 'Juan'
last = 'Gil'

print(first)
print(type(first))
print(type(first) == str)
print(isinstance(first,str))

#constructor Assignment
seperator ="***********"
pizza =str("Pepperoni")
print(pizza)
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza,str))

#concatation
seperator ="***********"
print(seperator)
fullname = first + " " + last
print(fullname)
fullname += "!"
print(fullname)

#Casting a number to a string
seperator ="***********"
print(seperator)
decade=str(2000)

print(type(decade))
print(decade)

statement = "I like music from the " + decade + "s."
print(statement)

#Multiline

multiline = '''
Hey, how are you?

                
                I was just checking in

                        All good?
'''
print(multiline)

#Escaping special charcters
seperator ="***********"
print(seperator)
sentence = 'I\'m at work!\tHey!\n\n Where\'s this at\\located?'
print(sentence)

#String Methods
seperator ="***********"
print(seperator)
print(first)
print(first.lower())
print(first.upper())
print(first)

seperator ="***********"
print(seperator)
print(multiline.title())
print(multiline.replace("good","ok"))
print(multiline)

seperator ="***********"
print(seperator)
print(len(multiline))
multiline += "                                                                "
multiline = "                                              " + multiline
print(len(multiline))

seperator ="***********"
print(seperator)
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

#Build a menu
seperator ="***********"
print(seperator)
title="Menu".upper()
print(title.center(20,"="))
print("Coffe".ljust(16,".") + "$1".rjust(4))
print("Muffin".ljust(16,".") + "$2".rjust(4))
print("Cheese Cake".ljust(16,".") + "$4".rjust(4))

#String Index Values
seperator ="***********"
print(seperator)
print(first[0])
print(first[-1])
print(first[1:-1])
print(first[1:])
print(first[0:])

#Some methods return boolean data
print(first.startswith("J"))
print(first.endswith("Z"))

#Boolean data type
seperator ="***********"
print(seperator)
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue,bool))

#Numeric Data Types

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price,int))

#Float Type
gpa = 3.28
y=float(1.48)
print(type(gpa))
print(isinstance(y,float))

#complex Type
comp_value = 3 + 5j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#Built in functions for numbers
seperator ="***********"
print(seperator)
print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa, 1))

#Math Module (any imports must be at the absolute top)
import math
seperator ="***********"
print(seperator)

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))