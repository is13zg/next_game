from PIL import Image
from PIL import ImageDraw


im4 = Image.new('RGB',(500,500),'black')

vert_img=Image.open("s12.jpg").convert('L')

t_m=Image.open("side_diag2.jpg").convert('L')
s2 = Image.composite(Image.open("s12.jpg"), im4, t_m)
s2.save("s2.jpg", quality=100, subsampling=0)
s2.show()


t_m=Image.open("horz2.jpg").convert('L')
s3=Image.composite(s2, im4, t_m)
s3.save("s3.jpg", quality=100, subsampling=0)
s3.show()


t_m=Image.open("main_diag2.jpg").convert('L')
s4=Image.composite(s3, im4, t_m)
s4.save("s4.jpg", quality=100, subsampling=0)
s4.show()