def capit(string_in):
	print("Input: " + string_in)
	list_string = string_in.split(" ")
	final_string = ""
	new_list = []
	for i in list_string:
		j = i.capitalize() + " "
		new_list.append(j)
	for i in new_list:
		final_string = final_string + i
	return final_string
print(capit("driver program to capitalize each word"))