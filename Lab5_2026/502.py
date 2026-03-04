import re

a = input()
b = input()
count = re.findall(re.escape(b), a)
print(len(count))   