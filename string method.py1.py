# Raed Al Kiswani
# PE2 Module 2.3 - String Methods
# Simple string practice done late at night after work at Amazon
# Data Science student at MCC

# Base text for testing
text = "raed works at amazon and studies data science at night"
extra_spaces = "   tired after work   "
mixed = "Late Night Coding"
letters_and_numbers = "python123"
letters_only = "python"
only_spaces = "   "
words = ["mcc", "data", "science"]

print("Base string:", text)
print()

# capitalize()
print("capitalize():", text.capitalize())

# center(width, fillchar)
print("center(40, '-'):", "focus".center(40, '-'))

# endswith(suffix)
print("endswith('night'):", text.endswith("night"))

# find(sub)
print("find('amazon'):", text.find("amazon"))

# isalnum(), isalpha(), islower(), isspace(), isupper()
print("isalnum on 'python123':", letters_and_numbers.isalnum())
print("isalpha on 'python':", letters_only.isalpha())
print("islower on base text:", text.islower())
print("isspace on '   ':", only_spaces.isspace())
print("isupper on 'HELLO':", "HELLO".isupper())

# join(iterable)
print("join words:", "-".join(words))

# lower(), upper(), swapcase(), title()
print("lower() on mixed:", mixed.lower())
print("upper() on mixed:", mixed.upper())
print("swapcase() on mixed:", mixed.swapcase())
print("title() on base text:", text.title())

# strip(), lstrip(), rstrip()
print("strip() removes spaces:", extra_spaces.strip())
print("lstrip() removes front spaces:", extra_spaces.lstrip())
print("rstrip() removes end spaces:", extra_spaces.rstrip())

# replace(old, new)
print("replace('night', 'morning'):", text.replace("night", "morning"))

# rfind(sub)
print("rfind('a') in text:", text.rfind("a"))

# split(separator) and startswith(prefix)
print("split() example:", "study hard sleep later".split())
print("startswith('raed'):", text.startswith("raed"))

# Combo example - clean then title
cleaned = extra_spaces.strip()
titled = cleaned.title()
print("cleaned (strip) ->", cleaned)
print("titled (title)  ->", titled)

# username test
username = "raed_k"
print("isalnum on username 'raed_k':", username.isalnum())

print("Done testing string methods. Probably time to sleep.")
