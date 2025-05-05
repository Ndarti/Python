n=1000
def namber(n):
	starttag=9
	lenght=int(len(str(n))) # количество знаков или через цикл
	i=0
	sum=0
	while(i!=lenght):
		i=i+1
		if(n-starttag)>0:n=n-starttag #определяем сколько раз диапазон вычесть >0
		else: sum=sum+n*i;print(sum); break
		starttag=starttag*i#диапазон 9  90*2   900*3 итд
		sum=starttag+sum
		starttag=starttag*10# диапазон  9*10  90*10 etc
namber(n)
