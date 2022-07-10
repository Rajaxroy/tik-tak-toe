
from os import system, name
import time

map = [
    [" ", "|", " ", "|", " "],
    ["----------"],
    [" ", "|", " ", "|", " "],
    ["----------"],
    [" ", "|", " ", "|", " "],
]

#Row 1
cell1 = map[0][0]
cell2 = map[0][2]
cell3 = map[0][4]
#Row 2
cell4 = map[2][0]
cell5 = map[2][2]
cell6 = map[2][4]
#Row 3
cell7 = map[4][0]
cell8 = map[4][2]
cell9 = map[4][4]

all_cells = [cell1 , cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]

def clear():
    # for windows
    _ = system('cls') if name == 'nt' else system('clear')


def print_map(map_):
    str1 = ""
    for row in map_:
        for r in row:
            str1 += f"{r} "
        str1 += "\n"
    print(str1)


def marker(term):
    ply = 1 if term else 2
    pos = input(f"Player {ply} Enter Cell No. E.g 21 Is Column no 2 in row 1: ")
    row = int(pos[1])
    column = int(pos[0])
    if 1 <= row <= 3 and 1 <= column <= 3:
        if row == 1:
            row = 0
        elif row == 3:
            row = 4

        if column == 1:
            column = 0
        elif column == 3:
            column = 4
    else:
        print("Please Enter a Valid Row-Column Number As per Example.")
        time.sleep(2)
        return False

    if map[row][column] == " ":
        map[row][column] = "X" if ply == 1 else "O"
        return True

    else:
        print("Do Not Over Write.")
        time.sleep(2)
        return False


def check_winner(map_):

    draw = all(cell != " " for cell in all_cells)
    if draw:
        return "draw"

        # Rows
    if cell1 == cell2 == cell3 == "X" or cell1 == cell2 == cell3 == "O":
        return True
    elif cell4 == cell5 == cell6 == "X":
        return True
    elif cell7 == cell8 == cell9 == "X" or cell7 == cell8 == cell9 == "O":
        return True

    elif cell1 == cell4 == cell7 == "X" or cell1 == cell4 == cell7 == "O":
        return True
    elif cell2 == cell5 == cell8 == "X" or cell2 == cell5 == cell8 == "O":
        return True
    elif cell3 == cell6 == cell9 == "X" or cell3 == cell6 == cell9 == "O":
        return True

    elif cell1 == cell5 == cell9 == "X" or cell1 == cell5 == cell9 == "O":
        return True
    elif cell3 == cell5 == cell7 == "X" or cell3 == cell5 == cell7 == "O":
        return True

    else:
        return False


game_over = False
player1 = True
while not game_over:
    clear()
    print_map(map)
    winner = 1

    if winner_result := check_winner(map):
        if player1:
            winner = 2

        print(f"Player {winner} is Winner Game Over..")
        game_over = True

    elif winner_result == "draw":
        print("It's a Draw")
        game_over = True

    elif player1:
        if marker(player1):
            player1 = False
    elif marker(player1):
        player1 = True



