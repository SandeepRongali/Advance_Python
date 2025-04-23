# Example 1: Basic try/except
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Example 2: Multiple except blocks
try:
    val = int("abc")
except ValueError:
    print("That’s not a valid integer.")
except Exception:
    print("Some other error occurred.")

# Example 3: finally clause
try:
    f = open("data.txt")
    data = f.read()
except FileNotFoundError:
    print("File missing!")
finally:
    print("Cleanup if needed.")
