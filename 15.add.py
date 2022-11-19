from tkinter import *

window = Tk()
window.title("Завдання 15. Додаткове")
screen = Canvas(window, width=700, height=700, bg="cyan")
screen.pack()

for i in range(71):
    screen.create_line(i*10, 0, 700-i*10, 700, fill="orange")
    screen.create_line(0, i*10, 700, 700-i*10, fill="red")
