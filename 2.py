import math
n = int (input('введите n'))
i = 1
k = 1
z = 0
for i in range (1,n+1):
	z = z + ((math.pow((k-4),3))*(k+7))/(math.factorial(k))
	k = k + 1
print (z)
