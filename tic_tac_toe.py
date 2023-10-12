import tkinter as tk
import tkinter.messagebox as mb

player = 'X'
AI = 'O'
stop = False

def click(r, c):
    global stop
    if states[r][c] == 0 and not stop:
        b[r][c].configure(text=player)
        states[r][c] = player
        if check_win_tie() is None:
            ai_move()
            check_win_tie()

def check_win_tie():
    global stop

    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:
            stop = True
            winner = states[i][0]
            if winner == AI:
                mb.showinfo("Winner", "AI won!")
            else:
                mb.showinfo("Winner", "You won!")
            reset_game()

        elif states[0][i] == states[1][i] == states[2][i] != 0:
            stop = True
            winner = states[0][i]
            if winner == AI:
                mb.showinfo("Winner", "AI won!")
            else:
                mb.showinfo("Winner", "You won!")
            reset_game()

    if states[0][0] == states[1][1] == states[2][2] != 0:
        stop = True
        winner = states[0][0]
        if winner == AI:
            mb.showinfo("Winner", "AI won!")
        else:
            mb.showinfo("Winner", "You won!")
        reset_game()

    elif states[0][2] == states[1][1] == states[2][0] != 0:
        stop = True
        winner = states[0][2]
        if winner == AI:
            mb.showinfo("Winner", "AI won!")
        else:
            mb.showinfo("Winner", "You won!")
        reset_game()

    elif all(states[i][j] != 0 for i in range(3) for j in range(3)):
        stop = True
        mb.showinfo("Tie", "It's a Tie!")
        reset_game()

    return None

def evaluate():
    for row in range(3):
        if states[row][0] == states[row][1] == states[row][2] != 0:
            if states[row][0] == AI:
                return 1
            elif states[row][0] == player:
                return -1

    for col in range(3):
        if states[0][col] == states[1][col] == states[2][col] != 0:
            if states[0][col] == AI:
                return 1
            elif states[0][col] == player:
                return -1

    if states[0][0] == states[1][1] == states[2][2] != 0:
        if states[0][0] == AI:
            return 1
        elif states[0][0] == player:
            return -1

    if states[0][2] == states[1][1] == states[2][0] != 0:
        if states[0][2] == AI:
            return 1
        elif states[0][2] == player:
            return -1
        
    if all(states[i][j] != 0 for i in range(3) for j in range(3)):
        return 0
    
    return None

def ai_move():
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if states[i][j] == 0:
                states[i][j] = AI
                score = minimax(0, False)
                states[i][j] = 0
                if score > best_score:
                    best_score = score
                    move = (i, j)
    r, c = move
    b[r][c].configure(text=AI)
    states[r][c] = AI

def minimax(depth, isMax):
    result = evaluate()
    if result is not None:
        return result
    
    if isMax:
        bestScore = -float('inf')
        for i in range(3):
            for j in range(3):
                if states[i][j] == 0:
                    states[i][j] = AI
                    score = minimax(depth+1, False)
                    states[i][j] = 0
                    bestScore = max(score, bestScore)
        return bestScore
    
    else:
        bestScore = float('inf')
        for i in range(3):
            for j in range(3):
                if states[i][j] == 0:
                    states[i][j] = player
                    score = minimax(depth+1, True)
                    states[i][j] = 0
                    bestScore = min(score, bestScore)
        return bestScore
    
def reset_game():
    global stop
    stop = False
    for i in range(3):
        for j in range(3):
            states[i][j] = 0
            b[i][j].configure(text="", state="normal")

b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Text for buttons
states = [[0, 0, 0], 
          [0, 0, 0], 
          [0, 0, 0]]

root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(0, 0)

for i in range(3):
    for j in range(3):
        b[i][j] = tk.Button(root, height=3, width=7, font=("Helvetica", "20"),
                         command=lambda r=i, c=j: click(r, c))
        b[i][j].grid(row=i, column=j)

root.mainloop()
