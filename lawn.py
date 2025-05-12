import numpy as np
def outputshooter(lawn,zombies,step):
    for i in range(len(lawn)-1):
        for j in range(len(lawn[0])-1):
            if lawn[i][j]!=' ':
                print(lawn[i][j], end=" ")
            else:
                print("0", end=" ")
        print()
        if i==step:
            lawn[i][0]=zombies[step][0][0]

    return lawn
def plantsAndZombies(lawn,zombies):
    step=0
    outputshooter(lawn,zombies,step)




lawn = [
    '2       ',
    '  S     ',
    '21  S   ',
    '13      ',
    '2 3     '
]
zombies = [[0,4,28],[1,1,6],[2,0,10],[2,4,15],[3,2,16],[3,3,13]]
plantsAndZombies(lawn,zombies)#10