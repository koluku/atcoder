import collections

s = input()
c = collections.Counter(s)
if len(c) == 2 and c[s[0]] == 2:
    print('YES')
else:
    print('NO')
