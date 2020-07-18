def sum_of_list(li, n):
	if len(li) == 1:
		return li[0]
	else:
		return li[0] + sum_of_list(li[1:], n)
list_1 = [1, 2, 3, 4, 5, 6]
print(sum_of_list(list_1, len(list_1)))
