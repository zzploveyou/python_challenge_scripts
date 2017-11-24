# coding:utf-8
'''
huge
file
http://www.pythonchallenge.com/pc/return/5808.html
http://www.pythonchallenge.com/pc/return/evil.html
'''

from PIL import Image


def main():
    im = Image.open("cave.jpg")
    width, height = im.size
    for i in range(width):
        for j in range(height):
            if((i + j) % 2 == 1):
                im.putpixel((i, j), 1)

    im.save("cave2.png")

if __name__ == '__main__':
    main()
