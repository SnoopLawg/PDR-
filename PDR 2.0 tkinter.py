from cgitb import text
import random
import tkinter as ttk

Athletic = {
    "Rock Climbing":[20.00,1,"1 Hour"],
    "Ice Skating":[10.00,1,"1 Hour"],
    "Snowboarding":[60.00,1,"10 minutes"]
    }

Activity = {
    "The Soap Factory":[18.00,1,"1.5 Hours"],
    "Nickel City":[7.00,1,"1.5 Hours"],
    "Axe Throwing":[14.00,1,"45 minutes"]
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

STYLE = ["Activity","Athletic","Hike","Relax","Food","Snack"]
def date_question():
    root = ttk.Tk()
    # window=ttk.Frame(root,padx=10,pady=10)
    # window.master.title("PDR")
    root.title("PDR")
    variable = ttk.StringVar(root)
    variable.set(STYLE[0]) # default value
    w = ttk.OptionMenu(root, variable,*STYLE)
    question=ttk.Label(text="Pick a date from the drop down")
    question.pack(padx=20,pady=3)
    w.pack(padx=20,pady=3)
    root.mainloop()

def choose_date():
    picker = random.choice(list(Activity))
    print("\n\t--> ",picker," <--\n")
    cost=("Price: "+"${:.2f}".format(int(Activity[picker][0])))
    time=("Duration: "+Activity[picker][2])
    display_date_info(picker,cost,time)

def display_date_info(picker,cost,time):
    window = ttk.Tk()
    window.title("PDR")
    #constant variables for date_name, price, duration are labeled in tkinter
    date_name=ttk.Label(text=picker,width=50,font='Helvetica 18 bold underline')
    price= ttk.Label(text=cost)
    duration=ttk.Label(text=time)
    date_name.pack()
    price.pack()
    duration.pack()
    window.mainloop()



date_question()


# #Assigns choice to what was randomly selected in the dictionary
# choice = random.choice(list(Food))

# #Prints the price of the key selected
# print(Food[choice][0])





    