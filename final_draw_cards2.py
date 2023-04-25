from PIL import Image
from PIL import ImageDraw, ImageFont
import cards_list

ih = 1200
iw = 1800  # 1836


def draw_9(name):
    mim = Image.new('RGBA', (ih, iw), "#fffce3")
    pim = Image.open(name)

    pim = pim.resize((round(pim.width * .95), round(pim.height * .95)))

    mim.paste(pim, (-2, 50), pim)
    mim.paste(pim, (-2, 550), pim)
    mim.paste(pim, (-2, 1075), pim)

    mim.paste(pim, (740, 50), pim)
    mim.paste(pim, (740, 550), pim)
    mim.paste(pim, (740, 1075), pim)

    mim.paste(pim, (370, 310), pim)
    mim.paste(pim, (370, 810), pim)
    mim.paste(pim, (370, 1310), pim)
    return mim


def draw_8(name):
    mim = Image.new('RGBA', (ih, iw), "#fffce3")
    pim = Image.open(name)
    mim.paste(pim, (-20, 20), pim)
    mim.paste(pim, (-20, 665), pim)
    mim.paste(pim, (-20, 1280), pim)

    mim.paste(pim, (720, 20), pim)
    mim.paste(pim, (720, 665), pim)
    mim.paste(pim, (720, 1250), pim)

    mim.paste(pim, (335, 350), pim)
    mim.paste(pim, (335, 1000), pim)
    return mim


def draw_7(name):
    mim = Image.new('RGBA', (ih, iw), "#fffce3")
    pim = Image.open(name)

    mim.paste(pim, (350, 10), pim)
    mim.paste(pim, (350, 675), pim)
    mim.paste(pim, (350, 1310), pim)

    mim.paste(pim, (10, 345), pim)
    mim.paste(pim, (10, 995), pim)

    mim.paste(pim, (700, 345), pim)
    mim.paste(pim, (700, 995), pim)
    return mim


def draw_6(name):
    mim = Image.new('RGBA', (ih, iw), "#fffce3")
    pim = Image.open(name)

    mim.paste(pim, (55, 150), pim)
    mim.paste(pim, (650, 150), pim)

    mim.paste(pim, (55, 1185), pim)
    mim.paste(pim, (650, 1185), pim)

    mim.paste(pim, (55, 685), pim)
    mim.paste(pim, (650, 685), pim)
    return mim


def draw_5(name):
    mim = Image.new('RGBA', (ih, iw), "#fffce3")
    pim = Image.open(name)

    mim.paste(pim, (55, 150), pim)
    mim.paste(pim, (650, 150), pim)

    mim.paste(pim, (55, 1185), pim)
    mim.paste(pim, (650, 1185), pim)

    mim.paste(pim, (350, 670), pim)
    return mim


def draw_4(name):
    mim = Image.new('RGBA', (ih, iw), "#fffce3")
    pim = Image.open(name)
    pim = pim.resize((round(pim.width * 1.2), round(pim.height * 1.2)))

    mim.paste(pim, (25, 200), pim)
    mim.paste(pim, (575, 400), pim)

    mim.paste(pim, (25, 850), pim)
    mim.paste(pim, (575, 1050), pim)

    return mim


def draw_3(name):
    mim = Image.new('RGBA', (ih, iw), "#fffce3")
    pim = Image.open(name)
    pim = pim.resize((round(pim.width * 1.2), round(pim.height * 1.2)))
    mim.paste(pim, (300, 40), pim)
    mim.paste(pim, (300, 600), pim)
    mim.paste(pim, (300, 1160), pim)
    return mim




def draw_2(name):
    mim = Image.new('RGBA', (ih, iw), "#fffce3")
    pim = Image.open(name)
    pim = pim.resize((round(pim.width * 1.5), round(pim.height * 1.5)))

    mim.paste(pim, (220, 100), pim)
    mim.paste(pim, (220, 875), pim)
    return mim


def draw_1(name):
    mim = Image.new('RGBA', (ih, iw), "#fffce3")
    pim = Image.open(name)
    pim = pim.resize((round(pim.width * 2.2),round(pim.height * 2.2)))
    mim.paste(pim, (50, 350), pim)
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
    font = ImageFont.truetype('Xolonium-Bold.otf', size=60)
    draw.text((40, 30), "№_" + str(count), font=font, fill='#000')
    draw.text((900, 30), "№_" + str(count), font=font, fill='#000')

    res = res.rotate(-180, expand=True)
    draw = ImageDraw.Draw(res)
    draw.text((40, 30), "№_" + str(count), font=font, fill='#000')
    draw.text((900, 30), "№_" + str(count), font=font, fill='#000')

    res.save(f"res\{a}_{b}_{c}_{d}.png", quality=100, subsampling=0)


# (a,b,c,d)
# какая фигура 0 уголник, 1 угольник и тд макс 7 уугольник 0..7 mod 8
# кол-во фигур на карточке от 1 до 9  0..8  mod 9
# цвет фигур от красного до фиолетового КОЖЗГСФ  0..6 mod 7
# тип закраски нет закраски, верт полосы, верт+гор, верт +гор+ 2 диагонали, полная закраска 0..5 mod 6
#    img.save(f"{x 6}_{z 8}_{clr 7}.png", quality=100, subsampling=0)
# типзакраски_угольник_цвет

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


# mf()
