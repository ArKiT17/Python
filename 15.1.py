from tkinter import *

window = Tk()
window.title("Завдання 15.1")
screen = Canvas(window, width=700, height=700, bg='white')
screen.pack()

screen.create_text(500, 30, text="Лікаренко Максим КН21Б", font=('', 20))
screen.create_text(350, 10, text="Лікаренко Максим КН21Б", anchor=N)
screen.create_text(440, 660, text="Курчатко", font=('', 20))
screen.create_text(350, 695, text="Курчатко", anchor=S)
#по центру не помістилося, було маленьке

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
