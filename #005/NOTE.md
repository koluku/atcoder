## A問題

単純に`/`で計算しようとするとfloat型になるので、結果をint型にするか、`//`で計算する必要がある。

### 解答

```
x, y = map(int, input().split())
print(y//x)
```

## B問題

### 解答

```
N = int(input())
l = []

for i in range(N):
    l.append(int(input()))
l.sort()
print(l[0])
```

### 補足

Python使っているんだからリスト内包表記を使えばいいのを後で思い出した。あと最小の値を出せばいいのでソートしなくても`min()`を使えばいいということを知った。

```
N = int(input())
l = [int(input()) for i in range(N)]
print(min(l))
```

## C問題

ifとforのせいで深い（不快）なネストとbreakの嵐。客が来る時間がたこ焼きができる時間と提供できる時間の間だったら通す。もしそうでないなら古いたこ焼きを処分して、新しいたこ焼きにして確認する。

### 解答

```
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
```

## D問題

最適化できず実行時間をオーバーしたため無し。
