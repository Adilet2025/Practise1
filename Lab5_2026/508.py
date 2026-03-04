import re

text = input()
pattern = input()

b = re.split(pattern, text)
print(",".join(b))