from PIL import Image
from PIL import ImageDraw, ImageFont

import cards_list

main_ls = cards_list.main_ls


# (a,b,c,d)
# какая фигура 0 уголник, 1 угольник и тд макс 7 уугольник 0..7 mod 8
# (0,1,2,3,4,5,6,7) - 8 шт
# кол-во фигур на карточке от 1 до 9  0..8  mod 9
# (1,2,3,4,5,6,7,8,9)- 9 шт
# цвет фигур от красного до фиолетового КОЖЗГСФ  0..6 mod 7
# (кр, ор, жлт, зел, глб, син, фил )- 7 шт
# тип закраски нет закраски, верт полосы, верт+гор, верт +гор+ 2 диагонали, полная закраска 0..5 mod 6
# ([нет], [верт], [верт + диаг], [верт + диаг + гор], [верт + диаг + гор + диаг2 ], [полн заливка]) - 6 шт
def card_by_num(num):
    return main_ls[num - 1]


def num_by_card(card):
    if type(card) == str:
        card = tuple(map(int, card.split("_")))
    return main_ls.index(card) + 1


def mf():
    iw = 1186  # 1297
    ih = 1762  # 1925  # ih
    line = 18

    main_ls = cards_list.main_ls

    page_cards_count = int(len(main_ls) / 9)

    t_ls = []
    to_pdf_ls = []
    f_im = None
    for i in range(page_cards_count):
        t_ls = main_ls[i * 9:(i + 1) * 9]
        print(*t_ls)
        print(i * 9, (i + 1) * 9)
        mim = Image.new('RGBA', (1297 * 3, 1925 * 3), "white")

        pim = Image.open(f"res\{t_ls[0][0]}_{t_ls[0][1]}_{t_ls[0][2]}_{t_ls[0][3]}.png")
        mim.paste(pim, ((iw + line) * 0, (ih + line) * 0), pim)

        pim = Image.open(f"res\{t_ls[1][0]}_{t_ls[1][1]}_{t_ls[1][2]}_{t_ls[1][3]}.png")
        mim.paste(pim, ((iw + line) * 1, (ih + line) * 0), pim)

        pim = Image.open(f"res\{t_ls[2][0]}_{t_ls[2][1]}_{t_ls[2][2]}_{t_ls[2][3]}.png")
        mim.paste(pim, ((iw + line) * 2, (ih + line) * 0), pim)

        pim = Image.open(f"res\{t_ls[3][0]}_{t_ls[3][1]}_{t_ls[3][2]}_{t_ls[3][3]}.png")
        mim.paste(pim, ((iw + line) * 0, (ih + line) * 1), pim)

        pim = Image.open(f"res\{t_ls[4][0]}_{t_ls[4][1]}_{t_ls[4][2]}_{t_ls[4][3]}.png")
        mim.paste(pim, ((iw + line) * 1, (ih + line) * 1), pim)

        pim = Image.open(f"res\{t_ls[5][0]}_{t_ls[5][1]}_{t_ls[5][2]}_{t_ls[5][3]}.png")
        mim.paste(pim, ((iw + line) * 2, (ih + line) * 1), pim)

        pim = Image.open(f"res\{t_ls[6][0]}_{t_ls[6][1]}_{t_ls[6][2]}_{t_ls[6][3]}.png")
        mim.paste(pim, ((iw + line) * 0, (ih + line) * 2), pim)

        pim = Image.open(f"res\{t_ls[7][0]}_{t_ls[7][1]}_{t_ls[7][2]}_{t_ls[7][3]}.png")
        mim.paste(pim, ((iw + line) * 1, (ih + line) * 2), pim)

        pim = Image.open(f"res\{t_ls[8][0]}_{t_ls[8][1]}_{t_ls[8][2]}_{t_ls[8][3]}.png")
        mim.paste(pim, ((iw + line) * 2, (ih + line) * 2), pim)

        draw = ImageDraw.Draw(mim)
        draw.line((iw * 1, ih * 0, iw * 1, ih * 3), fill="black", width=8)
        draw.line((iw * 2 + line, ih * 0, iw * 2 + line, ih * 3), fill="black", width=8)
        draw.line((iw * 0, ih * 1, iw * 3, ih * 1), fill="black", width=8)
        draw.line((iw * 0, ih * 2 + line, iw * 3, ih * 2 + line), fill="black", width=8)

        bg = Image.new("RGB", mim.size, (255, 255, 255))
        bg.paste(mim, mask=mim.split()[3])

        to_pdf_ls.append(bg)
        bg.save(f"res2\{i}.jpg", quality=100, subsampling=0)

    f_im = Image.open("res2/0.jpg")
    to_pdf_ls = to_pdf_ls[1:]
    f_im.save("res2\mainpdf.pdf", "PDF", resolution=100.0, save_all=True, append_images=to_pdf_ls)

mf()