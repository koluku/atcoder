all = []
for i in range(4):
    list = input().split()
    all.append(list)
for i in range(4):
    print(all[3 - i][3] + ' ' + all[3 - i][2] + ' ' + all[3 - i][1] + ' ' + all[3 - i][0])
