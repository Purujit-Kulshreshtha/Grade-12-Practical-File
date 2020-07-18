file_1 = open("Test Subject.txt", "r")
file_1_data = file_1.read()
file_1.close()

file_2 = open("New File.txt", "w")
file_2.write(file_1_data)
file_2.close()