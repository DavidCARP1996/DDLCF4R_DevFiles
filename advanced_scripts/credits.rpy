#This is a copy of credits.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Import the datetime library for using time
init python:
    import datetime

#This defines the CGs that disappear after a few seconds
#These are the colored CGs used for scene cgs
image credits_cg1:
    "images/cg/credits/1.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2:
    "images/cg/credits/2.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3:
    "images/cg/credits/3.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4:
    "images/cg/credits/4.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5:
    "images/cg/credits/5.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6:
    "images/cg/credits/6.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7:
    "images/cg/credits/7.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8:
    "images/cg/credits/8.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9:
    "images/cg/credits/9.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10:
    "images/cg/credits/10.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

#These are the grayed out CGs for unseen cgs
image credits_cg1_locked:
    "images/cg/credits/1b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2_locked:
    "images/cg/credits/2b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3_locked:
    "images/cg/credits/3b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4_locked:
    "images/cg/credits/4b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5_locked:
    "images/cg/credits/5b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6_locked:
    "images/cg/credits/6b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7_locked:
    "images/cg/credits/7b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8_locked:
    "images/cg/credits/8b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9_locked:
    "images/cg/credits/9b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10_locked:
    "images/cg/credits/10b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

#This defines the CGs that don't fade for a "perfect ending"
image credits_cg1_clearall:
    "images/cg/credits/1.png"
    size(640, 360)

image credits_cg2_clearall:
    "images/cg/credits/2.png"
    size(640, 360)

image credits_cg3_clearall:
    "images/cg/credits/3.png"
    size(640, 360)

image credits_cg4_clearall:
    "images/cg/credits/4.png"
    size(640, 360)

image credits_cg5_clearall:
    "images/cg/credits/5.png"
    size(640, 360)

image credits_cg6_clearall:
    "images/cg/credits/6.png"
    size(640, 360)

image credits_cg7_clearall:
    "images/cg/credits/7.png"
    size(640, 360)

image credits_cg8_clearall:
    "images/cg/credits/8.png"
    size(640, 360)

image credits_cg9_clearall:
    "images/cg/credits/9.png"
    size(640, 360)

image credits_cg10_clearall:
    "images/cg/credits/10.png"
    size(640, 360)

#DDLC Logo
image credits_logo:
    "gui/logo.png"
    truecenter
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

#Team Salvato logo
image credits_ts:
    "images/bg/splash-white.png"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

#This styles the different text in the credits
style credits_header:
    font "gui/font/RifficFree-Bold.ttf"
    color "#ffaae6"
    size 36
    text_align 0.5
    outlines []

style credits_text:
    font "gui/font/Halogen.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines []

style monika_credits_text:
    font "gui/font/m1.ttf"
    color "#fff"
    size 40
    text_align 0.5
    outlines []

style red_credits_text:
    font "gui/font/halogen.ttf"
    color "#fff"
    size 30
    text_align 0.5
    outlines []

image credits_header = ParameterizedText(style="credits_header", ypos=-40)
image credits_text = ParameterizedText(style="credits_text", ypos=40)
image monika_credits_text = ParameterizedText(style="monika_credits_text", xalign=0.5)
image red_credits_text = ParameterizedText(style="red_credits_text", xalign=0.5)

#These are the animations applied to the make the credits and images scroll
transform credits_scroll:
    subpixel True
    yoffset 740
    linear 15 yoffset -380

transform credits_text_scroll:
    anchor (0.5, 0.5) subpixel True
    yoffset 920
    linear 15 yoffset -200

transform credits_sticker_scroll:
    subpixel True
    yoffset 940
    7.8
    linear 15 yoffset -180

transform credits_scroll_right:
    xalign 0.9
    credits_scroll

transform credits_scroll_left:
    xalign 0.1
    credits_scroll

transform credits_text_scroll_right:
    xpos 960
    credits_text_scroll

transform credits_text_scroll_left:
    xpos 320
    credits_text_scroll

transform credits_sticker_1:
    yanchor 1.00
    xalign 0.32
    credits_sticker_scroll
transform credits_sticker_2:
    yanchor 1.00
    xalign 0.44
    credits_sticker_scroll
transform credits_sticker_3:
    yanchor 1.00
    xalign 0.56
    credits_sticker_scroll
transform credits_sticker_4:
    yanchor 1.00
    xalign 0.68
    credits_sticker_scroll

