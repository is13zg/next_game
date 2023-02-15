from PIL import Image
from PIL import ImageDraw, ImageFont


def draw_9(name):
    mim = Image.new('RGBA', (1297, 1836), "white")
    pim= Image.open(name)
    mim.paste(pim,(-2,20),pim)
    mim.paste(pim, (-2, 575),pim)
    mim.paste(pim, (-2, 1115),pim)

    mim.paste(pim,(815,20),pim)
    mim.paste(pim, (815, 575),pim)
    mim.paste(pim, (815, 1115),pim)

    mim.paste(pim, (408, 277),pim)
    mim.paste(pim, (408, 844),pim)
    mim.paste(pim, (408, 1350),pim)
    return mim


def draw_8(name):
    mim = Image.new('RGBA', (1297, 1836), "white")
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
    mim = Image.new('RGBA', (1297, 1836), "white")
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
    mim = Image.new('RGBA', (1297, 1836), "white")
    pim = Image.open(name)

    mim.paste(pim, (50, 70), pim)
    mim.paste(pim, (745, 70), pim)

    mim.paste(pim, (400, 410), pim)
    mim.paste(pim, (400, 920), pim)

    mim.paste(pim, (50, 1270), pim)
    mim.paste(pim, (745, 1270), pim)
    return mim


def draw_5(name):
    mim = Image.new('RGBA', (1297, 1836), "white")
    pim = Image.open(name)

    mim.paste(pim, (55, 150), pim)
    mim.paste(pim, (755, 150), pim)

    mim.paste(pim, (55, 1185), pim)
    mim.paste(pim, (755, 1185), pim)

    mim.paste(pim, (400, 670), pim)
    return mim


def draw_4(name):
    mim = Image.new('RGBA', (1297, 1836), "white")
    pim = Image.open(name)

    mim.paste(pim, (75, 200), pim)
    mim.paste(pim, (725, 200), pim)

    mim.paste(pim, (75, 1050), pim)
    mim.paste(pim, (725, 1050), pim)

    return mim

def draw_3(name):
    mim = Image.new('RGBA', (1297, 1836), "white")
    pim= Image.open(name)

    mim.paste(pim, (400, 110),pim)
    mim.paste(pim, (400, 635),pim)
    mim.paste(pim, (400, 1175),pim)
    return mim


def draw_2(name):
    mim = Image.new('RGBA', (1297, 1836), "white")
    pim= Image.open(name)

    mim.paste(pim, (400, 310),pim)
    mim.paste(pim, (400, 1075),pim)
    return mim

def draw_2(name):
    mim = Image.new('RGBA', (1297, 1836), "white")
    pim= Image.open(name)

    mim.paste(pim, (400, 310),pim)
    mim.paste(pim, (400, 1075),pim)
    return mim


def draw_1(name):
    mim = Image.new('RGBA', (1297, 1836), "white")
    pim = Image.open(name)
    mim.paste(pim, (400, 670), pim)
    return mim


def draw_all(a,b,c,d,count):
    fname = f"{a}_1_{c}_{d}.png"
    dict ={0:draw_1,
           1:draw_2,
           2:draw_3,
           3:draw_4,
           4:draw_5,
           5:draw_6,
           6:draw_7,
           7:draw_8,
           8:draw_9}
    f=dict[b];
    res=f(fname)


    draw = ImageDraw.Draw(res)
    font = ImageFont.truetype('Xolonium-Bold.otf', size=66)
    draw.text((40, 40), "№_" + str(count), font=font, fill='#000')
    draw.text((1000, 40), "№_" + str(count), font=font, fill='#000')

    res = res.rotate(-180, expand=True)
    draw = ImageDraw.Draw(res)
    draw.text((40, 40), "№_" + str(count), font=font, fill='#000')
    draw.text((1000, 40), "№_" + str(count), font=font, fill='#000')

    res.save(f"res\{a}_{b}_{c}_{d}.png", quality=100, subsampling=0)


