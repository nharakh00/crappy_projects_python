from tkinter import *
import random 


colors = ["red", "blue", "yellow", "green",
          "purple", "orange", "white", "grey"]

bg_color = "white"

def click():
    
    global colors
    global bg_color
    
    bg_color = colors[random.randint(0,6)]
    window.configure(bg = bg_color)
    label.configure(text = bg_color)
    
    
    
window = Tk()
window.geometry("500x500")
window.title("Color Change Button")
window.configure(bg = bg_color)

button = Button(window,
                text= "click me",
                command = click,
                font = ("Comic Sans", 30)
                )
button.pack()

label = Label(window,
              text = bg_color,
              font = ("Arial", 35, "bold"),
              fg = "black",
              bg = "white"
              )
label.pack()




window.mainloop()