define credits_ypos = 100

#This defines the Karaoke for Monika's singing

image mcredits_1a:
    ypos credits_ypos
    xoffset -150
    "black"
    10.33
    Text("Gracias por jugar a este mod", style="red_credits_text") with ImageDissolve("images/menu/wipedown.png", 15.0, ramplen=4, alpha=False)
image mcredits_1b:
    ypos credits_ypos
    xoffset 145
    "black"
    13.33
    Text("...de nuevo.", style="red_credits_text") with ImageDissolve("images/menu/wipedown.png", 15.0, ramplen=4, alpha=False)
image mcredits_2a:
    ypos credits_ypos + 100
    xoffset 0
    "black"
    16.33
    Text("Lamento mucho si fue algo corto, sólo quise hacerlo para promocionar mi sistema de combate :')", style="red_credits_text") with ImageDissolve("images/menu/wipedown.png", 15.0, ramplen=4, alpha=False)
image mcredits_3a:
    ypos credits_ypos + 170
    xoffset 0
    "black"
    19.33
    Text("Tenía planeado hacer un mod más grande con esto, pero me temo que no dispongo del tiempo suficiente para hacerlo...", style="red_credits_text") with ImageDissolve("images/menu/wipedown.png", 15.0, ramplen=4, alpha=False)
image mcredits_4a:
    ypos credits_ypos + 220
    xoffset -525
    "black"
    22.95
    Text("Sin embargo...", style="red_credits_text") with ImageDissolve("images/menu/wipedown.png", 15.0, ramplen=4, alpha=False)
image mcredits_5a:
    ypos credits_ypos + 220
    xoffset 70
    "black"
    26.33
    Text("Una vez terminen los créditos, podrás mirar unos avances incompletos de dicho mod.", style="red_credits_text") with ImageDissolve("images/menu/wipedown.png", 15.0, ramplen=4, alpha=False)

image mcredits_5b:
    ypos credits_ypos + 270
    xoffset 0
    "black"
    29.33
    Text("Digamos un... Una \"Alpha\" de la \"Demo\" de mi verdadero proyecto...", style="red_credits_text") with ImageDissolve("images/menu/wipedown.png", 15.0, ramplen=4, alpha=False)

image mcredits_6a:
    ypos credits_ypos + 220
    xoffset 70
    "black"
    26.33
    Text("Podrás acceder a porciones de dicho proyecto una vez me lleves al Nivel 40.", style="red_credits_text") with ImageDissolve("images/menu/wipedown.png", 15.0, ramplen=4, alpha=False)

image mcredits_6b:
    ypos credits_ypos + 270
    xoffset 0
    "black"
    29.33
    Text("Digamos un... Una \"Alpha\" de la \"Demo\" de ese verdadero proyecto mío...", style="red_credits_text") with ImageDissolve("images/menu/wipedown.png", 15.0, ramplen=4, alpha=False)

image mcredits_7a:
    ypos credits_ypos + 375
    xoffset 0
    "black"
    33.33
    Text("Bueno, dejo de hablar y te dejo mirar los créditos. ¡Nos vemos luego!", style="red_credits_text") with ImageDissolve("images/menu/wipedown.png", 15.0, ramplen=4, alpha=False)

image mcredits_8a:
    ypos credits_ypos + 550
    xoffset 250
    "black"
    37.33
    Text("- Te saluda... DavidCARP1996 a.k.a el creador del mod", style="red_credits_text") with ImageDissolve("images/menu/wipedown.png", 30.0, ramplen=4, alpha=False)

image mcredits_9a:
    ypos credits_ypos + 600
    xoffset 300
    "black"
    42.33
    Text("Gracias [player], the Main Character.", style="red_credits_text") with ImageDissolve("images/menu/wipedown.png", 65.0, ramplen=4, alpha=False)

image mcredits_1_test:
    ypos credits_ypos + 350
    Text("Te saluda... [player], the Main Character.", style="red_credits_text") with ImageDissolve("images/menu/wipedown.png", 50.0, ramplen=4)

image mcredits_bye:
    "black"
    alpha 0.0
    47.33
    linear 1.5 alpha 1.0

image mcredits_666a:
    ypos credits_ypos + 150
    xoffset -5
    "black"
    45.9
    Text("NO NECESITAMOS ESA MIERDA, AHORA SOY EL DIOS DE ESTE MUNDO !!!", style="red_credits_text") with ImageDissolve("images/menu/wipedown.png", 9.0, ramplen=4, alpha=False)

