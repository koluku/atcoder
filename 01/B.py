km = int(input())/1000

if km < 0.1:
    vv = 0
if 1 <= km <= 5:
    vv = km * 10
if 6 <= km <= 30:
    vv = km + 50
if 35 <= km <= 70:
    vv = (km - 30) / 5 + 80
if 70 < km:
    vv = 89

print(str(int(vv)).zfill(2))
