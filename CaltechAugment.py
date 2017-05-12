#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:50:05 2017

@author: sezan92
"""

from os import listdir
from os.path import isfile,join
import numpy as np
import cv2

import imutils 
import pandas as pd
def Rotate(img):
    img = imutils.rotate(img,np.random.normal(0,5))
    return img

def GaussNoise(img):
    noise = np.random.normal(0,1,img.shape)
    img = img+noise
    return img
    
    
    #im2.show()
    
 

Ant = '/home/sezan92/Classifier/Caltech101/ant'
Beaver = '/home/sezan92/Classifier/Caltech101/beaver'
Butterfly = '/home/sezan92/Classifier/Caltech101/butterfly'
Dalmatian = '/home/sezan92/Classifier/Caltech101/dalmatian'
Dolphin = '/home/sezan92/Classifier/Caltech101/dolphin'
Test ='/home/sezan92/Classifier/Caltech101/Test'
AntImages = [ f for f in listdir(Ant) if isfile(join(Ant,f)) ]
BeaverImages = [ f for f in listdir(Beaver) if isfile(join(Beaver,f)) ]
ButterflyImages = [ f for f in listdir(Butterfly) if isfile(join(Butterfly,f)) ]
DolphinImages = [ f for f in listdir(Dolphin) if isfile(join(Dolphin,f)) ]
DalmatianImages = [ f for f in listdir(Dalmatian) if isfile(join(Dalmatian,f)) ]
TestImages = [ f for f in listdir(Test) if isfile(join(Test,f)) ]

def ReadImages(ListName,FolderName,Flag = False):
    global NumberList
    global responseData
    global trainData
    global hog
    global cv2
    global imutils
    global winSize

    if Flag is True:
        
 
        folder = FolderName    
        for image in listdir(folder):
            print "Reading " + image + " And Saving"
            img =cv2.imread(join(folder,image))
            imgRot = Rotate(img)
            cv2.imwrite(folder+'/Rotated'+image,imgRot)
            imgRot2= -Rotate(img)
            cv2.imwrite(folder+'/Rotate2'+image,imgRot2)
            imNoise= GaussNoise(img)
            cv2.imwrite(folder+'/GNoise'+image,imNoise)
            imNoise2= GaussNoise(img)
            cv2.imwrite(folder+'/GNoise2'+image,imNoise2)
            print "Saving Images"

ReadImages(AntImages,Ant,Flag = True)
ReadImages(BeaverImages,Beaver,Flag = True)
ReadImages(ButterflyImages,Butterfly,Flag = True)
ReadImages(DolphinImages,Dolphin,Flag = True)
ReadImages(DalmatianImages,Dalmatian,Flag = True)

            
print " Saved All images"

