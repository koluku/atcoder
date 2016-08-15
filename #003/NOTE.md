# ABC#003の解答ノート

## A問題

タスクをこなした数を未知数xとして置くと、給料は`10000 * 1 / x + 10000 * 2 / x + 10000 * 3 / x + ... + 10000 * x / x`となる。

これをまとめると、

```
10000 * 1 / x + 10000 * 2 / x + 10000 * 3 / x + ... + 10000 * x / x
= 10000 * (1 + 2 + 3 + ... + x) / x
= 10000 * x * (x + 1) / 2 / x
= 10000 * (x + 1) / 2
= 5000 * (x + 1)
```

よって給料は`5000 * (x + 1)`と導き出される。

### 解答

```
N = int(input())
ave = (N + 1) * 5000
print(ave)
```

## B問題

`pattern = 'atcoder'`を作り、@があった時にpatternを対象に検索して解消するかどうか確認している。実は他のブログを見てると、発想とやり方が全く同じだった。

[AtCoder ABC #003 : Python練習編](http://kmjp.hatenablog.jp/entry/2013/12/14/0900)

### 解答

```
s = list(input())
t = list(input())

pattern = 'atcoder'
check = 0

for i in range(0, len(s)):
    ss = s[i]
    tt = t[i]

    if s[i] == '@' or t[i] == '@':
        if pattern.find(s[i]) != -1:
            ss = '@'
        if pattern.find(t[i]) != -1:
            tt = '@'
    if ss != tt:
        check += 1

if check != 0:
    print('You will lose')
else:
    print('You can win')
```

### 補足

str型はわざわざlist()でリストにしなくてもリスト同様に前から文字を取り出すことができる。

## C問題

最初に見る動画がn番目（1≦n≦K）に見る動画で追加されるレートは、動画のレートの1/2^(K-n+1)倍となる。つまり、はじめに見る動画ほどレートが小さくなり、最後に見る動画が一番大きくなるため昇順に計算していけば良い。

注意点として、昇順に計算するときに後ろからK番目から計算しないとN != Kの時に計算が合わない。

### 解答

```
N, K = map(int, input().split())
Rs = map(int, input().split())
Rs = sorted(Rs)

rate = 0.0;
for i in range(0, K):
    rate = (rate + Rs[N-K+i])/2.0

print(rate)
```

## D問題

わっからーん。
