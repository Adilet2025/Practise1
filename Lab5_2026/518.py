import re 

a = input()
s = input()

count = re.findall(re.escape(s), a)
print(len(count))