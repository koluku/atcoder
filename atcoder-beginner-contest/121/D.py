a, b = [int(x) for x in input().split()]


def xor(x):
    tmp = (x + 1) % 4
    if tmp == 0:
        return 0
    elif tmp == 1:
        return x
    elif tmp == 2:
        return 1
    else:
        return 1 ^ x


print(xor(a - 1) ^ xor(b))
