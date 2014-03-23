def contains_digits(number, digits):
	strn = str(number)
	
	for item in digits:
		if not(str(digits) in strn):
			return False
	return True
