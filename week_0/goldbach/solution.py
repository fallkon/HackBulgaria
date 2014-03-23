def is_prime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True


def goldbach(n):
    if n > 2 and n % 2 == 0:
        res = []
        for i in range(2, int(n / 2) + 1):
            if is_prime(i) and is_prime(n - i):
                res.append((i, n - i))
        return res
    else:
        return []