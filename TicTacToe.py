from tkinter import*
from tkinter import messagebox #paziņojums
mansLogs=Tk() #loga objekts
mansLogs.title("TicTacToe")


PlayerX=True
count=0

def btnClick(button): #padod visu pogu
    global PlayerX, count #kādi mainīgie tiks izmantoti visā programmā
    if button["text"]==""and PlayerX==True: #spēlē X spēlētājs
        button["text"]="X" #maina uz X
        PlayerX=False
        count+=1 #palielina rūtiņu skaitu
        checkWinner()
    elif button["text"]=="" and PlayerX==False:
        button["text"]="O"
        PlayerX=True
        count+=1
        checkWinner()
    else:
        messagebox.showerror("TicTacToe","Šeit jau kāds ir uzlicis")


def checkWinner():
    global checkWinner
    winner=False
    if (btn1["text"=="X"] and btn2["text"]=="X" and btn3["text"]=="X" or btn4["text"=="X"] and btn5["text"]=="X" and btn6["text"]=="X" or btn7["text"=="X"] and btn8["text"]=="X" and btn9["text"]=="X" or btn1["text"=="X"] and btn4["text"]=="X" and btn7["text"]=="X" or btn2["text"=="X"] and btn5["text"]=="X" and btn8["text"]=="X" or btn3["text"=="X"] and btn6["text"]=="X" and btn9["text"]=="X" or btn1["text"=="X"] and btn5["text"]=="X" and btn9["text"]=="X" or btn3["text"=="X"] and btn5["text"]=="X" and btn7["text"]=="X"):
        winner=True
        messagebox.showinfo("Uzvarētājs ir X")
    elif (btn1["text"=="O"] and btn2["text"]=="O" and btn3["text"]=="O" or btn4["text"=="O"] and btn5["text"]=="O" and btn6["text"]=="O" or btn7["text"=="O"] and btn8["text"]=="O" and btn9["text"]=="O" or btn1["text"=="O"] and btn4["text"]=="O" and btn7["text"]=="O" or btn2["text"=="O"] and btn5["text"]=="O" and btn8["text"]=="O" or btn3["text"=="O"] and btn6["text"]=="O" and btn9["text"]=="O" or btn1["text"=="O"] and btn5["text"]=="O" and btn9["text"]=="O" or btn3["text"=="O"] and btn5["text"]=="O" and btn7["text"]=="O"):
        winner=True
        messagebox.showinfo("Uzvarētājs ir O")
    elif count==9 and winner==False:
        messagebox.showinfo("Neizšķirts")


btn1=Button(mansLogs, text="", width=6, height=3, font=("Helvica"), command=lambda:btnClick(btn1))
btn2=Button(mansLogs, text="", width=6, height=3, font=("Helvica"), command=lambda:btnClick(btn2))
btn3=Button(mansLogs, text="", width=6, height=3, font=("Helvica"), command=lambda:btnClick(btn3))
btn4=Button(mansLogs, text="", width=6, height=3, font=("Helvica"), command=lambda:btnClick(btn4))
btn5=Button(mansLogs, text="", width=6, height=3, font=("Helvica"), command=lambda:btnClick(btn5))
btn6=Button(mansLogs, text="", width=6, height=3, font=("Helvica"), command=lambda:btnClick(btn6))
btn7=Button(mansLogs, text="", width=6, height=3, font=("Helvica"), command=lambda:btnClick(btn7))
btn8=Button(mansLogs, text="", width=6, height=3, font=("Helvica"), command=lambda:btnClick(btn8))
btn9=Button(mansLogs, text="", width=6, height=3, font=("Helvica"), command=lambda:btnClick(btn9))

btn1.grid(column=1, row=1)
btn2.grid(column=1, row=2)
btn3.grid(column=1, row=3)
btn4.grid(column=2, row=1)
btn5.grid(column=2, row=2)
btn6.grid(column=2, row=3)
btn7.grid(column=3, row=1)
btn8.grid(column=3, row=2)
btn9.grid(column=3, row=3)


mansLogs.mainloop()