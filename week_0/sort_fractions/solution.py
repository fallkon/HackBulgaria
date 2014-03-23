def comparation(f1, f2):
	f1 = f1[0] / f1[1]
	f2 = f2[0] / f2[1]
	if f1 < f2:
		return -1
	elif f1 == f2:
		return 0
	else :
		return 1


def sort_fractions(fractions):
	for i in range(int(len(fractions))):
		min_f = i
		for j in range(i, int(len(fractions))):
			if comparation(fractions[j], fractions[min_f]) == -1:
				min_f = j
		if i != min_f:
			tmp = fractions[i]
			fractions[i] = fractions[min_f]
			fractions[min_f] = tmp
	return fractions 
