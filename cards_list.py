import random

main_ls1 = [(0, 0, 0, 0), (1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3), (4, 4, 4, 4), (5, 5, 5, 5), (6, 6, 6, 0),
           (7, 7, 0, 1), (0, 8, 1, 2), (1, 0, 2, 3), (2, 1, 3, 4), (3, 2, 4, 5), (4, 3, 5, 0), (5, 4, 6, 1),
           (6, 5, 0, 2), (7, 6, 1, 3), (0, 7, 2, 4), (1, 8, 3, 5), (2, 0, 4, 0), (3, 1, 5, 1), (4, 2, 6, 2),
           (5, 3, 0, 3), (6, 4, 1, 4), (7, 5, 2, 5), (0, 6, 3, 0), (1, 7, 4, 1), (2, 8, 5, 2), (3, 0, 6, 3),
           (4, 1, 0, 4), (5, 2, 1, 5), (6, 3, 2, 0), (7, 4, 3, 1), (0, 5, 4, 2), (1, 6, 5, 3), (2, 7, 6, 4),
           (3, 8, 0, 5), (4, 0, 1, 0), (5, 1, 2, 1), (6, 2, 3, 2), (7, 3, 4, 3), (0, 4, 5, 4), (1, 5, 6, 5),
           (2, 6, 0, 0), (3, 7, 1, 1), (4, 8, 2, 2), (5, 0, 3, 3), (6, 1, 4, 4), (7, 2, 5, 5), (0, 3, 6, 0),
           (1, 4, 0, 1), (2, 5, 1, 2), (3, 6, 2, 3), (4, 7, 3, 4), (5, 8, 4, 5), (6, 0, 5, 0), (7, 1, 6, 1),
           (0, 2, 0, 2), (1, 3, 1, 3), (2, 4, 2, 4), (3, 5, 3, 5), (4, 6, 4, 0), (5, 7, 5, 1), (6, 8, 6, 2),
           (7, 0, 0, 3), (0, 1, 1, 4), (1, 2, 2, 5), (2, 3, 3, 0), (3, 4, 4, 1), (4, 5, 5, 2), (5, 6, 6, 3),
           (6, 7, 0, 4), (7, 8, 1, 5), (0, 0, 2, 0), (1, 1, 3, 1), (2, 2, 4, 2), (3, 3, 5, 3), (4, 4, 6, 4),
           (5, 5, 0, 5), (6, 6, 1, 0), (7, 7, 2, 1), (0, 8, 3, 2), (1, 0, 4, 3), (2, 1, 5, 4), (3, 2, 6, 5),
           (4, 3, 0, 0), (5, 4, 1, 1), (6, 5, 2, 2), (7, 6, 3, 3), (0, 7, 4, 4), (1, 8, 5, 5), (2, 0, 6, 0),
           (3, 1, 0, 1), (4, 2, 1, 2), (5, 3, 2, 3), (6, 4, 3, 4), (7, 5, 4, 5), (0, 6, 5, 0), (1, 7, 6, 1),
           (2, 8, 0, 2), (3, 0, 1, 3)]
main_ls2 = [(0, 0, 0, 0), (1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3), (4, 4, 4, 4), (5, 5, 5, 5), (6, 6, 6, 0),
           (7, 7, 0, 1), (0, 8, 1, 2), (1, 0, 2, 3), (2, 1, 3, 4), (3, 2, 4, 5), (4, 3, 5, 0), (5, 4, 6, 1),
           (6, 5, 0, 2), (7, 6, 1, 3), (0, 7, 2, 4), (1, 8, 3, 5), (2, 0, 4, 0), (3, 1, 5, 1), (4, 2, 6, 2),
           (5, 3, 0, 3), (6, 4, 1, 4), (7, 5, 2, 5), (0, 6, 3, 0), (1, 7, 4, 1), (2, 8, 5, 2), (3, 0, 6, 3),
           (4, 1, 0, 4), (5, 2, 1, 5), (6, 3, 2, 0), (7, 4, 3, 1), (0, 5, 4, 2), (1, 6, 5, 3), (2, 7, 6, 4),
           (3, 8, 0, 5), (4, 0, 1, 0), (5, 1, 2, 1), (6, 2, 3, 2), (7, 3, 4, 3), (0, 4, 5, 4), (1, 5, 6, 5),
           (2, 6, 0, 0), (3, 7, 1, 1), (4, 8, 2, 2), (5, 0, 3, 3), (6, 1, 4, 4), (7, 2, 5, 5), (0, 3, 6, 0),
           (1, 4, 0, 1), (2, 5, 1, 2), (3, 6, 2, 3), (4, 7, 3, 4), (5, 8, 4, 5), (6, 0, 5, 0), (7, 1, 6, 1),
           (0, 2, 0, 2), (1, 3, 1, 3), (2, 4, 2, 4), (3, 5, 3, 5), (4, 6, 4, 0), (5, 7, 5, 1), (6, 8, 6, 2),
           (7, 0, 0, 3), (0, 1, 1, 4), (1, 2, 2, 5), (2, 3, 3, 0), (3, 4, 4, 1), (4, 5, 5, 2), (5, 6, 6, 3),
           (6, 7, 0, 4), (7, 8, 1, 5), (0, 0, 2, 0), (1, 1, 3, 1), (2, 2, 4, 2), (3, 3, 5, 3), (4, 4, 6, 4),
           (5, 5, 0, 5), (6, 6, 1, 0), (7, 7, 2, 1), (0, 8, 3, 2)]

