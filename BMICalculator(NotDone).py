from tkinter import *

"""
# This is from the windows section
window = Tk()
window.geometry("420x420")
window.title("Playing Around With GUI")
# ignored the photo thing
window.config(background = "black")
window.mainloop()
"""

"""

window = Tk()

label = Label(window,
              text = "Hello World",
              font = ('Arial', 40, 'bold'),
              fg = "green",
              bg = "black",
              relief = RAISED,
              bd = 10,
              padx = 20,
              pady = 20)
label.pack()

#label.place(x=50,y=100)

window.mainloop()
# Skipped photo part

"""

window = Tk()

button = Button(window)

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
