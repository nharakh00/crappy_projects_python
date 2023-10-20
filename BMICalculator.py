from tkinter import *





# UI

# Creating Window For Our Calculator
window = Tk()
window.geometry("420x420")
window.title("BMI Calculator")




x = IntVar()

def click():

    global x

    if x.get() == 0:
        print("In standard mode")
    elif x.get() == 1:
        print("In Metric mode")
    else:
        print("pick a mode")








# Creating the Top Title Label for our Calculator
title = Label(window, text = "BMI Calculator",
              fg = "Black",
              bd = 10,
              cursor = "dot",
              font = ("Arial", 50),
              pady = 2)
title.pack()

# Creating our radio buttons
x = IntVar()
height_radio_1 = Radiobutton(window, text="standard", variable = x, value = 0)
height_radio_2 = Radiobutton(window, text ="metric", variable = x, value = 1)
height_radio_1.pack()
height_radio_2.pack()


# Telling user to input height in inches
height = Label(window, text = "Enter your height in specified units")
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

button = Button(window, text ="Calculate", command =click)
button.pack()

# Results
result_num = Label(window, text = "")
result_level = Label(window, text = "")

result_num.pack()
result_level.pack()



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
