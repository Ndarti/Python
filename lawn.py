import re
import numpy as np
import math
from colorama import Fore

def killdiog(mas,ind1,ind2):
    kill=0
    for i in range(ind1,-1,-1):
        for j in range(ind2,-1,-1):
            if round(mas[i][j]%1,3)==0.335:
                continue
            x=ind2-ind1
            if j-i==x and mas[i][j]==10:
                kill+=1
    for i in range(len(mas)):
        if ind1+i<=len(mas)-1 and ind2-i>=0 and round(mas[ind1+i][ind2-i] % 1, 3) == 0.335:
            continue
        if ind1+i<=len(mas)-1 and ind2-i>=0 and mas[ind1+i][ind2-i]==10:
            kill+=1
    return kill
def outputshooterandzomb(lawn,zombies,step):
    mas = np.zeros((len(lawn), len(lawn[0])), dtype=np.float64)#повторить типы
    for i in range(len(zombies)):
        for j in range(len(mas)):
            if step == zombies[i][0] and zombies[i][1]==j:
                mas[j][7] = zombies[i][2]+0.335
    for i in range(len(mas)):
        for j in range(len(mas[0])):
            if lawn[i][j] == 'S':
                mas[i][j] =10
            if lawn[i][j]!=' ' and lawn[i][j]!='10' and mas[i][j]==0:
                mas[i][j]=float(lawn[i][j])
            if(round(mas[i][j]%1,3)!=0.335):
                print(Fore.LIGHTBLACK_EX, round(mas[i][j]), end=' ')
            else:
                print(Fore.RED,round(mas[i][j]),end=' ')
        print()
    print()
    return mas
def stept(mas,xod):
    for i in range(len(mas)):
        kill=0
        ind=0
        for j in range(len(mas[0])):
            if round(mas[i][j]%1,3)==0.335:
                if j-1<0:
                    x=xod
                    return x
                    exit(1)
                if ind==0:
                    mas[i][j - 1] = mas[i][j] - kill-killdiog(mas,i,j)
                    mas[i][j] = 0
                    ind+=1
                else:
                    mas[i][j - 1] = mas[i][j]-killdiog(mas,i,j)
                    mas[i][j] = 0
                if round(mas[i][j - 1]) <= 0:
                    mas[i][j-1] = 0
            if mas[i][j]!=0 and round(mas[i][j]%1,3)!=0.335:
                if mas[i][j]==10:
                    kill=kill+1
                else:
                    kill = kill + mas[i][j]
    return mas
def plantsAndZombies(lawn,zombies):
    step=0
    for i in range(200):
        a=outputshooterandzomb(lawn, zombies, i)
        b=stept(a,i)
        if type(b)==int:
            return b+1
        else:
            lawn=b
    return None
lawn = [
    '2       ',
    '  S     ',
    '21  S   ',
    '13      ',
    '2 3     '
]
zombies = [[0,4,28],[1,1,6],[2,0,10],[2,4,15],[3,2,16],[3,3,13]]
print(plantsAndZombies(lawn,zombies))#10