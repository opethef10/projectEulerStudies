from math import log
NUMBER=20
liste=list(range(2,NUMBER))

def primesUntil(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]	

primeList=primesUntil(NUMBER)	
asal=[]
oldu=False

for prime in primeList:
	start=int(log(liste[-1],prime))
	while start>1:
		for i in liste[::-1]:
			if i%prime**start==0:
				oldu=True
				break
		if oldu:
			break		
		start=start-1
	asal.append(prime**start)	

result=1
for i in asal:
	result=result*i
print(result)
