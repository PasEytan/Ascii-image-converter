import os 
from PIL import Image

bright = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,^`'.           """
bright = bright[::-1]
the = []
def load_pix(im):
    im = f'Frames/content/output/{im}'
    im = Image.open(im) 
    x = list(im.getdata())
    for i in range(im.height * im.width):
        f = x[i]
        f = sum(f) // 3
        f = ((f * len(bright)) // 255) - 5
        val = bright[f]
        the.append(val)
    return the
path = '/Users/eytan/Desktop/CodingStuff/doing some python/Ascii image converter/Also vids/Frames/content/output/'
#with open('rend.txt', 'w'):
for i in range(len(os.listdir('/Users/eytan/Desktop/CodingStuff/doing some python/Ascii image converter/Also vids/Frames/content/output/'))):
    k = os.listdir('/Users/eytan/Desktop/CodingStuff/doing some python/Ascii image converter/Also vids/Frames/content/output/')
    k = sorted(k)
    x = k[i]
    load_pix(x)
string = ''.join(the)
with open('rend.txt', 'w') as f:
    f.write(string)