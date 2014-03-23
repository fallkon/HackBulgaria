def prepare_meal(number):
	res = []
	count = 0
	while number % 3 == 0:
		count += 1
		number /= 3
	res = 'spam ' * count #nemnogo herovato 
	if number % 5 == 0:
		if count > 0:
			res += 'and eggs'
		else :
			res += 'eggs'
	return res
