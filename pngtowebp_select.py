#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
import os
import threading
import sys
from Tkinter import * 
from tkMessageBox import *

from PIL import Image
 
path = os.path.abspath(os.path.dirname(sys.argv[0]))

def select10():
  successSelect(10)

def select20():
  successSelect(20)
 
def select30():
  successSelect(30)

def select40():
  successSelect(40)

def select50():
  successSelect(50)

def select60():
  successSelect(60)
 
def select70():
  successSelect(70)

def select80():
  successSelect(80)

def select90():
  successSelect(90)

def selectInput():
  str = raw_input("请输入0～100的整数: ")
  if str != "": 
    print str
    if str.isdigit():  
      ratio = int(str)
      successSelect(ratio)
      selectInput()
    else:
      print "输入错误!"
      selectInput()
  else:
    print "输入错误!"
    selectInput()

def selectExit():
  os._exit(0)

def successSelect(ratio):
  if os.path.exists(path+'/img_bigger_%d' % ratio) == False:
    os.mkdir(path+"/img_bigger_%d" % ratio)
  if os.path.exists(path+'/img_smaller_%d' % ratio) == False:
    os.mkdir(path+"/img_smaller_%d" % ratio)
  if ratio < 0:
    ratio = 0
  if ratio > 100:
    ratio = 100
  index = 0
  for infile in glob.glob(path+"/img/*.png"):
    t = threading.Thread(target=create_image, args=(infile, ratio, index,))
    t.start()
    t.join()
    index += 1

def create_image(infile, ratio, index):
  os.path.splitext(infile)
  im = Image.open(infile)
  w,h = im.size
  w = w*ratio//100
  h = h*ratio//100
  im = im.resize((w, h),Image.ANTIALIAS)
  (filepath,tempfilename) = os.path.split(infile)
  (filename,extension) = os.path.splitext(tempfilename)
  fullpath = path+"/img/"+filename + ".webp"
  im.save(fullpath, "WEBP")
  sizeinfile = os.path.getsize(infile)
  sizefullpath = os.path.getsize(fullpath)
  if sizeinfile > sizefullpath:
    im.save(path+"/img_smaller_%d/" % ratio+filename + ".webp", "WEBP")
  else:
    im.save(path+"/img_bigger_%d/" % ratio+filename + ".webp", "WEBP")


def start():
  Button(text='10', command=select10).pack(fill=X)
  Button(text='20', command=select20).pack(fill=X)
  Button(text='30', command=select30).pack(fill=X)
  Button(text='40', command=select40).pack(fill=X)
  Button(text='50', command=select50).pack(fill=X)
  Button(text='60', command=select60).pack(fill=X)
  Button(text='70', command=select70).pack(fill=X)
  Button(text='80', command=select80).pack(fill=X)
  Button(text='90', command=select90).pack(fill=X)
  Button(text='键盘输入', command=selectInput).pack(fill=X)
  Button(text='退出', command=selectExit).pack(fill=X)
  mainloop()
 
 
if __name__ == "__main__":
    start()
