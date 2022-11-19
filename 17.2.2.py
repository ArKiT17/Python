from tkinter import *
from random import randint, randrange

window = Tk()
window.title("17.1.2")
screen = Canvas(window, width=700, height=700, bg="white")
screen.pack()

colors = ['lime', 'green', 'red', 'orange', 'blue', 'light blue', 'yellow', 'purple', 'white', 'light gray', 'cyan']
f = True

while f == True:
    centerx = randint(30, 640)
    centery = randint(30, 640)
    radius = randint(30, 60)
    color = randint(0, 10)
#    color = "#" + "".join("{:02x}".format(randrange(256)) for x in range(3))
    screen.create_oval(centerx, centery, centerx+radius, centery+radius, fill=colors[color])
    window.update()
    print(colors[color])
    if colors[color] == 'orange' and radius > 50:
        f = False
