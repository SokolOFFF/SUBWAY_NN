from tkinter import *

root = Tk()
root.title("СОКОЛОВ МЕТРО. Навигация по Нижегородскому метрополитену в 2040 году")
root.geometry('1920x1080')


canvas=Canvas()

canvas.create_line(1500, 0, 1500, 1080, fill="black", width=5)

#LINES BETWEEN STATIONS
canvas.create_line(20, 20, 140, 120, fill="blue", width=13)
canvas.create_line(140, 120, 200, 190, fill="blue", width=13)
canvas.create_line(280, 260, 200, 190, fill="blue", width=13)
canvas.create_line(280, 260, 340, 320, fill="blue", width=13)
canvas.create_line(460, 350, 350, 330, fill="blue", width=13)
canvas.create_line(460, 350, 700, 378, fill="blue", width=13)
canvas.create_line(700, 388, 800, 320, fill="blue", width=13)
canvas.create_line(800, 305, 920, 365, fill="blue", width=13)
canvas.create_line(925, 365, 965, 450, fill="blue", width=13)
canvas.create_line(1060, 550, 955, 450, fill="blue", width=13)

canvas.create_line(456, 340, 407, 200,  fill="palevioletred", width=13)
canvas.create_line(463, 340, 445, 430,  fill="palevioletred", width=13)
canvas.create_line(421, 520, 445, 430,  fill="palevioletred", width=13)
canvas.create_line(421, 520, 395, 600,  fill="palevioletred", width=13)
canvas.create_line(348, 680, 395, 600,  fill="palevioletred", width=13)
canvas.create_line(348, 680, 305, 760,  fill="palevioletred", width=13)
canvas.create_line(275, 830, 310, 760,  fill="palevioletred", width=13)
canvas.create_line(280, 830, 230, 900,  fill="palevioletred", width=13)
canvas.create_line(520, 960, 230, 913,  fill="palevioletred", width=13)

canvas.create_line(520, 975, 600, 900,  fill="mediumseagreen", width=13)
canvas.create_line(655, 770, 610, 900,  fill="mediumseagreen", width=13)
canvas.create_line(655, 770, 695, 670, fill="mediumseagreen", width=13)
canvas.create_line(720, 580, 695, 670, fill="mediumseagreen", width=13)
canvas.create_line(710, 485, 715, 580,  fill="mediumseagreen", width=13)
canvas.create_line(710, 485, 710, 370,  fill="mediumseagreen", width=13)
canvas.create_line(705, 595, 960, 465,  fill="mediumseagreen", width=13)

canvas.create_line(152, 120, 123, 220,  fill="gray", width=13)
canvas.create_line(120, 220, 130, 360,  fill="gray", width=13)
canvas.create_line(140, 480, 130, 360,  fill="gray", width=13)
canvas.create_line(135, 480, 165, 580,  fill="gray", width=13)
canvas.create_line(206, 680, 165, 580,  fill="gray", width=13)
canvas.create_line(206, 690, 290, 760,  fill="gray", width=13)
canvas.create_line(290, 760, 380, 850, fill="gray", width=13)
canvas.create_line(600, 890, 380, 860, fill="gray", width=13)

qui = Button(canvas, text="QUIT", width = 20, bg = "gray", height = 3)

def exi(event):
    sys.exit()

qui.bind('<Button-1>', exi)
qui.place(x=1650, y=700)

class Best_Button:

    def __init__(self, x, y, f, color1, color2):
        self.x = x
        self.y = y
        self.f = f
        self.c1 = color1
        self.c2 = color2
        self.b = Button (root, text = "  ", bg = "green", activebackground="green", relief = "flat", state = "disabled")
        if self.f == 1:
            self.b["bg"]="orange"
        if self.f == 0:
            self.b["bg"]=self.c1
        self.b.bind('<Button-1>', self.change)
        self.b.place(x = self.x+3, y = self.y)
        if self.f == 0:
            canvas.create_oval(self.x - 7, self.y - 7, self.x + 30, self.y + 30, outline=self.c2,
                           fill=self.c1, width=5)
        if self.f == 1:
            canvas.create_oval(self.x - 7, self.y - 7, self.x + 30, self.y + 30, outline=self.c2,
                               fill="orange", width=5)
    def change(self, event):
        if self.f == 0:
            canvas.create_oval(self.x-7, self.y-7, self.x+30, self.y+30, outline=self.c2,
                               fill="orange", width=5)
            self.b["bg"]="orange"
            self.f=1
            self.b.place(x=self.x+3, y=self.y)
            return 0

        if self.f == 1:
            canvas.create_oval(self.x-7, self.y-7, self.x+30, self.y+30, outline=self.c2,
                                fill=self.c1, width=5)
            self.b["bg"] = self.c1
            self.f = 0
            self.b.place(x=self.x+3, y=self.y)

#blue line
s1 = Best_Button (20, 20, 0,  "white", "blue")
s2 = Best_Button (140, 120, 0, "gray","blue")
s3 = Best_Button (200, 190, 0, "white","blue")
s4 = Best_Button (280, 260, 0, "white","blue")
s5 = Best_Button (340, 320, 0, "white","blue")
s6 = Best_Button (450, 340, 0, "palevioletred","blue")
s7 = Best_Button (700, 370, 0, "mediumseagreen","blue")
s8 = Best_Button (800, 300, 0, "white","blue")
s9 = Best_Button (920, 360, 0, "white","blue")
s10 = Best_Button (960, 450, 0, "mediumseagreen","blue")
s11 = Best_Button (1060, 550, 0, "white","blue")

#red line
s12 = Best_Button (400, 200, 0, "white","palevioletred")
s13 = Best_Button (430, 430, 0, "white","palevioletred")
s14 = Best_Button (405, 520, 0, "white","palevioletred")
s15 = Best_Button (380, 600, 0, "white","palevioletred")
s16 = Best_Button (330, 680, 0, "white","palevioletred")
s17 = Best_Button (290, 760, 0, "gray","palevioletred")
s18 = Best_Button (260, 830, 0, "white","palevioletred")
s19 = Best_Button (210, 900, 0, "white","palevioletred")

#black line
s20 = Best_Button (110, 220, 0, "white", "gray")
s21 = Best_Button (120, 360, 0, "white", "gray")
s22 = Best_Button (130, 480, 0, "white", "gray")
s23 = Best_Button (160, 580, 0, "white", "gray")
s24 = Best_Button (200, 680, 0, "white", "gray")
s25 = Best_Button (380, 850, 0, "white", "gray")
s26 = Best_Button (600, 880, 0, "gray", "mediumseagreen")

#green line
s27 = Best_Button (520, 950, 0, "palevioletred", "mediumseagreen")
s28 = Best_Button (640, 770, 0, "white", "mediumseagreen")
s29 = Best_Button (680, 670, 0, "white", "mediumseagreen")
s30 = Best_Button (705, 580, 0, "blue", "mediumseagreen")
s31 = Best_Button (700, 485, 0, "white", "mediumseagreen")

canvas.pack(fill=BOTH, expand=1)
root.mainloop()
