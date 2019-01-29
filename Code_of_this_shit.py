from tkinter import *

root = Tk()
root.title("СОКОЛОВ МЕТРО. Навигация по Нижегородскому метрополитену в 2040 году")
root.geometry('1920x1080')



station_name = [""] * 32
station_name[1]="Сормовская"
station_name[2]="Спортивная"
station_name[3]="Калининская"
station_name[4]="Куйбышевская"
station_name[5]="Канавинская"
station_name[6]="Московская"
station_name[7]="Горьковская"
station_name[8]="Свердловская"
station_name[9]="Площать Свободы"
station_name[10]="Республиканская"
station_name[11]="Советская"
station_name[12]="Мещерская"
station_name[13]="Чкаловская"
station_name[14]="Ленинская"
station_name[15]="Заречная"
station_name[16]="Двигатель Революции"
station_name[17]="Пролетарская"
station_name[18]="Северная"
station_name[19]="Комсомольская"
station_name[20]="Красные Зори"
station_name[21]="Индустриальная"
station_name[22]="Первомайская"
station_name[23]="Дзержинская"
station_name[24]="Магистральная"
station_name[25]="Бауманская"
station_name[26]="Сельхозинститут"
station_name[27]="Щербинская"
station_name[28]="Мыза"
station_name[29]="Приокская"
station_name[30]="Дворец Спорта"
station_name[31]="Университет"