image mcredits_666b:
    ypos credits_ypos + 200
    xoffset -5
    "black"
    45.9
    Text("MUAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA !!!", style="red_credits_text") with ImageDissolve("images/menu/wipedown.png", 9.0, ramplen=4, alpha=False)

#Glitchy images
image end_glitch1:
    "bg/end-glitch1.jpg"
    alpha 0.0
    time 1.0
    alpha 1.0
    block:
        yoffset 1280 ytile 2
        linear 1 yoffset 0
        repeat
    time 9.45
    "end_glitch2"
    time 22.1
    "end_glitch3"
    time 28.65
    "end_glitch4"

image end_glitch2:
    "bg/end-glitch2.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch3:
    "bg/end-glitch3.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch4:
    parallel:
        "bg/end-glitch4.jpg"
        1.25
        "bg/end-glitch3.jpg"
        0.1
        repeat
    parallel:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

#Start for the actual credits scene
label credits:
    $ persistent.autoload = "credits" #Come back to the credits if the game is quit
    #Disable player interactions
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black

    #Play monika's song with Karaoke lines
    pause 1
    scene black
    pause 0.5
    $ consolehistory = []
    call updateconsole("os.deleting(\"characters/mc.chr\")", "mc.chr borrado exitosamente.") from _call_updateconsole
    $ delete_character("mc")
    pause 1.0
    call hideconsole from _call_hideconsole
    play music "<to 50.0>mod_bgm/credits_instrumental.mp3" noloop

    show mcredits_1a zorder 50
    show mcredits_1b zorder 49
    show mcredits_2a zorder 48
    show mcredits_3a zorder 47
    show mcredits_4a zorder 46
    if mc_lv >= 100:
        show mcredits_666a zorder 2
        show mcredits_666b zorder 1
        jump ch30_main
    elif mc_lv >= 40:
        show mcredits_5a zorder 45
        show mcredits_5b zorder 44
    else:
        show mcredits_6a zorder 45
        show mcredits_6b zorder 44
    show mcredits_7a zorder 43
    show mcredits_8a zorder 42
    show mcredits_9a zorder 41
    show mcredits_bye zorder 51


    pause 50
    jump credits2

