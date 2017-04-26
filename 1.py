import math
n = int (input('введите n'))
i = 1
p = 1
for i in range (1,n+1):
	p = p*i
	z = math.pow(2,i)
print (p)
print (z)

