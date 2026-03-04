import re 

s = input()

pattern = re.compile(r'Name:\s*(.+),\s*Age:\s*(.+)')
match = pattern.search(s)

if match:
    name = match.group(1)
    age = match.group(2)
    print(name, age)