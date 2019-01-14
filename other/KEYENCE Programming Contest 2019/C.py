N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
if sum(A) < sum(B):
    print(-1)
else:
    num, fix = 0, 0
    for i in range(N):
        if A[i] - B[i] < 0:
            num += 1
            fix += B[i] - A[i]
    if num != 0:
        ret = []
        for i in range(N):
            if A[i] - B[i] > 0:
                ret.append(A[i] - B[i])
        ret.sort(reverse=True)
        su = 0
        for i in range(len(ret)):
            su += ret[i]
            num += 1
            if su >= fix:
                break
    print(num)