#This is where the credits scroll starts
label credits2:
    python:
        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = 0
        natsukiPos = 0
        yuriPos = 0
        monikaPos = 0
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
        imagenum = 0
    scene black
    $ consolehistory = []
    play music "<from 50.0>mod_bgm/credits_instrumental.mp3" noloop
    $ starttime = datetime.datetime.now()
    pause 0.88
    show credits_logo
    pause 9.12
    #Each CG is shown. If it's unseen gray it out, if it's not a perfect ending
    #make each image get deleted after a few seconds
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    show image ("credits_cg1" + lockedtext) at credits_scroll_right as credits_image_1

    #Actual names for the credits
    show credits_header "Original Concept\n& Game Design" at credits_text_scroll_left as credits_header_1
    show credits_text "Dan Salvato" at credits_text_scroll_left as credits_text_1

    ##The rest of the sections follow this same pattern
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png deleted successfully.") from _call_updateconsole_1
    else:
        call updateconsole_clearall("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png deleted successfully.") from _call_updateconsole_clearall
    show image ("credits_cg2" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "Original Character Art" at credits_text_scroll_right as credits_header_2
    show credits_text "Satchely" at credits_text_scroll_right as credits_text_2
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png deleted successfully.") from _call_updateconsole_2
    else:
        call updateconsole_clearall("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png deleted successfully.") from _call_updateconsole_clearall_1
    show image ("credits_cg3" + lockedtext) at credits_scroll_right as credits_image_1
    show credits_header "Original Background Art" at credits_text_scroll_left as credits_header_1
    show credits_text "Velinquent" at credits_text_scroll_left as credits_text_1
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png deleted successfully.") from _call_updateconsole_3
    else:
        call updateconsole_clearall("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png deleted successfully.") from _call_updateconsole_clearall_2
    show image ("credits_cg4" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "Original Writing" at credits_text_scroll_right as credits_header_2
    show credits_text "Dan Salvato" at credits_text_scroll_right as credits_text_2
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png deleted successfully.") from _call_updateconsole_4
    else:
        call updateconsole_clearall("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png deleted successfully.") from _call_updateconsole_clearall_3
    show image ("credits_cg5" + lockedtext) at credits_scroll_right as credits_image_1
    show credits_header "Original Music" at credits_text_scroll_left as credits_header_1
    show credits_text "Dan Salvato" at credits_text_scroll_left as credits_text_1
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png deleted successfully.") from _call_updateconsole_5
    else:
        call updateconsole_clearall("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png deleted successfully.") from _call_updateconsole_clearall_4
    show image ("credits_cg6" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "Vocals" at credits_text_scroll_right as credits_header_2
    show credits_text "Jillian Ashcraft as Monika" at credits_text_scroll_right as credits_text_2
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png deleted successfully.") from _call_updateconsole_6
    else:
        call updateconsole_clearall("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png deleted successfully.") from _call_updateconsole_clearall_5
    show image ("credits_cg7" + lockedtext) at credits_scroll_right as credits_image_1
    show credits_header "Mod Music" at credits_text_scroll_left as credits_header_1
    show credits_text "Dulux\nG-RiNe Project\nKevin MacLeod\nDDMC Community Assets\nTony K\nJay Man\nI must find other's name :c" at credits_text_scroll_left as credits_text_1
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png deleted successfully.") from _call_updateconsole_7
    else:
        call updateconsole_clearall("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png deleted successfully.") from _call_updateconsole_clearall_6
    show image ("credits_cg8" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "Mod Backgrounds" at credits_text_scroll_right as credits_header_2
    show credits_text "DDMC Community Assets\nI must find other's names too :c" at credits_text_scroll_right as credits_text_2
    show s_sticker at credits_sticker_1
    show n_sticker at credits_sticker_2
    show y_sticker at credits_sticker_3
    show m_sticker at credits_sticker_4
    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png deleted successfully.") from _call_updateconsole_8
    else:
        call updateconsole_clearall("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png deleted successfully.") from _call_updateconsole_clearall_7
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    show image ("credits_cg9" + lockedtext) at credits_scroll_right as credits_image_1
    show credits_header "Mod Concept & Game Design" at credits_text_scroll_left as credits_header_1
    show credits_text "DavidCARP1996\n[player]" at credits_text_scroll_left as credits_text_1
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/s_cg3.png\")", "s_cg3.png deleted successfully.") from _call_updateconsole_9
    else:
        call updateconsole_clearall("os.remove(\"images/cg/s_cg3.png\")", "s_cg3.png deleted successfully.") from _call_updateconsole_clearall_8
    show image ("credits_cg10" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "Special Thanks" at credits_text_scroll_right as credits_header_2
    show credits_text "YOU for playing the mod <3" at credits_text_scroll_right as credits_text_2
    $ pause(104.10 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png deleted successfully.") from _call_updateconsole_10
    else:
        call updateconsole_clearall("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png deleted successfully.") from _call_updateconsole_clearall_9
    #pause 4.0
    call updateconsole("os.remove(\"game/screens.rpy\")", "screens.rpy deleted successfully.") from _call_updateconsole_11
    call updateconsole("os.remove(\"game/gui.rpy\")", "gui.rpy deleted successfully.") from _call_updateconsole_12
    call updateconsole("os.remove(\"game/menu.rpy\")", "menu.rpy deleted successfully.") from _call_updateconsole_13
    call updateconsole("os.remove(\"game/script.rpy\")", "script.rpy deleted successfully.") from _call_updateconsole_14
    $ pause(115.72 - (datetime.datetime.now() - starttime).total_seconds())

    #Hide console and show the Team salvato logo and thankyou
    call hideconsole from _call_hideconsole_1
    show credits_ts
    show credits_text "made with love by":
        zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
        linear 2.0 alpha 1
        4.5
        linear 2.0 alpha 0
    pause 9.3
    jump thankyou
    #play sound page_turn
    #show poem_end with Dissolve(1)

    #Fade to black and make player quit
    label postcredits_loop:
        #$ persistent.autoload = "postcredits_loop" #If the game quits come back here
        $ persistent.autoload = None

        #Disable player input
        $ config.keymap['game_menu'] = []
        $ config.keymap['hide_windows'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False

        #Fade to black
        scene black
        show poem_end #Show special ending message
        $ pause()
        #Make player quit
        call screen dialog(message="Error 404: Error Not Found.\nPlease reboot the game.", ok_action=Quit(confirm=False))
        return
