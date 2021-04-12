cache={}
def routes(m,n):
	if n == 0 or m == 0:
		return 1
	elif (m,n) in cache:
		return cache[(m,n)]
	cache[(m,n)] = routes(m, n - 1) + routes(m - 1, n)
	return cache[(m,n)]
print(routes(400,400))
