import os
import time

board = [' '] * 10  
player = 1

Win = 1
Draw = -1
Running = 0
Game = Running
Mark = 'X'

print("Ahmed Shaikh 323")

def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")

def CheckPosition(x):
    return board[x] == ' '

def CheckWin():
    global Game
    if (board[1] == board[2] == board[3] != ' ' or
        board[4] == board[5] == board[6] != ' ' or
        board[7] == board[8] == board[9] != ' '):
        Game = Win
    elif (board[1] == board[4] == board[7] != ' ' or
          board[2] == board[5] == board[8] != ' ' or
          board[3] == board[6] == board[9] != ' '):
        Game = Win
    elif (board[1] == board[5] == board[9] != ' ' or
          board[3] == board[5] == board[7] != ' '):
        Game = Win
    elif all(space != ' ' for space in board[1:]):
        Game = Draw
    else:
        Game = Running

print("Tic-Tac-Toe Game")
print("Player 1 [X] --- Player 2 [O]\n")
time.sleep(1)

while Game == Running:
    os.system('cls' if os.name == 'nt' else 'clear') 
    DrawBoard()
    
    if player % 2 != 0:
        print("Player 1's turn")
        Mark = 'X'
    else:
        print("Player 2's turn")
        Mark = 'O'

    try:
        choice = int(input("Enter the position between [1-9] where you want to mark: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 9.")
        continue

    if choice < 1 or choice > 9:
        print("Invalid input! Please enter a number between 1 and 9.")
        continue

    if CheckPosition(choice):
        board[choice] = Mark
        player += 1
        CheckWin()
    else:
        print("Position already occupied! Try again.")

os.system('cls' if os.name == 'nt' else 'clear')
DrawBoard()

if Game == Draw:
    print("It's a Draw!")
elif Game == Win:
    player -= 1
    if player % 2 == 0:
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")