from tkinter import *
import time

window = Tk()
window.title("Завдання 16.2")

screen = Canvas(window, width=700, height=700, bg="white")
screen.pack()

screen.create_line(350, 100, 350, 600, width=2)
while True:
    for i in range(0, 400, 5):
        screen.create_rectangle(150+i, 250, 350, 450, fill="lime", width=2)
        window.update()
        screen.create_rectangle(150+i, 250, 350, 450, fill="white", width=2, outline="white")
    for i in range(400, 0, -5):
        screen.create_rectangle(150+i, 250, 350, 450, fill="lime", width=2)
        window.update()
        screen.create_rectangle(150+i, 250, 350, 450, fill="white", width=2, outline="white")
