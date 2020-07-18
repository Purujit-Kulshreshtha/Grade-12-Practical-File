file = open("Test Subject.txt", "r")
file_data = file.readlines()
file.close()
print(max(file_data))