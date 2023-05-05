import random
import collections
import itertools
import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageDraw, ImageFont
from statistics import mode, median
from itertools import permutations
import pprint

# (a,b,c,d)
# какая фигура 0 уголник, 1 угольник и тд макс 7 уугольник 0..7 mod 8
# (0,1,2,3,4,5,6,7) - 8 шт
# кол-во фигур на карточке от 1 до 9  0..8  mod 9
# (1,2,3,4,5,6,7,8,9)- 9 шт
# цвет фигур от красного до фиолетового КОЖЗГСФ  0..6 mod 7
# (кр, ор, жлт, зел, глб, син, фил )- 7 шт
# тип закраски нет закраски, верт полосы, верт+гор, верт +гор+ 2 диагонали, полная закраска 0..5 mod 6
# ([нет], [верт], [верт + диаг], [верт + диаг + гор], [верт + диаг + гор + диаг2 ], [полн заливка]) - 6 шт

import cards_list

main_ls = cards_list.main_ls
perm_5_7 = list(permutations([0, 1, 2, 3, 4, 5, 6], 5))
perm_4_7 = list(permutations([0, 1, 2, 3, 4, 5, 6], 4))
perm_3_7 = list(permutations([0, 1, 2, 3, 4, 5, 6], 3))
perm_2_7 = list(permutations([0, 1, 2, 3, 4, 5, 6], 2))


def is_a_then_b(aa, bb, step=1):
    res = 0
    if (aa[0] + step) % 8 == bb[0]:
        res += 1
    if (aa[1] + step) % 9 == bb[1]:
        res += 1
    if (aa[2] + step) % 7 == bb[2]:
        res += 1
    if (aa[3] + step) % 6 == bb[3]:
        res += 1
    return res


def calc_score(tec_razdacha, ttype=0):
    scores = dict()
    t_score = 0
    t_stepeni = []
    for x in range(len(tec_razdacha) - 1):
        t_stepeni.append(is_a_then_b(tec_razdacha[x], tec_razdacha[x + 1]))
    scores["сумма степеней переходов"] = sum(t_stepeni) + 1
    scores["длина - 1  в степени"] = (len(tec_razdacha) - 1) ** min(t_stepeni) + 1 + sum(t_stepeni) - (
                len(tec_razdacha) - 1) * min(t_stepeni)
    scores["степени переходор"] = t_stepeni
    if 0 in t_stepeni:
        scores["сумма степеней переходов"] = 0
        scores["длина - 1  в степени"] = 0
        scores["степени переходор"] = 0
    if ttype == 0:
        return scores["сумма степеней переходов"]
    else:
        return scores


def draw_ans(answer):
    if len(answer) > 9:
        print("too long")
        return
    t_ls = answer
    while len(t_ls) < 9:
        t_ls.append((0, 0, 0, 0))

    mim = Image.new('RGBA', (1297 * 3, 1836 * 3), "white")

    pim = Image.open(f"res\{t_ls[0][0]}_{t_ls[0][1]}_{t_ls[0][2]}_{t_ls[0][3]}.png")
    mim.paste(pim, (1297 * 0, 1836 * 0), pim)

    pim = Image.open(f"res\{t_ls[1][0]}_{t_ls[1][1]}_{t_ls[1][2]}_{t_ls[1][3]}.png")
    mim.paste(pim, (1297 * 1, 1836 * 0), pim)

    pim = Image.open(f"res\{t_ls[2][0]}_{t_ls[2][1]}_{t_ls[2][2]}_{t_ls[2][3]}.png")
    mim.paste(pim, (1297 * 2, 1836 * 0), pim)

    pim = Image.open(f"res\{t_ls[3][0]}_{t_ls[3][1]}_{t_ls[3][2]}_{t_ls[3][3]}.png")
    mim.paste(pim, (1297 * 0, 1836 * 1), pim)

    pim = Image.open(f"res\{t_ls[4][0]}_{t_ls[4][1]}_{t_ls[4][2]}_{t_ls[4][3]}.png")
    mim.paste(pim, (1297 * 1, 1836 * 1), pim)

    pim = Image.open(f"res\{t_ls[5][0]}_{t_ls[5][1]}_{t_ls[5][2]}_{t_ls[5][3]}.png")
    mim.paste(pim, (1297 * 2, 1836 * 1), pim)

    pim = Image.open(f"res\{t_ls[6][0]}_{t_ls[6][1]}_{t_ls[6][2]}_{t_ls[6][3]}.png")
    mim.paste(pim, (1297 * 0, 1836 * 2), pim)

    pim = Image.open(f"res\{t_ls[7][0]}_{t_ls[7][1]}_{t_ls[7][2]}_{t_ls[7][3]}.png")
    mim.paste(pim, (1297 * 1, 1836 * 2), pim)

    pim = Image.open(f"res\{t_ls[8][0]}_{t_ls[8][1]}_{t_ls[8][2]}_{t_ls[8][3]}.png")
    mim.paste(pim, (1297 * 2, 1836 * 2), pim)

    draw = ImageDraw.Draw(mim)
    draw.line((1297 * 1, 1836 * 0, 1297 * 1, 1836 * 3), fill="black", width=8)
    draw.line((1297 * 2, 1836 * 0, 1297 * 2, 1836 * 3), fill="black", width=8)
    draw.line((1297 * 0, 1836 * 1, 1297 * 3, 1836 * 1), fill="black", width=8)
    draw.line((1297 * 0, 1836 * 2, 1297 * 3, 1836 * 2), fill="black", width=8)

    bg = Image.new("RGB", mim.size, (255, 255, 255))
    bg.paste(mim, mask=mim.split()[3])
    bg.show()
    bg.save("answer.jpg")
    # bg.save(f"res2\{i}.jpg", quality=100, subsampling=0)


