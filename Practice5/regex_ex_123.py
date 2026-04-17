import re   # re — Python module for working with regular expressions (pattern matching in text)

# ex 1
pattern_1 = re.compile(r"ab*")   
# re.compile() — creates a regular expression object for reuse
# a — the string must start with character 'a'
# b* — the character 'b' can appear 0 or more times
# pattern matches: a, ab, abbb, etc.

# ex 2
pattern_2 = re.compile(r"ab{2,3}")
# b{2,3} — the letter 'b' must appear 2 or 3 times after 'a'

txt = "abb"   # txt — the string where we search for matches
x = pattern_2.findall(txt)   
# findall() — returns all substrings that match the regex pattern
print(x)

# ex 3
pattern_3 = re.compile(r"[a-z]*_")
# [a-z] — any lowercase letter
# * — zero or more repetitions
# _ — underscore character
# pattern finds lowercase sequences ending with "_"

txt = "aokwergthjgb_cd"
print(pattern_3.findall(txt))   # prints all matching substrings

# ex 4
pattern_4 = re.compile(r"[A-Z][a-z]")
# [A-Z] — one uppercase letter
# [a-z] — one lowercase letter
# pattern finds uppercase letters followed by lowercase letters

txt = "AAAAAAAAAAAAABBBBBBBBBBBBcdcBIDNIDJbjvbjbn"
print(pattern_4.findall(txt))   # prints all matches

# ex 5
pattern_5 = re.compile(r"^a.*b$")
# ^ — beginning of the string
# a — string must start with 'a'
# .* — any character repeated any number of times
# b — string must end with 'b'
# $ — end of the string

txt = "ajdifjifhiprjg0w rumgueripgupeiurpiwi0eurgpeub"
print(pattern_5.findall(txt))   # returns the match only if entire string satisfies the pattern

# ex 6
pattern_6 = re.compile(r"[\s|,|.]")
# \s — whitespace (space, tab, newline)
# , — comma
# . — dot
# [] — character set meaning "any of these characters"

txt = "bro furina, she is the best. She is the hydro archon"
method_6 = re.sub(pattern_6, "|", txt)
# re.sub() — replaces characters that match the pattern
# here spaces, commas and dots are replaced with "|"
print(method_6)

# ex 7
pattern_7 = re.compile(r"_([a-zA-Z])")
# _ — underscore
# ([a-zA-Z]) — capturing group for one letter
# capturing group allows accessing the matched letter later

txt = "my_furina"
method_7 = re.sub(pattern_7, lambda match: match.group(1).upper(), txt)
# lambda — anonymous function used inside substitution
# match.group(1) — the letter captured after "_"
# upper() — converts it to uppercase
# converts snake_case → camelCase
print(method_7)

# ex 8
pattern_8 = re.compile(r"[A-Z]")
# [A-Z] — any uppercase letter

txt = "BroFurina,SheIsTheBest.SheIsTheHydroArchon"
method_8 = re.split(pattern_8, txt)
# re.split() — splits a string where the pattern occurs
# here the string is split at every uppercase letter
print(method_8)

# ex 9
pattern_9 = re.compile(r"(?<=\w)([A-Z])")
# (?<=\w) — positive lookbehind; checks that before the match there is a word character
# ([A-Z]) — uppercase letter captured as group 1

txt = "BroFurina,SheIsTheBest.SheIsTheHydroArchon"
method_9 = re.sub(pattern_9, r" \1", txt)
# r" \1" — inserts a space before the captured uppercase letter
# \1 refers to the first capturing group
# this separates words in CamelCase
print(method_9)

# ex 10
pattern_10 = re.compile(r"(?<=\w)([A-Z])")
# same pattern: finds uppercase letters that follow a word character

txt = "myFurina"
method_10 = re.sub(pattern_10, lambda match: "_" + match.group(1).lower(), txt)
# inserts "_" before the uppercase letter
# lower() converts that letter to lowercase
# converts camelCase → snake_case
print(method_10)