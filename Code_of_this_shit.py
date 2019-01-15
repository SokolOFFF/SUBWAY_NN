from tkinter import *

root = Tk()
root.title("СОКОЛОВ МЕТРО. Навигация по Нижегородскому метрополитену в 2040 году")
root.geometry('1920x1080')


canvas=Canvas()

canvas.create_line(1500, 0, 1500, 1080, fill="black", width=5)
canvas.create_line(1100, 0, 1100, 1080, fill="black", width=5)

label1 = Label (root, text = "", bg = "lightblue", width = 31, font = "Arial 15")
label1.place(x = 1530, y = 100)

label2 = Label (root, text = "", width = 35, height = 53, font = "Arial 10")
label2.place (x = 1150, y = 100)

#LINES BETWEEN STATIONS

class Lines:
    def __init__(self, x1, y1, x2, y2, color, wid):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.wid = wid
    def draw(self):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.color, width=self.wid)


lines = [[None for i in range(50)] for j in range (50)]

#blue line
lines[1][2] = Lines(20, 20, 140, 120, "blue", 13)
lines[1][2].draw()
lines[2][1] = Lines(20, 20, 140, 120, "blue", 13)
lines[2][1].draw()
lines[2][3] = Lines(140, 120, 200, 190, "blue", 13)
lines[2][3].draw()
lines[3][2] = Lines(140, 120, 200, 190, "blue", 13)
lines[3][2].draw()
lines[3][4] = Lines(280, 260, 200, 190, "blue", 13)
lines[3][4].draw()
lines[4][3] = Lines(280, 260, 200, 190, "blue", 13)
lines[4][3].draw()
lines[4][5] = Lines(280, 260, 340, 320, "blue", 13)
lines[4][5].draw()
lines[5][4] = Lines(280, 260, 340, 320, "blue", 13)
lines[5][4].draw()
lines[5][6] = Lines(460, 350, 350, 330, "blue", 13)
lines[5][6].draw()
lines[6][5] = Lines(460, 350, 350, 330, "blue", 13)
lines[6][5].draw()
lines[6][7] = Lines(460, 350, 700, 378, "blue", 13)
lines[6][7].draw()
lines[7][6] = Lines(460, 350, 700, 378, "blue", 13)
lines[7][6].draw()
lines[7][8] = Lines(700, 388, 800, 320, "blue", 13)
lines[7][8].draw()
lines[8][7] = Lines(700, 388, 800, 320, "blue", 13)
lines[8][7].draw()
lines[8][9] = Lines(800, 305, 920, 365, "blue", 13)
lines[8][9].draw()
lines[9][8] = Lines(800, 305, 920, 365, "blue", 13)
lines[9][8].draw()
lines[9][10] = Lines(925, 365, 965, 450, "blue", 13)
lines[9][10].draw()
lines[10][9] = Lines(925, 365, 965, 450, "blue", 13)
lines[10][9].draw()
lines[10][11] = Lines(1060, 550, 955, 450, "blue", 13)
lines[10][11].draw()
lines[11][10] = Lines(1060, 550, 955, 450, "blue", 13)
lines[11][10].draw()

