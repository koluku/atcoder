n = int(input())
d = [int(x) for x in input().split()]

d.sort()
print(d[int(n / 2)] - d[int(n / 2) - 1])
