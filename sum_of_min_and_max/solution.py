def sum_of_min_and_max(arr):
	arr.sort()
	return arr[0] + arr[len(arr) - 1]
