label ch3_prev:
    stop music fadeout 2.0
    with dissolve_scene_full
    
    scene bg bedroom
    with dissolve_scene_full
    $ ch3_winner = poemwinner[1].capitalize()
    mc "Aaaand it's done!"
    mc "Well, I guess I will play some videogames."
    "..."
    "If only I had bought that game..."
    mc "It's 23 PM."
    mc "I think I'd better go to sleep. I don't have such interesting games in my library to play."
    pause 0.5
    play sound click
    scene bg bedroom_night
    pause 0.5
    scene black
    with dissolve_scene_full
    pause 3.0
    scene bg bedroom
    with wipeleft_scene
    pause 1.0

    mc "..."
    mc "Eh?! 7:45 AM? I shall get ready for school!"
    pause 1.0
    mc "I've been thinking..."
    mc "Sayori is oversleeping more and more frequently lately."
    menu:
        mc "May should I wait for her again?"

        "Yes, do it for her.":
            mc "Fine."
            mc "Let's go to her house then."
            scene black
            with dissolve_scene_full
            pause 2.0
            jump ch2_prev_go_schoolA
            pass
        "No, you'll arrive very late.":
            mc "Are you sure?"
            mc "I don't want to be selfish with her, she doesn't deserve it..."
            menu:
                "You got a point.":
                    mc "Haha! See?"
                    mc "Don't worry, if she's not coming out, then I'll go alone."
                    mc "Let's go to her house then."
                    $ sayori_wait2 = True
                    scene black
                    with dissolve_scene_full
                    pause 2.0
                    jump ch2_prev_go_schoolA
                "Do what you want then!":
                    mc "Fuck you!"
                    mc "..."
                    mc "Whatever, just let's hope she doesn't get mad for this."
                    $ sayori_wait2 = False
                    scene black
                    with wipeleft_scene
                    pause 0.5
                    jump ch2_prev_go_schoolB

label ch1_prev_go_school_A:
    scene bg house
    with wipeleft_scene
    mc "Sayoriii~!"
    "..."
    mc "SAAAYOOOORIIIII----!!!"
    "..."
    "What's wrong with her? She's not even answering my phone."
    "I could enter to her house in case she's still sleeping but..."
    menu:
        "Do it.":
            mc "Alright then, let's go!"
            scene bg sayori_bedroom
            with dissolve_scene_full
            mc "What the fuck..."
            mc "She's not here?!"
            mc "Did she really went to the school without me?"
            mc "Or..."
            "..."
            mc "Ah, fuck this shit, let's go to the school then. Maybe she's waiting for me..."
            pass
        "Don't do that.":
            mc "Naaah!"
            mc "She may went sooner and she didn't advised me..."
            mc "Let's fucking go."
            pass
    jump ch2_prev_go_schoolB
    return

label ch2_prev_go_schoolB:
    play music t2
    scene bg school_entrance
    with wipeleft_scene
    #$ HKBShowButtons()
    "8:55 AM"
    "It's almost time to enter school..."
    "I'm worried about Sayori."
    mcf1 "Hey, [player]!"
    mc "Ryoma! What's up dude?"
return