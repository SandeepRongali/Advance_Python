# Example 1: Create and access
student = {"name": "John", "age": 20}
print(student["name"])

# Example 2: Add new key
student["grade"] = "A"

# Example 3: Loop through dictionary
for key, value in student.items():
    print(key, value)

for i in student:
    print(i)

for i in student:
    print(student[i])
    
for i in student:
    print({i:student[i]})