# набор чтобы не было близких по параметрам
main_ls = [(1, 0, 4, 3), (2, 1, 5, 4), (3, 2, 6, 5), (4, 3, 0, 0), (5, 4, 1, 1), (6, 5, 2, 2), (7, 6, 3, 3),
           (0, 7, 4, 4), (1, 8, 5, 5), (2, 0, 6, 0), (3, 1, 0, 1), (4, 2, 1, 2), (5, 3, 2, 3), (6, 4, 3, 4),
           (7, 5, 4, 5), (0, 6, 5, 0), (1, 7, 6, 1), (2, 8, 0, 2), (2, 0, 4, 0), (3, 1, 5, 1),
           (4, 2, 6, 2), (5, 3, 0, 3), (6, 4, 1, 4), (7, 5, 2, 5), (0, 6, 3, 0), (1, 7, 4, 1), (2, 8, 5, 2),
           (3, 0, 6, 3), (4, 1, 0, 4), (5, 2, 1, 5), (6, 3, 2, 0), (7, 4, 3, 1), (0, 5, 4, 2), (1, 6, 5, 3),
           (2, 7, 6, 4), (3, 8, 0, 5), (4, 0, 1, 0), (5, 1, 2, 1), (6, 2, 3, 2), (7, 3, 4, 3), (0, 4, 5, 4),
           (1, 5, 6, 5), (2, 6, 0, 0), (3, 7, 1, 1), (4, 8, 2, 2), (5, 0, 3, 3), (6, 1, 4, 4), (7, 2, 5, 5),
           (0, 3, 6, 0), (1, 4, 0, 1), (2, 5, 1, 2), (3, 6, 2, 3), (4, 7, 3, 4), (5, 8, 4, 5), (6, 0, 5, 0),
           (7, 1, 6, 1), (0, 2, 0, 2), (1, 3, 1, 3), (2, 4, 2, 4), (3, 5, 3, 5), (4, 6, 4, 0), (5, 7, 5, 1),
           (6, 8, 6, 2), (7, 0, 0, 3), (0, 1, 1, 4), (1, 2, 2, 5), (2, 3, 3, 0), (3, 4, 4, 1), (4, 5, 5, 2),
           (5, 6, 6, 3), (6, 7, 0, 4), (7, 8, 1, 5), (0, 0, 2, 0), (1, 1, 3, 1), (2, 2, 4, 2), (3, 3, 5, 3),
           (4, 4, 6, 4), (5, 5, 0, 5), (6, 6, 1, 0), (7, 7, 2, 1), (0, 8, 3, 2)]

# перемешанный набор
main_lsr = [(4, 1, 0, 4), (7, 5, 4, 5), (3, 8, 0, 5), (5, 6, 6, 3), (7, 1, 6, 1), (6, 2, 3, 2), (0, 8, 3, 2),
           (1, 4, 0, 1), (1, 5, 6, 5), (4, 8, 2, 2), (3, 0, 6, 3), (3, 7, 1, 1), (2, 0, 6, 0), (3, 5, 3, 5),
           (1, 1, 3, 1), (2, 8, 5, 2), (4, 0, 1, 0), (4, 5, 5, 2), (6, 1, 4, 4), (5, 3, 2, 3), (7, 4, 3, 1),
           (0, 1, 1, 4), (3, 3, 5, 3), (3, 1, 0, 1), (4, 2, 1, 2), (1, 3, 1, 3), (2, 7, 6, 4), (0, 0, 2, 0),
           (2, 4, 2, 4), (5, 2, 1, 5), (7, 6, 3, 3), (0, 3, 6, 0), (2, 2, 4, 2), (4, 4, 6, 4), (3, 6, 2, 3),
           (2, 6, 0, 0), (0, 5, 4, 2), (6, 3, 2, 0), (6, 8, 6, 2), (7, 0, 0, 3), (6, 4, 3, 4), (0, 6, 3, 0),
           (5, 8, 4, 5), (4, 3, 0, 0), (3, 2, 6, 5), (4, 7, 3, 4), (6, 4, 1, 4), (5, 5, 0, 5), (7, 7, 2, 1),
           (5, 7, 5, 1), (2, 1, 5, 4), (2, 0, 4, 0), (7, 3, 4, 3), (6, 5, 2, 2), (0, 6, 5, 0), (5, 0, 3, 3),
           (5, 1, 2, 1), (7, 8, 1, 5), (0, 7, 4, 4), (6, 0, 5, 0), (5, 3, 0, 3), (5, 4, 1, 1), (2, 3, 3, 0),
           (3, 4, 4, 1), (0, 2, 0, 2), (3, 1, 5, 1), (2, 5, 1, 2), (1, 6, 5, 3), (6, 7, 0, 4), (1, 8, 5, 5),
           (1, 7, 4, 1), (1, 2, 2, 5), (2, 8, 0, 2), (4, 2, 6, 2), (0, 4, 5, 4), (6, 6, 1, 0), (4, 6, 4, 0),
           (7, 2, 5, 5), (1, 0, 4, 3), (1, 7, 6, 1), (7, 5, 2, 5)]


