def contains_digit(number, digit):
	strn = str(number)
	for elem in strn:
		if elem == str(digit):
			return True
	return False
