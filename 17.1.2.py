from tkinter import *
import random

window = Tk()
window.title("17.1.2")
screen = Canvas(window, width=700, height=700, bg="white")
screen.pack()

colors = ['lime', 'green', 'red', 'orange', 'blue', 'light blue', 'yellow', 'purple', 'white', 'light gray', 'cyan']
for i in range(500):
    center = random.randint(0, 700)
    radius = random.randint(10, 50)
    screen.create_oval(center-radius, 700-center-radius, center+radius, 700-center+radius, fill=colors[random.randint(0, 10)])
    window.update
