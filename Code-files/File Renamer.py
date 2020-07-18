import time
import os

CURRENT_DIR = os.getcwd()

list_of_files = os.listdir()
time.sleep(10)

ext = input("Enter file extension: ")
if "." not in ext:
	ext = "." + ext
title = input("Enter title to be added before number: ")

to_change = False
file_number = 1

for i in list_of_files:

	if ext not in i or i == "File Renamer.py":
		continue

	os.rename(i, title + str(file_number) + ext)
	file_number += 1




