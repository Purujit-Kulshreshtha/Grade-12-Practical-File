file = open("Poem.txt", "r")
file_data = file.read()
file.close()
print(file_data)
count = 0
for i in file_data:
	if i.isupper():
		count += 1
print(count)