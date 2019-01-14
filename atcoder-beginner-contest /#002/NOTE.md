# ABC#002の解答ノート

前回と比べ、簡単な問題が多い。

## A問題

if~elseを使ってXかYを出力するだけの簡単な問題。

### 解答

```
x, y = map(int, input().split())
if x > y:
    print(x)
else:
    print(y)
```

## B問題

正規表現を使って文字を検索して置換するのがベスト。

### 解答

```
import re

word = input()
reword = re.sub('[aiueo]', '', word)
print(reword)
```

### 珍答

replace()を並べることでも同じことができる。実はこれで解答出してた。

```
word = input()
reword = word.replace('a', '').replace('i', '').replace('u', '').replace('e', '').replace('o', '')
print(reword)
```

## C問題

同じ点から始まる2つのベクトルによってできる三角系の面積なので、ベクトル(a, b), (c , d)のとき面積は`|ad-bc|/2`と計算できる。  
絶対値はmathモジュールを使うのが楽。

### 解答

```
import math

xa, ya, xb, yb, xc, yc = map(int, input().split())
a = xb - xa
b = yb - ya
c = xc - xa
d = yc - ya
area = math.fabs(a * d - b * c) / 2
print(area)
```

## D問題

どういうアルゴリズムでとけばいいのかわからなかったので未着手。二分探索だろうか。そのうち解く予定。
