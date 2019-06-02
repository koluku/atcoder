s = input()
if s.count("o") > 7:
    print("YES")
elif 8 - s.count("o") <= 15 - len(s):
    print("YES")
else:
    print("NO")
