def nth_fibonacci(n):
    #implementation here
    if n == 1 or n==2:
    	return 1
    return (nth_fibonacci(n-1)) + (nth_fibonacci(n-2))
