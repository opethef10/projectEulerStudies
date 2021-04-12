fib=[1,2]
while fib[-1] < 4000000:
	fib.append(fib[-2]+fib[-1])
print(sum(x for x in fib[:-1] if x%2==0))
