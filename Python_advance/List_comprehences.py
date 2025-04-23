# Example 1: Squaring numbers
squares = [x**2 for x in range(5)]
print(squares)

# Example 2: Filtering
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Example 3: Nested loops
pairs = [(x, y) for x in [1,2] for y in ['a','b']]
print(pairs)

pairs =[]
for x in [1,2]:
    for y in ['a','b']:
        pairs.append((x,y))
print(pairs)