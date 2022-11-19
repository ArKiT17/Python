from tkinter import *
import time

window = Tk()
window.title("Півень")
screen = Canvas(window, width=700, height=700, bg='white')
screen.pack()

screen.create_oval(218, 25, 336, 142, width=5, fill="#be112d")
screen.create_oval(327, 60, 445, 179, width=5, fill="#be112d")
screen.create_oval(386, 160, 504, 276, width=5, fill="#be112d")

screen.create_polygon(195, 180, 121, 116, 158, 228, 132, 337, 184, 278, width=5, outline="black", fill="red")

screen.create_oval(173, 140, 391, 355, width=5, fill="#eaec1a")
screen.create_oval(220, 184, 305, 267, width=5, fill="white")
screen.create_oval(245, 207, 280, 242, width=5, fill="black")

screen.create_polygon(287, 356, 398, 467, 287, 578, 176, 467, width=5, outline="black", fill="#eaec1a")
screen.create_polygon(287, 578, 340, 675, 234, 675, width=5, outline="black", fill="#d2d42c")
screen.create_arc(379, 307, 579, 507, start=36, extent=180, width=5, fill="#d2d42c")
screen.create_arc(398, 370, 610, 560, start=0, extent=180, width=5, fill="#d2d42c")
screen.create_arc(386, 412, 582, 623, start=-30, extent=180, width=5, fill="#d2d42c")

for a in range(45):   #від початку до правого кінця
    for i in range(1, 13):
        screen.move(i, 2, 0)
        window.update()
    time.sleep(0.00005)

while True :
    for a in range(105):
        for i in range(1, 13):
            screen.move(i, -2, 0)
            window.update()
    time.sleep(0.00005)
    
    for a in range(105):
        for i in range(1, 13):
            screen.move(i, 2, 0)
            window.update()
    time.sleep(0.00005)

