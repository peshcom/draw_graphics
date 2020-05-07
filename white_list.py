#! /usr/bin/env python3
from PIL import Image

def make(delta,length_mark,color,res):
	img = Image.new("RGB", (res,res), (255,255,255))

	#Наносим оси
	for i in range(0,img.size[0]):
		img.putpixel(
						(
							i,
							(img.size[0]/2 +1).__trunc__()
						),
						color
					)	#По оси X

	for i in range(0,img.size[1]):
		img.putpixel(
						(
							(img.size[0]/2 +1).__trunc__(),
							i
						),
						color
					) 	#По оси Y
	
	#Наносим разметку
	#По оси абсцис
	i = 0
	while i < img.size[0]:
		for j in range(0,length_mark):
			img.putpixel(
							(
								i, 
								(img.size[0]/2 - (length_mark/2) +j +1).__trunc__()
							),
							color
						)
		i = i + delta
	#По оси ординат
	i = 0
	while i < img.size[1]:
		for j in range(0,length_mark):
			img.putpixel(
							(
								(img.size[1]/2 - (length_mark/2) +j +1).__trunc__(),
								i
							),
							color
						)
		i = i + delta
	
	return img