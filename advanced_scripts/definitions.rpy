#This is a copy of definitions.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Explanation for Definitions
#This section defines stuff for the game: sprite poses for the girls, music, and backgrounds
#If you plan on adding new content, pop them over down there and mimic the appropriate lines!
define persistent.demo = False
define persistent.steam = False
define config.developer = "auto" #Change this flag to True to enable dev tools # Configurar modo dev

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        if persistent.do_not_delete: return
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass
    def pause(time=None):
        if not time:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time)

#Music
#The Music section is where you can reference existing DDLC audio

#You'll see this in some existing scripts as command 'play music [t1]' for example
#For easier reference, there are comments next to it so you can go DJ on the mod :)
define audio.t1 = "<loop 22.073>bgm/1.ogg"  #Main theme (title)


define audio.t2 = "<loop 4.499>bgm/2.ogg"   #Sayori theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"   #Main theme (in-game)
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"  #Poem minigame
define audio.t4g = "<loop 1.000>bgm/4g.ogg"

define audio.t5 = "<loop 4.444>bgm/5.ogg"   #Sharing poems...... 'Okay Everyone~!'
#Hey Mod team, our themes aren't defined here in the original script.
#Did some reading around and there was this + "_character" reference elsewhere.
#Anyhow, I'll try 'defining' them and see if it works!

define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" #Happy Thoughts with Ukelele & Snapping~!
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" #Fancy harps and instruments!
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" #Was it always cute on purpose?
define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" #Pianos

#Yeah, Monika... that should be good.
#So, take it from her and if you want to define music, make sure it exists in the appropriate folder
#Define its "audio.name" and see how it goes! (this should always be .ogg too, I think)

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"  #Yuri/Natsuki theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"   #Causing trouble
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"   #Trouble resolved
define audio.t9 = "<loop 3.172>bgm/9.ogg"   #Emotional
define audio.t9g = "<loop 1.532>bgm/9g.ogg" #207% speed
define audio.t10 = "<loop 5.861>bgm/10.ogg"   #Confession
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"

# The other music are just game's sfx, this line is for warning you here's end my OST list.


define audio.m1 = "<loop 0>bgm/m1.ogg" #Monika and her spaceroom music
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" #Monika music post-deletion

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"

# Backgrounds
image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image red = "#ff0000"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png"
image bg class_day = "bg/class.png"
image bg corridor = "bg/corridor.png"
image bg club_day = "bg/club.png"
image bg club_day2:
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png"
image bg bedroom = "bg/bedroom.png"
image bg sayori_bedroom = "bg/sayori_bedroom.png"
image bg house = "bg/house.png"
image bg kitchen = "bg/kitchen.png"

image bg notebook = "bg/notebook.png"
image bg notebook-glitch = "bg/notebook-glitch.png"

image bg glitch = LiveTile("bg/glitch.jpg")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

#------------------------------------------------From hereon, the girl's bodies are defined along with their heads.
#-----------------------------------------here's reference for the left half------the right half--------the head
# Sayori
image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")

image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat

# Natsuki
image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 41 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3.png")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3.png")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3.png")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3.png")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3.png")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3.png")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3.png")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3.png")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3.png")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3.png")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3.png")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3.png")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3.png")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3.png")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3.png")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3.png")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3.png")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3.png")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3.png")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3.png")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3.png")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")
#image natsuki 52 = im.Composite((960, 960), (0, 0), "natsuki/3.png", (0, 0), "natsuki/4t.png")


image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3b.png")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3b.png")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3b.png")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3b.png")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3b.png")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3b.png")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3b.png")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3b.png")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3b.png")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3b.png")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3b.png")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3b.png")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3b.png")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3b.png")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3b.png")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3b.png")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3b.png")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3b.png")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3b.png")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3b.png")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")

# Natsuki legacy
image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")

image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"

# Yuri
image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

image yuri 5a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 5b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 5c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 5d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 5e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 5f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 5g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 5h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 5i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 5j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 5k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 5l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 5m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 5n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 5o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 5p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 5q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 5r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 5s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 5t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 5u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 5v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 5w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")

image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

image yuri eyes_base = "yuri/eyes1.png"

image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"

#Monika

image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.png")

image monika 1a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 1b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 1c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 1d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 1e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 1f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 1g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 1h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 1i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 1n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 1o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 1p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")
image monika 1s = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/s.png")
image monika 1t = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/t.png")
image monika 1u = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/u.png")
image monika 1v = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/v.png")
image monika 1w = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/w.png")
image monika 1x = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/x.png")
image monika 1y = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/y.png")

image monika 2a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 2b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 2c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 2d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 2e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 2f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 2g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 2h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 2i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 2n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 2o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 2p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")
image monika 2s = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/s.png")
image monika 2t = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/t.png")
image monika 2u = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/u.png")
image monika 2v = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/v.png")
image monika 2w = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/w.png")
image monika 2x = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/x.png")
image monika 2y = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/y.png")

image monika 3a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 3b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 3c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 3d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 3e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 3f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 3g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 3h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 3i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 3n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 3o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 3p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")
image monika 3s = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/s.png")
image monika 3t = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/t.png")
image monika 3u = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/u.png")
image monika 3v = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/v.png")
image monika 3w = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/w.png")
image monika 3x = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/x.png")
image monika 3y = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/y.png")

image monika 4a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 4b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 4c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 4d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 4e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 4f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 4g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 4h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 4i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 4n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 4o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 4p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")
image monika 4s = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/s.png")
image monika 4t = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/t.png")
image monika 4u = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/u.png")
image monika 4v = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/v.png")
image monika 4w = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/w.png")
image monika 4x = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/x.png")
image monika 4y = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/y.png")

image monika 5a = im.Composite((960, 960), (0, 0), "monika/3a.png")
image monika 5b = im.Composite((960, 960), (0, 0), "monika/3b.png")

image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat


###### Character Variables ######
# These configure the shortcuts for writing dialog for each character.
define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', who_outlines=[ (4, "#cc1c2d") ], what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', who_outlines=[ (4, "#00a5ff") ], image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', who_outlines=[ (4, "#422d69") ], image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', who_outlines=[ (4, "#cd5683") ], image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', who_outlines=[ (4, "#66853e") ], image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define _dismiss_pause = config.developer

