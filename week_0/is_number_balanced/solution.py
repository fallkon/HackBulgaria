def is_number_balanced(n):
	strn = str(n)
	sum1 = 0
	sum2 = 0
	for i in range(0, int(len(strn) / 2)):
		sum1 += int(strn[i])
		sum2 += int(strn[-(i + 1)])
	if sum1 == sum2:
		return True
	return False
