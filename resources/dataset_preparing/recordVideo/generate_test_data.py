import xml.etree.ElementTree as ET
from ctypes import *
import math
import random
import cv2 as cv
import numpy as np
import time
import os

num=2
test_num=1
train_num=1
classname="stone_"
if __name__ == "__main__":
	for f in range(1, 117):
		img_path="Images/"+str(f)+".jpg"
		#xml_path="/home/artic/Desktop/Hand_Gesture_Paper/dataset4/VOCdevkit/VOC2012/Annotations/"+classname+str(f)+".xml"
		img=cv.imread(img_path)
		#in_file = open(xml_path)
		#tree=ET.parse(in_file)
		#root = tree.getroot()
		#tree = ET.ElementTree(root)
		#os.remove(img_path)
		#os.remove(xml_path)

		print(f)
		if f%10==0:
			cv.imwrite("VOCdevkit/VOC2007/JPEGImages/"+str(test_num)+".jpg",img)
			#tree.write("/home/artic/Desktop/Hand_Gesture_Paper/dataset4/VOCdevkit/VOC2007/Annotations/"+classname+str(test_num)+".xml")
			test_num+=1
		else:
			cv.imwrite("VOCdevkit/VOC2012/JPEGImages/"+str(train_num)+".jpg",img)
			#tree.write("/home/artic/Desktop/Hand_Gesture_Paper/dataset4/VOCdevkit/VOC2013/Annotations/"+classname+str(train_num)+".xml")
			train_num+=1
