from tkinter import *
from tkinter import messagebox


turn = 1
possible_moves = [['', '', ''], # (0,0), (0,1), (0,2)
                  ['', '', ''], # (1,0), (1,1), (1,2)
                  ['', '', '']] # (2,0), (2,1), (2,2)
def move(row, column):
    global turn, possible_moves
    if turn == 1:
        buttons[row][column].config(text='X', bg='green',
                    state=DISABLED, disabledforeground="black")
        possible_moves[row][column] = 'X'
        turn = 0 
        if iswinner(row, column):
            disable_game()
            who_win.config(text="Player 1 win!", fg = 'green')
            return
        if istie():
            disable_game()
            who_win.config(text="It's a tie!", fg = 'blue')
    elif turn == 0:
        buttons[row][column].config(text='O', bg='tomato',
                   state=DISABLED, disabledforeground="black")
        possible_moves[row][column] = 'O'
        turn = 1
        if iswinner(row, column):
            disable_game()
            who_win.config(text="Player 2 win!", fg = 'tomato')
            return
        if istie():
            disable_game()
            who_win.config(text="It's a tie!", fg = 'blue')
            
def iswinner(row, column):
    if possible_moves[row][0] == possible_moves[row][1] == possible_moves[row][2] != '':
        return True
    if possible_moves[0][column] == possible_moves[1][column] == possible_moves[2][column] != '':
        return True
    if possible_moves[0][0] == possible_moves[1][1] == possible_moves[2][2] != '':
        return True
    if possible_moves[2][0] == possible_moves[1][1] == possible_moves[0][2] != '':
        return True

def istie():
    counter = 0
    for i in range(3):
        for j in range(3):
            if possible_moves[i][j] != '':
                counter += 1
    if counter == 9:
        return True

def disable_game():
    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] == "":
                buttons[i][j].config(state=DISABLED)


root = Tk()
root.resizable(False,False)
root.title("XOXO")
Label(root, text="Tic Tac Toe Game",
    font=("consolas",16,"bold")).pack(side=TOP)
who_win = Label(root, text='...', font=("consolas",18,"bold"), fg = 'grey', bd=10)
who_win.pack(side=TOP)
frame = Frame(root)
frame.pack(side=BOTTOM)

buttons = [[], [], []] # to have acces to the buttons
for i in range(3):
    for j in range(3):
        buttons[i].append(Button(frame, text="", font=('consolas',30), width=5, height=2,
                bd=2, activebackground='aliceblue', command= lambda row=i, column=j: move(row, column)))
        buttons[i][j].grid(row=i, column=j)
root.mainloop()