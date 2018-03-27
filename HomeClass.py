# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 10:03:33 2018

@author: gokul
"""

from tkinter import *

class FrameClass():
    root = Tk()
    Frame1 = Frame(root, width=700, height=500, bg="grey", colormap="new")
    Frame1.pack()
    Frame1.pack_propagate(0)
    def __init__(self):
        TopFrame = Frame(self.Frame1, width=700, height=150)
        BottomFrame = Frame(self.Frame1, width=700, height=250)
        TopFrame.pack()
        TopFrame.pack_propagate(0)
        BottomFrame.pack()
        BottomFrame.pack_propagate(0)
        Label1 = Label(TopFrame, text = "Dr. Medinets \n Budgetry Strategy Game", 
                       font=("Courier", 20))
        Button1 = Button(BottomFrame, text="Instructions", command = self.instructions,
                         width=20, font=("Courier", 20))
        Button2 = Button(BottomFrame, text = "Start", width=20, font=("Courier", 20))
        Label1.pack(side=BOTTOM)
        Button1.pack(side = BOTTOM)
        Button2.pack(side = BOTTOM)
        
    def instructions(self):
        root = Tk()
        Frame2 = Frame(root, width=700, height=500, bg="grey", colormap="new")
        Frame2.pack()
        Frame2.pack_propagate(0)
        print("hello")
        photo = PhotoImage(file="C:/Users/gokul/Documents/Projects/AccountingGame/imgs/inst.png")
        print(type(photo))
        w = Label(Frame2, image=photo)
        w.photo = photo
        w.pack(side = TOP)
        self.mainloop()
        #NextB = Button(Frame1, text = "Next")
        #PreviousB = Button(Frame1, text = "Previous")
        
    def mainloop(self):
        self.root.mainloop()
        
#root = Tk()
obj = FrameClass()
obj.mainloop()