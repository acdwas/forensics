
# convert -coalesce gifwala.gif %05d.png

import numpy as np
from PIL import Image
import glob

list_im = []

for i in glob.glob("*.png"):
    list_im.append(i)

newimgdata = []

for i in range(len(list_im)):
    im = Image.open(list_im[i]).convert('RGB')
    x = 0
    for j in im.getdata():
        try:
            if j != newimgdata[x]:
                if j != (255, 255, 255):
                    newimgdata[x] = j
        except:
            newimgdata.append(j)
        x += 1

newimg = Image.new(im.mode, im.size)
newimg.putdata(newimgdata)

newimg.save('new.png')
