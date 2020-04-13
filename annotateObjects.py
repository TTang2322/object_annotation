#!/usr/bin/python  
# -*- coding:utf8 -*-  

'''
coding date:2018-08-12
modify date:2018-09-13
author:TTang
'''

import cv2
import os
import math
import colorsys
from PIL import Image
import matplotlib.pyplot as plt
import getRGB as colors

def annotateObject(fold,name):

	# initialize parameters
	global state,No
	state=True
	No=0

	cwd=os.getcwd()
	imagePath = cwd+'/datasets'+'/'+fold+'/'+name+'.png'
	txtPath=cwd+'/datasets'+'/'+fold+'/'+name+'.txt'
	file=open(txtPath)

	# annotate information for each object
	for content in file:

		# count the number of objects
		No=No+1
		print('#########  The '+str(No)+'th object is being annotated  ##########')

		# get the information of each object
		items=content.split('	')
		[x1,y1,width,height,theta]=[items[9],items[10],items[11],items[12],items[8]]
		x1=round(float(x1))
		x1=int(x1)
		y1=round(float(y1))
		y1=int(y1)
		x4=round(float(x1)+float(width))
		x4=int(x4)
		y4=round(float(y1)+float(height))
		y4=int(y4)
		theta=round(float(theta))
		theta=int(theta)
		size=float(width)*float(height)
		size=int(size)

		# load the image where object is in
		img = cv2.imread(imagePath)

		# draw bounding box of object
		cv2.rectangle(img, (x1,y1), (x4,y4), (0,255,0), 1)

		# get the RGB of object
		img2=Image.open(imagePath)
		box=[x1,y1,x4,y4]
		roi=img2.crop(box)
		rgb=colors.get_color(roi)

		# add information in image
		font = cv2.FONT_HERSHEY_SIMPLEX
		text0='Type is :'+fold
		text1 = 'Location '+'x:'+str(x1)+' y:'+str(y1)
		text2='Angle with X axis is '+ str(theta)
		text3='Color of object in RGB is '+str(rgb)
		text4='Size of object is '+str(size)+' pixles'
		cv2.putText(img, text0, (x4,y4-20), font, 0.5, (0,0,255), 1)
		cv2.putText(img, text1, (x4,y4), font, 0.5, (0,0,255), 1)
		cv2.putText(img, text2, (x4,y4+20), font, 0.5, (0,0,255), 1)
		cv2.putText(img, text3, (x4,y4+40), font, 0.5, (0,0,255), 1)
		cv2.putText(img, text4, (x4,y4+60), font, 0.5, (0,0,255), 1)

		# save the annotated image
		cv2.imwrite(cwd+'/annotation/'+fold+'_'+name+'_'+str(No)+'_.jpg', img)

		# show annotated image
		plt.ion()
		annotatedaImgPath=cwd+'/annotation/'+fold+'_'+name+'_'+str(No)+'_.jpg'
		annotatedImg=Image.open(annotatedaImgPath)
		plt.figure(figsize=(10, 5)) 
		plt.title('The '+str(No)+'th object')
		plt.imshow(annotatedImg)
		plt.axis('off')
		plt.pause(1)
		plt.close()

	return No
	file.close()

if __name__=="__main__":

	# set path of objective image
	# name='P0007'
	# fold='CAR'
	fold=raw_input('enter the fold name ===> ')
	name=raw_input('enter the image name ===> ')

	number=annotateObject(fold,name)
	print('')
	print('')
	print('The total number of '+fold+' in image is '+str(number))
	print('The annotated images is in fold :\n %s'%os.getcwd()+'/status')
	print('')
	print('')