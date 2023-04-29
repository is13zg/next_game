from PIL import Image
from PIL import ImageDraw
import os

Fat_Border_on_Empty_FIG = False
def gen_all_fill(z, x, clr):
    clrs = ["#cd1719", "#ed7004", "#ffcc08", "#3fa535", "#00a5d1", "#054798", "#60267b"];

    im_c = f"{z}_c.jpg";
    im_f = f"{z}_f.jpg";
    f_m = f"s{x}.jpg";

    # im_c = f"{z}_c.png";
    # im_f = f"{z}_f.png";
    # f_m = f"s{x}.png";
    color = clrs[clr]

    if x == 0 and Fat_Border_on_Empty_FIG:
        if os.path.exists(f"{z}_cc.jpg"):
            im_c = f"{z}_cc.jpg";
        else:
            im_c = f"{z}_c.jpg";
            print("No file with fat border")

    mask_c = Image.open(im_c)
    mask_f = Image.open(im_f).convert('L')
    all_black = Image.new('RGB', (500, 500), (0, 0, 0))

    im1 = Image.new('RGB', (500, 500), 'white')
    mask = Image.open(f_m).convert('L')
    t_m = Image.composite(im1, mask, mask_f)
    im = Image.composite(mask_c, all_black, t_m)
    m_im = im.convert('L')
    clr_im = Image.new('RGB', (500, 500), color)
    im = Image.composite(im1, clr_im, m_im)
    img = im.convert("RGBA")

    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] > 250 and item[1] > 250 and item[2] > 250:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(f"figures\{z}_1_{clr}_{x}.png", quality=100, subsampling=0)


def gen_all_fill11(z, x, clr):
    clrs = ["#cd1719", "#ed7004", "#ffcc08", "#3fa535", "#00a5d1", "#054798", "#60267b"];
    rszk = 1.1

    im_c = f"{z}_c.jpg";
    im_f = f"{z}_f.jpg";
    f_m = f"s{x}1.jpg";

    color = clrs[clr]

    if x == 0:
        im_c = f"{z}_cc.jpg";

    mask_c = Image.open(im_c)
    mask_f = Image.open(im_f)
    mask_c = mask_c.resize((round(mask_c.width * rszk), round(mask_c.height * rszk)))
    mask_f = mask_f.resize((round(mask_f.width * rszk), round(mask_f.height * rszk)))

    mask_f = mask_f.convert('L')
    all_black = Image.new('RGB', (round(500 * rszk), round(500 * rszk)), (0, 0, 0))

    im1 = Image.new('RGB', (round(500 * rszk), round(500 * rszk)), 'white')
    mask = Image.open(f_m).convert('L')
    t_m = Image.composite(im1, mask, mask_f)
    im = Image.composite(mask_c, all_black, t_m)
    m_im = im.convert('L')
    clr_im = Image.new('RGB', (round(500 * rszk), round(500 * rszk)), color)
    im = Image.composite(im1, clr_im, m_im)
    img = im.convert("RGBA")

    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] > 250 and item[1] > 250 and item[2] > 250:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(f"figures\{z}_1_{clr}_{x}11.png", quality=100, subsampling=0)


def gen_all_fill12(z, x, clr):
    clrs = ["#cd1719", "#ed7004", "#ffcc08", "#3fa535", "#00a5d1", "#054798", "#60267b"];
    rszk = 1.2

    im_c = f"{z}_c.jpg";
    im_f = f"{z}_f.jpg";
    f_m = f"s{x}2.jpg";

    color = clrs[clr]

    if x == 0:
        im_c = f"{z}_cc.jpg";

    mask_c = Image.open(im_c)
    mask_f = Image.open(im_f)
    mask_c = mask_c.resize((round(mask_c.width * rszk), round(mask_c.height * rszk)))
    mask_f = mask_f.resize((round(mask_f.width * rszk), round(mask_f.height * rszk)))

    mask_f = mask_f.convert('L')
    all_black = Image.new('RGB', (round(500 * rszk), round(500 * rszk)), (0, 0, 0))

    im1 = Image.new('RGB', (round(500 * rszk), round(500 * rszk)), 'white')
    mask = Image.open(f_m).convert('L')
    t_m = Image.composite(im1, mask, mask_f)
    im = Image.composite(mask_c, all_black, t_m)
    m_im = im.convert('L')
    clr_im = Image.new('RGB', (round(500 * rszk), round(500 * rszk)), color)
    im = Image.composite(im1, clr_im, m_im)
    img = im.convert("RGBA")

    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] > 250 and item[1] > 250 and item[2] > 250:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(f"figures\{z}_1_{clr}_{x}12.png", quality=100, subsampling=0)


