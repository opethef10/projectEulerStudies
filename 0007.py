number=1000000

def primesUntil(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]	

liste=primesUntil(int(number))	
print(liste[10000])
kalan=[]
for prime in liste[3:100]:
	kalan.append(prime%6)
