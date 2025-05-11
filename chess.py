import re
import colorama
from colorama import *
colorama.init()

def output(board):
    i = 0
    for k, v in board.items():  ##повторить функции словарей и библ цветов
        print(f'{Fore.LIGHTBLACK_EX}{k}: {Fore.RESET}{v}', end=" ")
        # if check_p or check_P:
        #    print(check_p or check_P)
        i = i + 1
        if i == 8:
            i = 0
            print()

def chess(mas):
    board={"a8":".","b8":".","c8":".","d8":".","e8":".","f8":".","g8":".","h8":".",
    "a7":"ч","b7":"ч","c7":"ч","d7":"ч","e7":"ч","f7":"ч","g7":"ч","h7":"ч",
    "a6":".","b6":".","c6":".","d6":".","e6":".","f6":".","g6":".","h6":".",
    "a5":".","b5":".","c5":".","d5":".","e5":".","f5":".","g5":".","h5":"." ,
    "a4":".","b4":".","c4":".","d4":".","e4":".","f4":".","g4":".","h4":".",
    "a3":".","b3":".","c3":".","d3":".","e3":".","f3":".","g3":".","h3":".",
    "a2":"б","b2":"б","c2":"б","d2":"б","e2":"б","f2":"б","g2":"б","h2":"б",
    "a1":".","b1":".","c1":".","d1":".","e1":".","f1":".","g1":".","h1":".",
    }
    output(board)
    for i in range(len(mas)):
        view_1=re.findall("^[a-h][1-8]$",mas[i])#f4
        view_2=re.findall("^[a-h]x[a-h][1-8]$",mas[i])#dxc5
        if board.get(mas[i])==".":
            if i%2==0 and view_1  and (board.get((mas[i][0])+str(int(mas[i][1])-1))=="б"):
                board[((mas[i][0]) + str(int(mas[i][1]) - 1))]="."
                board[mas[i]]="б"
            if i%2==0 and view_1 and (board.get((mas[i][0])+str(int(mas[i][1])-2))=="б"):
                board[((mas[i][0]) + str(int(mas[i][1]) - 2))] = "."
                board[mas[i]] = "б"
            if i % 2 != 0 and view_1 and (board.get((mas[i][0]) + str(int(mas[i][1]) + 1)) == "ч"):
                board[((mas[i][0]) + str(int(mas[i][1]) + 1))] = "."
                board[mas[i]] = "ч"
            if i % 2 != 0 and view_1 and (board.get((mas[i][0]) + str(int(mas[i][1]) + 2)) == "ч"):
                board[((mas[i][0]) + str(int(mas[i][1]) + 2))] = "."
                board[mas[i]] = "ч"
        elif view_2:#dxc5
            if i % 2 == 0:
                key=re.findall("[a-h][1-9]",mas[i])#тут не полная рег ибо нет смысла делать полную рез не изм
                white=re.findall("^[a-h]",mas[i])
                num_1=re.findall("[1-9]",mas[i])
                if board[key[0]]=="ч" and board[white[0]+str(int(num_1[0])-1)]=="б":
                    board[white[0] + str(int(num_1[0]) - 1)] ="."
                    board[key[0]] = "б"
                    print("белые рулят")
            if i % 2!= 0:
                key = re.findall("[a-h][1-9]", mas[i])  # тут не полная рег ибо нет смысла делать полную рез не изм
                white = re.findall("^[a-h]", mas[i])
                num_1 = re.findall("[1-9]", mas[i])
                if board[key[0]] == "б" and board[white[0] + str(int(num_1[0]) + 1)] == "ч":
                    board[white[0] + str(int(num_1[0]) + 1)] = "."
                    board[key[0]] = "ч"
        else:
            print(f'{mas[i]} is invalid')
            exit(1)
    print()
    output(board)
#можно было делать и через массивы
chess(["b3","a5","b4","axb4"])