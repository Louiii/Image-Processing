import numpy as np
from PIL import Image
import sys


def erode(read_name="lena.png", write_name="lena_erosion.png"):  # accepts two string parameters for the file to read and file to write, setting their default values to the ones specified in the assignment
    img = Image.open(read_name)#store our image in a variable called img
    ero(img).save(write_name)#run the ero function below, and save the result under the 'write_name'

def ero(img):
    img = np.array(img)#represent the greyscale image as a numpy array
    kernel = np.ones((5, 5), np.uint8)  # this is our structuring element
    deviation = (len(kernel) - 1) / 2 #we want to make sets of pixel values around each pixel the size of the kernel
    if not img is None:#if we have an image
        h, w = np.shape(img)#assign the dimensions of the image to height and width variables
        data = np.zeros((w, h), dtype=np.uint8)  # matrix the size of the image for appending data
        for py in range(h):#for each row, index py
            for px in range(w):#for each pixel px in row py
                set = []
                for i in range(len(kernel)):#for index i in the row from 0-4 the size of the sides of our kernel
                    for j in range(len(kernel)):#for index j in the column from 0-4 the size of the sides of our kernel
                        if (px-deviation+i > 0 and py-deviation+j > 0 and px-deviation+i < w and py-deviation+j < h) :#if there is a pixel, so not near the edge
                            set.append(img[px-2+i][py-2+j])#add it to the set
                data[px][py] = min(set)#add the min of our set to the new pixel value at that point
    im = Image.fromarray(data)#make an image out of this
    return im#return it


if len(sys.argv) == 3 :#requires 3 arguments, the file, and the name of the image to write and the name of what it should be writen as
    erode(str(sys.argv[1]), str(sys.argv[2]))
else:
    print ("incorrect number of arguments entered")
    erode()


