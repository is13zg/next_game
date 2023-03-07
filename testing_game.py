import random
import collections
import itertools
import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageDraw, ImageFont
from statistics import mode, median

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

tec_razdacha = []


def draw_graph(gr):
    graph = nx.DiGraph()
    for x in gr.keys():
        for xx in gr[x]:
            graph.add_edge(x, xx, weight=1)
    nx.draw_circular(graph,
                     node_color='red',
                     node_size=1000,
                     with_labels=True)
    plt.show()


def card_by_num(num):
    return main_ls[num - 1]


def num_by_card(card):
    if type(card) == str:
        card = tuple(map(int, card.split("_")))
    return main_ls.index(card) + 1


def is_a_then_b(aa, bb):
    if (aa[0] + 1) % 8 == bb[0]:
        return True
    if (aa[1] + 1) % 9 == bb[1]:
        return True
    if (aa[2] + 1) % 7 == bb[2]:
        return True
    if (aa[3] + 1) % 6 == bb[3]:
        return True
    return False


def get_kind_then(aa, bb):
    if (aa[0] + 1) % 8 == bb[0]:
        return "форма"
    if (aa[1] + 1) % 9 == bb[1]:
        return "кол-во"
    if (aa[2] + 1) % 7 == bb[2]:
        return "цвет"
    if (aa[3] + 1) % 6 == bb[3]:
        return "закраска"
    return False

def get_count_then(aa, bb):
    c = 0
    if (aa[0] + 1) % 8 == bb[0]:
        c += 1
    if (aa[1] + 1) % 9 == bb[1]:
        c += 1
    if (aa[2] + 1) % 7 == bb[2]:
        c += 1
    if (aa[3] + 1) % 6 == bb[3]:
        c += 1
    return c


def get_ls_of_prop_next_elem(elem, ls):
    res = set()
    for i, x in enumerate(ls):
        if is_a_then_b(elem, x):
            res.add(i)
    return res


def count_prob():
    count = 1
    ok = 0
    while count < 1000000:
        ind_1 = random.randint(0, 99)
        ind_2 = random.randint(0, 99)
        if (is_a_then_b(main_ls[ind_1], main_ls[ind_2])):
            ok += 1;
        count += 1;
    print(ok / 10)


def find_all_nodes_path2(gr):
    all_paths = itertools.permutations(gr.keys())
    kol = 0
    kol_of_correct_path = 0
    for path in all_paths:
        kol += 1
        n1 = path[0]
        have_path = True
        for n in path[1:]:
            if n in gr[n1]:
                n1 = n
            else:
                have_path = False
                break
        if have_path:
            kol_of_correct_path += 1
    print(kol_of_correct_path, kol, kol_of_correct_path * 100 / kol)


def find_all_nodes_path(gr):
    all_paths = itertools.permutations(gr.keys())
    max_path_len = 0
    for path in all_paths:

        path_len = 1
        n1 = path[0]
        have_path = True
        for n in path[1:]:
            if n in gr[n1]:
                n1 = n
                path_len += 1
            else:
                have_path = False
                if path_len > max_path_len:
                    max_path_len = path_len
                path_len = 0
                break
        if have_path:
            return (1, path, path_len)
    return (0, [], max_path_len)


def get_max_path(data):
    if type(data) == str:
        if "_" in data:
            data = list(map(int, data.split("_")))
        else:
            data = list(map(int, data.split(" ")))

    data = list(map(int, data))
    data = list(map(card_by_num, data))
    res = dict()
    for i, x in enumerate(data):
        res[i] = get_ls_of_prop_next_elem(x, data)
    # draw_graph(res)
    answer = find_all_nodes_path(res)
    print(answer)
    cards_number = list(map(num_by_card, data))
    path_answer = [cards_number[i] for i in answer[1]]
    print(f"path: {path_answer}")

    print(f"[{path_answer[0]}]", end=" ")
    for x in range(len(path_answer))[1:]:
        # print(x)
        print(get_kind_then(data[answer[1][x - 1]], data[answer[1][x]]), end=" ")
        print(f"[{path_answer[x]}]", end=" ")
    print()
    draw_ans([data[i] for i in answer[1]])

    gr2 = dict()
    for key in res.keys():
        td = set()
        for num in res[key]:
            td.add(path_answer[answer[1].index(num)])
        gr2[path_answer[answer[1].index(key)]] = td
    print(gr2)
    draw_graph(gr2)


def test(N=1000, vikladka=9):
    print(f"start test N={N} Size={vikladka}")
    SIZE = vikladka
    count = 0
    ok = 0
    res_dict = dict()
    while count < N:
        # print(f"count={count}")
        t_ls = main_ls[:]
        random.shuffle(t_ls)
        tec_razdacha = t_ls[:SIZE]
        res = dict()
        for i, x in enumerate(tec_razdacha):
            res[i] = get_ls_of_prop_next_elem(x, tec_razdacha)
        # print("graphs:", res)

        answer = find_all_nodes_path(res)
        res_dict[answer[2]] = res_dict.get(answer[2], 0) + 1
        # find_all_nodes_path2(res)
        ok += answer[0]
        # print(answer[1])

        count += 1
    print(ok, count)
    print(ok * 100 / count)
    print(res_dict)


def draw_ans(answer):
    if len(answer)>9:
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
    # bg.save(f"res2\{i}.jpg", quality=100, subsampling=0)


# запуск теста с тек картами, карты в файле card_list.py
# test()
main_ls = cards_list.main_lsr
res = dict()
for x in range(len(main_ls) -1):
    res[x] = get_count_then(main_ls[x], main_ls[x+1])
print(res)
print(max(res.values()))
print(min(res.values()))
print(median(res.values()))
print(mode(res.values()))
exit()


# подсчет кол-ва следующих элементов, моды , медианы
main_ls = cards_list.main_ls
print(len(main_ls))
res = dict()
res2= dict()
for i, x in enumerate(main_ls):
    res[i] = get_ls_of_prop_next_elem(x, main_ls)
for x in res.keys():
    res2[x]=len(res[x])
print(res2)
print(max(res2.values()))
print(min(res2.values()))
print(median(res2.values()))
print(mode(res2.values()))

exit(0)
# данный код показывает какискать путь для нужного набора
t_ls = main_ls[:]
random.shuffle(t_ls)
tec_razdacha = t_ls[:8]
print(len(tec_razdacha), tec_razdacha)
tec_razdacha = list(map(num_by_card, tec_razdacha))
print(f"tec_razdacha {tec_razdacha}")
# get_max_path([60, 12, 6, 16, 35, 68, 63])
# get_max_path("1 2 10 12")
get_max_path(tec_razdacha)

exit()

# приер графа
gr_ex = {0: {4, 5, 7}, 1: {3}, 2: {0, 3, 4, 6, 7, 8}, 3: {2, 4, 5, 6, 7}, 4: {0, 1, 2, 6}, 5: {1, 2, 3, 6, 7},
         6: {0, 7}, 7: {8, 1, 6}, 8: {1, 2, 3, 4, 5, 7}}

