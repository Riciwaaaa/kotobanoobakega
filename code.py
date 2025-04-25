import simplegui

music = simplegui.load_sound("https://riciwaaaa.github.io/schoolstuff/music.mp3")
is_preloaded = False

colors={
    "yellow":"RGB(235, 223, 199)",
    "green":"RGB(117, 165, 80)"
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
    canvas.draw_circle((350,270),160,5,colors["green"],colors["green"])
    canvas.draw_circle((350,300),130,5,colors["green"],colors["yellow"])

frame = simplegui.create_frame("Words", 720, 720)
frame.set_canvas_background(colors["yellow"])
frame.set_draw_handler(draw_handler)

#preload_music()
frame.start()
#play_music()
