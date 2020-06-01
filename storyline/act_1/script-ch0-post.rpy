label ch0_post:
    $ ch0_activities = 0
    $ stamina = 10
    $ hr_hour = 17
    $ park_closed = False
    $ cafe_closed = False
    $ gamestore_closed = False
    $ library_closed = False
    stop music fadeout 2.0
    scene bg house
    with wipeleft_scene
    pause 3.0
    "..."
    "What?"
    "Do you think I'm just gonna go in my house, jump to the poem game, and then automatically start at the Literature Club?"
    "Hahahahahaha!"
    "No, fuck you."
    "Now I'm out of school, and some free time, let's have some fun! Okay?"
    "Also, maybe we can encounter Yuri or someone else from the Club, and meet them better."
    $ HKBShowButtons()
    "..."
    "But..."
    "I don't know where to go..."
    pass

label ch0_post_loop:
    while (stamina > 0) and (hr_hour <= 20):
        show screen freeroam_hud
        with Dissolve(.5)
        play music t5
        if ch0_activities == 0:
            $ menutext = "Where should I go first?"
        else:
            $ menutext = "Where should I go next?"
        menu:
            "[menutext]"

            "Go to the park" if not park_closed:
                $ ch0_activities += 1
                #$ goto_park = True
                call ch0_go_to_park
                pass
            "Go to the cafe" if not cafe_closed:
                $ ch0_activities += 1
                #$ goto_cafe = True
                call ch0_go_to_cafe
                pass
            "Go to the gaming store" if not gamestore_closed:
                $ ch0_activities += 1
                #$ goto_gamestore = True
                call ch0_go_to_gaming_store
                pass
            "Go to the library" if not library_closed:
                $ ch0_activities += 1
                #$ goto_library = True
                call ch0_go_to_library
                pass
            "Go home":
                jump ch0_go_home
                pass

        pass
    jump ch0_go_home

    label ch0_go_to_park:
        mc "Well then, let's have a walk in the park."
        mc "I need to do some exercises anyway..."
        scene bg park_way
        with wipeleft_scene
        mc "Well, let's take 20 laps on the circuit."
        pause 1.0
        "This place give me some good memories..."
        "When I was a child, I used to play with Sayori running around, playing to races, or any other activities what childs do."
        "But now, we've grown up, so here's a low chance to revive those nice moments."
        "Also, I'm not in a good condition for that. The best exercise I can do is just walking around."
        "Geez, I miss those moments where I was able to run, dribbling people, do high jumps..."
        mc "Oh man, I'm only 18 and I'm talking like an fucking oldman!"
        "I take a break, that thought just took me down."
        stop music fadeout 2.0
        "..."
        "The only thing what I'm seeing are a lot of couples having a nice day, and also kids playing around."
        "Everyone seems happy about their lifes."
        "Why not me?"
        mc "Why not me?!"
        mc "..."
        "Some people starts to look at me, like if I have done something weird. Did I just spooke in high voice?"
        mc "Fuck!"
        mc "I need something to eat..."
        mc "I'm get the fuck out of here!"
        scene bg residential_day
        with wipeleft_scene
        $ stamina -= 3
        $ park_closed = True

        return

    label ch0_go_to_cafe:
        mc "I'm hungry."
        mc "Let's get something to eat, okay?"
        scene bg cafe
        with wipeleft_scene
        mc "Hmm..."
        menu:
            "What should I have for snack?"

            "Coffee with milk & croissants - $250":
                mc "..."
                pause 5.0
                $ mc_hp = mc_hp_max
                $ mc_mp = mc_mp_max
                "Oh man..."
                "This was delicious!"
                $ money -= 250
                pass
            "Orange juice & ham and cheese toast - $280":
                mc "..."
                pause 5.0
                $ mc_hp = mc_hp_max
                $ mc_mp = mc_mp_max
                "Oh man..."
                "This was delicious!"
                $ money -= 280
                pass
            "Strawberry smoothie & portion of cake - $320":
                mc "..."
                pause 5.0
                $ mc_hp = mc_hp_max
                $ mc_mp = mc_mp_max
                "Oh man..."
                "This was delicious!"
                $ money -= 320
                pass
        "Alright, let's pay the bill and let's go somewhere else..."
        scene bg residential_day
        with wipeleft_scene
        $ stamina -= 1
        $ cafe_closed = True

        return

    label ch0_go_to_gaming_store:
        mc "I want to see that game I've looking for so long."
        mc "Let's check the gaming store if it's available to buy..."
        scene bg gamingstore
        with wipeleft_scene
        mc "Hmm..."
        "Here it is!"
        "That new 'Car Thief' game for PC it's here. But..."
        mc "That shit costs $6000???"
        mc "Fuck!"
        mc "I don't even know if this can run in my computer..."
        menu:
            mc "..."

            "Buy\n Car Thief 5: $6000":
                if money >= 6000:
                    mc "Ok, I hope it's worth..."
                    $ money -= 6000
                    "[player] bought Car Thiefs 5."
                    pass
                else:
                    mc "No! I don't have such money by the way..."
                    pass
            "Don't buy anything":
                mc "I pass, for now."
                pass
        "Alright, let's go somewhere else..."
        scene bg residential_day
        with wipeleft_scene
        $ stamina -= 1
        $ gamestore_closed = True

        return

    label ch0_go_to_library:
        mc "If I want to impress Yuri or anybody from the Literature Club, the first thing I must do is..."
        mc "Going to a library and get some 'Literature skills'."

        if persistent.ytellyouherbookstore == True:
            "Let's go to the bookstore Yuri mentioned."
            "IT WORKED! HAHAHAHAHAHAHAHAHAHAHA! IT WORKS! THANKS MYSTERIOUS LADY!"
            scene bg library_old
            with wipeleft_scene
            "Well, as I said before... Sayori could like happy stuff, Natsuki anime stuff, Yuri horror and complex stuff, and Monika about epiphany."
            "Oh yes, I remember everything, hehe~!"
            mc "Eh?"
            mc "Hey! Yuri~!"
            play music tyuri
            show yuri 1e at t11 zorder 2
            y "Hmm?"
            y 1b "Oh! [player]... What a surprise! It's nice to see you here, with me..."
            mc "I think the same thing Yuri..."
            show yuri 1a
            mc "I was looking for a nice bookstore, and I've heard good things about here."
            mc "Now I can see everything was true, this place is so nice..."
            y 1c "Indeed, this place is awesome. You can find every kind of book here and the atmosphere is ideal."
            y 2j "I was... Looking for something to get inspired for the tomorrow's poem."
            y 2q "Y-you too?"
            mc "Correct."
            show yuri 1e
            mc "Honestly, I'm pretty bad about poem stuff. And I'm looking for something everybody could love in the club."
            mc "You gave me a hint in the club, so now I know where can I start first."
            y 4 "That's... nice of your part..."
            y "I hope you can find a nice book."
            mc "Thanks Yuri."
            y 4e "Don't mention it."
            y "Umm... Do you, will take much?"
            mc "I hope don't... If you're asking to walk together, I'll go the fast I can."
            y 2v "Don't push yourself. I-I can wait for you in the entrance if you want..."
            mc "I will do my best Yuri, don't worry."
            y 2s "Good, then I will pay these books I choose and I will wait for you."
            mc "Alright, hang on darling."
            show yuri at thide
            hide yuri
            "I guess that last line was too much..."
            "YES!!! I have a chance to talk with Yuri!"
            "But first, I must choose the best books what I can..."
            pass
        else:
            scene bg library
            with wipeleft_scene
            "If I want to write a good poem, first I must read something inspirative."
            "But... I don't know what kind of stuffs could like the girls of the club."
            "All I know is: Sayori likes happy stuffs, Yuri likes horror and complex stuffs, Natsuki could like... anime stuffs?"
            "Monika is the most complicated, but if she's the president, then I can try anything related to literature..."
            "I don't know, maybe they could like anything more else and I don't know that fact."
            mc "Hmm..."
            mc "..."
            pause 5.0
            mc "What the...?!"
            show monika 2 at t11 zorder 2
            m "Hey! [player]!"
            m 2b "Looking for some literature to get inspired?"
            mc "Ehm... Yes!"
            show monika 2
            "I didn't expect to meet her here, I though she could go around with any of the popular boys... but here, alone?"
            m 3b "That's sounds good."
            m "There's no better way to write poems by get inspired on famous artists."
            m 5 "Also, reading such great books can improve your knowledge skills, you know?"
            m "Hehehe~!"
            "Is she teasing me? Who she's think I am, an ignorant fuck?"
            m 1 "Hey!"
            m "I have a suggestion for you..."
            mc "What?"
            m 1n "Well..."
            m 2n "I've reading more about epiphany stuffs actually... And..."
            "..."
            if money < 500:
                m 1c "Here..."
                $ money += 500
                "Monika gives you $500."
                mc "Why are you giving me money?"
                m 1e "For books you dummy..."
                m 1n "Dude, the books here aren't free, you know?"
                mc "Huh-uh... I guess..."
                m 1m "Well..."
            else:
                m 1l "Whatever."
                m 1m "I must warn you... The books here doesn't cost less than $500."
                "What the fuck?!"
                "How much I need to purchase the best four books about the girls?"
            m 1n "Just go and search for the best books you can read, ok?"   
            m "It's up on you to choose what to read first."
            mc "Okay! Thanks Monika..."
            m 1k "Don't mention it."
            m "Alright, I see you tomorrow [player]~!"
            show monika at lhide
            hide monika
            pause 2.0
            show monika 1 at l41
            m "Oh, by the way..."
            m "The library will close soon, so hurry up and choose your book."
            m "Because once you get out of here, you must wait until tomorrow..."
            show monika at lhide
            hide monika
            "Monika lefts the library"
            mc "Shit, I must hurry!"
            pass

        $ books_bought = 0
        $ exit_library = False
        #while exit_library == False or "(Book) Happy Thoughts", "(Book) Dark in the blossoms", "(Book) How to understand a tsundere", "(Book) Shadows of epiphany" not in keyitems or money < 500:
        while (money > 500) and (not exit_library):

            menu:
                "Alright, let's see..."
                "Happy Thoughts \n $650" if not sbook_bought:
                    mc "..."
                    mc "Sayori may like this one..."
                    menu:
                        "Buy Happy Thoughts ($650)?"
                        "Yes":
                            $ money -= 650
                            $ sbook_bought = True
                            $ bag_inventory.add_item("sbook1", score=1)
                            "You bought the book \"Happy Thoughts\"."
                            $ books_bought += 1
                        "No":
                            pass
                "Dark in the blossoms \n $680" if not ybook_bought:
                    mc "..."
                    mc "Could Yuri love this?"
                    menu:
                        "Buy Dark in the blossoms ($680)?"
                        "Yes":
                            $ money -= 680
                            $ ybook_bought = True
                            $ bag_inventory.add_item("ybook1", score=1)
                            "You bought the book \"Dark in the blossoms\"."
                            $ books_bought += 1
                        "No":
                            pass
                "Anime & Stuff \n $760" if not nbook_bought:
                    mc "..."
                    mc "Maybe this can help me with Natsuki..."
                    menu:
                        "Anime & Stuff ($760)?"
                        "Yes":
                            $ money -= 760
                            $ nbook_bought = True
                            $ bag_inventory.add_item("nbook1", score=1)
                            "You bought the book \"Anime & Stuff\"."
                            $ books_bought += 1
                        "No":
                            pass
                "Shadows of epiphany \n $500" if not mbook_bought:
                    mc "..."
                    mc "So, this is the book that Monika talked about..."
                    menu:
                        "Buy Shadows of epiphany ($500)?"
                        "Yes":
                            $ money -= 500
                            $ mbook_bought = True
                            $ bag_inventory.add_item("mbook1", score=1)
                            "You bought the book \"Shadows of epiphany\"."
                            $ books_bought += 1
                        "No":
                            pass
                "Exit" if books_bought >= 1:
                    $ exit_library = True
                    pass

        if persistent.ytellyouherbookstore == True:
            "I think I'm done. Let's go with Yuri."
            show yuri 1d at t11 zorder 2
            y "Are you ready?"
            mc "Yes. Let's go..."

            scene black
            with wipeleft_scene
            pause 2.0
            show bg yuri_house
            with wipeleft_scene

            show yuri 4e at t11 zorder 2
            y "T-thanks for taking me to my house [player]..."
            y "Sayori is very fortunate for having you has her best friend."
            mc "Hehe~, I guess you're right."
            mc "But now I am very, very fortunate for having both of you has friends."
            y 2v "I..."
            "I said it with the bottom of my heart. I hope she doesn't get mad or something."
            y 2u "I'm also very, very fortunate to meet you..."
            y 2s "I hope we can... well, get our relationship more far..."
            y 3p "Ah, I'm not implying to change Sayori for me or something, I..."
            mc "Don't worry Yuri, both of you are very important for me at equally."
            show yuri 3t
            mc "No matter with who I want to spend the time, I will do my best to make them happy at the same time."
            y 2s "I can see you are a nice person."
            y 1q "Well, see you tomorrow then?"
            mc "Yes. I see you tomorrow Yuri..."
            y 1d "Thanks... See you later~!"
            show yuri at thide
            hide yuri
            pause 1.0
            "Really, I could love to spend more time with her..."
            "She's so beautiful... so smart... so elegant... so sexy..."
            "..."
            "Alright, let's go somewhere else."
            pass
        else:
            "I think I'm done. Let's go somewhere else..."
            pass
        $ library_closed = True
        scene bg residential_day
        with wipeleft_scene
        $ stamina -= 1
        #jump ch0_post_loop

        return

