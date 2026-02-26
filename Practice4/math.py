import math                      # import math library for π (pi)

degree = float(input("Input degree: "))   # ask user, change input to float number
radian = degree * math.pi / 180           # convert degree to radian using formula
print("Output radian: ", round(radian, 6)) # print result, round to 6 decimal places



import math                      # import math library (not necessary here, but allowed)

a = float(input("Height: "))              # read height, convert to float
b = float(input("Base, first value: "))   # read first base, convert to float
c = float(input("Base, second value: "))  # read second base, convert to float

area = ((b + c) / 2) * a         # formula of trapezoid area

print("Expected Output: ", round(area, 2)) # print area, round to 2 decimal places



import math                               # import math library for tan and pi

n = int(input("Input number of sides: ")) # read number of sides, convert to int
s = float(input("Input the length of a side: ")) # read side length, convert to float

area = (n * s * s) / (4 * math.tan(math.pi / n)) 
# formula for regular polygon area

print("The area of the polygon is:", round(area, 0)) 
# print result, round to 0 decimal places


import math                               # import math library (not necessary here)

base = float(input("Length of base: "))   # read base length, convert to float
height = float(input("Height of parallelogram: ")) # read height, convert to float

area = base * height                     # formula: area = base × height

print("Expected Output:", area)          # print area