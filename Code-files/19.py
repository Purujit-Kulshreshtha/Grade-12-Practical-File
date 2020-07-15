file_1 = open("Test Subject.txt", "r")
file_data = file_1.readlines()
file_1.close()
for i in file_data:
	if "a" in i:
		file_data.remove(i)
file_2 = open("New File.txt", "w")
file_2.writelines(file_data)
file_2.close()