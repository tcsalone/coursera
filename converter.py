#! /usr/bin/env python3

import os, sys
from PIL import Image

dirName = "/home/eamon/coursera/Course5/week1/images"
destDir = "/home/eamon/coursera/Course5/week1/"

#print (destDir)
listOfFiles = list()

for (dirpath, dirnames, filenames) in os.walk(dirName):
    listOfFiles += filenames

for infile in listOfFiles:
    f, e = os.path.splitext(infile)
    #print("F in file", f)
    outfile = destDir + f + ".jpeg"
    #print (outfile)
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                #print(im.format)
                rgb_im = im.convert("RGB")
                rotate_im = rgb_im.rotate(90)
                resize_im = rotate_im.resize((128, 128))
                resize_im.save(outfile, "JPEG")
        except IOError as err:
            print("I/O error: {0}".format(err))
            print("cannot convert", infile)
