# Example 1: for loop
for i in range(3):
    print("Hello")

# Example 2: while loop
count = 0
while count < 3:
    print("Counting:", count)
    count += 1

# Example 3: Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(i)
    print(fruits[i])

for i in enumerate(fruits):
    print(i)
