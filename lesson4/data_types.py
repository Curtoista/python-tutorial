import math

# String Data Type

# literal assignment


first = 'Curtis'
last = "Fuller"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
pizza = str("Pepperoni")

# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))


# Concatenation

fullname = first + " " + last

# print(fullname)

# fullname += "!"

# print(fullname)

# # Casting a number to a string
decade = str(1980)
# print(type(decade))
# print(decade)

year = 1988
# # print(type(year))
# # print(year)

statement = "I like the music of the " + decade + "s"
# print(statement)

# Multiple Lines
multiline = '''
Hey how are you?          

I was checking in.           
                    All good?

'''

# print(multiline)

# Escaping special characters

sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
# print(sentence)

# String Methods

# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace("good", "ok"))
# print(multiline)

# print(len(multiline))
# multiline += '                   '
# multiline = "                   " + multiline
# print(len(multiline))

# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))

# Build a menu

title = "menu".upper()
# print(title.center(20, "="))
# print("Coffee".ljust(16, ".") + "$1".rjust(4))
# print("Muffin".ljust(16, ".") + "$2".rjust(4))
# print("Cheesecake".ljust(16, ".") + "$4".rjust(4))


# string index values

# print(first[0])
# print(first[1])
# print(first[2])
# print(first[3])
# print(first[-1])
# print(first[0:])
# print(first[0:-1])

# # Some methods return booleans

# print(first.startswith("C")) #True
# print(first.endswith("F")) #False

# Boolean data type

myvalue = True
x = bool(False)

# print(type(x))    #<class bool>
# print(type(myvalue))    #<class bool>
# print(isinstance(x, bool))   #True
# print(isinstance(myvalue, bool))    #True
# print(isinstance(first, bool))     #False

# Numeric Data types

# integer types

price = 100
best_price = int(80)

# print(type(price))
# print(isinstance(best_price, int))

# Float type

gpa = 3.28
y = float(1.14)
# print(type(gpa))

# Complex type

comp_value = 5 + 3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)

# Built-in functions for numbers

# print(abs(gpa))
# print(abs(gpa * -1))
# print(round(gpa))
# print(round(gpa, 1))


# print(math.pi)
# print(math.sqrt(64))
# print(math.ceil(gpa))
# print(math.floor(gpa))


#Casting a string to a number

zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))
print(zip_value)

# Error if you attempt to cast incorrect data

# zip_value2 = int("NY")   ERROR