###### Persistent Variables ######
# These values are automatically loaded/saved on game start and exit.
# These exist across all saves

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
## default persistent.clear = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False] # Revisa si desbloqueaste todos los Cgs del juego.
default persistent.clear = [False, False, False, False, False, False, False, False, False, False, False, False, False] # Revisa si desbloqueaste todas las CGs de la Demo.
default persistent.clear12 = [False, False, False, False, False, False, False, False, False, False, False, False] # Revisa si se desbloquearon los 12 Cgs del Acto 1.
default persistent.special_poems = None
default persistent.mount_achieved = False # Una vez visitó la montaña, la opción de friendzonear a Sayori quedará anulada para siempre.
default persistent.clearall = None # En caso de sacar el Final Perfecto se pedirá eso para verificar si completaste el juego al 100%
default persistent.cleardemo = None # Al terminar en el Act1 sólo pedirá los 12 primeros CGs.
default persistent.clear12= None # Para verificar que desbloqueaste todas las Cgs antes del Ch5.
default persistent.clearneutral = None # En caso de sacar un final neutro dónde no requiera las CGs en la Ruta Perfecta.
default persistent.menu_bg_m = None
default persistent.first_load = None



###### Other global variables ######
# It's good practice to define global variables here, just so you know what you can call later

default in_sayori_kill = None
default in_yuri_kill = None
default in_natsuki_kill = None
default in_monika_kill = None
default in_mc_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None
default doki_choose = None
default dokisaved = None
default mount_achieved = False

# Create items

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"
default mcf1_name = "Ryoma"
default mcf2_name = "Camilla"
default mcf3_name = "Joe"
default mcf4_name = "Mac"
default mbf_name = "Maxxi"
default mf1_name = "Selene"
default fteach_name = "Profesora"
default mteach_name = "Profesor"
default mcmom_name = "Mamá"
default mcdad_name = "Papá"
default smom_name = "Mamá de Sayori"
default sdad_name = "Papá de Sayori"
default ymom_name = "Mamá de Yuri"
default ydad_name = "Papá de Yuri"
default nmom_name = "Mamá de Natsuki"
default ndad_name = "Papá de Natsuki"
default mmom_name = "Mamá de Monika"
default mdad_name = "Papá de Monika"
default f1mom_name = "Mamá de Ryoma"
default f1dad_name = "Papá de Ryoma"
default f2mom_name = "Mamá de Camilla"
default f2dad_name = "Papá de Camilla"

