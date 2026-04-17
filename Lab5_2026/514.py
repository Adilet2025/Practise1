
import re

pattern = re.compile(r'^\d+$')
s = input()

if pattern.match(s):
    print("Match")
else: 
    print("No match")
