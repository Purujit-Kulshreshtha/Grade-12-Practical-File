def check_length(string1, string2):
	if len(string1) == len(string2):
		return "The strings are of the same length."
	else:
		return "The strings are NOT of the same length."
print(check_length("Test", "Code"))
print(check_length("Program", "Test"))