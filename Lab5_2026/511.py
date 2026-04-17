import re

a = input()

letters = re.findall(r'[A-Z]', a)
print(len(letters))