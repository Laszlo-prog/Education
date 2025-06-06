from tkinter import *
root = Tk()
def myClick():
    myLabel = Label(root, text="Look! I clicked!")
    myLabel.pack()

#Creating a label widget
#myLabel1 = Label(root, text="Hello World!")
#myLabel2 = Label(root, text="Your Email!")
myButton = Button(root, text="Click", padx=5, pady=5, command=myClick)

#Shoving into the screen
#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=0) 
myButton.pack()





root.mainloop()
