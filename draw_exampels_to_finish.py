from PIL import Image
from PIL import ImageDraw, ImageFont


def draw_fon_lines():
    for ramka in range(1, 2):
        # fon lines
        for lines in range(1, 5):
            for tol in range(1, 5):
                mim = Image.open("pics/fon.png")

                t2 = Image.open("pics/zakras.png")
                mim.paste(t2, (0, 0), t2)

                tx = Image.open(f"pics/fline/{lines}/{tol}.png")
                mim.paste(tx, (0, 0), tx)

                tr = Image.open(f"pics/r/{ramka}.png")
                mim.paste(tr, (0, 0), tr)

                mim.save(f"pics/res/rmk{ramka}_flines{lines}_tol{tol}.png", quality=100, subsampling=0)


def draw_clr_lines():
    for ramka in range(1, 2):
        # clr lines
        for lines in range(1, 5):
            for tol in range(1, 5):
                mim = Image.open("pics/fon.png")

                tx = Image.open(f"pics/cline/{lines}/{tol}.png")
                mim.paste(tx, (0, 0), tx)

                t2 = Image.open("pics/fonaut2.png")
                mim.paste(t2, (0, 0), t2)

                tr = Image.open(f"pics/r/{ramka}.png")
                mim.paste(tr, (0, 0), tr)

                mim.save(f"pics/res/rmk{ramka}_clines{lines}_tol{tol}.png", quality=100, subsampling=0)


def draw_fon_lines2():
    for ramka in range(1, 2):
        # fon lines
        for lines in range(1, 5):
            for tol in range(5, 9):
                mim = Image.open("pics/fon.png")

                t2 = Image.open("pics/zakras.png")
                mim.paste(t2, (0, 0), t2)

                tx = Image.open(f"pics/fline/{tol}/{lines}.png")
                mim.paste(tx, (0, 0), tx)

                tr = Image.open(f"pics/r/{ramka}.png")
                mim.paste(tr, (0, 0), tr)

                mim.save(f"pics/res/rmk{ramka}_flines{lines}_tol{tol}.png", quality=100, subsampling=0)


def draw_clr_lines2():
    for ramka in range(1, 2):
        # clr lines
        for lines in range(1, 5):
            for tol in range(13, 17):
                mim = Image.open("pics/fon.png")

                tx = Image.open(f"pics/cline/{tol}/{lines}.png")
                mim.paste(tx, (0, 0), tx)

                t2 = Image.open("pics/fonaut2.png")
                mim.paste(t2, (0, 0), t2)

                tr = Image.open(f"pics/r/{ramka}.png")
                mim.paste(tr, (0, 0), tr)

                mim.save(f"pics/res/rmk{ramka}_clines{lines}_tol{tol}.png", quality=100, subsampling=0)

def make_res():
    ih = 400
    iw = 500

    for tol in range(1, 5):
        mim = Image.new('RGBA', (iw * 2, ih * 2), "white")
        for lines in range(1, 5):
            tx = Image.open(f"pics/res/rmk1_clines{lines}_tol{tol}.png")

            if lines == 1:
                mim.paste(tx, (0, 0))
            if lines == 2:
                mim.paste(tx, (iw, 0))
            if lines == 3:
                mim.paste(tx, (0, ih))
            if lines == 4:
                mim.paste(tx, (iw, ih))


        mim.save(f"pics/res/rclines_tol{tol}.png", quality=100, subsampling=0)

        for tol in range(1, 5):
            mim = Image.new('RGBA', (iw * 2, ih * 2), "white")
            for lines in range(1, 5):
                tx = Image.open(f"pics/res/rmk1_flines{lines}_tol{tol}.png")

                if lines == 1:
                    mim.paste(tx, (0, 0))
                if lines == 2:
                    mim.paste(tx, (iw, 0))
                if lines == 3:
                    mim.paste(tx, (0, ih))
                if lines == 4:
                    mim.paste(tx, (iw, ih))

            mim.save(f"pics/res/rflines_tol{tol}.png", quality=100, subsampling=0)

def make_res2():
    ih = 400
    iw = 500

    for tol in range(5, 9):
        mim = Image.new('RGBA', (iw * 2, ih * 2), "white")
        for lines in range(1, 5):
            tx = Image.open(f"pics/res/rmk1_flines{lines}_tol{tol}.png")

            if lines == 1:
                mim.paste(tx, (0, 0))
            if lines == 2:
                mim.paste(tx, (iw, 0))
            if lines == 3:
                mim.paste(tx, (0, ih))
            if lines == 4:
                mim.paste(tx, (iw, ih))


        mim.save(f"pics/res/rflines_tol{tol}.png", quality=100, subsampling=0)

        for tol in range(9, 13):
            mim = Image.new('RGBA', (iw * 2, ih * 2), "white")
            for lines in range(1, 5):
                tx = Image.open(f"pics/res/rmk1_clines{lines}_tol{tol}.png")

                if lines == 1:
                    mim.paste(tx, (0, 0))
                if lines == 2:
                    mim.paste(tx, (iw, 0))
                if lines == 3:
                    mim.paste(tx, (0, ih))
                if lines == 4:
                    mim.paste(tx, (iw, ih))

            mim.save(f"pics/res/cflines_tol{tol}.png", quality=100, subsampling=0)



def make_res3():
    ih = 400
    iw = 500



    for tol in range(13, 17):
        mim = Image.new('RGBA', (iw * 2, ih * 2), "white")
        for lines in range(1, 5):
            tx = Image.open(f"pics/res/rmk1_clines{lines}_tol{tol}.png")

            if lines == 1:
                mim.paste(tx, (0, 0))
            if lines == 2:
                mim.paste(tx, (iw, 0))
            if lines == 3:
                mim.paste(tx, (0, ih))
            if lines == 4:
                mim.paste(tx, (iw, ih))

        mim.save(f"pics/res/cflines_tol{tol}.png", quality=100, subsampling=0)
# draw_clr_lines()
# draw_fon_lines()
# make_res()
# draw_clr_lines2()
# draw_fon_lines2()
make_res3()
