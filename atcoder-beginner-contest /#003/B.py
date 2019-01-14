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
