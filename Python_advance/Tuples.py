# Example 1: Create and access
point = (10, 20)
x, y = point
print(x, y)  # 10 20

# Example 2: Immutability
t = (1, 2, 3)
# t[0] = 0  # Error! tuples can’t be changed

# Example 3: Tuple unpacking in loops
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
for num, letter in pairs:
    print(num, letter)

pairs = [[1, 'a',3], [2, 'b',5], [3, 'c', 9]]
for num, letter, data in pairs:
    print(num, letter)

t = (1,2,3,1,4,5,2)
print(t)