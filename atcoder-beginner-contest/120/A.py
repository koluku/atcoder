import math
a, b, c = [int(x) for x in input().split()]
if a*c <= b:
    print(math.floor(c))
else:
    print(math.floor(b/a))
