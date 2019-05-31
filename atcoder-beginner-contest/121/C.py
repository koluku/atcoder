N, M = [int(x) for x in input().split()]
A = []
for i in range(N):
    A.append([int(x) for x in input().split()])
A.sort()
result = 0
for i in range(N):
    tmp = 0
    if A[i][1] >= M:
        result += A[i][0]*M
        break
    else:
        result += A[i][0] * A[i][1]
        M -= A[i][1]
print(result)
