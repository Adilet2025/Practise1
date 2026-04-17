
import re

s = input()

numbers = re.findall(r'\w+', s)
print(len(numbers))