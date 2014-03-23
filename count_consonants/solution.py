def count_consonants(str):
	vowels = 'bcdfghjklmnpqrstvwxz'
	count = 0
	for item in str:
		if item.lower() in vowels:
			count += 1
	return count
