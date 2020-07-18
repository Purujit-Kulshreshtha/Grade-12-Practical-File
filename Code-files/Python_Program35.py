princ = int(input("Enter the base term: "))
ratio = float(input("Enter the ratio: "))
ran = int(input("Enter range: "))

sum_of_series = 0

for i in range(0, ran):
	if i == 0:
		sum_of_series += princ
	else:
		sum_of_series += princ * (ratio*i)

print(sum_of_series)