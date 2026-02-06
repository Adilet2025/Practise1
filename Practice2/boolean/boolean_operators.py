# Example of the AND operator

age = 18          # we set the value of age to 18
has_id = True     # has_id is True (the person has an ID)

if age >= 18 and has_id:
    # age >= 18 → True
    # has_id → True
    # True and True → True
    print("You can enter.")
else:
    print("You cannot enter.")