define mcf1 = DynamicCharacter('mcf1_name', color="#000000", who_outlines=[ (4, "#757575") ], image='ryoma', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define mcf2 = DynamicCharacter('mcf2_name', color="#f1ff30", who_outlines=[ (4, "#000000") ], image='camilla', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define mbf = DynamicCharacter('mbf_name', image='maxxii', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

#define y = DynamicCharacter('y_name', who_outlines=[ (4, "#422d69") ], image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

# Instantiating variables for poem appeal. This is how much each character likes the poem for each day.
# -1 = Dislike, 0 = Neutral, 1 = Like
default n_poemappeal = [0, 0, 0, 0]
default s_poemappeal = [0, 0, 0, 0]
default y_poemappeal = [0, 0, 0, 0]
default m_poemappeal = [0, 0, 0, 0]

# The last winner of the poem minigame.
default poemwinner = ['sayori', 'sayori', 'sayori', 'sayori']

# Keeping track of who read your poem when you're showing it to each of the girls.
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

# Used in poemresponse_start because it's easier than checking true/false on everyone's read state.
default poemsread = 0

# The main appeal points. Whoever likes your poem the most gets an appeal point for that chapter.
# Appeal points are used to keep track of which exclusive scene to show each chapter.
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

# We keep track of whether we watched Natsuki's and sayori's second exclusive scenes
# to decide whether to play them in chapter 3.
default n_exclusivewatched = False
default y_exclusivewatched = False

# Yuri runs away after the first exclusive scene of playthrough 2.
default y_gave = False
default y_ranaway = False

# We choose who to side with in chapter 1.
default ch1_choice = "sayori"

# If we choose to help Sayori in ch3, some of the dialogue changes.
default help_sayori = None
default help_monika = None

# We choose who to spend time with in chapter 4.
default ch4_scene = "yuri"
default ch4_name = "Yuri"
default sayori_confess = True

# We read Natsuki's confession poem in chapter 23.
default natsuki_23 = None


##############################################################################################################################################
##############################################################################################################################################
###############################################    DDLC Fighting For Reality Definitions   ###################################################
##############################################################################################################################################
##############################################################################################################################################

# Mod's Backgrounds, so they can't mix up with the game's bg. Yeah, just like with the Music...
# Template:: # image bg = "mod_bg/.png" #

# Original but edited backgrounds
image bg residential_morning = "mod_bg/residential-morning.png"
image bg house_morning = "mod_bg/house-morning.png"
image bg house_night = "mod_bg/house-night.png"
image bg sayori_bedroom_night = "mod_bg/sayori-bedroom-night.png"
image bg sayori_bedroom_night2 = "mod_bg/sayori-bedroom-night2.png"

# Houses backgrounds
image bg house_beta = "mod_bg/house.jpg" #This is the unused house background.
image bg bedroom_dark = "mod_bg/bedroom-dark.png"
image bg bedroom_night = "mod_bg/bedroom-night.png"
image bg hallway = "mod_bg/hallway.png"
image bg yuri_house = "mod_bg/yhouse.png"
image bg yuri_livingroom = "mod_bg/ylivingroom.png"
image bg yuri_bedroom = "mod_bg/ybedroom.png"
image bg natsuki_house = "mod_bg/nhouse.png"
image bg natsuki_bedroom = "mod_bg/nbedroom.png"
image bg monika_house = "mod_bg/mhouse.png"
image bg monika_bedroom = "mod_bg/mbedroom.png"

# School backgrounds
image bg sayori_classroom = "mod_bg/sclassroom.png"
image bg yuri_classroom = "mod_bg/yclassroom.png"
image bg natsuki_classroom = "mod_bg/nclassroom.png"
image bg monika_classroom = "mod_bg/mclassroom.png"
image bg school_entrance = "mod_bg/school-entrance.png"
image bg school_entrance_evening = "mod_bg/school-entrance-evening.png"
image bg school_entrance_night = "mod_bg/school-entrance-night.png"
image bg school_entrance_closed = "mod_bg/school-entrance-closed.png"
image bg school_backyard = "mod_bg/school-backyard.png"
image bg school_way = "mod_bg/school-way.png"
image bg school_way_cloudy = "mod_bg/school-way-cloudy.png"
image bg school_hall = "mod_bg/school-hall.png"
image bg school_hall_evening = "mod_bg/school-hall-evening.png"
image bg school_hall_night = "mod_bg/school-hall-night.png"
image bg school_dining_room = "mod_bg/school-dining.png"
image bg school_stairs1 = "mod_bg/school-stairs1.png"
image bg school_stairs2 = "mod_bg/school-stairs2.png"
image bg school_stairs3 = "mod_bg/school-stairs3.png"
image bg school_football_field = "mod_bg/school-football-field.png"
image bg school_roof = "mod_bg/school-roof-day.png"

# Streets backgrounds
image bg street_flashback = "mod_bg/street-flashback.png"
image bg streets1_day = "mod_bg/streets1-day.png"
image bg streets1_evening = "mod_bg/streets1-evening.png"
image bg streets1_cloudy = "mod_bg/streets1-cloudy.png"
image bg streets2_day = "mod_bg/streets2-day.png"
image bg streets2_evening = "mod_bg/streets2-evening.png"
image bg streets2_cloudy = "mod_bg/streets2-cloudy.png"

# Parks backgrounds
image bg park_way = "mod_bg/park1.jpg"
image bg park_way_morning = "mod_bg/park1-morning.jpg"
image bg park_bath = "mod_bg/park-bath.jpg"
image bg park_way2 = "mod_bg/park2.png"

# Shop interiors
image bg library = "mod_bg/library.png"
image bg library_evening = "mod_bg/library-evening.png"
image bg library_night = "mod_bg/library-night.png"
image bg library_old = "mod_bg/library-old.png"
image bg kiosco_day = "mod_bg/streetside-by-noraneko-games.png"
image bg kiosco_evening = "mod_bg/kiosco-evening.png"
image bg kiosco_night = "mod_bg/kiosco-night.png"
image bg cafe = "mod_bg/cafe.png"
image bg cafe_dark = "mod_bg/cafe-dark.png"
image bg gamingstore = "mod_bg/gaming-store.png"

# Nature backgrounds
image bg nature = "mod_bg/nature.png"
image bg forest_way_day = "mod_bg/forest-way-day.png"
image bg forest_way2 = "mod_bg/forest-way2-day.png"
image bg forest_bush = "mod_bg/forest-bush.png"
image bg meadow_day = "mod_bg/meadow-day.png"
image bg meadow_evening = "mod_bg/meadow-evening.png"
image bg seaside_road_day = "mod_bg/seaside-road-day.png"
image bg riverside_waterfall_bridge = "mod_bg/riverside-waterfall-bridge.png"
image bg riverside_waterfall = "mod_bg/riverside-waterfall.png"
image bg riverside_bridge = "mod_bg/riverside-bridge.png"
image bg deadend_rocky = "mod_bg/deadend-rocky.png"

# Other backgrounds
image bg truck_accident = "mod_bg/truck-accident-zoomed.png"
image bg bed_sex = "mod_bg/bed-sex.png"
image bg fightingclub_clean = "mod_bg/fightingclub-clean.png"
image bg fightingclub_dirty = "mod_bg/fightingclub-dirty.png"
image bg fightingclub_blood = "mod_bg/fightingclub-blood.png"
image bg health_room = "mod_bg/health-room.png"
image bg infernohall1 = "mod_bg/inferno-hall1.png"
image bg infernohall2 = "mod_bg/inferno-hall2.png"
image hxppy_thxughts = "mod_bg/hxppy-thxughts.png"

# Mod's CGs
# image s_cg4 = "mod_cg/s_cg4.png"

image s_cg3_ag1 = "mod_cg/s_cg3_ag1.png"
image s_cg3_ag2 = "mod_cg/s_cg3_ag2.png"
image s_cg3_ag3 = "mod_cg/s_cg3_ag3.png"
image s_cg3_ag4 = "mod_cg/s_cg3_ag4.png"
image s_cg3_g1 = "mod_cg/s_cg3_g1.png"
image s_cg3_g2 = "mod_cg/s_cg3_g2.png"
#image bg = "mod_bg/.png"
#image bg = "mod_bg/.png"
#image bg = "mod_bg/.png"
#image bg = "mod_bg/.png"

# Mod's Backgrounds end here.


#----------------Sprites personalizados del Mod.
# -------Sayori on pyjama (she's saved before hanging)
image sayori 1da = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/a.png")
image sayori 1db = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/b.png")
image sayori 1dc = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/c.png")
image sayori 1dd = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/d.png")
image sayori 1de = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/e.png")
image sayori 1df = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/f.png")
image sayori 1dg = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/g.png")
image sayori 1dh = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/h.png")
image sayori 1di = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/i.png")
image sayori 1dj = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/j.png")
image sayori 1dk = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/k.png")
image sayori 1dl = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/l.png")
image sayori 1dm = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/m.png")
image sayori 1dn = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/n.png")
image sayori 1do = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/o.png")
image sayori 1dp = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/p.png")
image sayori 1dq = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/q.png")
image sayori 1dr = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/r.png")
image sayori 1ds = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/s.png")
image sayori 1dt = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/t.png")
image sayori 1du = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/u.png")
image sayori 1dv = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/v.png")
image sayori 1dw = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/w.png")
image sayori 1dx = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/x.png")
image sayori 1dy = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/1dr.png", (0, 0), "sayori/y.png")

image sayori 2da = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/a.png")
image sayori 2db = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/b.png")
image sayori 2dc = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/c.png")
image sayori 2dd = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/d.png")
image sayori 2de = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/e.png")
image sayori 2df = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/f.png")
image sayori 2dg = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/g.png")
image sayori 2dh = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/h.png")
image sayori 2di = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/i.png")
image sayori 2dj = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/j.png")
image sayori 2dk = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/k.png")
image sayori 2dl = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/l.png")
image sayori 2dm = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/m.png")
image sayori 2dn = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/n.png")
image sayori 2do = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/o.png")
image sayori 2dp = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/p.png")
image sayori 2dq = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/q.png")
image sayori 2dr = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/r.png")
image sayori 2ds = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/s.png")
image sayori 2dt = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/t.png")
image sayori 2du = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/u.png")
image sayori 2dv = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/v.png")
image sayori 2dw = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/w.png")
image sayori 2dx = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/x.png")
image sayori 2dy = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/y.png")

image sayori 3da = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/a.png")
image sayori 3db = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/b.png")
image sayori 3dc = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/c.png")
image sayori 3dd = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/d.png")
image sayori 3de = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/e.png")
image sayori 3df = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/f.png")
image sayori 3dg = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/g.png")
image sayori 3dh = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/h.png")
image sayori 3di = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/i.png")
image sayori 3dj = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/j.png")
image sayori 3dk = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/k.png")
image sayori 3dl = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/l.png")
image sayori 3dm = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/m.png")
image sayori 3dn = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/n.png")
image sayori 3do = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/o.png")
image sayori 3dp = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/p.png")
image sayori 3dq = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/q.png")
image sayori 3dr = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/r.png")
image sayori 3ds = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/s.png")
image sayori 3dt = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/t.png")
image sayori 3du = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/u.png")
image sayori 3dv = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/v.png")
image sayori 3dw = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/w.png")
image sayori 3dx = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/x.png")
image sayori 3dy = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/y.png")

image sayori 4da = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/a.png")
image sayori 4db = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/b.png")
image sayori 4dc = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/c.png")
image sayori 4dd = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/d.png")
image sayori 4de = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/e.png")
image sayori 4df = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/f.png")
image sayori 4dg = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/g.png")
image sayori 4dh = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/h.png")
image sayori 4di = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/i.png")
image sayori 4dj = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/j.png")
image sayori 4dk = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/k.png")
image sayori 4dl = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/l.png")
image sayori 4dm = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/m.png")
image sayori 4dn = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/n.png")
image sayori 4do = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/o.png")
image sayori 4dp = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/p.png")
image sayori 4dq = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/q.png")
image sayori 4dr = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/r.png")
image sayori 4ds = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/s.png")
image sayori 4dt = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/t.png")
image sayori 4du = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/u.png")
image sayori 4dv = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/v.png")
image sayori 4dw = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/w.png")
image sayori 4dx = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/x.png")
image sayori 4dy = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/2dr.png", (0, 0), "sayori/y.png")

image sayori 5da = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/a.png")
image sayori 5db = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/b.png")
image sayori 5dc = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/c.png")
image sayori 5dd = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/d.png")
image sayori 5de = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/e.png")
image sayori 5df = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/f.png")
image sayori 5dg = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/g.png")
image sayori 5dh = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/h.png")
image sayori 5di = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/i.png")
image sayori 5dj = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/j.png")
image sayori 5dk = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/k.png")
image sayori 5dl = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/l.png")
image sayori 5dm = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/m.png")
image sayori 5dn = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/n.png")
image sayori 5do = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/o.png")
image sayori 5dp = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/p.png")
image sayori 5dq = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/q.png")
image sayori 5dr = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/r.png")
image sayori 5ds = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/s.png")
image sayori 5dt = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/t.png")
image sayori 5du = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/u.png")
image sayori 5dv = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/v.png")
image sayori 5dw = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/w.png")
image sayori 5dx = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/x.png")
image sayori 5dy = im.Composite((960, 960), (0, 0), "mod_sayori/1dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/y.png")

image sayori 6da = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/a.png")
image sayori 6db = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/b.png")
image sayori 6dc = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/c.png")
image sayori 6dd = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/d.png")
image sayori 6de = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/e.png")
image sayori 6df = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/f.png")
image sayori 6dg = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/g.png")
image sayori 6dh = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/h.png")
image sayori 6di = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/i.png")
image sayori 6dj = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/j.png")
image sayori 6dk = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/k.png")
image sayori 6dl = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/l.png")
image sayori 6dm = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/m.png")
image sayori 6dn = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/n.png")
image sayori 6do = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/o.png")
image sayori 6dp = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/p.png")
image sayori 6dq = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/q.png")
image sayori 6dr = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/r.png")
image sayori 6ds = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/s.png")
image sayori 6dt = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/t.png")
image sayori 6du = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/u.png")
image sayori 6dv = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/v.png")
image sayori 6dw = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/w.png")
image sayori 6dx = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/x.png")
image sayori 6dy = im.Composite((960, 960), (0, 0), "mod_sayori/2dl.png", (0, 0), "mod_sayori/3dr.png", (0, 0), "sayori/y.png")

# Long hair (past)

image sayori 1bal = im.Composite((960, 960), (0, 0), "mod_sayori/a_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bbl = im.Composite((960, 960), (0, 0), "mod_sayori/b_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bcl = im.Composite((960, 960), (0, 0), "mod_sayori/c_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bdl = im.Composite((960, 960), (0, 0), "mod_sayori/d_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bel = im.Composite((960, 960), (0, 0), "mod_sayori/e_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bfl = im.Composite((960, 960), (0, 0), "mod_sayori/f_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bgl = im.Composite((960, 960), (0, 0), "mod_sayori/g_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bhl = im.Composite((960, 960), (0, 0), "mod_sayori/h_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bil = im.Composite((960, 960), (0, 0), "mod_sayori/i_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bjl = im.Composite((960, 960), (0, 0), "mod_sayori/j_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bkl = im.Composite((960, 960), (0, 0), "mod_sayori/k_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bll = im.Composite((960, 960), (0, 0), "mod_sayori/l_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bml = im.Composite((960, 960), (0, 0), "mod_sayori/m_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bnl = im.Composite((960, 960), (0, 0), "mod_sayori/n_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bol = im.Composite((960, 960), (0, 0), "mod_sayori/o_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bpl = im.Composite((960, 960), (0, 0), "mod_sayori/p_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bql = im.Composite((960, 960), (0, 0), "mod_sayori/q_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1brl = im.Composite((960, 960), (0, 0), "mod_sayori/r_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bsl = im.Composite((960, 960), (0, 0), "mod_sayori/s_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1btl = im.Composite((960, 960), (0, 0), "mod_sayori/t_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bul = im.Composite((960, 960), (0, 0), "mod_sayori/u_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bvl = im.Composite((960, 960), (0, 0), "mod_sayori/v_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bwl = im.Composite((960, 960), (0, 0), "mod_sayori/w_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1bxl = im.Composite((960, 960), (0, 0), "mod_sayori/x_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")
image sayori 1byl = im.Composite((960, 960), (0, 0), "mod_sayori/y_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png")

image sayori 2bal = im.Composite((960, 960), (0, 0), "mod_sayori/a_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bbl = im.Composite((960, 960), (0, 0), "mod_sayori/b_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bcl = im.Composite((960, 960), (0, 0), "mod_sayori/c_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bdl = im.Composite((960, 960), (0, 0), "mod_sayori/d_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bel = im.Composite((960, 960), (0, 0), "mod_sayori/e_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bfl = im.Composite((960, 960), (0, 0), "mod_sayori/f_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bgl = im.Composite((960, 960), (0, 0), "mod_sayori/g_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bhl = im.Composite((960, 960), (0, 0), "mod_sayori/h_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bil = im.Composite((960, 960), (0, 0), "mod_sayori/i_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bjl = im.Composite((960, 960), (0, 0), "mod_sayori/j_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bkl = im.Composite((960, 960), (0, 0), "mod_sayori/k_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bll = im.Composite((960, 960), (0, 0), "mod_sayori/l_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bml = im.Composite((960, 960), (0, 0), "mod_sayori/m_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bnl = im.Composite((960, 960), (0, 0), "mod_sayori/n_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bol = im.Composite((960, 960), (0, 0), "mod_sayori/o_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bpl = im.Composite((960, 960), (0, 0), "mod_sayori/p_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bql = im.Composite((960, 960), (0, 0), "mod_sayori/q_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2brl = im.Composite((960, 960), (0, 0), "mod_sayori/r_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bsl = im.Composite((960, 960), (0, 0), "mod_sayori/s_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2btl = im.Composite((960, 960), (0, 0), "mod_sayori/t_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bul = im.Composite((960, 960), (0, 0), "mod_sayori/u_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bvl = im.Composite((960, 960), (0, 0), "mod_sayori/v_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bwl = im.Composite((960, 960), (0, 0), "mod_sayori/w_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2bxl = im.Composite((960, 960), (0, 0), "mod_sayori/x_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")
image sayori 2byl = im.Composite((960, 960), (0, 0), "mod_sayori/y_long.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png")

image sayori 3bal = im.Composite((960, 960), (0, 0), "mod_sayori/a_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bbl = im.Composite((960, 960), (0, 0), "mod_sayori/b_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bcl = im.Composite((960, 960), (0, 0), "mod_sayori/c_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bdl = im.Composite((960, 960), (0, 0), "mod_sayori/d_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bel = im.Composite((960, 960), (0, 0), "mod_sayori/e_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bfl = im.Composite((960, 960), (0, 0), "mod_sayori/f_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bgl = im.Composite((960, 960), (0, 0), "mod_sayori/g_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bhl = im.Composite((960, 960), (0, 0), "mod_sayori/h_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bil = im.Composite((960, 960), (0, 0), "mod_sayori/i_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bjl = im.Composite((960, 960), (0, 0), "mod_sayori/j_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bkl = im.Composite((960, 960), (0, 0), "mod_sayori/k_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bll = im.Composite((960, 960), (0, 0), "mod_sayori/l_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bml = im.Composite((960, 960), (0, 0), "mod_sayori/m_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bnl = im.Composite((960, 960), (0, 0), "mod_sayori/n_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bol = im.Composite((960, 960), (0, 0), "mod_sayori/o_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bpl = im.Composite((960, 960), (0, 0), "mod_sayori/p_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bql = im.Composite((960, 960), (0, 0), "mod_sayori/q_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3brl = im.Composite((960, 960), (0, 0), "mod_sayori/r_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bsl = im.Composite((960, 960), (0, 0), "mod_sayori/s_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3btl = im.Composite((960, 960), (0, 0), "mod_sayori/t_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bul = im.Composite((960, 960), (0, 0), "mod_sayori/u_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bvl = im.Composite((960, 960), (0, 0), "mod_sayori/v_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bwl = im.Composite((960, 960), (0, 0), "mod_sayori/w_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3bxl = im.Composite((960, 960), (0, 0), "mod_sayori/x_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")
image sayori 3byl = im.Composite((960, 960), (0, 0), "mod_sayori/y_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png")

image sayori 4bal = im.Composite((960, 960), (0, 0), "mod_sayori/a_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bbl = im.Composite((960, 960), (0, 0), "mod_sayori/b_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bcl = im.Composite((960, 960), (0, 0), "mod_sayori/c_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bdl = im.Composite((960, 960), (0, 0), "mod_sayori/d_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bel = im.Composite((960, 960), (0, 0), "mod_sayori/e_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bfl = im.Composite((960, 960), (0, 0), "mod_sayori/f_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bgl = im.Composite((960, 960), (0, 0), "mod_sayori/g_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bhl = im.Composite((960, 960), (0, 0), "mod_sayori/h_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bil = im.Composite((960, 960), (0, 0), "mod_sayori/i_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bjl = im.Composite((960, 960), (0, 0), "mod_sayori/j_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bkl = im.Composite((960, 960), (0, 0), "mod_sayori/k_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bll = im.Composite((960, 960), (0, 0), "mod_sayori/l_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bml = im.Composite((960, 960), (0, 0), "mod_sayori/m_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bnl = im.Composite((960, 960), (0, 0), "mod_sayori/n_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bol = im.Composite((960, 960), (0, 0), "mod_sayori/o_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bpl = im.Composite((960, 960), (0, 0), "mod_sayori/p_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bql = im.Composite((960, 960), (0, 0), "mod_sayori/q_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4brl = im.Composite((960, 960), (0, 0), "mod_sayori/r_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bsl = im.Composite((960, 960), (0, 0), "mod_sayori/s_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4btl = im.Composite((960, 960), (0, 0), "mod_sayori/t_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bul = im.Composite((960, 960), (0, 0), "mod_sayori/u_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bvl = im.Composite((960, 960), (0, 0), "mod_sayori/v_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bwl = im.Composite((960, 960), (0, 0), "mod_sayori/w_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4bxl = im.Composite((960, 960), (0, 0), "mod_sayori/x_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")
image sayori 4byl = im.Composite((960, 960), (0, 0), "mod_sayori/y_long.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png")

# -------Sayori naked 7w7

image sayori 1na = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/a.png")
image sayori 1nb = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/b.png")
image sayori 1nc = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/c.png")
image sayori 1nd = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/d.png")
image sayori 1ne = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/e.png")
image sayori 1nf = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/f.png")
image sayori 1ng = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/g.png")
image sayori 1nh = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/h.png")
image sayori 1ni = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/i.png")
image sayori 1nj = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/j.png")
image sayori 1nk = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/k.png")
image sayori 1nl = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/l.png")
image sayori 1nm = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/m.png")
image sayori 1nn = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/n.png")
image sayori 1no = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/o.png")
image sayori 1np = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/p.png")
image sayori 1nq = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/q.png")
image sayori 1nr = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/r.png")
image sayori 1ns = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/s.png")
image sayori 1nt = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/t.png")
image sayori 1nu = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/u.png")
image sayori 1nv = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/v.png")
image sayori 1nw = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/w.png")
image sayori 1nx = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/x.png")
image sayori 1ny = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/1nr.png", (0, 0), "sayori/y.png")

image sayori 2na = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/a.png")
image sayori 2nb = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/b.png")
image sayori 2nc = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/c.png")
image sayori 2nd = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/d.png")
image sayori 2ne = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/e.png")
image sayori 2nf = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/f.png")
image sayori 2ng = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/g.png")
image sayori 2nh = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/h.png")
image sayori 2ni = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/i.png")
image sayori 2nj = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/j.png")
image sayori 2nk = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/k.png")
image sayori 2nl = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/l.png")
image sayori 2nm = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/m.png")
image sayori 2nn = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/n.png")
image sayori 2no = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/o.png")
image sayori 2np = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/p.png")
image sayori 2nq = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/q.png")
image sayori 2nr = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/r.png")
image sayori 2ns = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/s.png")
image sayori 2nt = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/t.png")
image sayori 2nu = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/u.png")
image sayori 2nv = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/v.png")
image sayori 2nw = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/w.png")
image sayori 2nx = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/x.png")
image sayori 2ny = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/y.png")

image sayori 3na = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/a.png")
image sayori 3nb = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/b.png")
image sayori 3nc = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/c.png")
image sayori 3nd = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/d.png")
image sayori 3ne = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/e.png")
image sayori 3nf = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/f.png")
image sayori 3ng = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/g.png")
image sayori 3nh = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/h.png")
image sayori 3ni = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/i.png")
image sayori 3nj = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/j.png")
image sayori 3nk = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/k.png")
image sayori 3nl = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/l.png")
image sayori 3nm = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/m.png")
image sayori 3nn = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/n.png")
image sayori 3no = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/o.png")
image sayori 3np = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/p.png")
image sayori 3nq = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/q.png")
image sayori 3nr = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/r.png")
image sayori 3ns = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/s.png")
image sayori 3nt = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/t.png")
image sayori 3nu = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/u.png")
image sayori 3nv = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/v.png")
image sayori 3nw = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/w.png")
image sayori 3nx = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/x.png")
image sayori 3ny = im.Composite((960, 960), (0, 0), "mod_sayori/1nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/y.png")

image sayori 4na = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/a.png")
image sayori 4nb = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/b.png")
image sayori 4nc = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/c.png")
image sayori 4nd = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/d.png")
image sayori 4ne = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/e.png")
image sayori 4nf = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/f.png")
image sayori 4ng = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/g.png")
image sayori 4nh = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/h.png")
image sayori 4ni = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/i.png")
image sayori 4nj = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/j.png")
image sayori 4nk = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/k.png")
image sayori 4nl = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/l.png")
image sayori 4nm = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/m.png")
image sayori 4nn = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/n.png")
image sayori 4no = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/o.png")
image sayori 4np = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/p.png")
image sayori 4nq = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/q.png")
image sayori 4nr = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/r.png")
image sayori 4ns = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/s.png")
image sayori 4nt = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/t.png")
image sayori 4nu = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/u.png")
image sayori 4nv = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/v.png")
image sayori 4nw = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/w.png")
image sayori 4nx = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/x.png")
image sayori 4ny = im.Composite((960, 960), (0, 0), "mod_sayori/2nl.png", (0, 0), "mod_sayori/2nr.png", (0, 0), "sayori/y.png")

# -------Natsuki
image natsuki nb111 = im.Composite((960, 960), (0, 0), "mod_natsuki/bruise/nb1.png", (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png")
image natsuki nb211 = im.Composite((960, 960), (0, 0), "mod_natsuki/bruise/nb2.png", (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png")
image natsuki nb311 = im.Composite((960, 960), (0, 0), "mod_natsuki/bruise/nb3.png", (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png")
image natsuki nb411 = im.Composite((960, 960), (0, 0), "mod_natsuki/bruise/nb4.png", (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png")

image natsuki nb121 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_natsuki/bruise/nb1.png")
image natsuki nb221 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_natsuki/bruise/nb2.png")
image natsuki nb321 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_natsuki/bruise/nb3.png")
image natsuki nb421 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_natsuki/bruise/nb4.png")

image natsuki nb112 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_natsuki/bruise/nb1.png")
image natsuki nb212 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_natsuki/bruise/nb2.png")
image natsuki nb312 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_natsuki/bruise/nb3.png")
image natsuki nb412 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_natsuki/bruise/nb4.png")

image natsuki nb122 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_natsuki/bruise/nb1.png")
image natsuki nb222 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_natsuki/bruise/nb2.png")
image natsuki nb322 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_natsuki/bruise/nb3.png")
image natsuki nb422 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_natsuki/bruise/nb4.png")

image natsuki cry = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_natsuki/cry.png")

# -------Monika

image monika 1s = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/s.png")
image monika 1t = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/t.png")
image monika 1u = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/u.png")
image monika 1v = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/v.png")
image monika 1w = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/w.png")
image monika 1x = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/x.png")
image monika 1y = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/y.png")

image monika 2s = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/s.png")
image monika 2t = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/t.png")
image monika 2u = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/u.png")
image monika 2v = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/v.png")
image monika 2w = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/w.png")
image monika 2x = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/x.png")
image monika 2y = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/y.png")

image monika 3s = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/s.png")
image monika 3t = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/t.png")
image monika 3u = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/u.png")
image monika 3v = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/v.png")
image monika 3w = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/w.png")
image monika 3x = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/x.png")
image monika 3y = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_monika/y.png")

image monika 4s = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/s.png")
image monika 4t = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/t.png")
image monika 4u = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/u.png")
image monika 4v = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/v.png")
image monika 4w = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/w.png")
image monika 4x = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/x.png")
image monika 4y = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_monika/y.png")

image monika gun1 = im.Composite((960, 960), (0, 0), "mod_monika/monigun1.png")
image monika gun2 = im.Composite((960, 960), (0, 0), "mod_monika/monigun2.png")
image monika creepy = im.Composite((960, 960), (0, 0), "mod_monika/creepy.png")

#----------------La adorable Camilla <3

image camilla = im.Composite((960, 960), (0, 0), "camilla/camilla.png")

#----------------El Big Bro Ryoma

image ryoma = im.Composite((960, 960), (0, 0), "ryoma/ryoma.png")

#----------------NPCs exclusivos del Mod.

image mac = im.Composite((960, 960), (0, 0), "npcs/mac.png")
image dadsuki = im.Composite((960, 960), (0, 0), "npcs/dadsuki.png")
image robber = im.Composite((960, 960), (0, 0), "npcs/robber1.png")

#----------------Efectos de batalla.

image sword_swing:
    "images/yuri/za.png"
    0.1
    "images/yuri/zb.png"
    0.1
    "images/yuri/zc.png"
    0.1
    "images/yuri/zd.png"
    0.1
    

#------------------Monika forma sombra
image monika sdwf1 = im.Composite((960, 960), (0, 0), "mod_monika/sdwf1.png")
image monika sdwb1 = im.Composite((960, 960), (0, 0), "mod_monika/sdwb1.png")



# Mod's persisten variables
default save_load_system = False
default save_load_disabled = False



# Mod's soundtrack. Do you like them? :)

#define audio.title_theme = "<loop 22.073>mod_bgm/main-menu.ogg"  #Main theme (title)
define audio.title_theme = "<loop 0>mod_bgm/main-menu.ogg"  #Main theme (title)
define audio.final_battle = "<loop 0>mod_bgm/final-battle.ogg"
#define audio.tmod1 = "<loop 0>mod_bgm/bright-wish-by-kevin-macleod.mp3"
define audio.demobattle = "<loop 0>mod_bgm/world spinning-ncm.mp3"
define audio.credits2 = "mod_bgm/credits_instrumental.mp3"
define audio.midnight_piano = "<loop 0>mod_bgm/midnight-piano.mp3"
#define audio.ryomatheme = "<loop 0>mod_bgm/greetings_from_the_other_side.mp3"
define audio.parallel = "<loop 0>mod_bgm/parallel.ogg"
define audio.finalvictory = "<loop 0>mod_bgm/epic-victory-march.mp3"
#define audio.sorry = "<loop 0>mod_bgm/cant-help-falling-in-love.mp3"
#define audio.camillatheme = "mod_bgm/.mp3"
define audio.tmod2 = "<loop 0>mod_bgm/despair-and-triumph.mp3"
define audio.flashback1 = "<loop 0>mod_bgm/dissociation.mp3"


# Mod's sound effects...

define audio.click = "mod_sfx/click.mp3"
define audio.ding = "mod_sfx/ding.mp3"
define audio.school_bell = "mod_sfx/school_bell.ogg"
define audio.select_echo = "mod_sfx/select_echo.ogg"
define audio.slap = "sfx/slap.ogg"
define audio.defeated_boss = "mod_sfx/defeated_boss.ogg"
define audio.ringtone1 = "mod_sfx/samsung_skyline.mp3"
define audio.ringtone2 = "mod_sfx/samsung_skyline2.mp3"
define audio.ringtone3 = "mod_sfx/samsung_whistle.mp3"
define audio.iphone = "mod_sfx/iphone_sound.mp3"
define audio.waterfalls = "<loop 0>mod_sfx/waterfall.mp3"
define audio.truck_brakes = "mod_sfx/truck-brake.ogg"


# Mod's default variables

default money = 0
default hr_hour = 0
default hr_minutes = 0
default stamina_max = 10
default stamina = stamina_max
#default hour = "[hr_hour] : [hr_minutes]"
default boss_battle = False
default persistent.magic_enabled = False # Define si el MC logra aprender a usar magia.
default no_death_battle = False
default persistent.monika_help = True
default persistent.ytellyouherbookstore = False # Activa un evento dónde Yuri te revela en dónde compra sus libros. Una vez puesto en True, si vuelves al Día 0, MC irá a esa librería en vez de la que está cerca de su casa dónde se cruza con Monika.
default ch1_mc_busted = None # En el evento dónde arrestan al MC, si Monika hackeó al policia es False, si ella se presenta y paga el soborno es True, si no se desbloqueó el evento es None.
default ch2_tell_sayori_meet_later = False
default ch2_battle_3_event = False
default accept_kickboxingclub_offer = "No"


default sbook_bought = False
default ybook_bought = False
default nbook_bought = False
default mbook_bought = False

### Mod's Progress default variables

default total_progress = 0
default total_npc_defeated = 0

# MC's default stats

default playername_default = "Red"

# MC's level
default mc_lv = 1 # Nivel de pelea de MC. Mientras mayor sea su valor, más incrementarán sus Stats de combate. Sólo aumenta si el valor EXP iguala o supera el NEXT_LV

# MC's HP (Health Points) and MP (Magic Points)
default mc_hp_max = 100 # Valor máximo de salud que te permite soportar ataques. Este valor no se modifica a menos que MC suba de Lv.
default mc_hp = mc_hp_max # Valor base de salud. Si baja a 0, morirás. (Usualmente se rellena con el valor máximo)
default mc_mp_max = 50 # Valor máximo de magia que te permite usar hechizos. Este valor no se modifica a menos que MC suba de Lv.
default mc_mp = mc_mp_max # Valor base de magia. Si baja a 0 no podrás usar ninguno. (Usualmente se rellena con el valor máximo)

# MC's Fighting Base Stats
default mc_atk_base = 10 # Valor de ataque que con mayor valor hace mayor daño.
default mc_def_base = 8 # Valor de defensa que con mayor valor resiste mejor los ataques enemigos.
default mc_spd_base = 20 # Valor de velocidad que con mayor valor se desplazará más rápido. También ayuda a atacar antes que tus enemigos.
default mc_mat_base = 4 # Valor de ataque mágico que con mayor valor sus poderes mágicos producen mayor daño. También ayuda a curarte mejor en caso de usar conjuros cómo Cure en tí.
default mc_mdf_base = 6 # Valor de defensa mágica que con mayor valor resiste mejor los ataques mágicos enemigos.
default mc_evasion_base = 10 # Aumenta la probabilidad de esquivar ataques en combates.

# MC's Persistent Base Stats (min = 1 | max = 100)
default mc_luck_base = 1 # Sirve para muchas cosas indispensables para el MC... El amor, el azar, las peleas, etc etc...
default mc_charisma_base = 10 # Mientras más alto el valor, mejor será visto el MC frente a las personas.
default mc_intelligence_base = 50 # Sirve para ciertos momentos dónde se debe requerir la mentalidad del MC.

# MC's Other Base Stats (min = 1 | max = 100)
#default mc_money = 3500 # MONEY MONEY MONEY MONEY MONEY MONEY MONEY MONEY MONEY (infinite value)
default mc_respect_base = 5 # Porcentaje de cuánto respetan al MC en su escuela.
default mc_stamina_base = 10 # Sólo sirve para el Modo Freetime. Funciona cómo contador de cuántas actividades podrás hacer en el momento.
default mc_strength_base = 20 # Sirve para ciertos momentos dónde se debe requerir la fuerza física del MC.
default mc_fat_base = 40 # Calcula el sobrepeso del MC. ¡Cuidado, un porcentaje mayor a 70 implicaría problemas de salud!
default mc_muscle_base = 10 # Calcula la musculatura del MC. ¡Un porcentaje mayor a 70 te dejará mamadísimo!

# MC's Experience points and Next Level points
default mc_exp = 0
default mc_next_lv = 50

# MC' Current Weapon (None, Knife, Sword, etc.) and Buffing

default mc_current_weapon = None
default mc_current_weapon_type = None
default mc_wpn_buff = 0

default enemy_current_weapon = None

# Mc's Weapon Skills ( 1 = D | 2 = C | 3 = B | 4 = A | 5 = S )

default mc_sword_skill = 1 # Habilidad para usar espadas.
default mc_sword_exp = 0 # Puntos de experiencia que aumentan si usas determinado tipo de arma frecuentemente.
default mc_knife_skill = 1 # Habilidad para usar cuchillos.
default mc_knife_exp = 0 # Puntos de experiencia que aumentan si usas determinado tipo de arma frecuentemente.
default mc_melee_skill = 1 # Habilidad para usar armas blancas, cómo un bate de baseball.
default mc_melee_exp = 0 # Puntos de experiencia que aumentan si usas determinado tipo de arma frecuentemente.
default mc_chainsaw_skill = 1 # Habilidad para usar motosierras.
default mc_chainsaw_exp = 0 # Puntos de experiencia que aumentan si usas determinado tipo de arma frecuentemente.
default mc_handgun_skill = 1 # Habilidad para usar armas de fuego pequeñas.
default mc_handgun_exp = 0 # Puntos de experiencia que aumentan si usas determinado tipo de arma frecuentemente.
default mc_machinegun_skill = 1 # Habilidad para usar armas de fuego pesadas.
default mc_machinegun_exp = 0 # Puntos de experiencia que aumentan si usas determinado tipo de arma frecuentemente.
default mc_magic_skill = 1 # Habilidad para usar magia.
default mc_magic_exp = 0 # Puntos de experiencia que aumentan si usas determinado tipo de arma frecuentemente.

# Persistent para todos los Stats así se mantienen sin importar cuántas veces se reinicie la partida.
# (Se almacenan mediante un archivo caché para los stats)

default persistent.total_progress = 0

default persistent.mc_lv_base = 1
default persistent.mc_hp_max_base = 100
default persistent.mc_mp_max_base = 50
default persistent.mc_atk_base = 10
default persistent.mc_def_base = 8
default persistent.mc_spd_base = 20
default persistent.mc_mat_base = 4
default persistent.mc_mdf_base = 6
default persistent.mc_evasion_base = 10
default persistent.mc_intelligence_base = 50
default persistent.mc_exp_base = 0
default persistent.mc_next_lv_base = 50

default persistent.mc_luck_base = 1
default persistent.mc_charisma_base = 10
default persistent.mc_intelligence_base = 50

default persistent.mc_sword_skill = 1
default persistent.mc_sword_exp = 0
default persistent.mc_knife_skill = 1
default persistent.mc_knife_exp = 0
default persistent.mc_melee_skill = 1
default persistent.mc_melee_exp = 0
default persistent.mc_chainsaw_skill = 1
default persistent.mc_chainsaw_exp = 0
default persistent.mc_handgun_skill = 1
default persistent.mc_handgun_exp = 0
default persistent.mc_machinegun_skill = 1
default persistent.mc_machinegun_exp = 0
default persistent.mc_magic_skill = 1
default persistent.mc_magic_exp = 0

# Enemy's default stats

default enemy_lv = 1
default enemy_hp_max = 1
default enemy_hp = enemy_hp_max
default enemy_atk_base = 1
default enemy_def_base = 1
default enemy_spd_base = 1
default enemy_mat_base = 1
default enemy_mdf_base = 1

# Monika's Final Boss stats

default monika_lv = 100
default monika_hp_max = 999999
default monika_hp = monika_hp_max
default monika_mp_max = 999999
default monika_mp = monika_mp_max
default monika_atk_base = 45000
default monika_def_base = 89000
default monika_spd_base = 62000
default monika_mat_base = 98000
default monika_mdf_base = 95000
default monika_exp = 10000000
default monika_next_lv = 0