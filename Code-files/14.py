fh = open("Test subject.txt", "r")
lines = fh.read()
fh.close()
punctuations = [".", ",", "?", "!", ":"]
string_var = ""
for i in lines:
    if i in punctuations:
        pass
    else:
        string_var = string_var + i
print(string_var)
