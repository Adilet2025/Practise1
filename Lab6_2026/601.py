n = int(input())
a = list(map(int, input().split()))

s = sum(map(lambda x: x*x, a))
print(s)