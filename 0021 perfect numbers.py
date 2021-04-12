sözlük={}
LIMIT=10000
def sumOfDiv(sayı):
	divisors=[1]
	for i in range(2,int(sayı**0.5)+1):
		if sayı%i==0:
			divisors.append(i)
			divisors.append(sayı//i)
	return(sum(divisors))

for sayı in range(1,LIMIT):
	sözlük[sayı]=sumOfDiv(sayı)

amicable=list(filter(lambda i:sözlük.get(i)!=i and sözlük.get(sözlük[i])==i,sözlük))
print(sum(amicable))

perfect=list(filter(lambda i:sözlük.get(i)==i,sözlük))
#print(perfect)
