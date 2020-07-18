file_name_1 = input("Enter name of file to be read: ")
file_name_2 = input("Enter name of file to write: ")
file1 = open(file_name_1 + ".txt", "r")
file1_data = file1.readlines()
file1.close()
to_be_written = []
for i in file1_data:
	if i[0].isupper():
		to_be_written.append(i)
file2 = open(file_name_2 + ".txt", "w")
file2.writelines(to_be_written)
file2.close()