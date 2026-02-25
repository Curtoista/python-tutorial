#While Loops

value = 1

# while value <=10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while value <=10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

#For Loops

names = ["Curt", "Phil", "Scott"]
# for name in names:
#     print(name)

# for x in "Mississippi":
#     print(x)


# for x in names:
#     if x == "Phil":
#         break
#     print(x)

# for x in names:
#     if x == "Phil":
#         continue
#     print(x)

# for x in range(4):
#     print(x)

# for x in range(1,4):
#     print(x)

# for x in range(5,101, 5):
#     print(x)
# else:
#     print("Glad that\'s over")


names = ["Curt", "Phil", "Scott"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")