def gen_all_fill15(z, x, clr):
    clrs = ["#cd1719", "#ed7004", "#ffcc08", "#3fa535", "#00a5d1", "#054798", "#60267b"];
    rszk = 1.5

    im_c = f"{z}_c.jpg";
    im_f = f"{z}_f.jpg";
    f_m = f"s{x}3.jpg";

    color = clrs[clr]

    if x == 0:
        im_c = f"{z}_cc.jpg";

    mask_c = Image.open(im_c)
    mask_f = Image.open(im_f)
    mask_c = mask_c.resize((round(mask_c.width * rszk), round(mask_c.height * rszk)))
    mask_f = mask_f.resize((round(mask_f.width * rszk), round(mask_f.height * rszk)))

    mask_f = mask_f.convert('L')
    all_black = Image.new('RGB', (round(500 * rszk), round(500 * rszk)), (0, 0, 0))

    im1 = Image.new('RGB', (round(500 * rszk), round(500 * rszk)), 'white')
    mask = Image.open(f_m).convert('L')
    t_m = Image.composite(im1, mask, mask_f)
    im = Image.composite(mask_c, all_black, t_m)
    m_im = im.convert('L')
    clr_im = Image.new('RGB', (round(500 * rszk), round(500 * rszk)), color)
    im = Image.composite(im1, clr_im, m_im)
    img = im.convert("RGBA")

    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] > 250 and item[1] > 250 and item[2] > 250:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(f"figures\{z}_1_{clr}_{x}15.png", quality=100, subsampling=0)


def gen_all_fill2(z, x, clr):
    clrs = ["#cd1719", "#ed7004", "#ffcc08", "#3fa535", "#00a5d1", "#054798", "#60267b"];
    rszk = 2

    im_c = f"{z}_c.jpg";
    im_f = f"{z}_f.jpg";
    f_m = f"s{x}4.jpg";

    color = clrs[clr]

    if x == 0:
        im_c = f"{z}_cc.jpg";

    mask_c = Image.open(im_c)
    mask_f = Image.open(im_f)
    mask_c = mask_c.resize((round(mask_c.width * rszk), round(mask_c.height * rszk)))
    mask_f = mask_f.resize((round(mask_f.width * rszk), round(mask_f.height * rszk)))

    mask_f = mask_f.convert('L')
    all_black = Image.new('RGB', (round(500 * rszk), round(500 * rszk)), (0, 0, 0))

    im1 = Image.new('RGB', (round(500 * rszk), round(500 * rszk)), 'white')
    mask = Image.open(f_m).convert('L')
    t_m = Image.composite(im1, mask, mask_f)
    im = Image.composite(mask_c, all_black, t_m)
    m_im = im.convert('L')
    clr_im = Image.new('RGB', (round(500 * rszk), round(500 * rszk)), color)
    im = Image.composite(im1, clr_im, m_im)
    img = im.convert("RGBA")

    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] > 250 and item[1] > 250 and item[2] > 250:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(f"figures\{z}_1_{clr}_{x}2.png", quality=100, subsampling=0)


# (a,b,c,d)
# какая фигура 0 уголник, 1 угольник и тд макс 7 уугольник 0..7 mod 8
# кол-во фигур на карточке от 1 до 9  0..8  mod 9
# цвет фигур от красного до фиолетового КОЖЗГСФ  0..6 mod 7
# тип закраски нет закраски, верт полосы, верт+гор, верт +гор+ 2 диагонали, полная закраска 0..5 mod 6
#    img.save(f"{x 6}_{z 8}_{clr 7}.png", quality=100, subsampling=0)
# типзакраски_угольник_цвет

def make_patterns():
    for i in range(0, 6):
        for x in [(750, 3), (600, 2), (550, 1), (500, "")]:
            im = Image.open(f"s{i}4.jpg")
            im1 = im.crop((0, 0, x[0], x[0]))
            im1.save(f"s{i}{x[1]}.jpg")


def mf():
    make_patterns()
    ccc = 0
    for x in range(6):
        for clr in range(7):
            for z in range(8):
                gen_all_fill(z, x, clr)
                gen_all_fill11(z, x, clr)
                gen_all_fill12(z, x, clr)
                gen_all_fill15(z, x, clr)
                gen_all_fill2(z, x, clr)
                ccc += 1
                if ccc % 100 == 0:
                    print(ccc / 1680 * 100, "%")


# t_m=Image.composite(im1,mask_h_l,mask_f)
# t_m.show()

#
# im = Image.composite(im1, im2, mask_c)
# im.show()


# im = Image.composite(Image.open("0_c.jpg"), im4, t_m)
# im.show()
#
#
# t_m=Image.open("horz2.jpg").convert('L')
# im = Image.composite(Image.open("s12.jpg"), im4, t_m)
# im.show()
#


# def composite_2_im(i1,i2):
#    mask = Image.new("L", i1.size, 255)
#    im = Image.composite(i1,i2, mask)
#    im.show()
#    return im;
#
# composite_2_im(mask_h,mask_v)
#
if __name__ == "__main__":
    mf()
