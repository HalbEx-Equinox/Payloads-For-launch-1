from Tkinter import *
import random
import time
root = Tk()
root.geometry("610x610")
root.configure(background="white")
rightist=Frame(root,bg="white")
rightist.pack()
wo=0
ti=0
while (wo < 1):
    for i in range(1, 11):
        lab1 = Label(rightist, text='|', fg='red', bg="white", font="times 23")
        lab1.grid(row=i, column=0)
        lab2 = Label(rightist, text='__', fg='red', bg="white", font="times 23")
        lab2.grid(row=10, column=i)
    for y in range (1,11):
        ti=ti+.5
        joker=random.randint(1,1000)
        rw = 10-joker/100
        lab = Label(rightist, text= str(joker)+"\n"+"__"+"\n"+str(ti), fg='white', bg="maroon", font="times 8")
        lab.grid(row=rw, column=y)
        time.sleep(0.5)
        root.update()
    rightist.destroy()
    rightist = Frame(root, bg="white")
    rightist.pack()
root.mainloop()

