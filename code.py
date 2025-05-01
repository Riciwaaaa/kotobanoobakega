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

mouth_shapes = {
    "a": [(345,383),(375,383),(380,400),(340,400)],
    "i": [(340,385),(380,385),(380,392),(340,392)],
    "u": [(360,380),(370,400),(350,400)],
    "e": [(343,385),(377,385),(380,394),(340,394)],
    "o": [(345,383),(375,383),(375,400),(345,400)],
    "m": [(340,392),(380,392),(340,392)],
}

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
    #back hair
    canvas.draw_polygon([(435,125),(470,120),(490,60),(560,30),(635,95),(665,190),(610,240),(570,245),(545,275)],1,colors["dgreen"],colors["dgreen"])
    canvas.draw_polygon([(560,215),(575,160),(640,165),(620,215)],1,colors["yellow"],colors["yellow"])
    canvas.draw_polygon([(220,330),(500,330),(500,415),(360,470),(220,415)],1,colors["dbrown"],colors["dbrown"])
    #head
    canvas.draw_circle((360,280),130,8,colors["dyellow"],colors["yellow"])
    canvas.draw_polygon([(205,250),(205,370),(115,310)],1,colors["dyellow"],colors["dyellow"])
    canvas.draw_polygon([(515,250),(515,370),(605,310)],1,colors["dyellow"],colors["dyellow"])
    #body
    canvas.draw_polygon([(260,480),(120,570),(115,730),(605,730),(600,570),(460,480)],8,colors["dbrown"],colors["brown"])
    canvas.draw_polygon([(285,415),(205,405),(195,495),(285,510),(195,495),(115,570),(150,680),(290,670)],8,colors["dbrown"],colors["brown"])
    canvas.draw_polygon([(435,415),(515,405),(525,495),(435,510),(525,495),(605,570),(570,680),(430,670)],8,colors["dbrown"],colors["brown"])
    canvas.draw_polygon([(285,415),(285,510),(435,510),(435,415)],8,colors["dbrown"],colors["brown"])
    canvas.draw_polygon([(250,565),(250,600),(470,600),(470,565)],8,colors["dyellow"],colors["yellow"])
    #face
    canvas.draw_polygon([(240,240),(275,195),(335,195),(353,218),(350,245),(320,265),(240,265)],8,colors["dgreen"],colors["green"])
    canvas.draw_polygon([(480,240), (445,195), (385,195), (367,218), (370,245), (400,265), (480,265)],8,colors["dgreen"],colors["green"])
    canvas.draw_polygon([(280,105),(195,175),(155,400),(190,465),(235,465),(260,385),(240,240),(275,195),(445,195), (480,240), (460,385), (485,465), (530,465), (565,400), (525,175), (440,105)],8,colors["dgreen"],colors["green"])
    canvas.draw_circle((285,292),35,8,colors["dblue"],colors["blue"])
    canvas.draw_circle((285,292),20,5,colors["dblue"],colors["dblue"])
    canvas.draw_circle((435,292),35,8,colors["dblue"],colors["blue"])
    canvas.draw_circle((435,292),20,5,colors["dblue"],colors["dblue"])
    canvas.draw_line((330,300),(390,300),8,"black")
    canvas.draw_polygon([(235,255),(320,253),(330,285),(235,287)],1,"black","black")
    canvas.draw_polygon([(485,255), (400,253), (390,285), (485,287)],1,"black","black")
    
    canvas.draw_polygon([(345,383),(375,383),(375,400),(345,400)],5,colors["dgreen"],colors["green"])
    
frame = simplegui.create_frame("Words", 720, 720)
frame.set_canvas_background(colors["yellow"])
frame.set_draw_handler(draw_handler)

#preload_music()
frame.start()
#play_music()
