# List
attendance = ["Aaron", "James", "Chloe", "Hailey", "John", "Garlic", "Zach", "Ian"]

# Add Phoebe in the list
attendance.append("Phoebe")

# Add Noah in the list between John and Garlic
attendance.insert(5, "Noah")

# Add your name in the list
attendance.insert(2, "Brandon")

# Remove Garlic from the list
attendance.remove("Garlic")

# Organize name in Alphabetical order
attendance.remove ("Ian")
attendance.insert (5, "Ian")
attendance.remove("James")
attendance.insert(5, "James")
attendance.remove("Zach")
attendance.append("Zach")

# Replace John to Joshua
attendance[6] = "Joshua"

# print out 3th name in the list
attendance.pop(2)

print (attendance)



# Tuple; Cannot edit
sports = ("Golf", "Basketball", "Soccer", "Tenis", "Baseball")
print (sports[3])



# Dictionary
student = {}

# Add a key: name
student["name"] = "John"

# Add a key: age
student["age"] = 12

# Add a key: weight
student["weight"] = 110

# Add a key: school
student["school"] = "Evergreen"

# Add a key: Python
student["Python"] = True

print (student)
print (student["age"])


automobile = {"brand": "Ford", "model": "Mustang", "year": 2020}
print(automobile["brand"])
print(automobile)