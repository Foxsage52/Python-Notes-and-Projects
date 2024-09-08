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