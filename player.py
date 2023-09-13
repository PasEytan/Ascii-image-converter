import os
import time
from PIL import Image


def playvid():
    im = Image.open('Frames/content/output/frame_0001.png')
    l = []
    im_pix = []
    with open("rend (1).txt", 'r') as f:
        l.append(f.read())
    k = l[0]
    for i in range(int(len(k) / 84)):
        start = time.time()
        im_pix.append(k[i * im.width: im.width * i + im.width])
        string = im_pix[0]
        string = ' '.join(string)
        print(string)
        end = time.time()
        if i % im.height == 0:
            time.sleep(0.045)
            #os.system('clear')
        im_pix.clear()
        the_time = end - start



