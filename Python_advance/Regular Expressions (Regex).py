# Regular expressions are used to match patterns in strings.
#
# Python uses the re module.

import re

text = "My number is 987-654-3210"
pattern = r"\d{3}-\d{3}-\d{4}"

match = re.search(pattern, text)
if match:
    print(match.group())


# email = "test@example.com"
# pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
#
# if re.match(pattern, email):
#     print("Valid email")
# else:
#     print("Invalid email")