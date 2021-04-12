def isPalindrome(num):
	num=str(num)
	return num==num[::-1]

palinList=[]

for i in range(999,99,-1):
	for j in range(999,99,-1):
		sonuç=i*j
		if isPalindrome(sonuç):
			palinList.append(sonuç)
print(max(palinList))			
