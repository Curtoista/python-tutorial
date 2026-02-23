#Lists

users = ['Curt', 'John', 'Sara']

data = ['Curt', 42, True]

emptyList = []

# print('Curt' in emptyList)
# print('Curt' in data)
# print('Curt' in users)

# print(users[0])
# print(users[-1])
# print(users[-2])

# print(users.index('Sara'))

# print(users[0:2])
# print(users[0:])
# print(users[:2])
# print(users[1:])
# print(users[-3:-1])
  
# print(len(data))

# users.append('Bob')
# print(users)

# users += ['Alice']
# print(users)

# users.extend(['Eve', 'Charlie'])
# print(users)

# users.extend(data)
# print(users)

# users.insert(0, "Bob" )
# print(users) #Inserts into index 0

# users[2:2] = ["Jack", "Jill"]
# print(users) #Inserts list in between index 1/3

# users[1:3] = ["Bill", "Ted"] #Replace Index 1,2 -SLICE
# print(users)

# users.remove('Bob')
# print(users)

# print(users.pop()) #Returns last item in list
# print(users) #Returns list after last item has been removed by the pop method

# del users[0]
# print(users)

# # # del data
# # data.clear()
# # print(data)

# users[1:2] = ['alex']
# print(users)
# users.sort() #Lowercase will be sorted after uppercase
# print(users)

# users.sort(key=str.lower)
# print(users)

# nums = [4, 42, 78, 1, 5]
# nums.reverse()
# print(nums)

# nums.sort()
# print(nums)

# nums.sort(reverse=True)
# print(nums)

# print(sorted(nums, reverse=True))
# print(nums)

# numscopy = nums.copy()
# mynums = list(nums)
# mycopy = nums[:]

# print(numscopy)
# print(mynums)
# mycopy.sort()
# print(mycopy)

# print(type(nums))
# print(type(users[0]))

# mylist = list([1, 'Neil', True])
# print(mylist)

# Tuples

#Tuples are like lists except data inside doesn't change nor does order

mytuple = tuple(('Curt', 42, True))
anothertuple = (1,4,2,7,2,2)

print(mytuple)
print(type(mytuple))
print(anothertuple)
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)
print(type(newtuple))

#Unpacking tuples

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)
print(type(two))
print(type(hey))

print(anothertuple.count(2))