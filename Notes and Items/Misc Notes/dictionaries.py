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