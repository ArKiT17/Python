from tkinter import *
import random

window = Tk()
window.title("Завдання 16. Додаткове")

screen = Canvas(window, width=1000, height=750, bg="white")
screen.pack()

fill = PhotoImage(file="fill.gif")
animal_pig = PhotoImage(file="pig.gif")
animal_sheep = PhotoImage(file="sheep.gif")
animal_cow = PhotoImage(file="cow.gif")
animal_horse = PhotoImage(file="horse.gif")

screen.create_image(0, 0, anchor=NW, image=fill)
pig = screen.create_image(-500, 0, anchor=S, image=animal_pig)
sheep = screen.create_image(-500, 0, anchor=S, image=animal_sheep)
cow = screen.create_image(-500, 0, anchor=S, image=animal_cow)
horse = screen.create_image(-500, 0, anchor=SW, image=animal_horse)

animals = [pig, sheep, cow, horse]
speed = 2
while True:
    index = random.randint(0, 3)
    if index == 0:
        speed = 4
        screen.coords(animals[index], -200, 570)
    elif index == 1:
        speed = 3
        screen.coords(animals[index], -200, 570)
    elif index == 2:
        speed = 2
        screen.coords(animals[index], -200, 540)
    elif index == 3:
        speed = 3
        screen.coords(animals[index], -350, 560)
        
    for i in range(int(690/speed)):
        screen.move(animals[index], speed, 0.27)
        window.update()
        screen.after(1)
    for i in range(int(690/speed)):
        screen.move(animals[index], speed, -0.27)
        window.update()
        screen.after(1)
