NUMBER=167756

def primesUntil(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]	

factors=[prime for prime in primesUntil(NUMBER) if not NUMBER%prime]	

print("prime factors of {} are: {}".format(NUMBER,factors))
