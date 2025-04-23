# Example 1: Writing text
with open("hello.txt", "w") as f:
    f.write("Hello, file!")

# Example 2: Reading lines
with open("hello.txt", "r") as f:
    for line in f:
        print(line.strip())

# Example 3: Appending
with open("hello.txt", "a") as f:
    f.write("\nThis is appended.")
