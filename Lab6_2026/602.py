n = int(input())
a = list(map(int, input().split()))

even = list(filter(lambda x: x%2 == 0, a))
print(len(even))