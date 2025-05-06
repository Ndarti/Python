import math
from array import array
n=780
def pythagTrip(n): # prim way
    i =1
    while i<=100:
        j = 1
        while j<=100:
            sum=i**2+j**2
            if math.sqrt(sum)%1==0:
                sum=i*j*math.sqrt(sum)
            if n==sum:
                mas=array('i',[i,j,int(math.sqrt(i**2+j**2))])
                return mas
            j=j+1
        i=i+1

print(pythagTrip(n))
