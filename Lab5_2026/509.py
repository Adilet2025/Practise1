import re

a = input()

result = re.findall(r'\b\w{3}\b', a)
print(len(result))