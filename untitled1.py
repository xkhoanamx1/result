# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 13:22:35 2021

@author: NAY3HC
"""
import pandas as pd
import numpy as np
import os.path
import glob
import cv2

test_files = [os.path.basename(x) for x in glob.glob(r"C:/Users/NAY3HC/Desktop/core test/CV/KERAS-FASTERRCNN/keras-frcnn/test/*.jpeg")]
output = "C:\\Users\\NAY3HC\\Desktop\\core test\\CV\\KERAS-FASTERRCNN\\keras-frcnn\\test1\\"
link = "C:\\Users\\NAY3HC\\Desktop\\core test\\CV\\KERAS-FASTERRCNN\\keras-frcnn\\test\\"
for img in test_files:
    
    img1 = link + str(img)
    print(img1)
    ##img1 = np.array(img1)
    img2 = cv2.imread(img1)
    height,width,a =img2.shape
    img_array = cv2.resize(img2, dsize=(1024, 1024), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(output+img,img_array) 