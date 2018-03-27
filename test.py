# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 18:22:13 2018

@author: gokul
"""
from tkinter import *
 
def rootfunct():
    root = Tk()
    Frame1 = Frame(root, width=900, height=600, colormap="new")
    Frame1.pack()
    Frame1.pack_propagate(0)
    return Frame1

def stockpile(pile):
    print(pile)

def test(year=1, budget=100, resource=90, demand=10, activity = 78, stockpile = 0):
    Frame1 = rootfunct()
    text = "Year {}             Budget for year {}    $100".format(year,year)
    text1 = "Current stock pile for year {} = $0 ".format(year)
    text2 = "The amount of resources available for year {} = ($100 + $0) = $100".format(year)
    text3 = "Demand for year {} has an equal chance of being $110, $100, $90".format(year)
    text4 = "Actual demand for year {} is = {}".format(year,demand)
    #text5 = "{} of resources are available, and {} of activites are demanded.".format(resource,demand)
    #text6 = "So all activities can be done without using any stockpiled resources"
    text7 = "So only {} of activities can be done, and all the stockpiled resources must be used".format(budget)
    text8 = "Activities done in year {}".format(year)
    
    TopFrame = Frame(Frame1, width=750, height=50)
    TopFrame.pack(side = TOP)
    TopFrame.pack_propagate(0)
    #Labelclass(TopFrame, text)
    Label0 = Label(TopFrame, text = text, font=("Courier", 20))
    Label0.pack(side = BOTTOM)
    
    
    TopFrame1 = Frame(Frame1, width = 600, height = 30)
    TopFrame1.pack(side=TOP)
    TopFrame1.pack_propagate(0)
    Label2 = Label(TopFrame1, text = text1, font=("Courier", 15))
    Label2.pack(side = BOTTOM)
    #Labelclass(TopFrame1, text1)
    
    TopFrame2 = Frame(Frame1, width = 750, height = 50)
    TopFrame2.pack(side=TOP)
    #TopFrame2.pack_propagate(0)
    #Labelclass(TopFrame1, text1)
    Label1 = Label(TopFrame2, text = text2, font=("Courier", 15))
    Label1.pack(side = BOTTOM)
    #Labelclass(TopFrame2, text2)
    
    TopFrame3 = Frame(Frame1, width = 750, height = 50)
    TopFrame3.pack(side=TOP)
    #TopFrame2.pack_propagate(0)
    #Labelclass(TopFrame1, text1)
    Label3 = Label(TopFrame3, text = text3, font=("Courier", 15), anchor=W, justify=LEFT)
    Label3.pack(side = BOTTOM)
    
    TopFrame4 = Frame(Frame1, width = 750, height = 50)
    TopFrame4.pack(side=TOP)
    Label4 = Label(TopFrame4, text = text4, font=("Courier", 15), anchor=W, justify=LEFT)
    Label4.pack(side = BOTTOM)
    
    if budget==demand:
            text6 = "\n {resource} of resources are available, and {demand} of activites are demanded.\n So all activities can be done without using any stockpiled resources \n Activities done in year {year} = {activity} \n\n Since the {budget} budgeted equaled the {demand} deamanded. No resources were added \n to or taken from stockpile. \n\n The amount of stockpile at the end of the year {year} is ${stockpile}, and the cost \n for the {activity} activities done during the year is {budget} from the University's \n point of view ".format(year=year,activity=activity, resource = resource, budget=budget, demand=demand,stockpile=stockpile)
            TopFrame6 = Frame(Frame1, width = 750, height = 50)
            TopFrame6.pack(side=TOP)
            Label6 = Label(TopFrame6, text = text6, font=("Courier", 15), anchor=W, justify=LEFT, bg="WHITE")
            Label6.pack(side = BOTTOM)
            button2 = Button(Frame1,text = "Next",width=20, font=("Courier", 20),command =lambda:[Frame1.master.destroy(), game()])
            button2.pack()
    elif budget > demand:
        #radiot button 
        temp = budget - demand
        text6 = "\n {resource} of resources are available, and {demand} of activites are demanded.\n So all activities can be done without using any stockpiled resources \n Activities done in year {year} = {activity} \n\n Since the {budget} budgeted greater than {demand} deamanded. There is a surplus \n of {surp} \n\n Do you want to stockpile the surplus for future use or allow it to \n revert to the university? ".format(year=year,activity=activity, resource = resource, budget=budget, demand=demand,stockpile=stockpile,surp=temp)
        TopFrame6 = Frame(Frame1, width = 750, height = 50)
        Label6 = Label(TopFrame6, text = text6, font=("Courier", 15), anchor=W, justify=LEFT, bg="WHITE")
        Label6.pack(side = BOTTOM)
        TopFrame6.pack(side=TOP)
        TopFrame7 = Frame(Frame1, width = 750, height = 50)
        TopFrame7.pack(side=TOP)
        

        Label7 = Label(TopFrame7)
        def sel(Label7 = Label7):
            selection = "You selected the option " + str(var.get())
            sval = var.get()
            print(sval)
            stockpile(sval)
            
#            text = StringVar()
#            TopFrame8 = Frame(Frame1, width = 750, height = 50)
#            TopFrame8.pack(side=TOP)
#            if (var.get() == 1):
#                text7 = "\n You have chosen to stockpile the surplus, so your stockpile is now {stockpile} and \n the cost for {activity} activities done during the year is {resource} from the university point of view".format(stockpile = stockpile, resource = resource, activity = activity)
#                Label7 = Label(TopFrame8, text = text7, font=("Courier", 15), bg="WHITE", textvariable = text)
#                Label7.pack(side = BOTTOM)
#            else:
#                text8 = "\n You have chosen to allow the surplus to revert to university, so your stockpile \n is $0 and the cost for {activity} activities done during the year is {resource} from the university point of view".format(stockpile = stockpile, resource = resource, activity = activity)
#                text.set(text8)
        var = IntVar()
        Radiobutton(TopFrame7, text="Stockpile", variable=var, value=1, command=sel).pack(anchor=W)
        Radiobutton(TopFrame7, text="Revert", variable=var, value=2, command=sel).pack(anchor=W)
        button2 = Button(Frame1,text = "Next",width=20, font=("Courier", 20),command =lambda:[Frame1.master.destroy(), game()])
        button2.pack()
        
    else:
        text6 = "\n {resource} of resources are available, but {demand} of activites are demanded.\n So only {activity} activities can be done, and all stockpiled resources \n must be used. Activities done in year {year} = {activity} \n\n Since the {budget} budgeted was less than the {demand} deamanded. all {stockpile} resources \n were used. \n\n The amount of stockpile at the end of the year {year} is ${stockpile}, and the cost \n for the {activity} activities done during the year is {budget} from the University's \n point of view ".format(year=year,activity=activity, resource = resource, budget=budget, demand=demand,stockpile=stockpile)
        TopFrame6 = Frame(Frame1, width = 750, height = 50)
        TopFrame6.pack(side=TOP)
        Label6 = Label(TopFrame6, text = text6, font=("Courier", 15), anchor=W, justify=LEFT, bg = "WHITE")
        Label6.pack()
        button2 = Button(Frame1,text = "Next",width=20, font=("Courier", 20), command =lambda:[Frame1.master.destroy(), game()])
        button2.pack()
    
    Frame1.mainloop()
    
def values():
   dicval =  {"year":15, "budget":100, "resource":90, "demand":10, "activity": 78, "stockpile": 0}
   year=15
   return year
   #return dicval

def game():
    x = test(values())
game()