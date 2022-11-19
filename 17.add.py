from tkinter import *
import random

window = Tk()
window.title("17.add")
screen = Canvas(window, width=700, height=700, bg="white")
screen.pack()

colors = ['lime', 'red']

for i in range(1000):
    x = random.randint(0, 350)
    y = random.randint(0, 700)
    screen.create_line(350, 350, 350+x, y, fill="red")
    window.update
    
for i in range(1000):
    x = random.randint(0, 350)
    y = random.randint(0, 700)
    screen.create_line(350, 350, 350-x, y, fill="lime")
    window.update
