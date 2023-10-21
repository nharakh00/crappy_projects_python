from tkinter import *
from decimal import Decimal

# UI

# Creating Window For Our Calculator
window = Tk()
window.geometry("420x420")
window.title("BMI Calculator")

bmi_level = 0
status = ""

def click():
    
    if h_entry.get() == "" or w_entry.get() == "":
        print("Error: One of the fields is missing")
    else:
        if h_entry.get().isdigit() and w_entry.get().isdigit():
            num = 703 * int(w_entry.get())
            denom = int(h_entry.get()) * int(h_entry.get())
            BMI = num / denom
            print(BMI)

            if BMI < 18.5:
                status = "underweight"
            elif 18.5 <= BMI < 24.9:
                status = "normal"
            elif 24.9 <= BMI < 29.9:
                status = "overweight"
            elif 29.9 <= BMI < 34.9:
                status = "obese"
            elif BMI > 34.9:
                status = "severely obese"
            else:
                status = "Something has gone wrong"

            print("You are " + status + ".")

            result_num.configure(text = str(BMI))
            result_level.configure(text = "You are " + status + ".")
                
        else:
            print("Error: One of the fields is not a digit")
    
  
# Creating the Top Title Label for our Calculator
title = Label(window, text = "BMI Calculator",
              fg = "Black",
              bd = 10,
              cursor = "dot",
              font = ("Arial", 50),
              pady = 2)
title.pack()



# Telling user to input height in inches
height = Label(window, text = "Enter your height in inches")
height.pack()

# Entry bar for user height
h_entry = Entry(window, font = ("Arial", 15))
h_entry.pack()

# Telling User to input weight in pounds 
weight = Label(window, text = "Enter your weight in pounds")
weight.pack()

# Entry bar for user weight 
w_entry = Entry(window, font = ("Arial", 15))
w_entry.pack()

button = Button(window, text ="Calculate", command =click)
button.pack()

# Results
result_num = Label(window, text = "", font=("Arial", 20))
result_level = Label(window, text = "", font =("Arial", 20))

result_num.pack()
result_level.pack()


window.mainloop()

