value = 1
# while value < 10:
#     print(value)
#     value += 1

# print("**************")
# value = 1
# while value <= 10:
#     print(value)
#     value += 1

# print("**************")
# value = 1
# while value < 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# print("**************")    
# while value <= 10:
#     value +=1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

# print("**************")    
names = ["Juan", "Jane", "Mike"]
# for x in names:
#     print(x)
# print("**************")    
# for x in "Mississippi":
#     print(x)
# print("**************")    
# for x in names:
#     if x == "Jane":
#         break
#     print(x)
# print("**************")    
# for x in names:
#     if x == "Jane":
#         continue
#     print(x) 
# print("**************")    
# for x in range(4):
#     print(x)
# print("**************")    
# for x in range(2,4):
#     print(x)
print("**************")    
for x in range(0,101,5):
    print(x)
print("Glad that\'s over!")

print("**************")    
names = ["Juan", "Jane", "Mike"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")

