#Import necessary libraries
from tkinter import *
from datetime import date

#Create Window
root = Tk()
root.title("Finding products entered by the user!")
root.geometry('400x300')

#Add widgets
#Add Label
lbl = Label(text= "Enter 2 numbers that you want to find the product of. Make sure that the 2 numbers are separated with a *:", fg="white", bg="#072F5F", height=1, width=300)

#Add Label for getting name as input from user
#Use entry widget to create a text box for user to enter details
name_lbl = Label(text="User-inputted products", bg="#3895D3")
product_entry = Entry()
#Function to display message
def display():
    #Read input given by the user
    product_entry = product_entry.get()
    #Declaring a global variable to make it accessible anywhere in the program 
    global message
    message = ""
    greet = "Hello! Your product is:"+product_entry+"\n"
    #Display in a text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

#Add a text widget to display information
text_box = Text(height=3)

#Add button and give value of command as name of the function
#Press button. Display function will be called automatically
btn = Button(text="Calculate product", command=display, height=1, bg="#1261A0", fg='white')

#Organize all the widgets in the window
lbl.pack()
name_lbl.pack()
product_entry.pack()
btn.pack()
text_box.pack()

#Start the GUI even loop
root.mainloop()