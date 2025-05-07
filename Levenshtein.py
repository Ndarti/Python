import numpy as np
def Lev(str1, str2):
    mas = np.zeros((len(str2) + 1, len(str1) + 1))
    for i in range(len(str2) + 1):
        mas[i][0] = i
    for j in range(len(str1) + 1):
        mas[0][j] = j
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str1[j - 1] == str2[i - 1]:
                mas[i][j] = mas[i - 1][j - 1]
            else:
                mas[i][j] = min(mas[i - 1][j] + 1,mas[i][j - 1] + 1,mas[i - 1][j - 1] + 1  )
    print(f" {mas[len(str2)][len(str1)]}")
string1 = "ккпяпя"
string2 = "рчяп"
Lev(string1, string2)