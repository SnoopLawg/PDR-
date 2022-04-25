from asyncio import sleep
from cgitb import text
import random
import tkinter as ttk
from turtle import bgcolor, color

from setuptools import Command

#######################################################################################

#Dictionaries of possible date categories and their possible specific dates within
#TODO:The plan is to have a webscraper/integration to Google API

Athletic = {
    "Rock Climbing":[20.00,1,"1 Hour"],
    "Ice Skating":[10.00,1,"1 Hour"],
    "Snowboarding":[60.00,1,"10 minutes"]
    
    }

Activity = {
    "The Soap Factory":[18.00,1,"1.5 Hours"],
    "Nickel City":[7.00,1,"1.5 Hours"],
    "Axe Throwing":[14.00,1,"45 minutes"],
    "kiss me pleasssseeee":[10,1,"forever if you play your cards right"]
    }

Food = {
    "Subway":[8.00,1,"20 minutes"],
    "Wendys":[10.00,1,"30 minutes"],
    "Taco Bell":[9.00,1,"10 minutes"]
    }

Relax = {
    "Velour":[10.00,1,"45 minutes"],
    "Museum":["FREE",1,"30 minutes"],
    "Krishna Temple":["FREE",1,"45 minutes"]
    }

Snack = {
    "Ice Cream":[8.00,1,"30"],
    "Good Move":[10.00,1,"1 Hour"],
    "Chocolate Tasting":[9.00,1,"30 minutes"]
    }

Hike = {
    "Hike the Y":["FREE",1,"2 Hours"],
    "Hike Squaw Peek":["FREE",1,"3 Hours"],
    "Hike Mt. Timpanogas":["FREE",1,"5 Hours"]
    }

# #list of restaurants
# for i in restaurants:
#     print(restaurants[i][0])

#######################################################################################



STYLE = ["Activity","Athletic","Hike","Relax","Food","Snack"]
def date_survey():
    root = ttk.Tk()
    root.title("PDR")
    root.iconbitmap=("/Users/logansingleton/Documents/Code/DATE RANDOMIZER/Paomedia-Small-N-Flat-Calendar.ico")
    variable = ttk.StringVar(root)
    variable.set(STYLE[0]) # default first value
    optionmenu = ttk.OptionMenu(root, variable,*STYLE)
    question=ttk.Label(text="Pick a date from the drop down")
    question.grid(row=0,column=0,padx=20,pady=3)
    optionmenu.grid(row=1,column=0,padx=20,pady=3)
    myButton= ttk.Button(root,text="GENERATE",command=choose_date)
    myButton.grid(row=3,column=0,padx=20,pady=3)
    #TODO:get button push --> Redo choose_date ()
    root.mainloop()

def choose_date():
    picker = random.choice(list(Activity))
    print("\n\t--> ",picker," <--\n")
    cost=("Price: "+"${:.2f}".format(int(Activity[picker][0])))
    time=("Duration: "+Activity[picker][2])
    display_date_info(picker,cost,time)

def display_date_info(picker,cost,time):
    #constant variables for date_name, price, duration are labeled in tkinter
    global date_name
    global price
    global duration
    date_name=ttk.Label(text=picker,width=50,font='Helvetica 18 bold underline')
    price= ttk.Label(text=cost)
    duration=ttk.Label(text=time)
    #TODO:Make the variable go away each button press

    date_name.grid(row=4,column=0,)
    price.grid(row=5,column=0,)
    duration.grid(row=6,column=0,)
    
    
    



#######################################################################################
#TODO: fix Call the functions (date_survey --> choose_date --> display_date_info)

date_survey()
choose_date()






"""
PSEUDOO CODE:

::PHASE 1 ::(information retrieval) !!!SKIPPED FOR NOW!!!

Integrate google "Places" API so that it can pull the location based info like restuarants near me and put it in my dictionaries

::PHASE 2::(ask user their preferred date then randomize)

Step 1 --> Ask for input in terminal (DONE via Provo Date Randomizer.py)
Step 2 --> Use tkinter drop down to list selection of dicitonaries/date categories with a generate button
            a.Generate button causes new information to replace the dropdown and generate button displaying DATE NAME, DATE PRICEx2, DURATION
Step 3 --> Wrap this tkinter program into an exe file for windows/mac
Step 4 --> Compatibility with iphone/android

::PHASE 4::(have app be an extension to mutual/tinder/bumble)

?? Somehow make the app an extension to dating apps/within their chat/maybe imessage
Possibly add a spin wheel animation


"""