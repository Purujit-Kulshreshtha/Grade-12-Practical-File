def insertion_sort(list1):
	for i in range(len(list1) - 1):
		minpos = i
		for j in range(i, len(list1)):
			if list1[j] < list1[minpos]:
				minpos = j
		temp = list1[i]
		list1[i] = list1[minpos]
		list1[minpos] = temp
		return list1
print(insertion_sort([1, 2, 3, 3, 6, 6, 7]))