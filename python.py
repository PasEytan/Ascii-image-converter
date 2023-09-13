# start researching 
from PIL import Image


im = Image.open('pap.jpg', 'r')
new_im = im.resize((144, 96))
bright = ['  ', ',,', '--', '==', '++', 'gg', '##', '%%', '@@']

im.show()
pix_val = list(new_im.getdata())

get = 0

for g in range(700000):
    a = sum(pix_val[get])
    get = get + 1
    if g % 144 == 0:
        if a < 85:
            print(bright[0])
        elif 175 > a > 85:
            print(bright[1])
        elif 255 > a > 175:
            print(bright[2])
        elif 340 > a > 255:
            print(bright[3])
        elif 425 > a > 340:
            print(bright[4])
        elif 510 > a > 425:
            print(bright[5])
        elif 595 > a > 510:
            print(bright[6])
        elif 680 > a > 595:
            print(bright[7])
        elif 765 > a > 680:
            print(bright[8])
    else:
        if a < 85:
            print(bright[0], end='')
        elif 175 > a > 85:
            print(bright[1], end='')
        elif 255 > a > 175:
            print(bright[2], end='')
        elif 340 > a > 255:
            print(bright[3], end='')
        elif 425 > a > 340:
            print(bright[4], end='')
        elif 510 > a > 425:
            print(bright[5], end='')
        elif 595 > a > 510:
            print(bright[6], end='')
        elif 680 > a > 595:
            print(bright[7], end='')
        elif 765 > a > 680:
            print(bright[8], end='')



