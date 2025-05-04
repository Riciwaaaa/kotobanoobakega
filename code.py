



#PLEASE RUN ONCE BEFORE PLAYING TO AVOID DELAY




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

#Japanese contains only 5 vowels, so only 5+1 mouth shapes
mouth_shapes={
    "a": [(345,383),(375,383),(378,400),(342,400)],
    "i": [(340,385),(380,385),(380,392),(340,392)],
    "u": [(360,380),(370,400),(350,400)],
    "e": [(343,384),(377,384),(380,394),(340,394)],
    "o": [(348,383),(372,383),(372,400),(348,400)],
    " ": [(345,392),(375,392),(340,392)],
}

#I just realized that vertical sentences goes from right to left in Japanese, so 2 is actually supposed to be 1 but it's too late
#I hate (the language) Japanese
mouth_sequence2="-"*64+"o o a o o a e a a o a a i e i u o u o o a i a a i a e a a a a aio o a o o a e a a o a a i e i u o u o o a i a a i a e a a a a aio-  uiiae-i-o oae-i-o--ao o-a-u-u- aaeeu-u-u-aeu-u-u-aeo        a au-ae-        a au-ae-        a au-ae-        a au-ae-       o o a o o a e a a o a a i e i u o u o o a i a a i a e a a a a aio o a o o a e a a o a a i e i u o u o o a i a a i a e a a a a aio-  uiiae-i-o oae-i-o--ao o-a-u-u- aaeeu-u-u-aeu-u-u-aeo        a au-ae-        a au-ae-        a au-ae-        a au-ae-       o o a o o a e a a o a a i e i u o u o o a i a a i a e a a a a aio o a o o a e a a o a a i e i u o u o o a i a a i a e a a a a aio o a o o a e a a o a a i e i u o u o o a i a a i a e a a a a aio o a o o a e a a o a a i e i u o u o o a i a a i a e a a a a aio "+"-"*160
mouth_sequence1="-"*64+"o o a o o a e a a o a a i e i u o u o o a i a a i a e a a a a aio o a o o a e a a o a a i e i u o u o o a i a a i a e a a a a aio-          uiiae-i-o oae-i-o--ao o-a-u-u- aaeeu-u-u-aeo                a au-ae-        a au-ae-        a au-ae-a au-ae-       o o a o o a e a a o a a i e i u o u o o a i a a i a e a a a a aio o a o o a e a a o a a i e i u o u o o a i a a i a e a a a a aio-          uiiae-i-o oae-i-o--ao o-a-u-u- aaeeu-u-u-aeo                a au-ae-        a au-ae-        a au-ae-a au-ae-       o o a o o a e a a o a a i e i u o u o o a i a a i a e a a a a aio o a o o a e a a o a a i e i u o u o o a i a a i a e a a a a aio o a o o a e a a o a a i e i u o u o o a i a a i a e a a a a aio o a o o a e a a o a a i e i u o u o o a i a a i a e a a a a aio "+"-"*160
lyric_seq2 = " " * 64 +"k t b n o b k g m d k r m t i r y r n t b r a s n n r b d m t rso t n n k t e w n z b k r d i t m t m n s s a t r m e g w k r nik   fsgnn i r hrn i oonno t g s r  ngrtk r u tdk r u tds        asgkrmd         amtfram         ktwfrws         tdtgrdk        k t b n o b k g m d k r m t i r y r n t b r a s n n r b d m t rso t n n k t e w n z b k r d i t m t m n s s a t r m e g w k r nik   fsgnn i r hrn i oonno t g s r  ngrtk r u tdk r u tds        asgkrmd         amtfram         ktwfrws         tdtgrdk        ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ??? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ??k t b n o b k g m d k r m t i r y r n t b r a s n n r b d m t rso t n n k t e w n z b k r d i t m t m n s s a t r m e g w k r nik "+" "*160
lyric_seq1 = " " * 64 +"o t n n k t e w n z b k r d i t m t m n s s a t r m e g w k r nik t b n o b k g m d k r m t i r y r n t b r a s n n r b d m t rso           fsgnn i r hrn i oonno t g s r  ngrtk r u tds                ktruudk         kntfrkz         atmfrws tdtgrdk        o t n n k t e w n z b k r d i t m t m n s s a t r m e g w k r nik t b n o b k g m d k r m t i r y r n t b r a s n n r b d m t rso           fsgnn i r hrn i oonno t g s r  ngrtk r u tds                ktruudk         kntfrkz         atmfrws tdtgrdk        ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ??? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ??o t n n k t e w n z b k r d i t m t m n s s a t r m e g w k r nik t b n o b k g m d k r m t i r y r n t b r a s n n r b d m t rso "+" "*160
index=0
mouth1=" "
mouth2=" "
lyric1=" "
lyric2=" "
def update():
    global index, mouth1, mouth2, lyric1, lyric2

    if mouth_sequence1[index] != "-":
        mouth1 = mouth_sequence1[index]
    if mouth_sequence2[index] != "-":
        mouth2 = mouth_sequence2[index]
    lyric1 = lyric_seq1[index]
    lyric2 = lyric_seq2[index]
        
    index = (index + 1) % max(len(mouth_sequence1), len(mouth_sequence2))

