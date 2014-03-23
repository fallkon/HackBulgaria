def nth_fib_lists(listA, listB, n):
	if n == 1:
		return listA
	elif n == 2:
		return listB
	else :
		return nth_fib_lists(listB, listA + listB, n - 1)

def list_to_number(digits):
	count = 0
	for item in digits:
		count = count * 10 + item
	return count

def count_substrings(haystack, needle):
	return haystack.count(needle)#eta funkcia vozvra6iaet 4iso, skoliko ra vstre4aetsia substrin v stringe
    

def member_of_nth_fib_lists(listA, listB, needle):
	n = 1
	while n < 10:
		nth = nth_fib_lists(listA, listB, n)
		string = str(list_to_number(nth))
		if count_substrings(str(list_to_number(needle)), string):
			return True
		n += 1
	return False
