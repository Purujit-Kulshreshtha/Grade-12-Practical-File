def prime_or_not(num):
	if num < 2:
		return "Please enter a positive integer greater than 1."
	else:
		for i in range(2, num):
			if num % i == 0:
				return (str(num) + " is not a prime number.")
				break
		else:
			return (str(num) + " is a prime number.")
print(prime_or_not(9))
print(prime_or_not(13))