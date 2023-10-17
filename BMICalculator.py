from tkinter import *

# Working on UI


# Creating Window For Our Calculator
window = Tk()
window.geometry("420x420")
window.title("BMI Calculator")

# Creating the Top Title Label for our Calculator
title = Label(window, text = "BMI Calculator")
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
h_entry = Entry(window, font = ("Arial", 15))
h_entry.pack()

button = Button(window, text ="Calculate")
button.pack()



window.mainloop()


""" BMI Calculator """


"""

This portion contains the logic portion of our application 

print("What is your height in inches?")

height = int(input())

print("What is your weight in pounds?")

weight = int(input())



# Do THe BMI Calculation here

num = 703 * weight
denom = height * height

BMI = num / denom





print("Your BMI is: " + str(BMI))

status = ""


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



"""
