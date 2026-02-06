number = 0

while number < 6:      # the loop runs while number is less than 6
    number += 1        # increase number by 1
    if number == 3:    # check if number is equal to 3
        continue       # skip printing when number is 3
    print(number)      # print all numbers except 3
