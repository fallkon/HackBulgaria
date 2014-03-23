def list_to_number(digits):
	count = 0
	for item in digits:
		count = count * 10 + item
	return count
