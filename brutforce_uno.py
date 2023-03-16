import random


def gen_cards():
    res = list()
    for i in range(0, 1):
        for j in range(1, 5):
            res.append((i, j))

    for i in range(1, 13):
        for j in range(1, 5):
            res.append((i, j))
            res.append((i, j))
    res.extend([(20, 0), (20, 0), (20, 0), (20, 0), (20, 0), (20, 0), (20, 0), (20, 0)])
    return res


def have_card(tec, mycards):
    for x in mycards:
        if x[0] == tec[0] or x[1] == tec[1]:
            return x
    for x in mycards:
        if x[1] == 0:
            return x
    return None


def action(tec, mycards):
    global mainls, found_card, actions_count, not_found_card
    actions_count += 1
    x = have_card(tec, mycards)
    if x:
        found_card += 1
        mycards.remove(x)
        if x[0] == 20:
            return (20, random.randint(1, 4))
        else:
            return x
    else:
        not_found_card += 1
        mycards.append(mainls[0])
        mainls = mainls[1:]
        return tec


actions_count = 0
found_card = 0
not_found_card = 0
pl_win = 0
cards_over = 0

for x in range(1, 10000):
    mainls = gen_cards()
    random.shuffle(mainls)

    p1 = mainls[:7]
    mainls = mainls[7:]
    p2 = mainls[:7]
    mainls = mainls[7:]
    p3 = mainls[:7]
    mainls = mainls[7:]
    coloda = mainls[0]
    mainls = mainls[1:]

    while len(mainls) > 0:
        # print(f"tec = {coloda}")
        if len(p1) == 0:
            # print("p1 0")
            break
        if len(p2) == 0:
            # print("p2 0")
            break
        if len(p3) == 0:
            # print("p3 0")
            break
        # print(len(mainls))
        # print(f"p1 {p1}", f"p2 {p2}", f"p3 {p3}", sep="\n")
        coloda = action(coloda, p1)
        if len(mainls)== 0:
            break
        # print(f"tec = {coloda}")
        coloda = action(coloda, p2)
        if len(mainls) == 0:
            break
        # print(f"tec = {coloda}")
        coloda = action(coloda, p3)
        if len(mainls) == 0:
            break
        # print(f"tec = {coloda}")
    if len(mainls) == 0:
        cards_over += 1
    else:
        pl_win += 1

print(f"actions {actions_count}, found {found_card}, not_found {not_found_card}", sep="\n")
print(f"plwin {pl_win}, cards_over {cards_over}")
print(f"find_card {found_card/actions_count*100} not_find {not_found_card/actions_count*100}")