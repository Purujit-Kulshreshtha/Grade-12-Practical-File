def check_for_ones(num1, num2):
	print("The two numbers are " + str(num1) + " and " + str(num2))
	li = [num1, num2]
	list_of_ones = []
	basic = "The number with higher one's digit is: "
	for i in li:
		string_of_num = str(i)
		last_val = string_of_num[len(string_of_num) - 1]
		list_of_ones.append(last_val)
	if list_of_ones[0] > list_of_ones [1]:
		return basic + str(num1)
	else:
		return basic + str(num2)
print(check_for_ones(10248, 28391))