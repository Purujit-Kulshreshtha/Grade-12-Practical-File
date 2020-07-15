'''import math
n = 9
print(math.factorial(n))
print(math.sqrt(n))
print(math.log(n, 2))'''

import math
'''
ran = int(input("Please enter the range: "))
var = int(input("Please enter the variable: "))'''

sum_of = 0

def fact(num):
	if num == 1:
		return num
	else:
		return num*fact(num-1)

'''
for i in range(0, ran):
	sum_of += var**i/math.factorial(i)'''

print(sum_of)
print(fact(4))