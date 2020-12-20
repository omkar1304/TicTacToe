from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk

root = Tk()
root.title("Tic Tac Toe")
root.iconbitmap(r'images/game.ico')

# frame desgin
top_frame = Frame(root, pady=2, bg='cadet blue', width=1350, height=100, relief=RIDGE)
top_frame.grid(row=0, column=0)

lbl_title = Label(top_frame, font='arial 50 bold', text="Tic Tac Toe Game",
                  bd=21, bg='cadet blue', fg='cornsilk', justify=CENTER)
lbl_title.grid(row=0, column=0)

main_frame = Frame(root, pady=2, bg='powder blue', width=1350, height=600, relief=RIDGE)
main_frame.grid(row=1, column=0)

left_frame = Frame(main_frame, bd=10, pady=2, padx=10, bg='cadet blue', width=750, height=500, relief=RIDGE)
left_frame.grid(row=0, column=0)

right_frame = Frame(main_frame, bd=10, pady=2, padx=10, bg='cadet blue', width=560, height=500, relief=RIDGE)
right_frame.grid(row=0, column=1)

right_frame1 = Frame(right_frame, bd=10, pady=2, padx=10, bg='cadet blue', width=560, height=200, relief=RIDGE)
right_frame1.grid(row=0, column=0)

right_frame2 = Frame(right_frame, bd=10, pady=2, padx=10, bg='cadet blue', width=560, height=200, relief=RIDGE)
right_frame2.grid(row=1, column=0)

# right frame desgoin
# fright frame 1 desgin
playerX = IntVar()
playerO = IntVar()
playerX.set(0)
playerO.set(0)

buttons = StringVar()
click = True


def checker(buttons):
    global click
    if buttons['text'] == "" and click == True:
        buttons['text'] = "X"
        click = False
        scorekeeper()
    elif buttons['text'] == "" and click == False:
        buttons['text'] = "O"
        click = True
        scorekeeper()


def scorekeeper():
    # for player X
    if b1['text'] == "X" and b2['text'] == "X" and b3['text'] == "X":
        b1.config(background="powder blue")
        b2.config(background="powder blue")
        b3.config(background="powder blue")

        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        messagebox.showinfo("WINNER X", "You Have Just Won Game")
        reset()

    if b4['text'] == "X" and b5['text'] == "X" and b6['text'] == "X":
        b4.config(background="powder blue")
        b5.config(background="powder blue")
        b6.config(background="powder blue")

        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        messagebox.showinfo("WINNER X", "You Have Just Won Game")
        reset()

    if b7['text'] == "X" and b8['text'] == "X" and b9['text'] == "X":
        b7.config(background="powder blue")
        b8.config(background="powder blue")
        b9.config(background="powder blue")

        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        messagebox.showinfo("WINNER X", "You Have Just Won Game")
        reset()

    if b1['text'] == "X" and b4['text'] == "X" and b7['text'] == "X":
        b1.config(background="powder blue")
        b4.config(background="powder blue")
        b7.config(background="powder blue")

        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        messagebox.showinfo("WINNER X", "You Have Just Won Game")
        reset()

    if b2['text'] == "X" and b5['text'] == "X" and b8['text'] == "X":
        b2.config(background="powder blue")
        b5.config(background="powder blue")
        b8.config(background="powder blue")

        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        messagebox.showinfo("WINNER X", "You Have Just Won Game")
        reset()

    if b3['text'] == "X" and b6['text'] == "X" and b9['text'] == "X":
        b3.config(background="powder blue")
        b6.config(background="powder blue")
        b9.config(background="powder blue")

        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        messagebox.showinfo("WINNER X", "You Have Just Won Game")
        reset()

    if b1['text'] == "X" and b5['text'] == "X" and b9['text'] == "X":
        b1.config(background="powder blue")
        b5.config(background="powder blue")
        b9.config(background="powder blue")

        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        messagebox.showinfo("WINNER X", "You Have Just Won Game")
        reset()

    if b3['text'] == "X" and b5['text'] == "X" and b7['text'] == "X":
        b3.config(background="powder blue")
        b5.config(background="powder blue")
        b7.config(background="powder blue")

        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        messagebox.showinfo("WINNER X", "You Have Just Won Game")
        reset()

    # for player O
    if b1['text'] == "O" and b2['text'] == "O" and b3['text'] == "O":
        b1.config(background="powder blue")
        b2.config(background="powder blue")
        b3.config(background="powder blue")

        n = float(playerO.get())
        score = n + 1
        playerO.set(score)
        messagebox.showinfo("WINNER O", "You Have Just Won Game")
        reset()

    if b4['text'] == "O" and b5['text'] == "O" and b6['text'] == "O":
        b4.config(background="powder blue")
        b5.config(background="powder blue")
        b6.config(background="powder blue")

        n = float(playerO.get())
        score = n + 1
        playerO.set(score)
        messagebox.showinfo("WINNER O", "You Have Just Won Game")
        reset()

    if b7['text'] == "O" and b8['text'] == "O" and b9['text'] == "O":
        b7.config(background="powder blue")
        b8.config(background="powder blue")
        b9.config(background="powder blue")

        n = float(playerO.get())
        score = n + 1
        playerO.set(score)
        messagebox.showinfo("WINNER O", "You Have Just Won Game")
        reset()

    if b1['text'] == "O" and b4['text'] == "O" and b7['text'] == "O":
        b1.config(background="powder blue")
        b4.config(background="powder blue")
        b7.config(background="powder blue")

        n = float(playerO.get())
        score = n + 1
        playerO.set(score)
        messagebox.showinfo("WINNER O", "You Have Just Won Game")
        reset()

    if b2['text'] == "O" and b5['text'] == "O" and b8['text'] == "O":
        b2.config(background="powder blue")
        b5.config(background="powder blue")
        b8.config(background="powder blue")

        n = float(playerO.get())
        score = n + 1
        playerO.set(score)
        messagebox.showinfo("WINNER O", "You Have Just Won Game")
        reset()

    if b3['text'] == "O" and b6['text'] == "O" and b9['text'] == "O":
        b3.config(background="powder blue")
        b6.config(background="powder blue")
        b9.config(background="powder blue")

        n = float(playerO.get())
        score = n + 1
        playerO.set(score)
        messagebox.showinfo("WINNER O", "You Have Just Won Game")
        reset()

    if b1['text'] == "O" and b5['text'] == "O" and b9['text'] == "O":
        b1.config(background="powder blue")
        b5.config(background="powder blue")
        b9.config(background="powder blue")

        n = float(playerO.get())
        score = n + 1
        playerO.set(score)
        messagebox.showinfo("WINNER O", "You Have Just Won Game")
        reset()

    if b3['text'] == "O" and b5['text'] == "O" and b7['text'] == "O":
        b3.config(background="powder blue")
        b5.config(background="powder blue")
        b7.config(background="powder blue")

        n = float(playerO.get())
        score = n + 1
        playerO.set(score)
        messagebox.showinfo("WINNER O", "You Have Just Won Game")
        reset()


