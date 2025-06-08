# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 22:37:17 2018

@author: gokul
"""

from tkinter import *
import Labelclass as Lc

def ImgFunct(master):
    photo = PhotoImage(file="Images/inst.PNG")
    w = Label(master, image=photo)
    w.photo = photo
    w.pack()
    
Frame1 = Tk()
TopFrame = Frame(Frame1, width=900, height=600)
TopFrame.pack()
TopFrame.pack_propagate(0)
ImgFunct(TopFrame)
Lc.Buttonclass(Frame1,"Start")
Frame1.mainloop()