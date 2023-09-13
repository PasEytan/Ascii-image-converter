from PIL import Image
import numpy as np

bright = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,^`'.                  """
bright = bright[::-1]  
The_im = '../h.png'
the = []
width = 84
im = Image.open(The_im)

def get_new_val(old_val, nc):
    """
    Get the "closest" colour to old_val in the range [0,1] per channel divided
    into nc values.

    """

    return np.round(old_val * (nc - 1)) / (nc - 1)

# For RGB images, the following might give better colour-matching.
#p = np.linspace(0, 1, nc)
#p = np.array(list(product(p,p,p)))
#def get_new_val(old_val):
#    idx = np.argmin(np.sum((old_val[None,:] - p)**2, axis=1))
#    return p[idx]

def fs_dither(img, nc):
    """
    Floyd-Steinberg dither the image img into a palette with nc colours per
    channel.

    """

    arr = np.array(img, dtype=float) / 255

    for ir in range(im.height):
        for ic in range(im.width):
            # NB need to copy here for RGB arrays otherwise err will be (0,0,0)!
            old_val = arr[ir, ic].copy()
            new_val = get_new_val(old_val, nc)
            arr[ir, ic] = new_val
            err = old_val - new_val
            # In this simple example, we will just ignore the border pixels.
            if ic < im.width - 1:
                arr[ir, ic+1] += err * 7/16
            if ir < im.height - 1:
                if ic > 0:
                    arr[ir+1, ic-1] += err * 3/16
                arr[ir+1, ic] += err * 5/16
                if ic < im.width - 1:
                    arr[ir+1, ic+1] += err / 16

    carr = np.array(arr/np.max(arr, axis=(0,1)) * 255, dtype=np.uint8)
    return Image.fromarray(carr)

im  = fs_dither(im, 128)
im = im.resize((width, int(width / (im.width / im.height))))

def load_pix(the_image): 
    x = list(the_image.getdata())
    for i in range(im.height * im.width):
        f = x[i]
        f = sum(f) // 3
        f = ((f * len(bright)) // 255) - 5
        val = bright[f]
        the.append(val)
    return the

load_pix(im)
"""
if The_im[len(The_im) - 2] == 'j':
    for x in range(im.width):
        for y in range(im.height):
            i = y * im.width + x
            if i < len(the):
                print(the[i], end=' ')
        print()
"""
#elif The_im[len(The_im) - 2] == 'p':
for i in range(len(the)):
    if i % im.width != 0:
        print(the[i], end=' ')
    elif i % im.width == 0:
        print(the[i])
print()
im.show()