def reset():
    b1['text'] = ""
    b2['text'] = ""
    b3['text'] = ""
    b4['text'] = ""
    b5['text'] = ""
    b6['text'] = ""
    b7['text'] = ""
    b8['text'] = ""
    b9['text'] = ""

    b1.config(background='gainsboro')
    b2.config(background='gainsboro')
    b3.config(background='gainsboro')
    b4.config(background='gainsboro')
    b5.config(background='gainsboro')
    b6.config(background='gainsboro')
    b7.config(background='gainsboro')
    b8.config(background='gainsboro')
    b9.config(background='gainsboro')


def new_game():
    reset()
    playerX.set(0)
    playerO.set(0)


lbl_playerx = Label(right_frame1, font='arial 40 bold', text="Player X: ", padx=2, pady=2, bg='cadet blue')
lbl_playerx.grid(row=0, column=0)
ent_playerx = Entry(right_frame1, font='arial 40 bold', bd=2, fg='black',
                    textvariable=playerX, width=14, justify=LEFT)
ent_playerx.grid(row=0, column=1)

lbl_playero = Label(right_frame1, font='arial 40 bold', text="Player O: ", padx=2, pady=2, bg='cadet blue')
lbl_playero.grid(row=1, column=0)
ent_player0 = Entry(right_frame1, font='arial 40 bold', bd=2, fg='black',
                    textvariable=playerO, width=14, justify=LEFT)
ent_player0.grid(row=1, column=1)

# right frame 2 desgin

btn_reset = Button(right_frame2, text="RESET", height=3, width=20, font='times 26 bold', bg='gainsboro', command=reset)
btn_reset.grid(row=2, column=0, padx=6, pady=11)
btn_new = Button(right_frame2, text="NEW GAME", height=3, width=20, font='times 26 bold', bg='gainsboro',
                 command=new_game)
btn_new.grid(row=3, column=0, padx=6, pady=10)

# left frame desgin
b1 = Button(left_frame, text="", height=3, width=8, font='times 26 bold', bg='gainsboro', command=lambda: checker(b1))
b1.grid(row=1, column=0, sticky=S + N + E + W)
b2 = Button(left_frame, text="", height=3, width=8, font='times 26 bold', bg='gainsboro', command=lambda: checker(b2))
b2.grid(row=1, column=1, sticky=S + N + E + W)
b3 = Button(left_frame, text="", height=3, width=8, font='times 26 bold', bg='gainsboro', command=lambda: checker(b3))
b3.grid(row=1, column=2, sticky=S + N + E + W)
b4 = Button(left_frame, text="", height=3, width=8, font='times 26 bold', bg='gainsboro', command=lambda: checker(b4))
b4.grid(row=2, column=0, sticky=S + N + E + W)
b5 = Button(left_frame, text="", height=3, width=8, font='times 26 bold', bg='gainsboro', command=lambda: checker(b5))
b5.grid(row=2, column=1, sticky=S + N + E + W)
b6 = Button(left_frame, text="", height=3, width=8, font='times 26 bold', bg='gainsboro', command=lambda: checker(b6))
b6.grid(row=2, column=2, sticky=S + N + E + W)
b7 = Button(left_frame, text="", height=3, width=8, font='times 26 bold', bg='gainsboro', command=lambda: checker(b7))
b7.grid(row=3, column=0, sticky=S + N + E + W)
b8 = Button(left_frame, text="", height=3, width=8, font='times 26 bold', bg='gainsboro', command=lambda: checker(b8))
b8.grid(row=3, column=1, sticky=S + N + E + W)
b9 = Button(left_frame, text="", height=3, width=8, font='times 26 bold', bg='gainsboro', command=lambda: checker(b9))
b9.grid(row=3, column=2, sticky=S + N + E + W)

root.geometry("1350x750+0+0")
root.config(bg="cadet blue")
root.mainloop()
