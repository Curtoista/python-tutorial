#Dictionaries -looks like JS Objects

band = {
    "vocals": "Trey",
    "guitar": "Trey",
    "bass": "Mike" 
}

band2 = dict(guitar="Dave", bass="Stefan", drums="Carter")

# print(band)
# print(band2)
# print(type(band))
# print(len(band))

#Access dictionary items

# print(band["guitar"])
# print(band.get("bass"))

# #List all keys

# print(band.keys())

#List all values

# print(band.values())

#List of key/value pairs as tuples

# print(band.items())

#Verify a key exists

# print("guitar" in band) #True
# print("triangle" in band) #False
# print("Trey" in band) #False

#Change Values
# print(band)
# band["vocals"] = "Page"
# band.update({"drums": "Fish"})

# print(band)

# # Remove items

# print(band.pop("vocals"))
# print(band)

# band["keys"] = "Page"
# print(band)

# print(band.popitem()) #Returns tuple
# print(band)

# #Delete and clear

# band["keys"] = "Page"
# print(band)
# del band["keys"]
# print(band)

# print(band2)
# band2.clear()
# print(band2)

# del band2
# print(band2)

#Copy dictionaries

# band2 = band #creates a reference -don't do this?
# print("Bad Copy")
# print(band2)
# print(band)

# band2["keys"] = "Page" #Also adds "keys" to band, not just band2
# print(band)

# band2 = band.copy()
# band2["keys"] = "Page"
# print("Good copy!")
# print(band)
# print(band2)

# # Can use the dict() constructor function

# band3 = dict(band)

# print("Good copy!")
# print(band)
# print(band3)


#Nested Dictionaries

member1 = {
    "name": "Trey",
    "insrument": "guitar"
}
member2 = {
    "name": "Mike",
    "insrument": "bass"
}
member3 = {
    "name": "Fish",
    "insrument": "drums"
}
member4 = {
    "name": "Page",
    "insrument": "keys"
}

phish = {
    "member1": member1,
    "member2": member2,
    "member3": member3,
    "member4": member4
}

# print(phish)
# print(phish["member1"]['name'])


# Sets

# nums = {1, 2, 3, 4}
# nums2 = set((1,2,3,4))

# print(nums)
# print(nums2)
# print(type(nums))
# print(len(nums2))

# # Sets do not allow duplicates

# nums3 = {1,2,2,4}

# print(nums3)

# #True is a duplicate of 1, and False is a dupe of zero

# nums4 = {1, True, 2, False, 3, 4, 0}
# print(nums4) #Returns {False, 1, 2, 3, 4}

# #Check if a value is in a set

# print(2 in nums4)

# #Cannot refer to an element in the set with an index position or key 

# #Add a new element to a set

# nums4.add(8)
# print(nums4)

# #Add elements from one set to another

# more_nums = {5, 6, 7}
# nums4.update(more_nums)
# print(nums4)
# nums4.update(phish)
# print(nums4)

# You can use update with lists, tuples, and dictionaries too. I.E nums4.update(band)


#Sets do not necessarily come out ordered when removing duplicates. Will seemingly order at lower values, but longer and more complicated numbers will make it random

# nums5 = {1, True, 2, False, 3, 2.234652345, 0}
# print(nums5)


#Merge two sets to create a new set

one = {1, 2, 3}
two = {5, 6, 7}

my_new_set = one.union(two)
print(my_new_set)

#Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

#Keep everything but the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)