N, K = map(int, input().split())
Rs = map(int, input().split())
Rs = sorted(Rs)

rate = 0.0;
for i in range(0, K):
    rate = (rate + Rs[N-K+i])/2.0

print(rate)
