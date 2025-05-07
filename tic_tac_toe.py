def tic(mas,play1):
    string=0
    colum=0
    diagonal_1=0
    diagonal_2=0
    result=0
    for i in range(0,3):
        for j in range(0,3):
            print(mas[i][j],end="  ")
            if mas[i][j]==play1:
                string= string + 1
            if mas[j][i] == play1:
                colum = colum + 1
            if mas[i][j]==0:
                result="-1"
        for j in range(2,-1,-1):
            if i==j and mas[i][2-i]==play1:
                diagonal_2=diagonal_2+1
        if mas[i][i] == play1:
            diagonal_1 = diagonal_1 + 1
        if string>=3:
            string=3
        else:string=0
        if colum>=3:
            colum=3
        else:colum=0
        print()
    if diagonal_2==3 or diagonal_1==3 or string==3 or colum==3 :
        if play1==1:print("X", end="")
        else:print("О(2)", end="")
    elif play1<2:
        play1=play1+1
        print("+++++++++++++++++++++++++++")
        tic(mas,play1)
    else:
        print(result)
mas=[[2,2,1],
     [1,1,2],
     [2,1,2]]
player=1
tic(mas,player)