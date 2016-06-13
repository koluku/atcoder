deg, dis = map(int, input().split())

dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
wps = [2, 15, 33, 54, 79, 107, 138, 171, 207, 244, 284, 326]

w = 0
for n in wps:
    if int(dis/6 + 0.5) > n:
        w += 1
dir = dirs[(deg * 10 +1125) % 36000 // 2250] if w > 0 else "C"

print(dir, w)