label ch0_go_home:
    stop music fadeout 2.0
    hide screen freeroam_hud
    $ HKBShowButtons()
    $ HKBHideButtons()
    with Dissolve(.5)
    pass
    if menutext == "Where should I go next?" or stamina <= 0:
        mc "Finally! Home sweet home..."
        mc "I'm tired, you know?"
    mc "..."
    mc "You know what?"
    mc "Fuck this shit."
    mc "I'm so fucking tired, that I prefer to take a nap before start to write a fucking poem."
    scene bg bedroom
    with wipeleft_scene
    pause 1.0
    play sound click
    scene bg bedroom_dark
    mc "Yeah!"
    mc "Let's do that poem shit another time..."
    mc "Zzzzzzzzzzz..."
    scene black
    with dissolve_scene_full
    pause 1.0
    scene bg bedroom_dark
    with dissolve_scene_full
    "..."
    mc "Hm? 23 PM?"
    mc "Did I fall asleep in the middle of the afternoon?"
    mc "Shit..."
    play sound click
    scene bg bedroom
    mc "The poem!"
    mc "I didn't did it!"
    mc "Alright alright..."
    mc "There's still time left. Once it finished, I'll sleep again."
    mc "First of all, I'll go make coffee and a sandwich because I get hungry."
    scene black
    with dissolve_scene_full
    pause 2.0
    scene bg bedroom
    with dissolve_scene_full
    mc "Okay? Let's go!"

return

