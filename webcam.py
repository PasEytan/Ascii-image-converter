import cv2
import numpy as np
from PIL import Image

bright = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,^`'.                  """
bright = bright[::-1]  
the = []
width = 84

def load_pix(the_image): 
    x = list(the_image.getdata())
    for i in range(im.height * im.width):
        f = x[i]
        f = sum(f) // 3
        f = ((f * len(bright)) // 255) - 5
        val = bright[f]
        the.append(val)
    return the

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    load_pix(frame)
    for i in range(len(the)):
        if i % frame.width != 0:
            print(the[i], end=' ')
        elif i % frame.width == 0:
            print(the[i])
        print()

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()