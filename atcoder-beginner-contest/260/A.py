S = input()

tmp = {}
for x in list(S):
    if not x in tmp.keys():
        tmp[x] = 0
    tmp[x] += 1

flag = "-1"
for key in tmp.keys():
    if tmp[key] == 1:
        flag = key
        break

print(flag)
