from tkinter import*
from tkinter import messagebox #paziņojums
mansLogs=Tk() #loga objekts
mansLogs.title("TicTacToe")

def btnClick(button): #padod visu pogu
    global playerX, count #kādi mainīgie tiks izmantoti visā programmā
    if button["text"]==""and playerX==True: #spēlē X spēlētājs
        button["text"]=X #maina uz X
        playerX=False
        count+=1 #palielina rūtiņu skaitu

btn1=Button(mansLogs, text="", width=6, height=3, font=("Helvica"))
btn2=Button(mansLogs, text="", width=6, height=3, font=("Helvica"))
btn3=Button(mansLogs, text="", width=6, height=3, font=("Helvica"))
btn4=Button(mansLogs, text="", width=6, height=3, font=("Helvica"))
btn5=Button(mansLogs, text="", width=6, height=3, font=("Helvica"))
btn6=Button(mansLogs, text="", width=6, height=3, font=("Helvica"))
btn7=Button(mansLogs, text="", width=6, height=3, font=("Helvica"))
btn8=Button(mansLogs, text="", width=6, height=3, font=("Helvica"))
btn9=Button(mansLogs, text="", width=6, height=3, font=("Helvica"))

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