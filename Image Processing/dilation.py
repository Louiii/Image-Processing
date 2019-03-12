import numpy as np
from PIL import Image
import sys
from erosion import ero

def dilate(read_name = "lena.png", write_name = "lena_dilation.png"):#accepts two string parameters for the file to read and file to write, setting their default values to the ones specified in the assignment
    img = Image.open(read_name)#store our image in a variable called img
    dil(img).save(write_name)#run the dil function below, and save the result under the 'write_name'

def dil(img):#dilation is the same process as erosion except you find the max of the structuring element for each pixel
    comp = complement(img)#assign a varible comp the complement of the image
    ero_im = ero(comp)#erode this complement will find the min value for each structuring element
    dil_im = complement(ero_im)#finding the complement of this will give the dilated image since we will now have the max of each structuring element
    return dil_im#return the dilated image to be saved

def complement(img):#this just finds opposite pixel values of the image, 255 - each pixel value
    img = np.array(img.getdata()).reshape(img.size[0], img.size[1])#makes a numpy array of all the pixel values in the image
    if not img is None:#if we have an image
        h, w = np.shape(img)#assign the dimensions of the image to height and width variables
        data = np.zeros((w, h), dtype=np.uint8)# matrix the size of the image for appending data
        for py in range(h):#for each row, index py
            for px in range(w):#for each pixel px in row py
                data[px][py] = 255 - img[px][py]#calculate and assign the new pixel value
    im = Image.fromarray(data)#make an image
    return im#return the image

if len(sys.argv) == 3 :#requires 3 arguments, the file, and the name of the image to write and the name of what it should be writen as
    dilate(str(sys.argv[1]), str(sys.argv[2]))
else:
    print ("incorrect number of arguments entered")
    dilate()
