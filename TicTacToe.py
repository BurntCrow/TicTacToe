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
        button["foreground"]='#FFFFFF'
        PlayerX=False
        count+=1 #palielina rūtiņu skaitu
        checkWinner()
    elif button["text"]=="" and PlayerX==False:
        button["text"]="O"
        button["foreground"]='#FFFFFF'
        PlayerX=True
        count+=1
        checkWinner()
    else:
        messagebox.showerror("TicTacToe","Šeit jau kāds ir uzlicis")


def checkWinner():
    global winner
    winner=False
    if (btn1["text"]=="X" and btn2["text"]=="X" and btn3["text"]=="X" or btn4["text"]=="X" and btn5["text"]=="X" and btn6["text"]=="X" or btn7["text"]=="X" and btn8["text"]=="X" and btn9["text"]=="X" or btn1["text"]=="X" and btn4["text"]=="X" and btn7["text"]=="X" or btn2["text"]=="X" and btn5["text"]=="X" and btn8["text"]=="X" or btn3["text"]=="X" and btn6["text"]=="X" and btn9["text"]=="X" or btn1["text"]=="X" and btn5["text"]=="X" and btn9["text"]=="X" or btn3["text"]=="X" and btn5["text"]=="X" and btn7["text"]=="X"):
        winner=True
        disableButtons()
        messagebox.showinfo("TicTacToe","Uzvarētājs ir X")
    elif (btn1["text"]=="O" and btn2["text"]=="O" and btn3["text"]=="O" or btn4["text"]=="O" and btn5["text"]=="O" and btn6["text"]=="O" or btn7["text"]=="O" and btn8["text"]=="O" and btn9["text"]=="O" or btn1["text"]=="O" and btn4["text"]=="O" and btn7["text"]=="O" or btn2["text"]=="O" and btn5["text"]=="O" and btn8["text"]=="O" or btn3["text"]=="O" and btn6["text"]=="O" and btn9["text"]=="O" or btn1["text"]=="O" and btn5["text"]=="O" and btn9["text"]=="O" or btn3["text"]=="O" and btn5["text"]=="O" and btn7["text"]=="O"):
        winner=True
        disableButtons()
        messagebox.showinfo("TicTacToe","Uzvarētājs ir O")
    elif count==9 and winner==False:
        disableButtons()
        messagebox.showinfo("TicTacToe","Neizšķirts")

def disableButtons():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)

def reset():
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    btn1["text"]=""
    btn2["text"]=""
    btn3["text"]=""
    btn4["text"]=""
    btn5["text"]=""
    btn6["text"]=""
    btn7["text"]=""
    btn8["text"]=""
    btn9["text"]=""
    global winner, count, PlayerX
    winner=False
    count=0
    PlayerX=True
    return 0


def infoLogs():
    newLogs=Toplevel()
    newLogs.title('info par programmu')
    newLogs.geometry("350x350")
    desc=Label(newLogs, text='Spēlētāji pēc kārtas liek savas zīmes tukšajos laukumos.')
    desc.grid(row=0, column=0)
    desc=Label(newLogs, text=" Uzvar tas spēlētājs, kurš pirmais iegūst 3 zīmes pēc kārtas")
    desc.grid(row=1, column=0)
    desc=Label(newLogs, text="(uz augšu, uz leju, šķērsām vai pa diagonāli).")
    desc.grid(row=2, column=0)
    desc=Label(newLogs, text="ja ir aizpildīti visi lauciņi, tad ir neizšķirts")
    desc.grid(row=3, column=0)
    return 0


#Lielā izvēlne
mainIzvelne=Menu(mansLogs)
mansLogs.config(menu=mainIzvelne)

#Mazā izvēlne
opcijas=Menu(mainIzvelne, tearoff=False)
mainIzvelne.add_cascade(label="Opcijas", menu=opcijas)

#Komandas
opcijas.add_command(label="Jauna Spēle", command=reset)
opcijas.add_command(label="Iziet", command=mansLogs.quit)
mainIzvelne.add_command(label="Par Programmu", command=infoLogs)


btn1=Button(mansLogs, text="", width=6, height=3, font=("Helvica", 15), bg='light green', command=lambda:btnClick(btn1))
btn2=Button(mansLogs, text="", width=6, height=3, font=("Helvica", 15), bg='green', command=lambda:btnClick(btn2))
btn3=Button(mansLogs, text="", width=6, height=3, font=("Helvica", 15), bg='light green', command=lambda:btnClick(btn3))
btn4=Button(mansLogs, text="", width=6, height=3, font=("Helvica", 15), bg='green', command=lambda:btnClick(btn4))
btn5=Button(mansLogs, text="", width=6, height=3, font=("Helvica", 15), bg='light green', command=lambda:btnClick(btn5))
btn6=Button(mansLogs, text="", width=6, height=3, font=("Helvica", 15), bg='green', command=lambda:btnClick(btn6))
btn7=Button(mansLogs, text="", width=6, height=3, font=("Helvica", 15), bg='light green', command=lambda:btnClick(btn7))
btn8=Button(mansLogs, text="", width=6, height=3, font=("Helvica", 15), bg='green', command=lambda:btnClick(btn8))
btn9=Button(mansLogs, text="", width=6, height=3, font=("Helvica", 15), bg='light green', command=lambda:btnClick(btn9))

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