def test(N=1000, vikladka=7):
    print(f"start test N={N} Size={vikladka}")
    SIZE = vikladka
    count = 0
    equal_count = 0

    while count < N:
        # print(f"count={count}")
        t_ls = main_ls[:]
        random.shuffle(t_ls)
        tec_razdacha = t_ls[:SIZE]
        res_dict = dict()
        res_dict["посумме"] = (0, [])
        res_dict["длина - 1  в степени"] = (0, [])

        for index_list in perm_5_7:
            res_list = [tec_razdacha[i] for i in index_list]
            tres = calc_score(res_list, ttype=1)
            if tres["сумма степеней переходов"] > res_dict["посумме"][0]:
                res_dict["посумме"] = (tres["сумма степеней переходов"], res_list, tres["степени переходор"])
            if tres["длина - 1  в степени"] > res_dict["длина - 1  в степени"][0]:
                res_dict["длина - 1  в степени"] = (tres["длина - 1  в степени"], res_list, tres["степени переходор"])

        for index_list in perm_4_7:
            res_list = [tec_razdacha[i] for i in index_list]
            tres = calc_score(res_list, ttype=1)
            if tres["сумма степеней переходов"] > res_dict["посумме"][0]:
                res_dict["посумме"] = (tres["сумма степеней переходов"], res_list, tres["степени переходор"])
            if tres["длина - 1  в степени"] > res_dict["длина - 1  в степени"][0]:
                res_dict["длина - 1  в степени"] = (tres["длина - 1  в степени"], res_list, tres["степени переходор"])

        for index_list in perm_3_7:
            res_list = [tec_razdacha[i] for i in index_list]
            tres = calc_score(res_list, ttype=1)
            if tres["сумма степеней переходов"] > res_dict["посумме"][0]:
                res_dict["посумме"] = (tres["сумма степеней переходов"], res_list, tres["степени переходор"])
            if tres["длина - 1  в степени"] > res_dict["длина - 1  в степени"][0]:
                res_dict["длина - 1  в степени"] = (tres["длина - 1  в степени"], res_list, tres["степени переходор"])

        for index_list in perm_2_7:
            res_list = [tec_razdacha[i] for i in index_list]
            tres = calc_score(res_list, ttype=1)
            if tres["сумма степеней переходов"] > res_dict["посумме"][0]:
                res_dict["посумме"] = (tres["сумма степеней переходов"], res_list, tres["степени переходор"])
            if tres["длина - 1  в степени"] > res_dict["длина - 1  в степени"][0]:
                res_dict["длина - 1  в степени"] = (tres["длина - 1  в степени"], res_list, tres["степени переходор"])
        count += 1
        print(res_dict)
        if res_dict["длина - 1  в степени"][0] == res_dict["посумме"][0]:
            equal_count+=1
    print(equal_count)
        # pprint.pprint(res_dict)
        # draw_ans(res_dict["посумме"][1])
        # draw_ans(res_dict["длина в степени"][1])


# test()
draw_ans([(7, 8, 1, 5), (0, 6, 5, 0), (2, 7, 6, 4), (3, 2, 6, 5)])
# draw_ans([(2, 0, 6, 0), (3, 1, 5, 1)])
# draw_ans([(4, 6, 4, 0), (5, 7, 5, 1), (6, 0, 5, 0), (7, 4, 3, 1), (0, 7, 4, 4)])