ver = [[0, 156,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [156, 0, 92,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,104,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1, 92, 0,106,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1, -1,106,0, 92,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1, -1,-1,92,0,111,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1, -1,-1,-1,111,0,372,-1,-1,-1,-1,228,92,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1, -1,-1,-1,-1,372,0,116,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,110],
       [-1, -1,-1,-1,-1,-1,116,0,134,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1, -1,-1,-1,-1,-1,-1,134,0,96,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1, -1,-1,-1,-1,-1,-1,-1,96,0,141,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,269,-1],
       [-1, -1,-1,-1,-1,-1,-1,-1,-1,141,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1, -1,-1,-1,-1,228,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1, -1,-1,-1,-1,92,-1,-1,-1,-1,-1,-1,0,92,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,92,0,121,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,121,0,94,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,94,0,100,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,100,0,80,-1,-1,-1,-1,-1,114,127,-1,-1,-1,-1,-1,-1],
       [-1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,80,0,86,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,86,0,-1,-1,-1,-1,-1,-1,-1,304,-1,-1,-1,-1],
       [-1, 104,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,140,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,140,0,120,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,120,0,104,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,104,0,107,-1,-1,-1,-1,-1,-1,-1],
       [-1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,114,-1,-1,-1,-1,-1,107,0,-1,-1,-1,-1,-1,-1,-1],
       [-1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,127,-1,-1,-1,-1,-1,-1,-1,0,222,-1,-1,-1,-1,-1],
       [-1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,222,0,106,136,-1,-1,-1],
       [-1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,304,-1,-1,-1,-1,-1,-1,106,0,-1,-1,-1,-1],
       [-1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,136,-1,0,107,-1,-1],
       [-1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,107,0,192,-1],
       [-1, -1,-1,-1,-1,-1,-1,-1,-1,269,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,192,0,100],
       [-1, -1,-1,-1,-1,-1,110,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,100,0]]



canvas=Canvas()

canvas.create_text(105, 13, text="Сормовская",
                 font="fangsongti  14")
canvas.create_text(220, 110, text="Спортивная",
                 font="fangsongti  14")
canvas.create_text(290, 180, text="Калининская",
                 font="fangsongti  14")
canvas.create_text(350, 240, text="Куйбышевская",
                 font="fangsongti  14")
canvas.create_text(360, 360, text="Канавинская",
                 font="fangsongti  14")
canvas.create_text(530, 310, text="Московская",
                 font="fangsongti  14")
canvas.create_text(700, 330, text="Горьковская",
                 font="fangsongti  14")
canvas.create_text(810, 270, text="Свердловская",
                 font="fangsongti  14")
canvas.create_text(1000, 350, text="Площадь\nСвободы",
                 font="fangsongti  14", justify = "left")
canvas.create_text(870, 440, text="Республиканская",
                 font="fangsongti  14")
canvas.create_text(1000, 566, text="Советская",
                 font="fangsongti  14")
canvas.create_text(485, 196, text="Мещерская",
                 font="fangsongti  14")
canvas.create_text(520, 440, text="Чкаловская",
                 font="fangsongti  14")
canvas.create_text(490, 535, text="Ленинская",
                 font="fangsongti  14")
canvas.create_text(465, 615, text="Заречная",
                 font="fangsongti  14")
canvas.create_text(430, 690, text="  Двигатель \n Революции",
                 font="fangsongti  14")
canvas.create_text(390, 760, text="Пролетарская",
                 font="fangsongti  14")
canvas.create_text(205, 820, text="Северная",
                 font="fangsongti  14")
canvas.create_text(125, 895, text="Комсомольская",
                 font="fangsongti  14")
canvas.create_text(189, 240, text="Красные \n Зори",
                 font="fangsongti  14")
canvas.create_text(230, 390, text="Индустриальная",
                 font="fangsongti  14")
canvas.create_text(230, 490, text="Первомайская",
                 font="fangsongti  14")
canvas.create_text(260, 590, text="Дзержинская",
                 font="fangsongti  14")
canvas.create_text(280, 655, text="Магистральная",
                 font="fangsongti  14")
canvas.create_text(460, 825, text="Бауманская",
                 font="fangsongti  14")
canvas.create_text(720, 890, text="Сельхозинститут",
                 font="fangsongti  14")
canvas.create_text(620, 970, text="Щербинская",
                 font="fangsongti  14")
canvas.create_text(705, 790, text="Мыза",
                 font="fangsongti  14")
canvas.create_text(765, 680, text="Приокское",
                 font="fangsongti  14")
canvas.create_text(785, 610, text="Дворец \n спорта",
                 font="fangsongti  14")
canvas.create_text(795, 490, text="Университет",
                 font="fangsongti  14")





canvas.create_line(1500, 0, 1500, 1080, fill="black", width=5)
canvas.create_line(1100, 0, 1100, 1080, fill="black", width=5)

label1 = Label (root, text = "", bg = "lightblue", width = 31, font = "Arial 15" , fg = "navy")
label1.place(x = 1530, y = 100)

label2 = Label (root, text = "", width = 20,  font = "Arial 20", bg = "lightblue", fg = "navy")
label2.place (x = 1140, y = 100)

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


lines = [[None for i in range(50)] for j in range(50)]

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
lines[6][13] = Lines (463, 340, 445, 430, "palevioletred", 13)
lines[6][13].draw()
lines[13][6] = Lines (463, 340, 445, 430, "palevioletred", 13)
lines[13][6].draw()
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
lines[30][10] = Lines(705,595,960,465,  "mediumseagreen", 13)
lines[30][10].draw()
lines[10][30] = Lines(705,595,960,465,  "mediumseagreen", 13)
lines[10][30].draw()

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

Quit = Button(canvas, text="QUIT", width = 20, bg = "tan", height = 3)

def exi(event):
    sys.exit()

Quit.bind('<Button-1>', exi)
Quit.place(x=1650, y=900)


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

Start = Button(canvas, text="START", width = 20, bg = "tan", height = 3, activebackground = "tan")

def start(event):
    global count_of_flags
    global ver
    pp = []
    report = [0]*31
    length = [[1000000 for i in range(2)] for j in range(31)]
    for i in range(31):
        length[i][1]=-1
    if count_of_flags < 2:
        label1['text']="I can't do it"
        return 0
    if count_of_flags == 2:
        label1['text']=""
        for i in range(32):
            if s[i].f==1:
                pp.append(i)
        #print(*pp)
        be = pp[0]-1
        en = pp[1]-1
        length[be][0]=0
        length[be][1]=be
        report[be]=1
        for i in range(31):
            if ver[be][i]>0:
                length[i][0]=min(length[i][0], length[be][0]+ver[be][i])
                length[i][1]=be

        while (1!=0):
            minn=10000000
            v = -12312
            for i in range(31):
                if length[i][0]<minn and report[i]==0:
                    minn = length[i][0]
                    v = i
            if minn == 10000000:
                break

            for i in range(31):
                if report[i]==0 and i != v and ver[v][i] > 0:
                    if length[i][0] > length[v][0]+ver[v][i]:
                        length[i][0] = length[v][0]+ver[v][i]
                        length[i][1] = v
            report[v]=1

        q=[]
        q.append(en+1)
        p = en
        while length[p][1] != be:
            q.append(length[p][1]+1)
            p=length[p][1]
        q.append(be+1)
        for i in range(len(q)-1):
            lines[q[i]][q[i+1]].__init__(lines[q[i]][q[i+1]].x1, lines[q[i]][q[i+1]].y1, lines[q[i]][q[i+1]].x2, lines[q[i]][q[i+1]].y2, "orange", 13)
            lines[q[i]][q[i + 1]].draw()
        for i in q:
            s[i].__init__(s[i].x, s[i].y, s[i].f, "orange", "black")
        def show(event):
            label2["text"]=""
            for i in q:
                label2["text"] += station_name[i]
                label2["text"] += "\n"
        show_name = Button(canvas, text="SHOW", width = 20, bg = "tan", height = 3, activebackground = "tan")
        show_name.bind('<Button-1>', show)
        show_name.place(x = 1650, y = 760)



Start.bind('<Button-1>', start)
Start.place(x=1650, y = 830)

canvas.pack(fill=BOTH, expand=1)
root.mainloop()
