import re   # re — Python module for working with regular expressions (pattern matching in strings)

# Ex1 
s = input()   # input() — reads a string from the user
if re.match(r"^ab*$", s):   # re.match() checks if the pattern matches from the start of the string
    print("Match")   # print() outputs text to the screen
else:
    print("No match")

# ^ — start of the string
# a — first character must be 'a'
# b* — 'b' repeated 0 or more times
# $ — end of the string

# Ex 2

s = input()
if re.match(r"^ab{2,3}$", s):   # b{2,3} — 'b' must appear 2 or 3 times
    print("Match")
else:
    print("No match")

# Ex 3

s = input()
if re.match(r'^[a-z]+_[a-z]+$', s):   # [a-z] — any lowercase letter
    print("Match")
else:
    print("No match")

# + — one or more repetitions
# _ — underscore character
# This pattern checks snake_case format

# Ex 4

s = input()
pattern = re.compile(r"[A-Z][a-z]+")   # re.compile() creates a regex pattern object
txt = "ASTANAAlmaty"   # txt — string to search in
print(pattern.findall(txt))   # findall() returns all matches in the string

# [A-Z] — one uppercase letter
# [a-z]+ — one or more lowercase letters

# Ex 5
s = "asertnb"
pattern = re.match(r'^a.*b$', s)   # .* — any character repeated any number of times 
print(pattern)   # prints match object if pattern matches
# re.match() is a function in Python’s re (regular expression) module that checks whether a pattern matches the beginning of a string.
# Ex 6

s = input()
result = re.sub(r'[ ,.]', ':', s)   # re.sub() replaces characters that match the pattern
print(result)

# [ ,.] — space, comma, or dot

# Ex 7

a = input()

camel = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), a)
print(camel)

# _([a-z]) — underscore followed by a lowercase letter
# () — capturing group
# lambda — anonymous (short) function
# m.group(1) — extracts the captured letter
# upper() — converts the letter to uppercase
# This converts snake_case → camelCase

# Ex 8

a = input()

result = re.split(r'(?=[A-Z])', a)
print(result)

# re.split() — splits a string using a regex pattern
# (?=[A-Z]) — positive lookahead
# Splits the string before every uppercase letter

# Ex 9

a = input()

words = re.findall(r'[A-Z][a-z]*', a)
print(" ".join(words))

# findall() — returns all matches as a list
# [A-Z] — uppercase letter
# [a-z]* — zero or more lowercase letters
# join() — combines list elements into a single string with spaces

# Ex 10
txt = "myCar"
snake = re.sub(r'(?<!^)(?=[A-Z])', '_', txt).lower()
print(snake)

# (?<!^) — not at the start of the string
# (?=[A-Z]) — position before an uppercase letter
# _ — insert underscore
# lower() — converts the whole string to lowercase
# This converts camelCase → snake_case