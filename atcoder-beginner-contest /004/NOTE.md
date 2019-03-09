他人の答えを見ないとわからないあたり、まだまだだと思う。

## A問題

もはや語ることもあるまい。

### 解答

```
print(int(input()) * 2)
```

## B問題

二重リストにして表示する順番を入れ替えるだけ。

### 解答

```
all = []
for i in range(4):
    list = input().split()
    all.append(list)
for i in range(4):
    print(all[3 - i][3] + ' ' + all[3 - i][2] + ' ' + all[3 - i][1] + ' ' + all[3 - i][0])
```

## C問題

Nが5につき左端の数字が右端に移動することを利用して、30で割ったあまりだけ計算する。逆にそうしないとプログラム実行時間を超えてしまう。

### 解答

```
N = int(input())
cards = ['1', '2', '3', '4', '5', '6']

for i in range(N % 30):
    a = cards[i % 5]
    cards[i % 5] = cards[ i % 5 + 1]
    cards[ i % 5 + 1] = a

print(cards[0] + cards[1] + cards[2] + cards[3] + cards[4] + cards[5])
```

## D問題

時間切れにて終了。
