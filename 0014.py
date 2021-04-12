uzunluk=[]
def collatz(n):
	chain=[]
	while n!=1:
		chain.append(n)
		if n%2:
			n=3*n+1
		else:
			n=n//2
	chain.append(1)
	return chain

for i in range(1,10000):
	uzunluk.append(len(collatz(i)))
print(uzunluk.index(max(uzunluk))+1)
