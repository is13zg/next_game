import random
import collections
import itertools
import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt


main_ls=[(0, 0, 0, 0), (1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3), (4, 4, 4, 4), (5, 5, 5, 5), (6, 6, 6, 0), (7, 7, 0, 1), (0, 8, 1, 2), (1, 0, 2, 3), (2, 1, 3, 4), (3, 2, 4, 5), (4, 3, 5, 0), (5, 4, 6, 1), (6, 5, 0, 2), (7, 6, 1, 3), (0, 7, 2, 4), (1, 8, 3, 5), (2, 0, 4, 0), (3, 1, 5, 1), (4, 2, 6, 2), (5, 3, 0, 3), (6, 4, 1, 4), (7, 5, 2, 5), (0, 6, 3, 0), (1, 7, 4, 1), (2, 8, 5, 2), (3, 0, 6, 3), (4, 1, 0, 4), (5, 2, 1, 5), (6, 3, 2, 0), (7, 4, 3, 1), (0, 5, 4, 2), (1, 6, 5, 3), (2, 7, 6, 4), (3, 8, 0, 5), (4, 0, 1, 0), (5, 1, 2, 1), (6, 2, 3, 2), (7, 3, 4, 3), (0, 4, 5, 4), (1, 5, 6, 5), (2, 6, 0, 0), (3, 7, 1, 1), (4, 8, 2, 2), (5, 0, 3, 3), (6, 1, 4, 4), (7, 2, 5, 5), (0, 3, 6, 0), (1, 4, 0, 1), (2, 5, 1, 2), (3, 6, 2, 3), (4, 7, 3, 4), (5, 8, 4, 5), (6, 0, 5, 0), (7, 1, 6, 1), (0, 2, 0, 2), (1, 3, 1, 3), (2, 4, 2, 4), (3, 5, 3, 5), (4, 6, 4, 0), (5, 7, 5, 1), (6, 8, 6, 2), (7, 0, 0, 3), (0, 1, 1, 4), (1, 2, 2, 5), (2, 3, 3, 0), (3, 4, 4, 1), (4, 5, 5, 2), (5, 6, 6, 3), (6, 7, 0, 4), (7, 8, 1, 5), (0, 0, 2, 0), (1, 1, 3, 1), (2, 2, 4, 2), (3, 3, 5, 3), (4, 4, 6, 4), (5, 5, 0, 5), (6, 6, 1, 0), (7, 7, 2, 1), (0, 8, 3, 2), (1, 0, 4, 3), (2, 1, 5, 4), (3, 2, 6, 5), (4, 3, 0, 0), (5, 4, 1, 1), (6, 5, 2, 2), (7, 6, 3, 3), (0, 7, 4, 4), (1, 8, 5, 5), (2, 0, 6, 0), (3, 1, 0, 1), (4, 2, 1, 2), (5, 3, 2, 3), (6, 4, 3, 4), (7, 5, 4, 5), (0, 6, 5, 0), (1, 7, 6, 1), (2, 8, 0, 2), (3, 0, 1, 3)]
main_ls = [(0, 0, 0, 0), (1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3), (4, 4, 4, 4), (5, 5, 5, 5), (6, 6, 6, 0), (7, 7, 0, 1), (0, 8, 1, 2), (1, 0, 2, 3), (2, 1, 3, 4), (3, 2, 4, 5), (4, 3, 5, 0), (5, 4, 6, 1), (6, 5, 0, 2), (7, 6, 1, 3), (0, 7, 2, 4), (1, 8, 3, 5), (2, 0, 4, 0), (3, 1, 5, 1), (4, 2, 6, 2), (5, 3, 0, 3), (6, 4, 1, 4), (7, 5, 2, 5), (0, 6, 3, 0), (1, 7, 4, 1), (2, 8, 5, 2), (3, 0, 6, 3), (4, 1, 0, 4), (5, 2, 1, 5), (6, 3, 2, 0), (7, 4, 3, 1), (0, 5, 4, 2), (1, 6, 5, 3), (2, 7, 6, 4), (3, 8, 0, 5), (4, 0, 1, 0), (5, 1, 2, 1), (6, 2, 3, 2), (7, 3, 4, 3), (0, 4, 5, 4), (1, 5, 6, 5), (2, 6, 0, 0), (3, 7, 1, 1), (4, 8, 2, 2), (5, 0, 3, 3), (6, 1, 4, 4), (7, 2, 5, 5), (0, 3, 6, 0), (1, 4, 0, 1), (2, 5, 1, 2), (3, 6, 2, 3), (4, 7, 3, 4), (5, 8, 4, 5), (6, 0, 5, 0), (7, 1, 6, 1), (0, 2, 0, 2), (1, 3, 1, 3), (2, 4, 2, 4), (3, 5, 3, 5), (4, 6, 4, 0), (5, 7, 5, 1), (6, 8, 6, 2), (7, 0, 0, 3), (0, 1, 1, 4), (1, 2, 2, 5), (2, 3, 3, 0), (3, 4, 4, 1), (4, 5, 5, 2), (5, 6, 6, 3), (6, 7, 0, 4), (7, 8, 1, 5), (0, 0, 2, 0), (1, 1, 3, 1), (2, 2, 4, 2), (3, 3, 5, 3), (4, 4, 6, 4), (5, 5, 0, 5), (6, 6, 1, 0), (7, 7, 2, 1), (0, 8, 3, 2)]

