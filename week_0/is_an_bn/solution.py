def is_an_bn(word):
	flg1 = True
	flg2 = True
	n = 0
	if len(word) % 2 == 0:
		n = int(len(word) / 2)
	for i in range(n):
		if word[i] !='a':
			flg1 = False
			break

	for l in range (n+1, int(len(word))):
		if word[l] != 'b':
			flg2 == False
			break
	if flg1 and flg2 == True:
		return True
	return False
