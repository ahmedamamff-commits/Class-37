#Import necessary libraries
from tkinter import *
from datetime import date

#Create Window
root = Tk()
root.title("Exploiting Arham Hossain Syed's address! :D")
root.geometry('400x300')

#Add widgets
#Add Label
lbl = Label(text="Hey there! Lets exploit Arham's address!", fg="white", bg="#072F5F", height=1, width=300)

#Add Label for getting name as input from user
#Use entry widget to create a text box for user to enter details
name_lbl = Label(text="Arham's Address", bg="#3895D3")
name_entry = Entry()
#Function to display message
def display():
    #Read input given by the user
    name = name_entry.get()
    #Declaring a global variable to make it accessible anywhere in the program that exploits Arham's address
    global message
    message = "Welcome to the Application, where we will exploit\n Arham Syed's address!"
    greet = "Hello "+name+"\n"
    #Display Arham's exploited address in a text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

#Add a text widget to display information
text_box = Text(height=3)

#Add button and give value of command as name of the function
#Press button. Display function will be called automatically
btn = Button(text="Begin exploitation process", command=display, height=1, bg="#1261A0", fg='white')

#Organize all the widgets in the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

#Start the GUI even loop
root.mainloop()