import math
i = -20
z = 0
for i in range (-20,20):
	if (math.fmod(i,5) == 0) and (-20<=i<0):
		z = z + i
		i = i + 1
	else: 
		i = i + 1
print (z)
