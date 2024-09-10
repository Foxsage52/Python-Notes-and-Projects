# Dictionaries
band = {
    "Vocals": "Plant",
    "Guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

#Accessing Items
print(band["Vocals"])
print(band.get("Guitar"))

#List all key
print(band.keys())

#List all Values
print(band.values())

#List of Key/value paris as tuples
print(band.items())

#Verify a key exists
print("Guitar" in band)
print("Triangle" in band)

#Change Values
band["Vocals"] = "Cloverdale"
band.update({"bass":"JPJ"})

print(band)

#Remove Items
print(band.pop("bass"))
print(band)

band["drums"] = "bohman"
print(band)

print(band.popitem()) # Tuple
print(band)

#Delete and Clear

band["drums"] = "Bohman"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# #Copy Dictonaries

# band2 = band #creates a reference
# print("Bad Reference!")
# print(band2)
# print(band)

# band2["drums"] = "Juan"
# print(band)
print('')
band2 = band.copy()
band2["drums"] = "Juan"
print("Good Copy!")
print(band)
print(band2)

#or we can use the dict() constructor function
band3 = dict(band)
print("Good Copy!")
print(band3)

#nested dictionary
print("")
member1 = {
    "Name": "Plant",
    "Instrument": "Vocals"
}

member2 = {
    "Name": "Page",
    "Instrument": "Guitar"
}
band = {
    "member1": member1,
    "memeber2": member2
}
print(band)
print(band["member1"]["Name"])

#Sets
nums = {1, 2 , 3, 4}

nums2 = set((1, 2, 3 ,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#No duplicates Allowed
nums = {1, 2, 2, 3}
print(nums)

#True value is a dupe of zero, false is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

#Check if a value is in a set
print(2 in nums)

#but you can't refer to an element in the set with an index position or key

#adds a new element to a set
nums.add(8)
print(nums)

#Adds element from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

#You can use updates with lists, tuples, and dictonaries too

#Merge two sets to create a new one
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)