def draw_mouth(canvas,char,i):
    if char in mouth_shapes:
        points= [(x+i,y) for (x,y) in mouth_shapes[char]]
        canvas.draw_polygon(points,5,colors["dgreen"],colors["green"])    
    
def dummy_handler(): #Load music
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
        canvas.draw_line((330+i,300),(390+i,300),8,"black")
        
        if (index>304 and index<318) or (index>561 and index<575):
            canvas.draw_polygon([(235+i,250),(310+i,240),(325+i,270),(235+i,275)],1,"black","black")
            canvas.draw_polygon([(485+i,250),(410+i,240),(395+i,270),(485+i,275)],1,"black","black")
            canvas.draw_circle((290+i,292),10,8,colors["dblue"],colors["blue"])
            canvas.draw_circle((430+i,292),10,8,colors["dblue"],colors["blue"])
            canvas.draw_line((260+i,325),(315+i,325),8,"black")
            canvas.draw_line((460+i,325),(405+i,325),8,"black")
            canvas.draw_polygon([(275+i,350),(275+i,360),(285+i,360),(285+i,350),(285+i,360),(275+i,360)],5,"black")
            canvas.draw_polygon([(445+i,350),(445+i,360),(435+i,360),(435+i,350),(435+i,360),(445+i,360)],5,"black")
        elif index % 40 in [1] or index == 304 or index == 318 or index == 561 or index == 575:
            canvas.draw_polygon([(235+i,270),(320+i,268),(330+i,310),(235+i,312)],1,"black","black")
            canvas.draw_polygon([(485+i,270), (400+i,268), (390+i,310), (485+i,312)],1,"black","black")
        else:
            canvas.draw_circle((285+i,292),35,8,colors["dblue"],colors["blue"])
            canvas.draw_circle((285+i,292),20,5,colors["dblue"],colors["dblue"])
            canvas.draw_circle((435+i,292),35,8,colors["dblue"],colors["blue"])
            canvas.draw_circle((435+i,292),20,5,colors["dblue"],colors["dblue"])
            canvas.draw_polygon([(235+i,255),(320+i,253),(330+i,285),(235+i,287)],1,"black","black")
            canvas.draw_polygon([(485+i,255), (400+i,253), (390+i,285), (485+i,287)],1,"black","black")
    
   
    for n in range((index//2) % 8 + 1):  
        x = 18 + n * 88             
        if index>64:
            canvas.draw_polygon([(x, 18), (x, 83), (x + 65, 83), (x + 65, 18)],5, colors["dyellow"])
            canvas.draw_polygon([(653-x, 702), (653-x, 637), (653-x + 65, 637), (653-x + 65, 702)],5, colors["dyellow"])
    
    draw_character(-340)
    draw_character(340)
    
    draw_mouth(canvas, mouth1, -340)
    draw_mouth(canvas, mouth2, 340)
    #consonants
    canvas.draw_text(lyric1.upper(), (305, 360), 40, colors["dbrown"])
    canvas.draw_text(lyric2.upper(), (385, 360), 40, colors["dbrown"])
    #subtitle
    if index >= 32 and index < 56:
        canvas.draw_text("The ghost of words", (245, 360), 25, colors["dbrown"])
    elif index >= 836 and index <= 864:
        canvas.draw_text("Song Furokuro", (260, 360), 29, colors["dbrown"])
    elif index >= 864 and index <= 896:
        canvas.draw_text("By Riciwaaaa", (260, 360), 30, colors["dbrown"])
    elif index >= 960:
        canvas.draw_polygon([(0,0),(0,750),(750,750),(750,0)],5,"black","black")
    
frame = simplegui.create_frame("Words", 720, 720)
timer = simplegui.create_timer(188, update)

frame.set_canvas_background(colors["yellow"])
frame.set_draw_handler(draw_handler)

preload_music()
timer.start()
frame.start()
play_music()
