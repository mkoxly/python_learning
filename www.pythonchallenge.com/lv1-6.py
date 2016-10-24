# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 09:50:41 2016

@author: Administrator
"""

import re, urllib, pickle, string, zipfile
import os
import os.path


def lv0():
    '''
     http://www.pythonchallenge.com/pc/def/0.html
     
     answer : 274877906944

    '''
    print pow(2, 38)


def lv1_map():
    '''
     http://www.pythonchallenge.com/pc/def/map.html
     k -> m
     o -> q    +2
     a -> c
     z  -> b     
    '''
    src = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
    print ''.join([chr((ord(i) + 2 - 96) % 26 + 96) if ord(i) >= ord('a') and ord(i) <= ord('z') else i for i in src])
    # map ->ocr


def lv2_ocr():
    '''
    http://www.pythonchallenge.com/pc/def/ocr.html
    find rare word in source of page  it below the word 'below'
    '''
    data = urllib.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()
    print filter(lambda a: a in string.letters, data).split('below')[-1]


def lv3_equality():
    '''
     http://www.pythonchallenge.com/pc/def/equality.html
    '''
    data = urllib.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read()
    pattern = re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
    print ''.join(pattern.findall(data))


def lv4_linkedlist():
    '''
    level 4 http://www.pythonchallenge.com/pc/def/linkedlist.php
    
    anwser loop 358: peak.html
    '''
    nothing = '12345'
    o = 'D:\temp\resource\linkedlist-answer.txt'
    data = []
    i = 1
    while (i <= 400):
        try:
            page = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothing).read()
            data += [nothing]
            nothing = page.split()[-1]
            i += 1
        except:
            pass
        print '{:^5}:{:^10}'.format(i, nothing)
    f = open(o, 'w')
    f.write(''.join([str(l) + ':' + data[l] + '\n' for l in range(len(data))]))
    f.close()
    # for i in range(len(data)):
    #    f.write(str(i)+':'+data[i]+'\n')        


def lv5_pickle():
    '''
    peak pronouce like pickle in python 
    www.pythonchallenge.com/pc/def/pickle.html 
    http://www.pythonchallenge.com/pc/def/banner.p
    level 5  chracter picture -> channel
    序列化对象
    '''
    url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    objsrc = urllib.urlopen(url).read()
    obj = pickle.loads(objsrc)
    print ''.join([''.join([str(i[0]) * i[1] for i in row]) + '\n' for row in obj])
    # for line in obj:
    #  s=''  
    #  for word in line:
    #      s+=str(word[0])*word[1]
    #  print(s) 


def lv6_channel():
    '''
             <html> <!-- <-- zip -->
<head>
  <title>now there are pairs</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<center>
<img src="channel.jpg">
<br/>
<!-- The following has nothing to do with the riddle itself. I just
thought it would be the right point to offer you to donate to the
Python Challenge project. Any amount will be greatly appreciated.

-thesamet
-->

   get http://www.pythonchallenge.com/pc/def/channel.zip
   
   read zip comment in order
   
   
   answer:  hockey  picture char   oxygen
'''
    fname = r'D:\temp\download\channel.zip'
    # t = r'D:\temp\download\channel'
    zipf = zipfile.ZipFile(fname)
    # zipf.extractall(r'D:\temp\download\channel')  #already run
    # ans=[]
    f = '90052.txt'
    ptn = re.compile(r'Next nothing is (\d+)')
    comment = []
    while True:
        content = zipf.read(f)
        comment.append(zipf.getinfo(f).comment)
        m = ptn.match(content)
        if m:
            f = m.group(1) + '.txt'
        else:
            break
    print ''.join(comment)
    zipf.close()
    
#        n = os.path.join(t,f)
#        if not os.path.exists(n):break
#        ans+=[f]
#        fh = open(n)        
#        f = fh.read().split()[-1]+'.txt'
#        fh.close()
#    print ans
#    s=''
#    for f in ans:
#       s+=zipf.getinfo(f).comment.decode()  
#      
#    print s



if (__name__ == '__main__'):
    print 'MAIN'
    lv5_pickle()
    lv6_channel()
