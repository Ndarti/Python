def Week(mas,k):
    minimum=100000
    day1=0
    day2=0
    ii=0
    jj=0
    result=0
    for i in range(0,len(mas)):
        if i+k+1<len(mas):
            summ=mas[i]+mas[i+k+1]
            if summ<minimum:
                minimum=summ
                day1=mas[i]
                day2=mas[i+k+1]
                ii=i
                jj=i+k+1
    for i in range(0,len(mas)):
        if i!=ii and i!=jj:
            result=result+mas[i]
    print(str(result)+" Отказаться от заработка "+str(day1)+" и "+str(day2))
    return minimum

k=3
mas=[60, 70, 80, 40, 80, 90, 100, 20]
print(Week(mas,k))