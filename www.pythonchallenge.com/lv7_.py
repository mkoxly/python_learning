# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:34:18 2016

@author: Administrator


"""
from PIL import Image, ImageDraw
import re
import bz2


def lv7_oxygen():
    '''
     http://www.pythonchallenge.com/pc/def/oxygen.html
     http://www.pythonchallenge.com/pc/def/oxygen.png
     读出图片最中间一条像素的R,G,B值. 这些R=G=B
     以这些RGB数值取chr可得
     sssssmmmmmmmaaaaaaarrrrrrrttttttt       ggggggguuuuuuuyyyyyyy,,,,,,,
     yyyyyyyooooooouuuuuuu       mmmmmmmaaaaaaadddddddeeeeeee       iiiiiiittttttt.......
     ttttttthhhhhhheeeeeee       nnnnnnneeeeeeexxxxxxxttttttt       llllllleeeeeeevvvvvvveeeeeeelllllll       iiiiiiisssssss       [[[[[[[111111100000005555555,,,,,,,       111111111111110000000,,,,,,,       111111111111116666666,,,,,,,       111111100000001111111,,,,,,,       111111100000003333333,,,,,,,       111111111111114444444,,,,,,,       111111100000005555555,,,,,,,       111111111111116666666,,,,,,,       111111122222221111111]]]]]]]]womhehnleghfbda]`egea

     去重可见smart guy,you made it .the next level is  [105,110,116,101,103,114,105,116,121]
     chr() 即为 integrity
    '''
    pic = r'D:\temp\python-code\python_learning\www.pythonchallenge.com\oxygen.png'
    im = Image.open(pic)
    (width, height) = im.size
    rs = []
    for k in range(0, 629, 7):  # the same for 7 pixel
        (r, g, b, a) = im.getpixel((k, 48))  # 48 = height/2
        rs.append(r)
    ans = ''.join([chr(i) for i in rs])
    # print ans
    # print re.findall(r'\d+',ans)
    print ''.join(map(chr, map(int, re.findall(r'\d+', ans))))


def lv8_integrity():
    '''
    http://www.pythonchallenge.com/pc/def/integrity.html
    find compress data at source of page
    ans: huge  file
    '''

    print bz2.decompress(
        'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
    print bz2.decompress('BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')


def lv9_good():
    '''
    http://www.pythonchallenge.com/pc/return/good.html
    '''
    first = [146, 399, 163, 403, 170, 393, 169, 391, 166, 386, 170, 381, 170, 371, 170, 355, 169, 346, 167, 335, 170,
             329, 170, 320, 170,
             310, 171, 301, 173, 290, 178, 289, 182, 287, 188, 286, 190, 286, 192, 291, 194, 296, 195, 305, 194, 307,
             191, 312, 190, 316,
             190, 321, 192, 331, 193, 338, 196, 341, 197, 346, 199, 352, 198, 360, 197, 366, 197, 373, 196, 380, 197,
             383, 196, 387, 192,
             389, 191, 392, 190, 396, 189, 400, 194, 401, 201, 402, 208, 403, 213, 402, 216, 401, 219, 397, 219, 393,
             216, 390, 215, 385,
             215, 379, 213, 373, 213, 365, 212, 360, 210, 353, 210, 347, 212, 338, 213, 329, 214, 319, 215, 311, 215,
             306, 216, 296, 218,
             290, 221, 283, 225, 282, 233, 284, 238, 287, 243, 290, 250, 291, 255, 294, 261, 293, 265, 291, 271, 291,
             273, 289, 278, 287,
             279, 285, 281, 280, 284, 278, 284, 276, 287, 277, 289, 283, 291, 286, 294, 291, 296, 295, 299, 300, 301,
             304, 304, 320, 305,
             327, 306, 332, 307, 341, 306, 349, 303, 354, 301, 364, 301, 371, 297, 375, 292, 384, 291, 386, 302, 393,
             324, 391, 333, 387,
             328, 375, 329, 367, 329, 353, 330, 341, 331, 328, 336, 319, 338, 310, 341, 304, 341, 285, 341, 278, 343,
             269, 344, 262, 346,
             259, 346, 251, 349, 259, 349, 264, 349, 273, 349, 280, 349, 288, 349, 295, 349, 298, 354, 293, 356, 286,
             354, 279, 352, 268,
             352, 257, 351, 249, 350, 234, 351, 211, 352, 197, 354, 185, 353, 171, 351, 154, 348, 147, 342, 137, 339,
             132, 330, 122, 327,
             120, 314, 116, 304, 117, 293, 118, 284, 118, 281, 122, 275, 128, 265, 129, 257, 131, 244, 133, 239, 134,
             228, 136, 221, 137,
             214, 138, 209, 135, 201, 132, 192, 130, 184, 131, 175, 129, 170, 131, 159, 134, 157, 134, 160, 130, 170,
             125, 176, 114, 176,
             102, 173, 103, 172, 108, 171, 111, 163, 115, 156, 116, 149, 117, 142, 116, 136, 115, 129, 115, 124, 115,
             120, 115, 115, 117,
             113, 120, 109, 122, 102, 122, 100, 121, 95, 121, 89, 115, 87, 110, 82, 109, 84, 118, 89, 123, 93, 129, 100,
             130, 108, 132, 110,
             133, 110, 136, 107, 138, 105, 140, 95, 138, 86, 141, 79, 149, 77, 155, 81, 162, 90, 165, 97, 167, 99, 171,
             109, 171, 107, 161,
             111, 156, 113, 170, 115, 185, 118, 208, 117, 223, 121, 239, 128, 251, 133, 259, 136, 266, 139, 276, 143,
             290, 148, 310, 151,
             332, 155, 348, 156, 353, 153, 366, 149, 379, 147, 394, 146, 399]
    second = [156, 141, 165, 135, 169, 131, 176, 130, 187, 134, 191, 140, 191, 146, 186, 150, 179, 155, 175, 157, 168,
              157, 163, 157, 159,
              157, 158, 164, 159, 175, 159, 181, 157, 191, 154, 197, 153, 205, 153, 210, 152, 212, 147, 215, 146, 218,
              143, 220, 132, 220,
              125, 217, 119, 209, 116, 196, 115, 185, 114, 172, 114, 167, 112, 161, 109, 165, 107, 170, 99, 171, 97,
              167, 89, 164, 81, 162,
              77, 155, 81, 148, 87, 140, 96, 138, 105, 141, 110, 136, 111, 126, 113, 129, 118, 117, 128, 114, 137, 115,
              146, 114, 155, 115,
              158, 121, 157, 128, 156, 134, 157, 136, 156, 136]
    img = Image.new('RGB', (640, 480))
    draw = ImageDraw.Draw(img)
    draw.line(first)
    draw.line(second)
    img.show()  # a bull in picture


def lv10_bull():
    """""
    http://www.pythonchallenge.com/pc/return/bull.html
    http://www.pythonchallenge.com/pc/return/sequence.txt
    a = [1, 11, 21, 1211, 111221,
    #1,2,3,5,8,
    len(a[30]) = ? 5808
    """""

    def nextSeq(seq):
        strList = str(seq)
        curChar = ' '
        chars = []
        counts = []
        for i in strList:
            if (i != curChar):
                chars.append(i)
                counts.append(1)
                curChar = i
            else:
                counts[-1] += 1
        o = zip(counts, chars)
        return ''.join([str(row[0]) + row[1] for row in o])

    print nextSeq('2011')
    loop = 1
    bseq = '1'
    ans = []
    #while loop <= 31:
    #    ans.append(bseq)
    #    bseq = nextSeq(bseq)
    #    loop += 1
    # for i in range(len(ans)):
    #    print '{:5d} : '.format(i)+ans[i]
    #print len(ans[30])

    ## use re
    def nextSeqRE(bseq):
        return ''.join([str(len(c[1]) + 1) + c[0] for c in re.findall(r'(\d)(\1*)', bseq)])

    bseq = '1'
    for i in range(30):
        bseq = nextSeqRE(bseq)
        print len(bseq)


def lv11_5808():
    im = Image.open('cave.jpg')
    data = list(im.getdata())
    im_new = Image.new(im.mode, im.size)
    im_new.putdata(data[::2] + data[1::2])
    im_new.show()


def new_ff():
    pic = Image.open("cave.jpg")
    width, height = pic.size

    even = Image.new("RGB", [640, 480])
    odd = Image.new("RGB", [640, 480])
    evenpixels = even.load()
    oddpixels = odd.load()

    for x in range(0, width, 2):
        for y in range(0, height, 2):
            evenpixels[x, y] = pic.getpixel((x, y))
            evenpixels[x + 1, y + 1] = pic.getpixel((x + 1, y + 1))
            oddpixels[x, y + 1] = pic.getpixel((x, y + 1))
            oddpixels[x + 1, y] = pic.getpixel((x + 1, y))

    even.show()
    odd.show()


def my_ff():
    od = lambda x: x % 2 == 0
    pic = Image.open("cave.jpg")
    w, h = pic.size
    p1 = Image.new("RGB", [640, 480])
    p2 = Image.new("RGB", [640, 480])
    p3 = Image.new("RGB", [640, 480])
    p4 = Image.new("RGB", [640, 480])
    p1pixels = p1.load()
    p2pixels = p2.load()
    p3pixels = p3.load()
    p4pixels = p4.load()
    for x in range(w):
        for y in range(h):
            if od(x):
                if od(y):
                    p1pixels[x, y] = pic.getpixel((x, y))
                else:
                    p2pixels[x, y] = pic.getpixel((x, y))
            else:
                if od(y):
                    p3pixels[x, y] = pic.getpixel((x, y))
                else:
                    p4pixels[x, y] = pic.getpixel((x, y))
    p1.show()
    p2.show()
    p3.show()
    p4.show()


if __name__ == '__main__':
    # lv9_good()
    lv10_bull()
    # lv11_5808()
    # my_ff()
