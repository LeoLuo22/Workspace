# -*- coding:utf-8 -*-

from PIL import Image
import argparse
import sys, os
ASCII_CHAR = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

parser = argparse.ArgumentParser()

parser.add_argument('--file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type=int)#, defalut=80)
parser.add_argument('--height', type=int)#, defalut=80)

args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

def get_char(r, g, b, alpha=256):

    if alpha == 0:
        return ' '
    length = len(ASCII_CHAR)
    #Get the value of gray
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length

    #mapping
    return ASCII_CHAR[int(gray/unit)]

if __name__ == "__main__":

    im = Image.open("test.jpg")
    im = im.resize((108, 192), Image.NEAREST)
    pix = im.load()
    width = im.size[0]
    height = im.size[1]

    text = ""
    for i in range(width):
        for j in range(height):
            r, g, b = pix[i, j]
            text += get_char(r, g, b)
        text += "\n"

    print(text)

