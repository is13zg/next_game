from PIL import Image
from PIL import ImageDraw, ImageFont
import cards_list

ih = 1297
iw = 1925  # 1836


def draw_9(name):
    mim = Image.new('RGBA', (ih, iw), "white")
    pim = Image.open(name)
    mim.paste(pim, (-2, 20), pim)
    mim.paste(pim, (-2, 575), pim)
    mim.paste(pim, (-2, 1115), pim)

    mim.paste(pim, (815, 20), pim)
    mim.paste(pim, (815, 575), pim)
    mim.paste(pim, (815, 1115), pim)

    mim.paste(pim, (408, 277), pim)
    mim.paste(pim, (408, 844), pim)
    mim.paste(pim, (408, 1350), pim)
    return mim


def draw_8(name):
    mim = Image.new('RGBA', (ih, iw), "white")
    pim = Image.open(name)
    mim.paste(pim, (-20, 25), pim)
    mim.paste(pim, (-20, 665), pim)
    mim.paste(pim, (-20, 1320), pim)

    mim.paste(pim, (810, 25), pim)
    mim.paste(pim, (810, 665), pim)
    mim.paste(pim, (810, 1320), pim)

    mim.paste(pim, (395, 350), pim)
    mim.paste(pim, (395, 1000), pim)
    return mim


def draw_7(name):
    mim = Image.new('RGBA', (ih, iw), "white")
    pim = Image.open(name)

    mim.paste(pim, (395, 5), pim)
    mim.paste(pim, (395, 675), pim)
    mim.paste(pim, (395, 1320), pim)

    mim.paste(pim, (40, 345), pim)
    mim.paste(pim, (40, 995), pim)

    mim.paste(pim, (770, 345), pim)
    mim.paste(pim, (770, 995), pim)
    return mim


def draw_6(name):
    mim = Image.new('RGBA', (ih, iw), "white")
    pim = Image.open(name)

    mim.paste(pim, (50, 70), pim)
    mim.paste(pim, (745, 70), pim)

    mim.paste(pim, (400, 410), pim)
    mim.paste(pim, (400, 920), pim)

    mim.paste(pim, (50, 1270), pim)
    mim.paste(pim, (745, 1270), pim)
    return mim


def draw_5(name):
    mim = Image.new('RGBA', (ih, iw), "white")
    pim = Image.open(name)

    mim.paste(pim, (55, 150), pim)
    mim.paste(pim, (755, 150), pim)

    mim.paste(pim, (55, 1185), pim)
    mim.paste(pim, (755, 1185), pim)

    mim.paste(pim, (400, 670), pim)
    return mim


def draw_4(name):
    mim = Image.new('RGBA', (ih, iw), "white")
    pim = Image.open(name)

    mim.paste(pim, (75, 200), pim)
    mim.paste(pim, (725, 200), pim)

    mim.paste(pim, (75, 1050), pim)
    mim.paste(pim, (725, 1050), pim)

    return mim


def draw_3(name):
    mim = Image.new('RGBA', (ih, iw), "white")
    pim = Image.open(name)

    mim.paste(pim, (400, 110), pim)
    mim.paste(pim, (400, 635), pim)
    mim.paste(pim, (400, 1175), pim)
    return mim


def draw_2(name):
    mim = Image.new('RGBA', (ih, iw), "white")
    pim = Image.open(name)

    mim.paste(pim, (400, 310), pim)
    mim.paste(pim, (400, 1075), pim)
    return mim


def draw_2(name):
    mim = Image.new('RGBA', (ih, iw), "white")
    pim = Image.open(name)

    mim.paste(pim, (400, 310), pim)
    mim.paste(pim, (400, 1075), pim)
    return mim


def draw_1(name):
    mim = Image.new('RGBA', (ih, iw), "white")
    pim = Image.open(name)
    mim.paste(pim, (400, 670), pim)
    return mim


def draw_all(a, b, c, d, count):
    fname = f"figures\{a}_1_{c}_{d}.png"
    dict = {0: draw_1,
            1: draw_2,
            2: draw_3,
            3: draw_4,
            4: draw_5,
            5: draw_6,
            6: draw_7,
            7: draw_8,
            8: draw_9}
    f = dict[b];
    res = f(fname)

    draw = ImageDraw.Draw(res)
    font = ImageFont.truetype('Xolonium-Bold.otf', size=66)
    draw.text((40, 40), "???_" + str(count), font=font, fill='#000')
    draw.text((1000, 40), "???_" + str(count), font=font, fill='#000')

    res = res.rotate(-180, expand=True)
    draw = ImageDraw.Draw(res)
    draw.text((40, 40), "???_" + str(count), font=font, fill='#000')
    draw.text((1000, 40), "???_" + str(count), font=font, fill='#000')
    res = res.resize((1186, 1762))

    res.save(f"res\{a}_{b}_{c}_{d}.png", quality=100, subsampling=0)


# (a,b,c,d)
# ?????????? ???????????? 0 ??????????????, 1 ???????????????? ?? ???? ???????? 7 ?????????????????? 0..7 mod 8
# ??????-???? ?????????? ???? ???????????????? ???? 1 ???? 9  0..8  mod 9
# ???????? ?????????? ???? ???????????????? ???? ?????????????????????? ??????????????  0..6 mod 7
# ?????? ???????????????? ?????? ????????????????, ???????? ????????????, ????????+??????, ???????? +??????+ 2 ??????????????????, ???????????? ???????????????? 0..5 mod 6
#    img.save(f"{x 6}_{z 8}_{clr 7}.png", quality=100, subsampling=0)
# ??????????????????????_????????????????_????????

# a = (a + 1) % 8
# b = (b + 1) % 9
# c = (c + 1) % 7
# d = (d + 1) % 6
def mf():
    main_ls = cards_list.main_ls
    count = 0
    for x in main_ls:
        draw_all(x[0], x[1], x[2], x[3], count + 1)
        count += 1


mf()