tec_razdacha=[]



def is_a_then_b(aa,bb):
    if (aa[0]+1)%8 == bb[0]:
        return True
    if (aa[1]+1)%9 == bb[1]:
        return True
    if (aa[2]+1)%7 == bb[2]:
        return True
    if (aa[3]+1)%6 == bb[3]:
        return True
    return False

def get_ls_of_prop_next_elem(elem,ls):
    res = set()
    for i,x in enumerate(ls):
        if is_a_then_b(elem,x):
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
    all_paths=itertools.permutations(gr.keys())
    kol=0
    kol_of_correct_path=0
    for path in all_paths:
        kol+=1
        n1=path[0]
        have_path=True
        for n in path[1:]:
            if n in gr[n1]:
                n1=n
            else:
                have_path=False
                break
        if have_path:
            kol_of_correct_path+=1
    print(kol_of_correct_path,kol,kol_of_correct_path*100/kol)



def find_all_nodes_path(gr):
    all_paths=itertools.permutations(gr.keys())
    for path in all_paths:
        n1=path[0]
        have_path=True
        for n in path[1:]:
            if n in gr[n1]:
                n1=n
            else:
                have_path=False
                break
        if have_path:
            return (1,path)
    return (0,[])



gr_ex= {0: {4, 5, 7}, 1: {3}, 2: {0, 3, 4, 6, 7, 8}, 3: {2, 4, 5, 6, 7}, 4: {0, 1, 2, 6}, 5: {1, 2, 3, 6, 7}, 6: {0, 7}, 7: {8, 1, 6}, 8: {1, 2, 3, 4, 5, 7}}
tec_razdacha=[(2, 4, 2, 3), (2, 0, 6, 0), (6, 4, 1, 2), (7, 0, 0, 3), (7, 3, 4, 4), (5, 6, 6, 4), (7, 6, 1, 0), (7, 7, 2, 4), (5, 8, 4, 3)]


SIZE=9

count = 1
ok = 0
while count <= 100:
    t_ls = main_ls[:]
    random.shuffle(t_ls)
    tec_razdacha = t_ls[:SIZE]
    res = dict()
    for i, x in enumerate(tec_razdacha):
        res[i] = get_ls_of_prop_next_elem(x, tec_razdacha)
    # print(res)

    answer=find_all_nodes_path(res)
    #find_all_nodes_path2(res)
    ok+= answer[0]
    # print(answer[1])

    count += 1;
print(ok*100 /count)





