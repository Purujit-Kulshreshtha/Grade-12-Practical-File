import os

CURRENT_DIR = os.getcwd()

list_of_files = os.listdir()

ext = input("Enter file extension: ")
if "." not in ext:
	ext = "." + ext
to_change = False
file_number = 1

for i in list_of_files:

	if ext not in i or i == "File Renamer.py":
		continue

	os.rename(i, "Practical_File_Program" + str(file_number) + ext)
	file_number += 1



