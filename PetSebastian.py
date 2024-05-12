# This program is a name generator for Pets
# To use the program, please specify the type of pet you have; (Dog, Cat, Hamster)
# Next, Type the first letter (Capitalized) you would like the name generated to start with
# Only letters A-F are available, but more can be added into code
# Additionally, you do not have to input any letter and can just generate any name if you chose CAT, DOG, or HAMSTER
# Lastly click the Generate Name button
# A name will be presented to you at random with names starting from that letter

# Sources:
# https://stackoverflow.com/questions/40921767/generate-list-of-random-names-python
# Reference Radio Button and StringVar concept: https://www.pythontutorial.net/tkinter/tkinter-radio-button/
# Pets Logo/Image: https://pngtree.com/freebackground/cute-cartoon-dog-wallpaper_1348618.html

# Reference Legend:
# ME (Sebastian wrote and/or modified this code)
# SO (Stack Overflow Forum)
# PT (Python source tutorial)
# CW (BUS 472 class/hwk/midterm project works - specified)

# Imports
import tkinter as tk  # Used for GUI (ME)
from tkinter import *  # Used for GUI (ME)
import random  # (CW - class work - choosing randomly from a list)
from PIL import Image, ImageTk  # (CW - Midterm - Project 1)

# Opens background logo and assigned the variable 'im'
im = Image.open('Pets.jpg')  # (CW - Midterm - Project 1)

# Condition for names (ME, SO, & CW - Module 5 - Assignment 2)
# Also sets the list of names that can be generated depending on first letter choice
def generate_name(pettype, starting_letter):
    dog_names = [  # sets list for dog names
        "Alco", "Abra",
        "Brix", "Bree",
        "Catcher", "Cash",
        "Diver", "Dina",
        "Ether", "Emmy",
        "Fran", "Frank"]
    cat_names = [  # sets list for cat names
        "Abigail", "Astro",
        "Bella", "Braxton",
        "Chloe", "Caz",
        "Emma", "Ember",
        "Faith", "Flash"]
    ham_names = [  # sets list for hamster names
        "Aly", "Amp",
        "Biscuit", "Butters",
        "Chewy", "Choom",
        "Droopy", "Dino",
        "Earthy", "Elmo",
        "Fasty", "Flow"]
    if pettype == "Dog":
        names = [name for name in dog_names if name.startswith(starting_letter)]
    elif pettype == "Cat":
        names = [name for name in cat_names if name.startswith(starting_letter)]
    elif pettype == "Hamster":
        names = [name for name in ham_names if name.startswith(starting_letter)]
    else:
        return "No name found for this combination"
    if names:
        return random.choice(names)

# Call for button click (ME & PT)
def generate_button_click():
    pettype = pettype_var.get()  # retrieves input from first def condition
    starting_letter = starting_letter_var.get().upper()  # retrieves the first letter

    name = generate_name(pettype, starting_letter)  # calls to values pettype and starting_letter variables
    result_label.config(text=name)  # name is generated if all conditions are met

# Creates root main window (ME)
root = tk.Tk()
root.title("Pet Name Generator") # Title of window
root.geometry("500x400")  # size of window
root.configure(background="dark orange")  # window visuals, background color
root.resizable(0,0) # Disables manipulation of window size

# Background Image Manipulation (CW - Midterm - Project 1)
im_resize = im.resize((405, 300))  # resizes image Pet.jpg
img = ImageTk.PhotoImage(im_resize)  # change image to photo type
label = Label(root, image=img)  # sets image as label
label.place(x=45, y=50)  # Positioning of Label image


# Select Pet Type Label (ME)
pettype_label = tk.Label(root, width=30, background="SlateBlue", font=("Impact", 27), fg="White", text="Select Pet Type:")
pettype_label.pack(pady=0)

# Pet Type Selections (ME & PT)
pettype_var = tk.StringVar()  # StringVar allows for inputs into Radio button be called and connected to def function
pettype_var.set("Dog")  # default value

# Radio Buttons for CAT, DOG, and HAMSTER, along with visual customizations (ME & PT)
pettype_radio_dog = tk.Radiobutton(root, background="DarkOrange", text="DOG", font=("Impact", 10), fg="White", variable=pettype_var, value="Dog")  # visual customizations and connects to variable
pettype_radio_dog.pack(pady=4)  # positioning on y-axis of window, sets container for Radiobutton
pettype_radio_cat = tk.Radiobutton(root, background="DarkOrange", text="CAT", font=("Impact", 10), fg="White", variable=pettype_var, value="Cat")  # visual customizations and connects to variable
pettype_radio_cat.pack(pady=5)  # positioning on y-axis of window, sets container for Radiobutton
pettype_radio_ham = tk.Radiobutton(root, background="DarkOrange", text="HAMSTER", font=("Impact", 10), fg="White", variable=pettype_var, value="Hamster")  # visual customizations and connects to variable
pettype_radio_ham.pack(pady=6)  # positioning on y-axis of window, sets container for Radiobutton

# Starting letter Label with visual customizations(ME)
starting_letter_label = tk.Label(root, background="White", font=("Impact", 15), fg="SlateBlue", text="Enter Starting Letter:")
starting_letter_label.pack(pady=8)  # positioning on y-axis of window
# Starting letter Entry with visual customizations (ME & PT)
starting_letter_var = tk.StringVar()  # StringVar allows for inputs into Radio button be called and connected to def function
starting_letter_entry = tk.Entry(root, width=10, background="DarkOrange", font=("HP Simplified", 10), textvariable=starting_letter_var) # visual customizations and connects to variable
starting_letter_entry.pack(pady=9)  # positioning on y-axis of window

# Generate Name button with visual customizations - Button is connected 2nd def function (ME)
generate_button = tk.Button(root, background="White", text="Generate Name", font=("Impact", 10), fg="SlateBlue", command=generate_button_click)
generate_button.pack()  # no manipulation, default container
# Label for output with visual customizations (ME)
result_label = tk.Label(root, width=23, background="SlateBlue", font=("Impact", 27), fg="White", text="")
result_label.pack(pady=40)  # positioning on y-axis of window, sets container for Label

# Runs GUI (ME)
root.mainloop()

