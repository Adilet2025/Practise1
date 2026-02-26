def squares(N):              # defines a generator function named squares with parameter N
    for i in range(N + 1):   # loop variable i from 0 to N inclusive
        yield i * i          # produce (return lazily) the square of i

N = int(input())             # read input, convert string to integer, store in N
for i in squares(N):         # iterate over each yielded value from squares(N)
    print(i)                 # output each generated square



def Evven(N):                # defines a generator function that yields even numbers up to N
    for i in range(N + 1):   # iterate from 0 to N inclusive
        if i % 2 == 0:       # check condition: remainder of division by 2 equals 0 (even)
            yield i          # produce the even number i

N = int(input())             # read integer input
print(", ".join(str(val) for val in Evven(N)))  
# convert each yielded number to string, join with ", ", print result



def div(N):                           # defines a generator function for special divisibility
    for i in range(N + 1):            # iterate from 0 to N inclusive
        if i % 3 == 0 and i % 4 == 0: # check if divisible by 3 AND by 4
            yield i                   # produce number divisible by both (i.e., by 12)

N = int(input())             # read integer input
for i in div(N):             # iterate through generated values
    print(i)                 # print each valid number



def sqr(a, b):               # defines a generator from range a to b
    for i in range(a, b + 1):# iterate from a to b inclusive
        yield i ** 2         # produce square of current number (power operator **)

a, b = map(int, input().split())  
# read two numbers, split input, convert each to integer, assign to a and b

for val in sqr(a, b):        # iterate through generated squares
    print(val)               # print each square 