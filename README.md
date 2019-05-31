# AtCoder

AtCoder Beginner ContestのPythonでの解答集です。ACで通ったものだけ置いてあります。
一部解いていない問題や、最適解ではないものありますので参考までに。

Atcoder Beginner Contest 999の6問分の準備例
※毎回直前になって準備しているので生成コード用意しました。

```
python3 make.py abc 999 --num 6
```

## よく使うコード

### 標準入力

```
n = int(input())
```

```
n, m = [int(x) for x in input().split()]
```

```
a = [int(x) for x in input().split()]
```

### 正規表現

```
import re
content = r"hellow python, 123, end."
pattern = "^.*python.*$"

result = re.match(pattern, content)

if result:
  print(result.group())
```

| 文字  | 説明               | 例      | マッチする       | マッチしない |
| ----- | ------------------ | ------- | ---------------- | ------------ |
| \d    | 任意の数字         |         |                  |              |
| \D    | 任意の数字以外     |         |                  |              |
| \s    | 任意の空白文字     |         |                  |              |
| \S    | 任意の空白文字以外 |         |                  |              |
| \w    | 任意の英数字       |         |                  |              |
| \W    | 任意の英数字以外   |         |                  |              |
| .     | 任意の一文字       | a.c     | abc, acc, aac    | abbc, accc   |
| ^     | 文字列の先頭       | ^abc    | abcdef           | defabc       |
| $     | 文字列の末尾       | abc$    | defabc           | abcdef       |
| *     | ０回以上の繰り返し | ab*     | a, ab, abb, abbb | aa, bb       |
| +     | １回以上の繰り返し | ab+     | ab, abb, abbb    | a, aa, bb    |
| ?     | ０回または１回     | ab?     | a, ab            | abb          |
| {m}   | m回の繰り返し      | a{3}    | aaa              | a, aa, aaaa  |
| {m,n} | m〜n回の繰り返し   | a{2, 4} | aa, aaa, aaaa    | a, aaaaa     |
| []    | 集合               | [a-c]   | a, b, c          | d, e, f      |
| \|   | 和集合（または）   | a\|b    | a, b             | c, d         |
| ()    | グループ化         | (abc)+  | abc, abcabc      | a, ab, abcd  |

## LICENSE

[MIT LICENSE](LICENSE)にて公開しているのでご自由にお使いください。
