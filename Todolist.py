#CODSOFT
#Task 1 To do list.

from tkinter import *
root = Tk()
root.title("TO DO LIST")
root.geometry("600x400")
root.configure(bg="lightblue")

a=None
buttom1=None

headline=Label(text="WELCOME TO ABHISHEK TO DO LIST\n\n",font=("bold"),bg="lightblue")
headline.pack(side=TOP)

def destroy():
    if a is not None:
        a.destroy()
    if buttom1 is not None:
        buttom1.destroy()    

def ADD():
    with open("todo.txt","r") as f:
        while True:
            b=f.readline()
            if not b:
                break
            f3=Frame(root,bg="lightblue")
            f3.pack()
            checkbox=Checkbutton(f3,bg="lightblue")
            checkbox.pack(side=LEFT)
            l1=Label(f3,text=f"{b}",bg="lightblue")
            l1.pack(side=LEFT)
    A=a.get()
    f2=Frame(root,bg="lightblue")
    f2.pack()
    checkbox=Checkbutton(f2,bg="lightblue")
    checkbox.pack(side=LEFT)
    l1=Label(f2,text=f"{A}",bg="lightblue")
    l1.pack(side=LEFT,pady=5)  
    with open("todo.txt","a")as f:
        f.write(f"{A}\n")  
    a.delete(0,END)
    destroy()

def add():
    destroy()
    global a,buttom1
    a=Entry(root)
    a.pack(fill= X,padx=40,pady=10)
    buttom1=Button(root,text="Add",command=ADD)
    buttom1.pack()
   
buttom=Button(text="+ ADD TO DO list ",command=add)
buttom.pack(fill=X,padx=50)

root.mainloop()
