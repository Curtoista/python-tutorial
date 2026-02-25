#Functions

def hello_world():
    print("Hello world!")

hello_world()

# def sum(num1, num2):
#     print(num1 + num2)


# sum(2,3)
# sum(1,5)
# sum(100,5)

def sum(num1=0, num2=0): #Default values as parameters to avoid errors
    if (type(num1) is not int or type(num2) is not int):
        return 0 #return just returns NONE
    return num1 + num2

total = sum(7,2)
print(total)    

def multiple_items(*args):  # *args is for an unknown amount of arguments. Makes type a tuple*
    print(args[0]) #prints first item in tuple
    print(args)  #prints whole tuple
    print(type(args))

multiple_items("Curt", "Phil", "Dave")

def mult_named_items(**kwargs): #kwargs is key word arguments
    print(kwargs)
    print(type(kwargs))

mult_named_items(first="Curt", middle="Cutler", last="Fuller")