#red line
lines[12][6] = Lines (456, 340, 407, 200, "palevioletred", 13)
lines[12][6].draw()
lines[6][12] = Lines (456, 340, 407, 200, "palevioletred", 13)
lines[6][12].draw()
lines[12][13] = Lines (463, 340, 445, 430, "palevioletred", 13)
lines[12][13].draw()
lines[13][12] = Lines (463, 340, 445, 430, "palevioletred", 13)
lines[13][12].draw()
lines[13][14] = Lines (421, 520, 445, 430, "palevioletred", 13)
lines[13][14].draw()
lines[14][13] = Lines (421, 520, 445, 430, "palevioletred", 13)
lines[14][13].draw()
lines[14][15] = Lines (421, 520, 395, 600, "palevioletred", 13)
lines[14][15].draw()
lines[15][14] = Lines (421, 520, 395, 600, "palevioletred", 13)
lines[15][14].draw()
lines[15][16] = Lines (348, 680, 395, 600, "palevioletred", 13)
lines[15][16].draw()
lines[16][15] = Lines (348, 680, 395, 600, "palevioletred", 13)
lines[16][15].draw()
lines[16][17] = Lines (348, 680, 305, 760, "palevioletred", 13)
lines[16][17].draw()
lines[17][16] = Lines (348, 680, 305, 760, "palevioletred", 13)
lines[17][16].draw()
lines[17][18] = Lines (275, 830, 310, 760, "palevioletred", 13)
lines[17][18].draw()
lines[18][17] = Lines (275, 830, 310, 760, "palevioletred", 13)
lines[18][17].draw()
lines[18][19] = Lines (280, 830, 230, 900, "palevioletred", 13)
lines[18][19].draw()
lines[19][18] = Lines (280, 830, 230, 900, "palevioletred", 13)
lines[19][18].draw()
lines[19][27] = Lines (520, 960, 230, 913, "palevioletred", 13)
lines[19][27].draw()
lines[27][19] = Lines (520, 960, 230, 913, "palevioletred", 13)
lines[27][19].draw()

#green line
lines[27][26] = Lines (520, 975, 600, 900, "mediumseagreen", 13)
lines[27][26].draw()
lines[26][27] = Lines (520, 975, 600, 900, "mediumseagreen", 13)
lines[26][27].draw()
lines[26][28] = Lines (655, 770, 610, 900, "mediumseagreen", 13)
lines[26][28].draw()
lines[28][26] = Lines (655, 770, 610, 900, "mediumseagreen", 13)
lines[28][26].draw()
lines[28][29] = Lines (655, 770, 695, 670, "mediumseagreen", 13)
lines[28][29].draw()
lines[29][28] = Lines (655, 770, 695, 670, "mediumseagreen", 13)
lines[29][28].draw()
lines[29][30] = Lines (720, 580, 695, 670, "mediumseagreen", 13)
lines[29][30].draw()
lines[30][29] = Lines (720, 580, 695, 670, "mediumseagreen", 13)
lines[30][29].draw()
lines[30][31] = Lines (710, 485, 715, 580, "mediumseagreen", 13)
lines[30][31].draw()
lines[31][30] = Lines (710, 485, 715, 580, "mediumseagreen", 13)
lines[31][30].draw()
lines[31][7] = Lines (710, 485, 710, 370, "mediumseagreen", 13)
lines[31][7].draw()
lines[7][31] = Lines (710, 485, 710, 370, "mediumseagreen", 13)
lines[7][31].draw()
lines[31][10] = Lines(705,595,960,465,  "mediumseagreen", 13)
lines[31][10].draw()
lines[10][31] = Lines(705,595,960,465,  "mediumseagreen", 13)
lines[10][31].draw()

#black line
lines[2][20] = Lines(152,120,123,220,  "gray", 13)
lines[2][20].draw()
lines[20][2] = Lines(152,120,123,220,  "gray", 13)
lines[20][2].draw()
lines[20][21] = Lines(130,360,120,220,  "gray", 13)
lines[20][21].draw()
lines[21][20] = Lines(130,360,120,220,  "gray", 13)
lines[21][20].draw()
lines[21][22] = Lines(140,480,130,360,  "gray", 13)
lines[21][22].draw()
lines[22][21] = Lines(140,480,130,360,  "gray", 13)
lines[22][21].draw()
lines[22][23] = Lines(135,480,165,580,  "gray", 13)
lines[22][23].draw()
lines[23][22] = Lines(135,480,165,580,  "gray", 13)
lines[23][22].draw()
lines[23][24] = Lines(206,680,165,580,  "gray", 13)
lines[23][24].draw()
lines[24][23] = Lines(206,680,165,580,  "gray", 13)
lines[24][23].draw()
lines[17][24] = Lines(206,690,290,760,  "gray", 13)
lines[17][24].draw()
lines[24][17] = Lines(206,690,290,760,  "gray", 13)
lines[24][17].draw()
lines[17][25] = Lines(290,760,380,850,  "gray", 13)
lines[17][25].draw()
lines[25][17] = Lines(290,760,380,850,  "gray", 13)
lines[25][17].draw()
lines[26][25] = Lines(600,890,380,860,  "gray", 13)
lines[26][25].draw()
lines[25][26] = Lines(600,890,380,860,  "gray", 13)
lines[25][26].draw()

