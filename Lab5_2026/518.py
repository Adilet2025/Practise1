import re 

a = input()

count = re.findall(r'\w+', a)
print(count)