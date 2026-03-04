import re 

a = input()

b = re.search(r'\S+@\S+\.\S+', a)
if b:
    print(b.group())
else:
    print("No email")