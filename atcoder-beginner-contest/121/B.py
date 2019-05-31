N, M, C = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
A = []
for i in range(N):
    A.append([int(x) for x in input().split()])
result = 0
for i in range(N):
    tmp = 0
    for j in range(M):
        tmp += A[i][j] * B[j]
    if tmp + C > 0:
        result += 1
print(result)
