import math
n = int (input("Введите n "))
i = 1
for i in range (1,n+1):
	z = 1
	f = 0
	for z in range (1,i+1):
		if math.fmod(i,z) == 0 :
			f = f+1
	if (f <= 2):
		print (i , " ")

