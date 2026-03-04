
import re

s = input()

if re.compile(r'^\d+$', s):
    print("Match")
else: 
    print("match")
