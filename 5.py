import math
print ('2*4')
print ('3*4')
print ('2*6')
print ('5*5')
print ('2*9')
print ('7*4')
print ('8*2')
print ('7*5')
print ('4*4')
print ('2*2')
n = int (input ('ответ на первый пример'))
j = int (input ('ответ на второй пример'))
a = int (input ('ответ на третий пример'))
b = int (input ('ответ на четвертый пример'))
c = int (input ('ответ на пятый пример'))
d = int (input ('ответ на шестой пример'))
e = int (input ('ответ на седьмой пример'))
f = int (input ('ответ на восьмой пример'))
g = int (input ('ответ на девятый пример'))
h = int (input ('ответ на десятый пример'))
x = 10
if n == 8:
	x = x-1
if j == 12:
	x = x-1
if a == 12:
	x = x-1
if b == 25:
	x = x-1
if c == 18:
	x = x-1
if d == 28:
	x = x-1
if e == 16:
	x = x-1
if f == 35:
	x = x-1
if g == 16:
	x = x-1
if g == 4:
	x = x-1
if x == 0:
	print ('отлично')
	if x <= 2:
		print ('хорошо')
		if x <= 4:
			print ('удовлетворительно')
			if x >= 5:
				print ('плохо')



