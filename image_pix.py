# coding:utf-8
'''
http://www.pythonchallenge.com/pc/def/oxygen.html
Results:
[115, 109, 97, 114, 116, 32, 103, 117, 121, 44, 32, 121, 111, 117, 32, 109, 97, 100, 101, 32, 105, 116, 46, 32, 116, 104, 101, 32, 110, 101, 120, 116, 32, 108, 101,
118, 101, 108, 32, 105, 115, 32, 91, 49, 48, 53, 44, 32, 49, 49, 48, 44, 32, 49, 49, 54, 44, 32, 49, 48, 49, 44, 32, 49, 48, 51, 44, 32, 49, 49, 52, 44, 32, 49, 48,
53, 44, 32, 49, 49, 54, 44, 32, 49, 50, 49, 93]
smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
integrity

'''
from PIL import Image
im = Image.open("oxygen.png")
x, y = im.size
pix = im.load()
nums = []
temp = 0
for i in range(0,x,7):
    # pix[a,b] is (R, G, B, A)
    p = pix[i, y/2]
    if p[0] == p[1] == p[2]:
        num = p[0]
        nums.append(num)
    else:
        break
print nums
print ''.join(map(chr, nums))
print ''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))
