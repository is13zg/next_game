from PIL import Image
from PIL import ImageDraw


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
        im_c = f"{z}_cc.jpg";

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


# (a,b,c,d)
# какая фигура 0 уголник, 1 угольник и тд макс 7 уугольник 0..7 mod 8
# кол-во фигур на карточке от 1 до 9  0..8  mod 9
# цвет фигур от красного до фиолетового КОЖЗГСФ  0..6 mod 7
# тип закраски нет закраски, верт полосы, верт+гор, верт +гор+ 2 диагонали, полная закраска 0..5 mod 6
#    img.save(f"{x 6}_{z 8}_{clr 7}.png", quality=100, subsampling=0)
# типзакраски_угольник_цвет

def mf():
    im1 = Image.new('RGB', (500, 500), 'white')  # background image

    im2 = Image.new('RGB', (500, 500), 'red')
    im3 = Image.new('RGB', (500, 500), 'red')
    im4 = Image.new('RGB', (500, 500), 'black')

    mask_c = Image.open("0_c.jpg").convert('L')
    mask_f = Image.open("0_f.jpg").convert('L')

    # mask_h = Image.open("horz.jpg")
    # mask_v = Image.open("vert.jpg")
    # mask_sd = Image.open("side_diag.jpg")
    # mask_md = Image.open("main_diag.jpg")
    #
    # mask_h_l  = Image.open("horz.jpg").convert('L')
    # mask_v_l = Image.open("vert.jpg").convert('L')
    # mask_sd_l = Image.open("side_diag.jpg").convert('L')
    # mask_md_l = Image.open("main_diag.jpg").convert('L')

    #
    # mask_h = Image.open("20pcfill.jpg")
    # mask_v = Image.open("40pcfill.jpg")
    # mask_sd = Image.open("60pcfill.jpg")
    # mask_md = Image.open("80pcfill.jpg")
    #
    # mask_h_l = Image.open("20pcfill.jpg").convert('L')
    # mask_v_l = Image.open("40pcfill.jpg").convert('L')
    # mask_sd_l = Image.open("60pcfill.jpg").convert('L')
    # mask_md_l = Image.open("80pcfill.jpg").convert('L')
    for x in range(6):
        for clr in range(7):
            for z in range(8):
                gen_all_fill( z, x, clr)


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