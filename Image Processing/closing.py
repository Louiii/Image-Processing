from erosion import ero
from dilation import dil
from PIL import Image
import sys

def closing(read_name = "lena.png", write_name = "lena_closing.png"):#accepts two string parameters for the file to read and file to write, setting their default values to the ones specified in the assignment
    img = Image.open(read_name)#store our image in a variable called img
    ero(dil(img)).save(write_name)#closing is the morphological process of dilating an image then eroding it, this line also saves the image under the 'write_name'

if len(sys.argv) == 3 :#requires 3 arguments, the file, and the name of the image to write and the name of what it should be writen as
    closing(str(sys.argv[1]), str(sys.argv[2]))
else:
    print ("incorrect number of arguments entered")
    closing()
