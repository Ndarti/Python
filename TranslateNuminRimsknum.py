import random
from array import*
start=1
end=3999
number: int=random.randint(start,end)
print(number)
def Rimsk(number):
    i=0
    startcount=1
    sotki=0
    leng=len(str(number))
    mas= array('u',["I","I","I","V","V","V","X","X","X","L","L","L","C","C","C","D","D","D","M","M","M"])#i-int d-double
    masdidgital= array('i',[1,1,1,5,5,5,10,10,10,50,50,50,100,100,100,500,500,500,1000,1000,1000])#i-int d-double
    STR=""
    while i<leng:
        i=i+1
        strin=""
        index=0
        j=21
        decrementnum=0
        count=0
        numbers= number// startcount % 10
        if numbers!=0:
            sotki=numbers*startcount
            while(j!=0):
                j = j - 1
                if sotki>=masdidgital[j] and sotki>=count+masdidgital[j]:
                        count=count+masdidgital[j]
                        if(sotki//startcount%10==4):
                            STR=STR+''.join(reversed(str(mas[j])+mas[j+1]))
                            break
                        if (sotki // startcount % 10 == 9):
                            STR = STR + ''.join(reversed(str(mas[j-3])+str(mas[j+1])))
                            break
                        strin=str(mas[j])+strin
                        index=index+1
        STR=STR+''.join(strin) ####такие числа как 4 40 400 90 900 и т д всегда римская цифра стоит слева :) +можно сделать с помощю словоря присвоить 90 100 110 и т д
        startcount=startcount*10
    print(''.join(reversed(STR)))
Rimsk(number)