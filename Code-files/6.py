def fib(n):
	n1 = 0
	n2 = 1
	fib_list = []
	for i in range(2, n):
		n3 = n1 + n2
		n1 = n2
		n2 = n3
		fib_list.append(n3)		
	return fib_list
print(fib(10))