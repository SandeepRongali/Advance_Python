# A generator is a function that returns one value at a time using yield.

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

for num in count_up_to(3):
    print(num)
    
# Instead of storing all values in memory, yield gives one at a time — super efficient for large data.