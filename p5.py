import os
import time
board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player=1
##wins flags##
Win=1
Draw=-1
Running=0
Stop=1
#########
Game=Running
Mark='X'
##This Function Draws game Board
def DrawBoard():
    print("%c|%c|%c"%(board[1],board[2],board[3]))
    print("||_")
    print("%c|%c|%c"%(board[4],board[5],board[6]))
    print("||_")
    print("%c|%c|%c"%(board[7],board[8],board[9]))
    print(" | | ")
##This function checks position is empty or not
def CheckPosition(x):
    if(board[x]==' '):
        return True
    else:
        return False
##This function Checks player has won or not
def CheckWin():
    global Game
##Horizontal winning condition
    if(board[1]==board[2]and board[2]==board[3]and board[1]!=' '):
        Game=Win
    elif(board[4]==board[5]and board[5]==board[6]and board[4]!=' '):
        Game=Win
    elif(board[7]==board[8]and board[8]==board[9]and board[7]!=' '):
        Game=Win
##Vertical winning condition
    elif(board[1]==board[4]and board[4]==board[7]and board[1]!=' '):
        Game=Win
    elif(board[2]==board[5]and board[5]==board[8]and board[2]!=' '):
        Game=Win
    elif(board[3]==board[6]and board[6]==board[9]and board[3]!=' '):
        Game=Win
##Diagonal winning condition
    elif(board[1]==board[5]and board[5]==board[9]and board[5]!=' '):
        Game=Win
    elif(board[3]==board[5]and board[5]==board[7]and board[5]!=' '):
        Game=Win
##match Tie or draw condition
    elif(board[1]!=' 'and board[2]!=' 'and board[3]!=' 'and board[4]!=' 'and board[5]!=' 'and board[6]!=' 'and board[7]!=' 'and board[8]!=' 'and board[9]!=' '):
        Game=Draw
    else:
        Game=Running
print("Tic-Tac-Toe Game")
print("Player 1[X]---Player 2[0]\n")
print()
print()
print("Please wait....")
time.sleep(1)
while(Game==Running):
    os.system('cls')
    DrawBoard()
    if(player%2!=0):
        print("Player 1's chance")
        Mark='X'
    else:
        print("player 2's chance")
        Mark='0'
    choice=int(input("enter the position between 1-9 where you want to place"))
    if(CheckPosition(choice)):
               board[choice]=Mark
               player+=1
               CheckWin()
os.system('cls')
DrawBoard()
if(Game==Draw):
    print("Game Draw")
elif(Game==Win):
    player-=1
    if(player%2!=0):
        print("player 1 won")
    else:
        print("player 2 won")
