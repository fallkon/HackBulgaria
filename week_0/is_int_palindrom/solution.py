def is_int_palindrom(n):
	strn = str(n)
	for i in range(int(len(strn) / 2)):
		if strn[i] != strn[-(i+1)]:
			return False
	return True
