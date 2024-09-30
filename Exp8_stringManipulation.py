
import re

from numpy.testing.print_coercion_tables import print_new_cast_table

# String Manipulation

# 1. Creating a string
text = "Hello, my name is Parth. I live in Mumbai!"

# 2. Basic string operations
print("Original String:")
print(text)

# Length of the string
print("\nLength of the string:", len(text))

# Converting to uppercase
upper_text = text.upper()
print("\nUppercase:", upper_text)

# Finding a substring
substring = "Parth"
if substring in text:
    print(f"\nSubstring '{substring}' found at index:", text.index(substring))
else:
    print(f"\nSubstring '{substring}' not found.")


# searching pattern in string

text = "Hello my email address is parth@parth.com"
pattern = r'\w+@\w+\.\w+'

match = re.search(pattern,text)
if match:
    print("Found email",match.group())
replaced_txt = re.sub(pattern,"REDACTED",text)
print("replaced text: ",replaced_txt)
