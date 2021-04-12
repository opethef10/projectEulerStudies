ayınGünleri=[31,28,31,30,31,30,31,31,30,31,30,31]
yıllık={}
yıllık[1900]=[6]

for year in range(1901,2001):
	if year%4:
		isleap=0
	else:
		isleap=1
	thisyear=[(yıllık[year-1][-1]+31)%7]
	for month in range(1,2):
		thisyear.append((thisyear[-1]+ayınGünleri[month-1])%7)
		
	month+=1
	thisyear.append((thisyear[-1]+ayınGünleri[month-1]+isleap)%7)
	for month in range(3,12):
		thisyear.append((thisyear[-1]+ayınGünleri[month-1])%7)
	yıllık[year]=thisyear
del yıllık[1900]

countSun=0
for year in yıllık:
	for month in yıllık[year]:
		if month==0:
			countSun+=1
print(countSun)
