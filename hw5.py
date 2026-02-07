import struct
import functools

'''
You need to implement the six empty functions defined below.
Each function takes a single argument:
  an image represented as a list of lists of pixels, where
  each pixel is a dictionary as described in the HTML file.
Each function returns a new list in exactly that same form.

The inputPPM and outputPPM functions defined at the end of the file should NOT be
called by your code.  Rather, they are provided to help you test your code:
inputPPM allows you to convert PPM image files into lists of lists of pixels that
can be passed as arguments to your functions, and outputPPM allows you to write the
results of your functions to image files so that the images can be viewed.  See
the HTML file for an example of how to use these functions.

But viewing images is not sufficient!  You should also test as we usually do, by
writing tests to ensure that the output of your function is as expected.  See
hw5test.py.
'''

def negate(pixels):
    return list(map(lambda innerRow: list(map(lambda pixel: {'r': 255 - pixel['r'], 'g': 255 - pixel['g'], 'b': 255 - pixel['b']}, innerRow)), pixels))


                       
def greyscale(pixels):
    return list(map(lambda innerRow: list(map(lambda pixel: {'r': int(round((pixel['r'] + pixel['g'] + pixel['b'])/3)), 'g': int(round((pixel['r'] + pixel['g'] + pixel['b'])/3)), 'b': int(round((pixel['r'] + pixel['g'] + pixel['b'])/3))}, innerRow)), pixels))
     


def upsideDown(pixels):
    return pixels[::-1]


def mirrorImage(pixels):
    innerList = list(map(lambda row: row[::-1], pixels))
    return innerList

def compress(pixels):
    list1 = list(map(lambda row: row[::2], pixels))
    return list1[::2]


def decompress(pixels):
    #we need to "walk" over the list first
    duplicate_pixel = lambda row: functools.reduce(lambda acc, pixel: acc + [pixel,pixel], row, [])
    #return a list
    innerlist = list(map(duplicate_pixel, pixels))
    #then duplicate that using the same thing
    return functools.reduce(lambda acc, decomp: acc + [decomp, decomp], innerlist, [])
    


# input the PPM image file named fname and convert it to a list of lists of pixels.
# each pixel is an RGB triple, represented using a dictionary with keys "r", "g",
# and "b". each list of pixels represents one row in the image, ordered from top to
# bottom.
def inputPPM(fname):
    f = open(fname, "rb")
    p6Ignore = f.readline()
    dimensions = f.readline().split()
    width = int(dimensions[0])
    height = int(dimensions[1])
    maxIgnore = f.readline()

    pixels = []
    rgbData = [x for x in f.read()]
    f.close()
    for r in range(height):
        row = []
        for c in range(width):
            i = 3 * (r * width + c)
            row.append({"r":rgbData[i], "g":rgbData[i+1], "b":rgbData[i+2]})
        pixels.append(row)
    return pixels


# pixels should be a list of list of RGB triples, in the same format as returned
# by the inputPPM function above.
# this function outputs those pixels to the file named fname as a PPM image.
def outputPPM(pixels, fname):
    f = open(fname, "wb")
    f.write("P6\n".encode())
    width = len(pixels[0])
    height = len(pixels)
    f.write((str(width) + " " + str(height) + "\n").encode())
    f.write((str(255) + "\n").encode())
    bPixels = [[struct.pack('BBB', p["r"], p["g"], p["b"]) for p in r] for r in pixels]
    flatPixels = functools.reduce(lambda x,y: x+y, bPixels)
    f.writelines(flatPixels)
    f.close()


