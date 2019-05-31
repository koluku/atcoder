n = int(input())
v = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

vc = [(v[i] - c[i]) for i in range(n)]
vc.sort(reverse=True)

result = 0
for profit in vc:
    if profit <= 0:
        break
    result += profit

print(result)
