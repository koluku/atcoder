T = int(input())
N = int(input())
As = list(map(int, input().split()))
M = int(input())
Bs = list(map(int, input().split()))

check = 0
p = 0

if N >= M:
    for i in range(M):
        if p <= N:
            for j in range(p, N):
                if As[j] <= Bs[i] <= As[j] + T:
                    p += 1
                    break
                else:
                    if j != N -1:
                        p += 1
                        continue
                    else:
                        check += 1
                        break
        else:
            break
else:
    check += 1

if check != 0:
    print('no')
else:
    print('yes')
