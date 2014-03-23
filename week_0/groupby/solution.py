def groupby(func, seq):
	res = {}
	for item in seq:
		if func(item) in res:
			res[func(item)].append(item) #if nujen potomu4to ne mogu appendvati k pustommu slovariu 
		else:
			res[func(item)] = [item]
	return res