import re

input_string = input()
keyence = "keyence"
patterns = [
    "^.*(keyence)$",
    "^k.*eyence$",
    "^ke.*yence$",
    "^key.*ence$",
    "^keye.*nce$",
    "^keyen.*ce$",
    "^keyenc.*e$",
    "^keyence.*$",
]
flag = False
for i in range(len(patterns)):
    result = re.match(patterns[i], input_string)
    if result:
        flag = True
        break
if flag == True:
    print("YES")
else:
    print("NO")
