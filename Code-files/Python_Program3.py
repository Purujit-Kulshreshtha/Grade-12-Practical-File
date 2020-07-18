import random
def radom_generation(low, high):
	return random.randint(low, high)
for i in range(0, 3):
	print(radom_generation(20, 40), end = " ")