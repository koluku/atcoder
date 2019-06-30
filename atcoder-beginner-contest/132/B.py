n = int(input())
p = [int(x) for x in input().split()]

c = 0
for i in range(n-2):
    if p[i] < p[i+1] < p[i+2] or p[i+2] < p[i+1] < p[i]:
        c += 1

print(c)
