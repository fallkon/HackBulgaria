def is_prime(n):
	if n == 1:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True


def prime_number_of_divisors(n):
	numb_divisors = 0
	for i in range(1, n + 1):
		if n % i == 0 :
			numb_divisors +=1
	return is_prime(numb_divisors)
