def armstrong(num):
	addition = 0
	a = num
	while num > 0:
		dg = num % 10
		addition += dg**3
		num = num//10
	if addition == a:
		return f"{a} is an armstrong number."
	else:
		return f"{a} is not an armstrong number."
print(armstrong(153))
print(armstrong(406))