main_ls=[(0, 0, 0, 0), (1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3), (4, 4, 4, 4), (5, 5, 5, 5), (6, 6, 6, 0), (7, 7, 0, 1), (0, 8, 1, 2), (1, 0, 2, 3), (2, 1, 3, 4), (3, 2, 4, 5), (4, 3, 5, 0), (5, 4, 6, 1), (6, 5, 0, 2), (7, 6, 1, 3), (0, 7, 2, 4), (1, 8, 3, 5), (2, 0, 4, 0), (3, 1, 5, 1), (4, 2, 6, 2), (5, 3, 0, 3), (6, 4, 1, 4), (7, 5, 2, 5), (0, 6, 3, 0), (1, 7, 4, 1), (2, 8, 5, 2), (3, 0, 6, 3), (4, 1, 0, 4), (5, 2, 1, 5), (6, 3, 2, 0), (7, 4, 3, 1), (0, 5, 4, 2), (1, 6, 5, 3), (2, 7, 6, 4), (3, 8, 0, 5), (4, 0, 1, 0), (5, 1, 2, 1), (6, 2, 3, 2), (7, 3, 4, 3), (0, 4, 5, 4), (1, 5, 6, 5), (2, 6, 0, 0), (3, 7, 1, 1), (4, 8, 2, 2), (5, 0, 3, 3), (6, 1, 4, 4), (7, 2, 5, 5), (0, 3, 6, 0), (1, 4, 0, 1), (2, 5, 1, 2), (3, 6, 2, 3), (4, 7, 3, 4), (5, 8, 4, 5), (6, 0, 5, 0), (7, 1, 6, 1), (0, 2, 0, 2), (1, 3, 1, 3), (2, 4, 2, 4), (3, 5, 3, 5), (4, 6, 4, 0), (5, 7, 5, 1), (6, 8, 6, 2), (7, 0, 0, 3), (0, 1, 1, 4), (1, 2, 2, 5), (2, 3, 3, 0), (3, 4, 4, 1), (4, 5, 5, 2), (5, 6, 6, 3), (6, 7, 0, 4), (7, 8, 1, 5), (0, 0, 2, 0), (1, 1, 3, 1), (2, 2, 4, 2), (3, 3, 5, 3), (4, 4, 6, 4), (5, 5, 0, 5), (6, 6, 1, 0), (7, 7, 2, 1), (0, 8, 3, 2), (1, 0, 4, 3), (2, 1, 5, 4), (3, 2, 6, 5), (4, 3, 0, 0), (5, 4, 1, 1), (6, 5, 2, 2), (7, 6, 3, 3), (0, 7, 4, 4), (1, 8, 5, 5), (2, 0, 6, 0), (3, 1, 0, 1), (4, 2, 1, 2), (5, 3, 2, 3), (6, 4, 3, 4), (7, 5, 4, 5), (0, 6, 5, 0), (1, 7, 6, 1), (2, 8, 0, 2), (3, 0, 1, 3)]
main_ls = [(0, 0, 0, 0), (1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3), (4, 4, 4, 4), (5, 5, 5, 5), (6, 6, 6, 0), (7, 7, 0, 1), (0, 8, 1, 2), (1, 0, 2, 3), (2, 1, 3, 4), (3, 2, 4, 5), (4, 3, 5, 0), (5, 4, 6, 1), (6, 5, 0, 2), (7, 6, 1, 3), (0, 7, 2, 4), (1, 8, 3, 5), (2, 0, 4, 0), (3, 1, 5, 1), (4, 2, 6, 2), (5, 3, 0, 3), (6, 4, 1, 4), (7, 5, 2, 5), (0, 6, 3, 0), (1, 7, 4, 1), (2, 8, 5, 2), (3, 0, 6, 3), (4, 1, 0, 4), (5, 2, 1, 5), (6, 3, 2, 0), (7, 4, 3, 1), (0, 5, 4, 2), (1, 6, 5, 3), (2, 7, 6, 4), (3, 8, 0, 5), (4, 0, 1, 0), (5, 1, 2, 1), (6, 2, 3, 2), (7, 3, 4, 3), (0, 4, 5, 4), (1, 5, 6, 5), (2, 6, 0, 0), (3, 7, 1, 1), (4, 8, 2, 2), (5, 0, 3, 3), (6, 1, 4, 4), (7, 2, 5, 5), (0, 3, 6, 0), (1, 4, 0, 1), (2, 5, 1, 2), (3, 6, 2, 3), (4, 7, 3, 4), (5, 8, 4, 5), (6, 0, 5, 0), (7, 1, 6, 1), (0, 2, 0, 2), (1, 3, 1, 3), (2, 4, 2, 4), (3, 5, 3, 5), (4, 6, 4, 0), (5, 7, 5, 1), (6, 8, 6, 2), (7, 0, 0, 3), (0, 1, 1, 4), (1, 2, 2, 5), (2, 3, 3, 0), (3, 4, 4, 1), (4, 5, 5, 2), (5, 6, 6, 3), (6, 7, 0, 4), (7, 8, 1, 5), (0, 0, 2, 0), (1, 1, 3, 1), (2, 2, 4, 2), (3, 3, 5, 3), (4, 4, 6, 4), (5, 5, 0, 5), (6, 6, 1, 0), (7, 7, 2, 1), (0, 8, 3, 2)]


#(a,b,c,d)
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

count=0
for x in main_ls:
    draw_all(x[0],x[1],x[2],x[3],count+1)
    count+=1