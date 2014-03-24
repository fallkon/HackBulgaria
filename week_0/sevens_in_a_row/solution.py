def sevens_in_a_row(arr, n):
	count = 0 
	for item in arr:
		if item > 0 and item == 7:
			count += 1
	if n <= count:
		return True
	return False
