file = open("Article.txt", "r")
file_data = file.read()
file.close()
words = file_data.split(" ")
count_to = 0
count_the = 0
for i in words:
	if i == "to":
		count_to += 1
	elif i == "the":
		count_the += 1
print(f'Number of "The"s: {count_the} \n Number of "To"s: {count_to}')
