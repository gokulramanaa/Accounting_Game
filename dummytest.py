# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 12:14:26 2018

@author: gokul
"""
from tkinter import *
 
def rootfunct():
    root = Tk()
    Frame1 = Frame(root, width=900, height=600, colormap="new")
    Frame1.pack()
    Frame1.pack_propagate(0)
    return Frame1

def abcd():
    global year
    global activity
    global cost
    global demand
    global efficient 
    global effective 
    global score 
    global avgscore 
    global cumavgscore

    Frame1 = rootfunct()
    text = "\nDetermining Efficiency, Effectiveness, Score in this period, \nCumulative points, and Cumulative average at the end of Year {}\n\n".format(year)
    text1 = "   Efficiency in year {}: \n   Activities done/Cost of activities done = ${} / ${} = {}  \n".format(year, activity,cost,efficient)
    text2 = "Effectiveness in year {}: \nActivities done/ Activities Demanded = ${} / ${} = {}  \n".format(year, activity,demand,efficient)
    text3 = "Your Average score in year {} = {}                   \n".format(year, avgscore)
    text4 = "Actual demand for year {} = {}                       \n".format(year,demand)
    text5 = "Your Cumulative Average score in year {} = {}        ".format(year, cumavgscore)
    
#    TopFrame = Frame(Frame1, width=750, height=50)
#    TopFrame.pack(side = TOP)
#    TopFrame.pack_propagate(0)
    Label0 = Label(Frame1, text = text, font=("Courier", 18))
    Label0.pack(side = TOP)
    

    Label2 = Label(Frame1, text = text1, font=("Courier", 18), anchor=E,justify=LEFT)
    Label2.pack(side = TOP)
    

    Label1 = Label(Frame1, text = text2, font=("Courier", 18),anchor=E,justify=LEFT)
    Label1.pack(side = TOP)
    

    Label3 = Label(Frame1, text = text3, font=("Courier", 18),anchor=E,justify=LEFT)
    Label3.pack(side = TOP)

    Label4 = Label(Frame1, text = text4, font=("Courier", 18),anchor=E,justify=LEFT)
    Label4.pack(side = TOP)
    

    Label5 = Label(Frame1, text = text5, font=("Courier", 18), anchor=E,justify=LEFT)
    Label5.pack(side = TOP)
    
    button = Button(Frame1,text = "Continue",width=20, font=("Courier", 20), command =lambda:[Frame1.master.destroy(), game()])
    button.pack(side = BOTTOM)
    
    Frame1.mainloop()
    
year = 3
activity = 3
cost = 9
demand = 9
efficient  = 7
effective  = 8
score =8
avgscore =7
cumavgscore=3
abcd()
    
    