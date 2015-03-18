# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 12:38:35 2014

@author: manom
"""


from PIL import Image
import glob
import os
import cv2

for infile in glob.glob("C:\AUTOMATION\IMAGE RECOVERY TOOL\dist\images\*.jpg"):
          file, ext = os.path.splitext(infile)


          #img = Image.open(infile)
          img = cv2.imread(infile)
          print 'Filename: '+infile[46:74]
          print '...................'
          print 'Converting to JPEG'
          print '...................'
          print 'Converting Done !!!'
          
          
          
          #img.save(file +".jpg","JPEG")
          img = cv2.imwrite(infile,img)
         
         