def count_vowels(str):
	vowels = 'aeiouy'
	count = 0
	for item in str:
		if item in vowels:
			count += 1
	return count
