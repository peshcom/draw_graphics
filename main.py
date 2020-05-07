#! /usr/bin/env python3
from PIL import Image
import math
import white_list

folder = "Files/"
out = "out.png"

open = True #Открывать ли фото после отрисовки

#Цвет линии графика
color = (0,0,255) 
#color = (255,0,0)	#RED
#color = (0,0,0) 	#Black

koef = 128 			# коэфицент количества измерений
delta = 64 			# Размер единицы - шаг между рисками на координатных осях в пикселях

res = 2049 								#Разрешение картинки 513 1025 2049 и тд (2^N +1)
color_xy = (0,0,0) 						#цвет координатных линий
length_mark = (delta/2).__trunc__() 	#Длинна рисок на координатных осях

def fun(x):
	try:
		print(x)
		y = math.sin(x)/x
		#y = math.exp(-math.pow(x, 2)/72)/15.0397
	except Exception as e:
		y = -100
		print(e)
	return y
''' 
math.sin()	math.sinh()
math.cos()	math.cosh()
math.tan()	math.tanh()

math.asin()	math.asinh()
math.acos()	math.acosh()
math.atan()	math.atanh() math.atan2()

math.frexp()
math.fsum()
math.gamma()
math.hypot()
math.isfinite()
math.isinf()
math.isnan()
math.ldexp()
math.lgamma()
math.copysign()
math.modf()
math.degrees()

#Мат константы
math.pi 	math.e

math.exp()	math.pow()	math.sqrt()	math.fabs()	math.factorial()
math.ceil() #Округление
math.log()	math.log10()		math.log1p()		math.log2()

math.erf()
math.radians()
math.erfc()
math.expm1()
math.fmod()             
'''

#Ставит точку по координатам x,y
def punkt(img, x,y):
	# Если делать точку = 1 пиксель, то на графике линия будет слишком тонкая.
	# Поэтому рисуем квадрат.
	# k - размер квадратика=точки на графике
	k = 6 #Используй четные 2 4 6 

	try:
		for i in range(0, k):
			for j in range(0, k):
				img.putpixel(
								(
									x-(k/2).__trunc__()+i,	#рисуем квадрат по X
									y-(k/2).__trunc__()+j	#рисуем квадрат по Y
								),		
								color
							)
	except Exception as e:
		pass
	return img


if __name__ == "__main__":
	# Создаем белый лист с нанесенными горизонтальными и вертикальными линияим и рисками на них.
	img = white_list.make(
							delta,		 #шаг между рисками по осям
							length_mark, #Длинна рисок на координатных осях
							color_xy,	 #цвет координатных линий
							res			 #Разрешение картинки
						)
	
	# Проходимся по всей оси абсцис и вычисляем значение y=f(x)
	# Затем ставим точку M(x,y) на графике 
	x = 0
	i = -(res-1)/(2*delta)
	while x < img.size[0]:
		img = punkt(img, x.__trunc__(), (img.size[1]/2 + 1 - fun(i)*delta).__trunc__())
		i = i + 1/(delta*koef)
		x = x + 1/koef
	img.save(out)
	img.close()

	if open:
		import os
		# Даем команду на открытие файла. 
		# На моей системе это делается так:
		os.system("bl-image-viewer " + out + " &")
