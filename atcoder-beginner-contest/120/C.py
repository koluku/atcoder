s = list(input())
count = 0
flag = True
while flag:
    if  len(s) < 2:
        flag = False
        break
    for i in range(len(s)-1):
        if s[i:i+2] == ["0", "1"] or s[i:i+2] == ["1", "0"]:
            s.pop(i)
            s.pop(i)
            count += 2
            break
        elif i == len(s)-2:
            flag = False
            break
print(count)
