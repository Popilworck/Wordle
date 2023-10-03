from tkinter import *
from tkinter import messagebox
import wordlemodule as w
from random import randrange as r
with open("WordList.txt","r") as f:
	a = f.read().splitlines()
b=r(0,len(a))
strword = a[b]
print(strword)
window = Tk()
def x(a):messagebox.showerror("ERROR", a)
window.geometry('660x750')
canvas = Canvas(window,bg = "#121213",height = 888,width = 1536,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x=0,y=0)
chances=0

def submit():
    global chances
    chances+=1
    chosen = choicevar.get().lower()
    
    if chances<6:
        a = w.main(strword,chosen)
        choicevar.set('')
        def place(k):
            for i in range(1,6):
                h = f'{k}{i*100}'
                #print(h)
                exec(f'{h}.configure(text="{chosen[i-1].upper()}")')
                colour = "green" if a[i-1]==1 else "red" if a[i-1]==2 else "grey"
                #print(colour)
                exec(f'{h}.configure(bg="{colour}")')

        if type(a) != list:
            chances-=1
            if a == 0:
                x(f"WRONG NUMBER OF CHARACTERS. SHOULD BE EXACTLY 5. YOU ENTERED, {len(chosen)}")
            elif a==1:
                x("WORD NOT IN DICTIONARY")
            elif a==2:
                messagebox.showinfo("Congrats",'You Have correctly guessed the word. Congratulations')
                window.destroy()
        else:
            if chances ==1:
                 place('box_100')
            elif chances==2:place('box_175')
            elif chances==3:place('box_250')
            elif chances==4:place('box_325')
            elif chances ==5:place('box_400')
    else:
        messagebox.showinfo("Try Again Next Time",f'You Couldnt correctly guess the word. It was, {strword}')
        window.destroy()
Label(window,text="WORDLE",font=("Inter ExtraBold", 40 * -1,'bold'),bg='#121213',fg='#FFFFFF').place(x=230,y=0)
for  j in range(100,500,75):
    for i in range(100,600,100):
        a=f'box_{j}{i}'
        exec(f'{a} = Button(window,font=("Inter ExtraBold", 20 * -1,"bold"))')
        exec(f'{a}.place(x=i,y=j,width=50,height=50)')
Label(window,text="Enter Guess",font=("Inter ExtraBold", 40 * -1,'bold'),bg='#121213',fg='#FFFFFF').place(x=200,y=550)
choicevar = StringVar()
entry1 = Entry(window,textvariable=choicevar,width=22,font=("Inter ExtraBold", 20 * -1,'bold')).place(x=200,y=600)
sub_but = Button(window,command=submit,text='Submit',font=("Inter ExtraBold", 20 * -1,'bold'))
sub_but.place(x=500-20,y=595,width=75,height=35)
Button(window,command=window.destroy,text='Close',font=("Inter ExtraBold", 20 * -1,'bold')).place(x=580,y=700,width=75,height=35)
window.mainloop()