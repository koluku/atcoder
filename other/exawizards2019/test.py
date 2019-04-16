n, q = [int(x) for x in input().split()]
room = list(input())
magics = [[x for x in input().split()] for i in range(q)]
golems = [1 for x in range(n)]

for magic, dirc in magics:
    target_golems = [i for i, x in enumerate(room) if x == magic]
    if dirc == "R":
        target_golems.sort(reverse=True)
    for golem_id in target_golems:
        if (golem_id == 0 and dirc == "L") or (golem_id == n - 1 and dirc == "R"):
            pass
        elif dirc == "L":
            golems[golem_id - 1] += golems[golem_id]
        elif dirc == "R":
            golems[golem_id + 1] += golems[golem_id]
        golems[golem_id] = 0
print(sum(golems))
