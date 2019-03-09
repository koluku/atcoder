# ABC#001の解答ノート

Python 3を勉強するついでに初めてのAtCoder Beginner Contestをやってみたので、解答集を書いておこうと思う。GitHubにコード(.py)とドキュメント(.md)を置いといたのでまとめてみたい人はcloneするといい。

## A問題

問題文にてh1-h2の結果を出力すれば良いとあるので、結果がマイナスになっても問題はない。整数値を与えられるが、変数にそのまま代入するとint型かstr型か不明でエラーが出るので、int()でデータを揃える。

### 解答

```
h1 = int(input())
h2 = int(input())

print(h1 - h2)
```

### 補足

一度変数に代入しなくても計算できるので、こういう書き方もできる。

```
print(int(input())-int(input()))
```

## B問題

問題文に従ってコードを記述すればよいので特に難しくはない。VVが2桁の整数になることに気をつけてformat()でゼロ埋めをする。

### 解答

```
km = int(input())/1000

if km < 0.1:
    vv = 0
if 0.1 <= km and km <= 5:
    vv = km * 10
if 6 <= km and km <= 30:
    vv = km + 50
if 35 <= km and km <= 70:
    vv = (km - 30) / 5 + 80
if 70 < km:
    vv = 89

vv = int(vv)

print('{0:02d}'.format(vv))
```

### 補足

条件式にandを使用したが、Python 3では左右で評価しても同じことができる。また、ゼロ埋めにはstr型でzfill()を使うことができる。

```
km = int(input())/1000

if km < 0.1:
    vv = 0
if 0.1 <= km <= 5:
    vv = km * 10
if 6 <= km <= 30:
    vv = km + 50
if 35 <= km <= 70:
    vv = (km - 30) / 5 + 80
if 70 < km:
    vv = 89

print(str(int(vv)).zfill(2))
```

## C問題

round()を使った小数点以下の四捨五入は不正確になる場合があるので注意。今回は四捨五入したい小数点以下の位を一の位まで上げ、0.5を足してint型することで正確さを出している。

### 解答

```
deg, dis = map(int, input().split())

dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
wps = [2, 15, 33, 54, 79, 107, 138, 171, 207, 244, 284, 326]

dir = dirs[(deg * 10 + 1125) % 36000 // 2250] if w > 0 else "C"

w = 0
for n in wps:
    if int(dis/6 + 0.5) > n:
        w += 1

print(dir, w)
```

## D問題

アルゴリズムの問題だったので勉強していない僕にはお手上げです。後々更新するつもり。
