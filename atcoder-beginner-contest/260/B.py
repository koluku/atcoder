N, X, Y, Z = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

students = []
for i, point in enumerate(A):
    students.append({'index': i, 'X_point': point, 'is_pass': False})
for i, point in enumerate(B):
    students[i].update({'Y_point': point})
for i in range(N):
    students[i].update({'Z_point': students[i]['X_point'] + students[i]['Y_point']})

win = []

# print('=================')
sorted_by_X = sorted(students, key = lambda x: (x['is_pass'], -x['X_point'], x['index']))
for student in sorted_by_X[:X]:
    # print(x['is_pass'], student['index'], student['X_point'])
    if student['is_pass']:
        continue
    win.append(student['index'])
    students[student['index']].update({'is_pass': True})
# print('-----------------')

sorted_by_Y = sorted(students, key = lambda x: (x['is_pass'], -x['Y_point'], x['index']))
for student in sorted_by_Y[:Y]:
    # print(x['is_pass'], student['index'], student['Y_point'])
    if student['is_pass']:
        continue
    win.append(student['index'])
    students[student['index']].update({'is_pass': True})
# print('-----------------')

sorted_by_Z = sorted(students, key = lambda x: (x['is_pass'], -x['Z_point'], x['index']))
for student in sorted_by_Z[:Z]:
    # print(x['is_pass'], student['index'], student['Z_point'])
    if student['is_pass']:
        continue
    win.append(student['index'])
    students[student['index']].update({'is_pass': True})
# print('=================')

win.sort()
for index in win:
    print(index + 1)
