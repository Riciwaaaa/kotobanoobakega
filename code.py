import simplegui

music = simplegui.load_sound("https://riciwaaaa.github.io/schoolstuff/music.mp3")
is_preloaded = False

colors={
    "yellow":"RGB(235, 223, 199)",
    "dyellow":"RGB(195, 171, 140)",
    "brown":"RGB(105, 96, 73)",
    "dbrown":"RGB(75, 65, 57)",
    "green":"RGB(117, 165, 80)",
    "dgreen":"RGB(46, 104, 37)",
    "blue":"RGB(117, 158, 188)",
    "dblue":"RGB(58, 92, 117)",
}

mouth_shapes={
    "a": [(345,383),(375,383),(378,400),(342,400)],
    "i": [(340,385),(380,385),(380,392),(340,392)],
    "u": [(360,380),(370,400),(350,400)],
    "e": [(343,384),(377,384),(380,394),(340,394)],
    "o": [(348,383),(372,383),(372,400),(348,400)],
    " ": [(340,392),(380,392),(340,392)],
}

mouth_sequence1="-"*64+"a-i-u-e-o- -a-a-e-i"
mouth_sequence2="-"*64+"o-u-e- -e-i-u-a-i-e"
index=0
mouth1=" "
mouth2=" "

def update():
    global index, mouth1, mouth2
    char1 = mouth_sequence1[index]
    char2 = mouth_sequence2[index]

    if char1 != "-":
        mouth1 = char1
    if char2 != "-":
        mouth2 = char2

    index = (index + 1) % max(len(mouth_sequence1), len(mouth_sequence2))

def draw_mouth(canvas,char,i):
    if char in mouth_shapes:
        points= [(x+i,y) for (x,y) in mouth_shapes[char]]
        canvas.draw_polygon(points,5,colors["dgreen"],colors["green"])    
    
def dummy_handler(): #Load music.
    pass

def preload_music():  
    global is_preloaded
    if not is_preloaded:
        music.set_volume(0.0)
        music.play()
        preload_timer = simplegui.create_timer(500, dummy_handler)
        preload_timer.start()
        is_preloaded = True
        print("Music preloaded")

def play_music():
    music.set_volume(1.0)
    music.play()
    print("Music playing")
    
    
def draw_handler(canvas):
    def draw_character(i):
        #back hair
        canvas.draw_polygon([(435+i,125),(470+i,120),(490+i,60),(560+i,30),(635+i,95),(665+i,190),(610+i,240),(570+i,245),(545+i,275)],1,colors["dgreen"],colors["dgreen"])
        canvas.draw_polygon([(560+i,215),(575+i,160),(640+i,165),(620+i,215)],1,colors["yellow"],colors["yellow"])
        canvas.draw_polygon([(220+i,330),(500+i,330),(500+i,415),(360+i,470),(220+i,415)],1,colors["dbrown"],colors["dbrown"])
        #head
        canvas.draw_circle((360+i,280),130,8,colors["dyellow"],colors["yellow"])
        canvas.draw_polygon([(205+i,250),(205+i,370),(115+i,310)],1,colors["dyellow"],colors["dyellow"])
        canvas.draw_polygon([(515+i,250),(515+i,370),(605+i,310)],1,colors["dyellow"],colors["dyellow"])
        #body
        canvas.draw_polygon([(260+i,480),(120+i,570),(115+i,730),(605+i,730),(600+i,570),(460+i,480)],8,colors["dbrown"],colors["brown"])
        canvas.draw_polygon([(285+i,415),(205+i,405),(195+i,495),(285+i,510),(195+i,495),(115+i,570),(150+i,680),(290+i,670)],8,colors["dbrown"],colors["brown"])
        canvas.draw_polygon([(435+i,415),(515+i,405),(525+i,495),(435+i,510),(525+i,495),(605+i,570),(570+i,680),(430+i,670)],8,colors["dbrown"],colors["brown"])
        canvas.draw_polygon([(285+i,415),(285+i,510),(435+i,510),(435+i,415)],8,colors["dbrown"],colors["brown"])
        canvas.draw_polygon([(250+i,565),(250+i,600),(470+i,600),(470+i,565)],8,colors["dyellow"],colors["yellow"])
        #face
        canvas.draw_polygon([(240+i,240),(275+i,195),(335+i,195),(353+i,218),(350+i,245),(320+i,265),(240+i,265)],8,colors["dgreen"],colors["green"])
        canvas.draw_polygon([(480+i,240), (445+i,195), (385+i,195), (367+i,218), (370+i,245), (400+i,265), (480+i,265)],8,colors["dgreen"],colors["green"])
        canvas.draw_polygon([(280+i,105),(195+i,175),(155+i,400),(190+i,465),(235+i,465),(260+i,385),(240+i,240),(275+i,195),(445+i,195), (480+i,240), (460+i,385), (485+i,465), (530+i,465), (565+i,400), (525+i,175), (440+i,105)],8,colors["dgreen"],colors["green"])
        canvas.draw_circle((285+i,292),35,8,colors["dblue"],colors["blue"])
        canvas.draw_circle((285+i,292),20,5,colors["dblue"],colors["dblue"])
        canvas.draw_circle((435+i,292),35,8,colors["dblue"],colors["blue"])
        canvas.draw_circle((435+i,292),20,5,colors["dblue"],colors["dblue"])
        canvas.draw_line((330+i,300),(390+i,300),8,"black")
        canvas.draw_polygon([(235+i,255),(320+i,253),(330+i,285),(235+i,287)],1,"black","black")
        canvas.draw_polygon([(485+i,255), (400+i,253), (390+i,285), (485+i,287)],1,"black","black")

        
    draw_character(-340)
    draw_character(340)
    
    draw_mouth(canvas, mouth1, -340)
    canvas.draw_text(mouth1.upper(), (320, 360), 40, "black")

    draw_mouth(canvas, mouth2, 340)
    canvas.draw_text(mouth2.upper(), (380, 360), 40, "black")
    
    
frame = simplegui.create_frame("Words", 720, 720)
frame.set_canvas_background(colors["yellow"])
frame.set_draw_handler(draw_handler)

timer = simplegui.create_timer(188, update)
timer.start()
preload_music()
frame.start()
play_music()
