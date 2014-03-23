def calculate_coins(sum):
	sum *= 100
	coins = [100, 50, 20, 10, 5, 2, 1]
	res = {}
	for elem in coins:
		count = 0
		while sum - elem >= 0:
			count += 1
			sum -= elem 
		res[elem] = count
	return res