qui = Button(canvas, text="QUIT", width = 20, bg = "tan", height = 3)

def exi(event):
    sys.exit()

qui.bind('<Button-1>', exi)
qui.place(x=1650, y=900)


count_of_flags=0

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
        global count_of_flags
        if self.f == 0:
            count_of_flags+=1
            if count_of_flags>2:
                label1['text']="You can't choose more, than 2 stations"
                count_of_flags-=1
                return 0
            else:
                canvas.create_oval(self.x-7, self.y-7, self.x+30, self.y+30, outline=self.c2,
                                   fill="orange", width=5)
                self.b["bg"]="orange"
                self.f=1
                self.b.place(x=self.x+3, y=self.y)
                return 0

        if self.f == 1:
            count_of_flags-=1
            if count_of_flags<2:
                label1['text']=""
            canvas.create_oval(self.x-7, self.y-7, self.x+30, self.y+30, outline=self.c2,
                                fill=self.c1, width=5)
            self.b["bg"] = self.c1
            self.f = 0
            self.b.place(x=self.x+3, y=self.y)


s=[Best_Button(20,20,0,"white", "black")]*32

#blue line
s[1] = Best_Button (20, 20, 0,  "white", "blue")
s[2] = Best_Button (140, 120, 0, "gray","blue")
s[3] = Best_Button (200, 190, 0, "white","blue")
s[4] = Best_Button (280, 260, 0, "white","blue")
s[5] = Best_Button (340, 320, 0, "white","blue")
s[6] = Best_Button (450, 340, 0, "palevioletred","blue")
s[7] = Best_Button (700, 370, 0, "mediumseagreen","blue")
s[8] = Best_Button (800, 300, 0, "white","blue")
s[9] = Best_Button (920, 360, 0, "white","blue")
s[10] = Best_Button (960, 450, 0, "mediumseagreen","blue")
s[11] = Best_Button (1060, 550, 0, "white","blue")

#red line
s[12]= Best_Button (400, 200, 0, "white","palevioletred")
s[13] = Best_Button (430, 430, 0, "white","palevioletred")
s[14] = Best_Button (405, 520, 0, "white","palevioletred")
s[15] = Best_Button (380, 600, 0, "white","palevioletred")
s[16] = Best_Button (330, 680, 0, "white","palevioletred")
s[17] = Best_Button (290, 760, 0, "gray","palevioletred")
s[18] = Best_Button (260, 830, 0, "white","palevioletred")
s[19] = Best_Button (210, 900, 0, "white","palevioletred")

#black line
s[20] = Best_Button (110, 220, 0, "white", "gray")
s[21] = Best_Button (120, 360, 0, "white", "gray")
s[22] = Best_Button (130, 480, 0, "white", "gray")
s[23] = Best_Button (160, 580, 0, "white", "gray")
s[24] = Best_Button (200, 680, 0, "white", "gray")
s[25] = Best_Button (380, 850, 0, "white", "gray")
s[26] = Best_Button (600, 880, 0, "gray", "mediumseagreen")

#green line
s[27] = Best_Button (520, 950, 0, "palevioletred", "mediumseagreen")
s[28] = Best_Button (640, 770, 0, "white", "mediumseagreen")
s[29] = Best_Button (680, 670, 0, "white", "mediumseagreen")
s[30] = Best_Button (705, 580, 0, "blue", "mediumseagreen")
s[31] = Best_Button (700, 485, 0, "white", "mediumseagreen")

canvas.pack(fill=BOTH, expand=1)
root.mainloop()
