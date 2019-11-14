def start2():
	a={1, "a", "ee", "ww", "c", "d"}	
	b={4, "a", "b", "ee", 1, 3}
	f=(a.symmetric_difference(b)).union(a.difference(b))
	print(f)
