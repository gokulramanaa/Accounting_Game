# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 17:35:38 2018

@author: gokul
"""
from tkinter import *
import pandas as pd
import numpy as np

import pandas as pd
import random
import openpyxl
import webbrowser

df = pd.DataFrame(index=range(0,60),columns = ['Year', 'Budget', 'Stockpile', 'Available', 'Demand', 'Activity', 'Shortage', 'Surplus', 'Revert', 'Newstock', 'Cost', 'Efficient', 'Effective', 'Score', 'Points', 'Avgscore','CumAvg'])

def center_window(root,width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (0.6*height)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

def rootfunct():
    root = Tk()
    center_window(root,900,600)
    Frame1 = Frame(root, width=900, height=600, colormap="new")
    Frame1.pack()
    Frame1.pack_propagate(0)
    return Frame1

def act(demand, budget, available):
    if(budget >= demand):
        activity = demand
    elif((budget < demand) and (demand <= available)):
        activity = demand
    elif (available < demand):
        activity = available
    return activity

def short(demand, budget, available):
    if((budget == demand) or (budget > demand)):
        shortage = 0
    elif((budget < demand) and (demand <= available)):
        shortage = demand-budget
    elif(available < demand):
        shortage = demand-available
    return shortage

def surp(demand, budget, available):
    if((budget == demand) or (budget < demand and demand <= available) or (available < demand)):
        surplus = 0
    elif(budget > demand):
        surplus = budget - demand
    return surplus

def revt(demand, budget, available, revtInd, surplus):
    if((budget > demand) and (revtInd == 'Y')):
        revert = surplus
    else:
        revert = 0
    return revert


def nws(budget, demand, available, stkInd, revtInd, shortage, surplus,stockpile):
    #print(budget, demand, available, stkInd, revtInd, shortage, surplus,stockpile)
    if(budget == demand):
        newstock = stockpile
    elif((budget > demand) and (stkInd == 'Y')):
        newstock = stockpile + surplus
    elif((budget > demand) and (revtInd == 'Y')):
        newstock = stockpile
    elif((budget < demand) and (demand <= available)):
        newstock = stockpile-shortage
    elif(available < demand):
        newstock = 0
    else:
        newstock = 0
    #else:
     #   newstock = stockpile
    return newstock

def cst(demand, budget, stkInd, revtInd,available, activity, surplus):
    if(budget == demand):
        cost = activity
    elif((budget > demand) and (stkInd == 'Y')):
        cost = activity + surplus
    elif((budget > demand) and (revtInd == 'Y')):
        cost = activity
    elif((budget < demand) and (demand <= available)):
        cost = activity
    elif(available < demand):
        cost = activity
    else:
        cost = activity
    #else:
      #  cost = activity
    return cost

def effi(activity,cost):
    efficient = (float(activity/cost))
    return efficient

def effe(activity,demand):
    effective = (float(activity/demand))
    return effective

def scr(efficient,effective):
    score = ((efficient+effective)/2)
    return score

def pts(points,score):
    points = points + score
    return points

def avg(points, year):
    avgscore = (points/year)
    #print("Average score {}".format(avgscore))
    return avgscore
    
def wrapup():
    global df
    c = (df['Surplus'] != 0).sum()
    d = (df['Shortage'] != 0).sum()
    finalavg = df["Avgscore"].mean()
    finalscr = df["Score"].mean()
    
    #print(df)
    
    df2 = pd.DataFrame(df,columns=['Year','Demand','Budget'])
    df3 = pd.DataFrame(df,columns=['Year','Efficient','Effective'])
    df4 = pd.DataFrame(df,columns=['Year','Avgscore', 'CumAvg'])
    
    writer = pd.ExcelWriter('output.xlsx', engine = 'xlsxwriter')
    df.to_excel(writer, sheet_name = 'x1')
    df2.to_excel(writer, sheet_name = 'x2')
    df3.to_excel(writer, sheet_name = 'x3')
    df4.to_excel(writer, sheet_name = 'x4')
    
    workbook = writer.book
    worksheet = writer.sheets['x2']
    
    chart = workbook.add_chart({'type': 'line'})
    #chart.add_series({...})
    
    # Configure a series with a secondary axis
    chart.add_series({
        'name':       '=x2!$C$1',
        'categories': '=x2!$B$2:$B$61',
        'values':     '=x2!$C$2:$C$61',
        'y2_axis': 1,
    })
    
    chart.add_series({
        'name':       '=x2!$D$1',
        'categories': '=x2!$B$2:$B$61',
        'values':     '=x2!$D$2:$D$61',
    })
    
    # Add a chart title and some axis labels.
    
    chart.set_title({'name': 'Budget/Demand v Year'})
    chart.set_legend({'position': 'top'})
    chart.set_x_axis({'name': 'Year', })
    chart.set_y_axis({'name': 'Budget', 'major_gridlines': {'visible': 0}})
    chart.set_y_axis({'min': 30, 'max': 210}) #, 'major_gridlines': {'visible': 0}}
    #chart.set_y_axis({'interval_unit': 5})
    chart.set_y2_axis({'name': 'Demand', 'major_gridlines': {'visible': 0}})
    chart.set_y2_axis({'min': 30, 'max': 210})
    #chart.set_y2_axis({'interval_unit': 5})
    chart.set_size({'width': 1100, 'height': 375})
    
    # Insert the chart into the worksheet (with an offset).
    worksheet.insert_chart('E2', chart) #, {'x_offset': 50, 'y_offset': 20}
    
    #workbook.close()
    
    workbook = writer.book
    worksheet = writer.sheets['x3']
    
    chart = workbook.add_chart({'type': 'line'})
    
    # Configure a series with a secondary axis
    chart.add_series({
        'name':       '=x3!$D$1',
        'categories': '=x3!$B$2:$B$61',
        'values':     '=x3!$D$2:$D$61',
        'y2_axis': 1,
    })
    
    chart.add_series({
        'name':       '=x3!$C$1',
        'categories': '=x3!$B$2:$B$61',
        'values':     '=x3!$C$2:$C$61',
    })
    
    chart.set_legend({'position': 'top'})
    
    # Add a chart title and some axis labels.
    chart.set_title({'name': 'Efficency/Effectivness v Year'})
    chart.set_x_axis({'name': 'Year', })
    chart.set_y_axis({'name': 'Efficient', 'major_gridlines': {'visible': 0}})
    chart.set_y_axis({'min': 0.85, 'max': 1.1}) #, 'major_gridlines': {'visible': 0}}
    #chart.set_y_axis({'interval_unit': 0.025})
    chart.set_y2_axis({'name': 'Effective', 'major_gridlines': {'visible': 0}})
    chart.set_y2_axis({'min': 0.85, 'max': 1.1})
    #chart.set_y2_axis({'interval_unit': 0.025})
    chart.set_size({'width': 1100, 'height': 350})
    
    # Insert the chart into the worksheet (with an offset).
    worksheet.insert_chart('E2', chart, {'x_offset': 50, 'y_offset': 20}) #, {'x_offset': 50, 'y_offset': 20}
    
    workbook = writer.book
    worksheet = writer.sheets['x4']
    
    chart = workbook.add_chart({'type': 'line'})
    
    # Configure a series with a secondary axis
    chart = workbook.add_chart({'type': 'line'})
    
    # Configure a series with a secondary axis
    chart.add_series({
        'name':       '=x4!$D$1',
        'categories': '=x4!$B$2:$B$61',
        'values':     '=x4!$D$2:$D$61',
        'y2_axis': 1,
    })
    
    chart.add_series({
        'name':       '=x4!$C$1',
        'categories': '=x4!$B$2:$B$61',
        'values':     '=x4!$C$2:$C$61',
    })
    
    chart.set_legend({'position': 'top'})
    
    # Add a chart title and some axis labels.
    chart.set_title({'name': 'Avg Score/Cumulative Avg v Year'})
    chart.set_x_axis({'name': 'Year', })
    chart.set_y_axis({'name': 'CumAvg', 'major_gridlines': {'visible': 0}})
    chart.set_y_axis({'min': 0.9, 'max': 1.1}) #, 'major_gridlines': {'visible': 0}}
    #chart.set_y_axis({'interval_unit': 0.025})
    chart.set_y2_axis({'name': 'AvgScore', 'major_gridlines': {'visible': 0}})
    chart.set_y2_axis({'min': 0.9, 'max': 1.1})
    #chart.set_y2_axis({'interval_unit': 0.025})
    chart.set_size({'width': 1100, 'height': 350})
    
    # Insert the chart into the worksheet (with an offset).
    worksheet.insert_chart('E2', chart, {'x_offset': 50, 'y_offset': 20})
    
    workbook.close()
    
    writer.save()
    
    
    #with pd.ExcelWriter('output.xlsx', engine='xlsxwriter') as writer:    
    #df.to_excel(writer, '1st_sheet')   
    #df2.to_excel(writer, '2nd_sheet')   
    #writer.save()    
    
    
    #writer = pd.ExcelWriter('output.xlsx',engine='xlsxwriter')
    #df.to_excel(writer,sheet_name='Sheet1')
    #df2.to_excel(writer,sheet_name='Sheet2')
    #writer.save()
    
    #workbook = writer.book
    #worksheet = writer.sheets[2nd_sheet]
    
    # Create a new chart object. In this case an embedded chart.
    
    print("your output file has been saved to same location as this executable file")
    '''
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
     
    fromaddr = "## from address"
    toaddr = "## to address"
     
    msg = MIMEMultipart()
     
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Budget Game Result"
     
    body = "Hi, This is an Automated mail. Please find the output file attached"
     
    msg.attach(MIMEText(body, 'plain'))
     
    filename = "output.xlsx"
    attachment = open("output.xlsx", "rb")
     
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    msg.attach(part)
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "## password")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    '''
#    print("The number of times Surplus occurred in this game", c)
#    print("The number of times Shortage occured in this game", d)
#    print("Your Average Score for this game is",finalavg*100,"%")
#    print("Your final combined efficency and effectiveness for this game is", finalscr*100,"%")
    
    webbrowser.open('output.xlsx')


def scoredisplay():
    global year
    global activity
    global cost
    global demand
    global efficient 
    global effective 
    global score 
    global avgscore 
    global cumavg

    Frame1 = rootfunct()
    text = "\nDetermining Efficiency, Effectiveness, Score in this period, \nCumulative points, and Cumulative average at the end of Year {}\n\n".format(year)
    text1 = "  Efficiency in year {}: \n  Activities done/Cost of activities done = ${} / ${} = {}  \n".format(year, activity,cost,efficient)
    text2 = "Effectiveness in year {}: \nActivities done/ Activities Demanded = ${} / ${} = {}  \n".format(year, activity,demand,effective)
    text3 = "Average score in year {}:  \n Points/Year = {}\n".format(year, avgscore)
    #text4 = "Actual demand for year {} = {}                       \n".format(year,demand)
    text5 = "Cumulative Average score in year {}:  \n Sum of Average/Number of years = {}         ".format(year, cumavg)
    
#    TopFrame = Frame(Frame1, width=750, height=50)
#    TopFrame.pack(side = TOP)
#    TopFrame.pack_propagate(0)
    Label0 = Label(Frame1, text = text, font=("Courier", 18))
    Label0.pack(side = TOP)
    Label2 = Label(Frame1, text = text1, font=("Courier", 16), anchor=W,justify=LEFT)
    Label2.pack(side = TOP)
    Label1 = Label(Frame1, text = text2, font=("Courier", 16),anchor=W,justify=LEFT)
    Label1.pack(side = TOP)
    Label3 = Label(Frame1, text = text3, font=("Courier", 16),anchor=W,justify=LEFT)
    Label3.pack(side = TOP)
    Label5 = Label(Frame1, text = text5, font=("Courier", 16), anchor=W,justify=LEFT)
    Label5.pack(side = TOP)
    
    if year == 60:
        button2 = Button(Frame1,text = "Finish",width=20, font=("Courier", 20),command =lambda:[Frame1.master.destroy(), wrapup()])
        button2.pack(side = BOTTOM)
    else:
        button = Button(Frame1,text = "Continue",width=20, font=("Courier", 20), command =lambda:[Frame1.master.destroy(), game()])
        button.pack(side = BOTTOM)
    
    Frame1.mainloop()
    
def backend():
    global year
    global budget
    global stockpile 
    global available 
    global demand 
    global activity 
    global shortage 
    global surplus 
    global revert 
    global cumavg
    global newstock 
    global cost 
    global efficient 
    global effective 
    global score 
    global points 
    global avgscore 
    global newyear 
    global revtInd 
    global stkInd 
    global newInd 
    global newdemand
    global budget1
    global mylist
    global revert1
    global finalavg
    global finalscr
    global df
    global c
    if (year == 1 and demand == 0):
        budget = 100
        df['Budget'].iloc[0]= budget
        stockpile = 0
        df['Stockpile'].iloc[0]= stockpile
        df['Year'].iloc[0]= year
        mylist = [90,100,110]
        demand = random.choice(mylist)
        #temp = int(input("Enter demand "))
        #demand = temp
        df['Demand'].iloc[0]= demand
        available = budget + stockpile
        df['Available'].iloc[0]= available
        activity = act(demand, budget, available)
        df['Activity'].iloc[0]= activity
        shortage = short(demand, budget, available)
        df['Shortage'].iloc[0]= shortage
        surplus = surp(demand, budget, available)
        df['Surplus'].iloc[0]= surplus
        shortage = short(demand, budget, available)
        df['Shortage'].iloc[0]= shortage
            
        return (year, budget, available, demand, activity, stockpile, shortage, surplus)
    elif year>1:
        df['Year'].iloc[year-1] = year
        if(df['Revert'].iloc[year-2] > 0):
            budget1 = df['Budget'].iloc[year-2]
            revert1 = df['Revert'].iloc[year-2]
            budget = int(budget1-(0.5*revert1))
            df['Budget'].iloc[year-1]= budget
        else:
            newdemand = df['Demand'].iloc[year-2]
            mylist1 = [newdemand+10, newdemand, newdemand-10]
            budget = random.choice(mylist1)
            #temp1 = int(input("Enter budget "))
            #budget = temp1
            
            df['Budget'].iloc[year-1]= budget
        if((budget<50) or (budget>200)):
            budget = 100
            df['Budget'].iloc[year-1]= budget
        
        #stockpile = stockpile + df['Stockpile'].iloc[year-2]
        stockpile = newstock
        df['Stockpile'].iloc[year-1] = stockpile
        available = budget + stockpile
        df['Available'].iloc[year-1]= available
        mylist = [budget+10, budget, budget-10]
        demand = random.choice(mylist)
        #temp = int(input("Enter demand "))
        #demand = temp
        df['Demand'].iloc[year-1]= demand
        activity = act(demand, budget, available)
        df['Activity'].iloc[year-1]= activity
        shortage = short(demand, budget, available)
        df['Shortage'].iloc[year-1]= shortage
#        revtInd = 'N'
#        stkInd = 'N'
        surplus = surp(demand, budget, available)
        df['Surplus'].iloc[year-1]= surplus
        shortage = short(demand, budget, available)
        df['Shortage'].iloc[year-1]= shortage
        
        return(year, budget, available, demand, activity, stockpile, shortage, surplus)


def stockpilef(newInd, year, budget, available, demand, activity, stockpile, shortage, surplus):
        global revtInd
        global stkInd
        if(surplus > 0):
            if(newInd == 1 ):
                stkInd = 'Y'
                df['Stockpile'].iloc[0]= surplus
            elif(newInd == 2):
                revtInd = 'Y'
            else:
                revtInd = 'N'
        return 1
        
def calculation():
    global year
    global budget
    global stockpile 
    global available 
    global demand 
    global activity 
    global shortage 
    global surplus 
    global cumavg
    global revert 
    global newstock 
    global cost 
    global efficient 
    global effective 
    global score 
    global points 
    global avgscore 
    global newyear 
    global revtInd 
    global stkInd 
    global newInd 
    global newdemand
    global budget1
    global revert1
    global finalavg
    global i
    global finalscr 
    
    if((revtInd == 'Y') & (newInd == 2)):
        revert = revt(demand, budget, available, revtInd, surplus)
        df['Revert'].iloc[year-1]= revert
    else:
        df['Revert'].iloc[year-1] = 0  
    newstock = nws(budget, demand, available, stkInd, revtInd, shortage, surplus,stockpile)
    df['Newstock'].iloc[year-1]= newstock
    cost = cst(demand, budget, stkInd, revtInd,available, activity, surplus)
    df['Cost'].iloc[year-1]= cost
    efficient = effi(activity,cost)
    df['Efficient'].iloc[year-1]= efficient
    effective = effe(activity,demand)
    df['Effective'].iloc[year-1]= effective
    score=scr(efficient,effective)
    df['Score'].iloc[year-1]= score
    points = pts(points,score)
    df['Points'].iloc[year-1]= points
    avgscore = avg(points, year)
    df['Avgscore'].iloc[year-1]= avgscore
    if year ==1:
        cumavg = avgscore
        df['CumAvg'].iloc[0]= cumavg
    else:
        cavg = df['Avgscore'].sum()
        cumavg = cavg /  year
        df['CumAvg'].iloc[year-1]= cumavg
     
def test():
    global year
    global budget
    #print("budget: {}".format(budget))
    global stockpile 
    #print("stockpile: {}".format(stockpile))
    global available 
    #print("available: {}".format(available))
    global demand 
    global activity 
    global shortage 
    #print("shortage: {}".format(shortage))
    global surplus 
    #print("surplus: {}".format(surplus))
    global revert 
    global newstock 
    global cost 
    #print("cost: {}".format(cost))
    global efficient 
    global effective 
    global score 
    global points 
    global avgscore 
    global newyear 
    global revtInd 
    global stkInd 
    global newInd 
    global mylist
    global newdemand
    global budget1
    global revert1
    global finalavg
    global finalscr
    temp = budget + stockpile
    Frame1 = rootfunct()
    text = "Year {}               Budget for year {}    {}".format(year,year,budget)
    text1 = "Current stock pile for year {}                            = ${}".format(year,stockpile)
    text2 = "The amount of resources available for year {} = (${} + ${}) = ${}\n".format(year,budget,stockpile,temp)
    text3 = "Demand for year {} has an equal chance of being {}   ".format(year,mylist)
    text4 = "Actual demand for year {} is                                 = {}\n".format(year,demand)
    text7 = "So only {} of activities can be done, and all the stockpiled resources must be used".format(budget)
    text8 = "Activities done in year {}".format(year)
    
    TopFrame = Frame(Frame1, width=750, height=50)
    TopFrame.pack(side = TOP)
    TopFrame.pack_propagate(0)
    Label0 = Label(TopFrame, text = text, font=("Courier", 20), justify = LEFT)
    Label0.pack(side = BOTTOM)
    
    TopFrame1 = Frame(Frame1, width = 750, height = 30)
    TopFrame1.pack(side=TOP)
    TopFrame1.pack_propagate(0)
    Label2 = Label(TopFrame1, text = text1, font=("Courier", 15), justify = LEFT)
    Label2.pack(side = BOTTOM)
    
    TopFrame2 = Frame(Frame1, width = 750, height = 50)
    TopFrame2.pack(side=TOP)
    Label1 = Label(TopFrame2, text = text2, font=("Courier", 15), justify = LEFT)
    Label1.pack(side = BOTTOM)
    
    TopFrame3 = Frame(Frame1, width = 750, height = 50)
    TopFrame3.pack(side=TOP)
    Label3 = Label(TopFrame3, text = text3, font=("Courier 15 bold"), anchor=W, justify=LEFT)
    Label3.pack(side = BOTTOM)
    
    TopFrame4 = Frame(Frame1, width = 750, height = 50)
    TopFrame4.pack(side=TOP)
    Label4 = Label(TopFrame4, text = text4, font=("Courier", 15,), anchor=W, justify=LEFT)
    Label4.pack(side = BOTTOM)
    
    if budget==demand:
            text6 = "\n {available} of resources are available, and {demand} of activites are demanded.\n So all activities can be done without using any stockpiled resources \n Activities done in year {year}                                = {activity} \n\n Since the {budget} budgeted equaled the {demand} deamanded. No resources were added \n to or taken from stockpile. \n\n The amount of stockpile at the end of the year {year} is ${stockpile}, and the cost \n for the {activity} activities done during the year is {budget} from the University's \n point of view ".format(year=year,activity=activity, available = available, budget=budget, demand=demand,stockpile=stockpile)
            TopFrame6 = Frame(Frame1, width = 750, height = 50)
            TopFrame6.pack(side=TOP)
            Label6 = Label(TopFrame6, text = text6, font=("Courier", 15), anchor=W, justify=LEFT, bg="WHITE")
            Label6.pack(side = BOTTOM)
            button2 = Button(Frame1,text = "Next",width=20, font=("Courier", 20),command =lambda:[Frame1.master.destroy(), scoredisplay()])
            button2.pack(side = BOTTOM)
            calculation()
    elif budget > demand:
        temp = budget - demand
        text6 = "\n {available} of resources are available, and {demand} of activites are demanded.\n So all activities can be done without using any stockpiled resources \n Activities done in year {year}                                    = {activity} \n\n Since the {budget} budgeted greater than {demand} deamanded. There is a surplus \n of {surp} \n\n Do you want to stockpile the surplus for future use or allow it to \n revert to the university? ".format(year=year,activity=activity, available = available, budget=budget, demand=demand,stockpile=stockpile,surp=temp)
        TopFrame6 = Frame(Frame1, width = 750, height = 50)
        Label6 = Label(TopFrame6, text = text6, font=("Courier", 15), anchor=W, justify=LEFT, bg="WHITE")
        Label6.pack(side = BOTTOM)
        TopFrame6.pack(side=TOP)
        
        TopFrame7 = Frame(Frame1, width = 750, height = 50)
        TopFrame7.pack(side=TOP)
        Label7 = Label(Frame1, text = "")
        Label7.pack(side=BOTTOM)
        
        def dummy1(Frame1, stock):
            global Label7
            dummy1.has_been_called = True
            global stockpile
            global available
            global activity
            global Label7
            if (stock == 1):
                #Label7.destroy()
                text7 = "\n You have chosen to stockpile the surplus, so your stockpile is now {stockpile} and \n the cost for {activity} activities done during the year is {resource} from the university point of view".format(stockpile = stockpile, resource = available, activity = activity)
                Label7 = Label(Frame1, text = text7, font=("Courier", 15), bg="WHITE", textvariable = text)
                Label7.pack(side = BOTTOM)
            elif (stock == 2):
                #Label7.destroy()
                text8 = "\n You have chosen to allow the surplus to revert to university, so your stockpile \n is $0 and the cost for {activity} activities done during the year is {resource} from the university point of view".format(stockpile = stockpile, resource = available, activity = activity)
                Label7 = Label(Frame1, text = text8, font=("Courier", 15), bg="WHITE", textvariable = text)
                Label7.pack(side = BOTTOM)
            return 1
        dummy1.has_been_called = False
        
        def decid1(Frame1,stock):
            global Label7
            if dummy1.has_been_called == False:
                dummy1(Frame1, stock)
            else:
                Label7.destroy()
                dummy1(Frame1,stock)
            
        Label7 = Label(TopFrame7)
        def sel():
            selection = "You selected the option " + str(var.get())
            #print(var.get())
            global stock 
            stock = var.get()
            #dummy1(Frame1,stock)
            #decid1(Frame1, stock)
            stockpilef(stock, year, budget, available, demand, activity, stockpile, shortage, surplus)
            calculation()
            return 1
        
            text = StringVar()
            TopFrame8 = Frame(Frame1, width = 750, height = 50)
            TopFrame8.pack(side=TOP)
#        def dummy1():
#            if (var.get() == 1):
#                text7 = "\n You have chosen to stockpile the surplus, so your stockpile is now {stockpile} and \n the cost for {activity} activities done during the year is {resource} from the university point of view".format(stockpile = stockpile, resource = available, activity = activity)
#                Label7 = Label(TopFrame8, text = text7, font=("Courier", 15), bg="WHITE", textvariable = text)
#                Label7.pack(side = BOTTOM)
#            else:
#                text8 = "\n You have chosen to allow the surplus to revert to university, so your stockpile \n is $0 and the cost for {activity} activities done during the year is {resource} from the university point of view".format(stockpile = stockpile, resource = available, activity = activity)
#                text.set(text8)
#            return 1

        def dummy(Frame1):
            dummy.has_been_called = True
            button2 = Button(Frame1,text = "Next",width=20, font=("Courier", 20), command =lambda:[Frame1.master.destroy(), scoredisplay()])
            button2.pack(side = BOTTOM)
        dummy.has_been_called = False
        
        def decid(Frame1):
            if dummy.has_been_called == False:
                dummy(Frame1)
            else:
                pass
            
        var = IntVar()
        stock = 0
        Radiobutton(TopFrame7, text="Stockpile", variable=var, value=1, command=lambda:[sel(), decid(Frame1)]).pack(anchor=W)
        Radiobutton(TopFrame7, text="Revert", variable=var, value=2, command=lambda:[sel(), decid(Frame1)]).pack(anchor=W)
        #print("radio button value: {}".format(stock))
        
#        button2 = Button(Frame1,text = "Next",width=20, font=("Courier", 20), command =lambda:[Frame1.master.destroy(), game()])
#        button2.pack()
        
    else:
        text6 = "\n {available} of resources are available, but {demand} of activites are demanded.\n So only {activity} activities can be done, and all stockpiled resources \n must be used. Activities done in year {year}                                   = {activity} \n\n Since the {budget} budgeted was less than the {demand} deamanded. all {stockpile} resources \n were used. \n\n The amount of stockpile at the end of the year {year} is ${stockpile}, and the cost \n for the {activity} activities done during the year is {budget} from the University's \n point of view ".format(year=year,activity=activity, available = available, budget=budget, demand=demand,stockpile=stockpile)
        TopFrame6 = Frame(Frame1, width = 750, height = 50)
        TopFrame6.pack(side=TOP)
        Label6 = Label(TopFrame6, text = text6, font=("Courier", 15), anchor=W, justify=LEFT, bg = "WHITE")
        Label6.pack()
        button2 = Button(Frame1,text = "Next",width=20, font=("Courier", 20),command =lambda:[Frame1.master.destroy(), scoredisplay()])
        button2.pack(side = BOTTOM)
        calculation()
    
    Frame1.mainloop()


def game():
    global year
    year +=1
#    if year == 61:
#        wrapup()
#    else:
    y = backend()
    x = test()

##########################################################################################################
class Labelclass():
    def __init__(self,master,txt, font=("Courier", 30)):
        Label1 = Label(master, text = txt, 
                       font=font)
        Label1.pack(side = BOTTOM)
def InstFunct():
    TopFrame = rootfunct()
    photo = PhotoImage(file="C:/Users/gokul/Documents/Projects/AccountingGame/imgs/inst.png")
    w = Label(TopFrame, image=photo)
    w.photo = photo
    w.pack()
    button1 = Button(TopFrame,text = "Start",width=20, font=("Courier", 20), command =lambda:[TopFrame.master.destroy(), game()])
    button1.pack(side = BOTTOM)
    Frame1.mainloop()
def InstFunct2():
    TopFrame = rootfunct()
    photo = PhotoImage(file="C:/Users/gokul/Documents/Projects/AccountingGame/imgs/inst1.png")
    w = Label(TopFrame, image=photo)
    w.photo = photo
    w.pack()
    button2 = Button(TopFrame,text = "Next",width=20, font=("Courier", 20), command =lambda:[TopFrame.master.destroy(), InstFunct()])
    button2.pack(side = BOTTOM)
    Frame1.mainloop() 
def quit(self):
    self.root.destroy()
#################################################################################################


if __name__ == "__main__":
    year = 0
    budget = 0
    stockpile = 0
    available = 0
    demand = 0
    activity = 0
    shortage = 0
    surplus = 0
    revert = 0
    newstock = 0
    cost = 0
    efficient = 0
    effective = 0
    score = 0
    points = 0
    avgscore = 0
    newyear = 0
    revtInd = 'N'
    stkInd = 'N'
    newInd = 'N'
    newdemand = 0
    budget1 = 0
    revert1 = 0
    mylist =[]
    finalavg = 0
    finalscr = 0
    cumavgscore = 8
    Frame1 = rootfunct()
    TopFrame = Frame(Frame1, width=700, height=150)
    TopFrame.pack()
    TopFrame.pack_propagate(0)
    text = "Dr. Medinets \n Budgetry Strategy Game"
    Labelclass(TopFrame, text)

    #Buttons
    CButton = Button(Frame1,text="Close",width=10, font=("Courier", 10), command = Frame1.master.destroy)
    CButton.pack(side=BOTTOM)
    IButton = Button(Frame1,text="Instructions",width=20, font=("Courier", 20), command =lambda:[Frame1.master.destroy(), InstFunct2()])
    IButton.pack(side=BOTTOM)
    SButton = Button(Frame1,text="Start",width=20, font=("Courier", 20), command =lambda:[Frame1.master.destroy(), game()])
    SButton.pack(side=BOTTOM)
    #quit(self)
    Frame1.mainloop()