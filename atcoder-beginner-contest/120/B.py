a, b, k = [int(x) for x in input().split()]
al = set()
bl = set()
for i in range(1, a+1):
    if a%i == 0:
        al.add(i)
for i in range(1, b+1):
    if b%i == 0:
        bl.add(i)
kk = list(al & bl)
kk.sort(reverse=True)
print(kk[k-1])
