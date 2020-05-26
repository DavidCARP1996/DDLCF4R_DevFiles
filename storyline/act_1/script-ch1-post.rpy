label ch1_post:
    $ ch1_post_activities = 0
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
    "You know what?"
    "I'm thirsty... I want to go to the cafeteria and drink something."
    $ HKBShowButtons()
    "So, let's go!"
    "And if you want, we can do something else..."
    pass

label ch1_post_loop:
    while (stamina > 0) and (hr_hour <= 20):
        show screen freeroam_hud
        with Dissolve(.5)
        play music t5
        if ch1_post_activities == 0:
            $ menutext = "Where should I go first?"
        else:
            $ menutext = "Where should I go next?"
        menu:
            "[menutext]"

            "Go to the park" if not park_closed:
                $ ch1_post_activities += 1
                call ch1_post_go_to_park
                pass
            "Go to the cafe" if not cafe_closed:
                $ ch1_post_activities += 1
                call ch1_post_go_to_cafe
                pass
            "Go to the gaming store" if not gamestore_closed:
                $ ch1_post_activities += 1
                call ch1_post_go_to_gaming_store
                pass
            "Go to the library" if not library_closed:
                $ ch1_post_activities += 1
                call ch1_post_go_to_library
                pass
            "Go home":
                jump ch1_post_go_home
                pass

        pass
    jump ch1_post_go_home

    label ch1_post_go_to_park:
        mc "Well then, let's have a walk in the park."
        mc "I need to do some exercises anyway..."
        scene bg park way
        with wipeleft_scene
        mc "Hmmm... It's weird."
        mc "Why it's so loud in that point?"
        mc "Let's check it out..."
        scene bg park way 2
        with wipeleft_scene
        "What's happening...?"
        stop music fadeout 2.0
        mc "Oh-oh!"
        "Woman" "Please somebody stop him!"
        "So was that! An robber in this park!"
        "Some guys are trying to stop him, but..."
        "Man 1" "Hey you! Stop!"
        "*bonk!*"
        "Man 1" "Aahhh!!!"
        "Man 2" "I will stop him!"
        "*bonk!*"
        "Man 2" "You piece of sh...!"
        "Shit, both were beaten up..."
        menu:
            "Try to chase him!":
                $ HKBShowButtons()
                $ HKBHideButtons()
                hide screen freeroam_hud
                with Dissolve(.5)
                mc "Well, I guess I must do it by myself."
                call ch1_battle_2
                $ HKBShowButtons()
                mc "Phew! That was close..."
                $ bag_inventory.add_item("pistol", score=1)
                "[player] received 9mm pistol."
                if battle_extra_rewards_rate <= 5:
                    mc "!"
                    $ money += 2000
                    "[player] received $2000 additional."
                    mc "Nice!"
                "Cop" "Hey you!"
                mc "Wha-?"
                "Thank goodness I hide the pistol just in time..."
                "Cop" "Didn't you killed him, isn't?"
                mc "Well..."
                "I check his corpse... Fuck, he's dead."
                mc "I..."
                "Cop" "I guess you must come with me to the Police station because of homicide."
                mc "WHAT THE FUCK?! THAT ASSHOLE WAS TRYING TO KILL ME WITH A GUN!! I TRIED TO STOP IT AT ANY COST!! I DEFENDED MY OWN LIFE!!!"
                mc "AND ONE MORE THING... IF I {nw}"
                $ gtext = glitchtext(4)
                $ gtext2 = glitchtext(80)
                "[gtext]" "{cps=60}[gtext2]{/cps}{nw}"
                show screen tear(20, 0.1, 0.1, 0, 40)
                play sound "sfx/s_kill_glitch1.ogg"
                pause 0.25
                stop sound
                hide screen tear
                "Cop" "I mean, congratulations boy!"
                "Cop" "If people were like you, there would be less criminals on the streets."
                mc "I..."
                "What did just happened?!"
                "Cop" "Here is your reward for good citizen boy."
                $ money += 500
                "[player] received $500."
                mc "Ehm... Thank you...(?)"
                "Cop" "It was nothing boy, good luck!"
                "The cop leaves me alone."
                mc "..."
                scene bg park way
                with wipeleft_scene
                $ money += 500
                "I move away from the scene, giving back the wallet to the woman on the way."
                "She gave me $500 too."
                "I take a sit un a bench."
                mc "What the fuck did just happened?"
                mc "First I kill that asshole and the cop was trying to arrest me, but then he changed of mind..."
                mc "*sigh*"
                pause 1.0
                show monika 1e at t11 zorder 1
                m "[player], are you okay?"
                mc "Monika?! What are you doing here?"
                mc "I-I mean... Did you saw ev-"
                m "Yes, I do."
                m "Thank goodness you were able to win."
                m "Otherwise, we'll be still 4 members in the club. Hahaha~!"
                "What's so funny? I would be fucking dead right now!"
                m "Anyway. I'm so glad you're okay after all!"
                m "Sayori could be very sad if something happens to you."
                "After Monika said that, I feel like my stomach is twisting for no reason."
                m "So, do you want to take you to your house?"
                menu:
                    "Sorry, but I have things to do...":
                        m "Hmm... Okay!"
                        m "Good luck with your bussiness~!"
                        mc "Thanks Monika."
                        mc "I see you later!"
                        show monika at thide zorder 1
                        hide monika
                        "Alright, let's go somewhere else..."
                        scene bg residential_day
                        with wipeleft_scene
                        $ stamina -= 4
                        pass
                    "Sure...":
                        m "Alright! I'll take you in my car then."
                        m "Come with me."
                        mc "Okay!"
                        scene bg house
                        with wipeleft_scene
                        m "Here we are."
                        mc "Thanks Monika, I owe you one."
                        m "It was nothing."
                        m "So, see you tomorrow?"
                        mc "Yes Monika, see you tomorrow."
                        m "Fine. Good luck bro~!"
                        show monika at thide zorder 1
                        hide monika
                        "Monika's car is gone in the horizon..."
                        "Now what?"
                        $ stamina -= 1
                        pass
                show screen freeroam_hud
                with Dissolve(.5)

                pass
            "Ignore the situation...":
                mc "..."
                "He gone in the horizon."
                "Let's get the fuck out of here!"
                scene bg residential_day
                with wipeleft_scene
                pass

        $ park_closed = True
        return

    label ch1_post_go_to_cafe:
        mc "Hmm..."
        $ ch1_winner = poemwinner[0].capitalize()
        if poemwinner[0] == "Sayori" and backyard_check == False:
            $ menutext2 = "Should I invite Sayori?"
        else:
            $ menutext2 = "I want to share it with someone else... But with who?"

        menu:
            "[menutext2]"

            "Sayori":
                mc "Good idea, she will love this!"
                mc "Let's go to her home to pick up her and then let's go to the cafe."
                scene bg cafe
                with wipeleft_scene
                s "Thank you very much for taking me to eat [player]!"
                s "That's why you are my favourite person in the entire World!"
                mc "Hehe-! If you say so..."
                pass
            "[ch1_winner]" if poemwinner[0] != "Sayori":
                mc "It's not bad idea after all... I can get more chances to know her better!"
                mc "I feel bad about not inviting Sayori, but my wallet is not so big, you know..."
                mc "I'm gonna call her so we can meet in the cafe."
                scene bg cafe
                with wipeleft_scene
                if ch1_winner == "Yuri":
                    if ch1_choice == "yuri":
                        y "Thank you for inviting me to eat [player], it's very nice from your part..."
                        y "I-If you don't mind, I brought a book with me... I mean, if you want to read something while we're waiting for our food."
                        mc "Hehe-! No problem Yuri. I was planing to talk about each other, but if you want to read then-"
                        y "I..."
                        y "Well, that's nice too..."
                        "Oh-oh, I'm in trouble..."
                        menu:
                            "Let's read":
                                mc "I don't want to force you to talk if you don't want. I..."
                                mc "I guess reading is, something to share our interests too..."
                                mc "Right?"
                                y "You got a point!"
                                y "Well, don't you mind if we read something called..."
                                pass
                            "Let's talk":
                                mc "Listen Yuri, you know how much I love to read with you..."
                                mc "But, don't you think a little talk can help us to know each other a bit better?"
                                mc "I mean, I want to tell you stories about my life, the things what I love, your interests, and check if we have compatibilities on something we like."
                                mc "Isn't that how socializing works?"
                                y "I... I guess you're right..."
                                y "I would love to talk about m-my life too..."
                                y "Umm..."
                                y "Who starts first?"
                                pass
                    elif ch1_choice == "natsuki":
                        y "Thank you for inviting me to eat [player], it's very nice from your part..."
                        y "I-I hope the thing what happened in the club doesn't..."
                        mc "Don't worry Yuri, it wasn't your fault."
                        mc "In fact, I wanted to apologize about what I said in that moment."
                        mc "I mean, I knew Natsuki was wrong... But I thought the thing what I said was a neutral position, because I don't want troubles with anyone in the club."
                        mc "I never wanted to hurt you... You are a wonderful girl, you deserve the best."
                        "If with 'the best' I'm meaning to myself, I'm gonna laugh out loud... Hahahahahaha!"
                        y "That's... That's nice from your part..."
                        y "And yes, I will forgive you. Afterwards, you tried to calm the things down."
                        mc "Thank you very much Yuri... I wished for this!"
                        "I grab Yuri's hands in thanks."
                        y "It's nothing..."
                        y "I-I hope Natsuki stop beign so hot-headed... If she feels somebody is against to her ideologies, she starts to be defensive and tends to attack the people, even the ones she loves."
                        mc "Really? I never thought that she could behave like this."
                        mc "Well, maybe yes. She was the only one who wasn't nice to me when I enter in the club for first time, you know..."
                        y "It's a shame... She's a nice girl if she wants."
                        y "I hope we can do something for her, I have the feeling she's hiding something that got her in that state..."
                        mc "Hmm... Maybe you're right."
                        mc "Well, how much do you know about her?"
                        pass
                    else:
                        y "Thank you for inviting me to eat [player], it's very nice from your part..."
                        y "I thought you could like more spending time with Sayori, but..."
                        mc "Hey."
                        mc "She's just my best friend. Also, it was for her we met each other."
                        mc "Maybe she wants me to spend time with you. At least that's what I think."
                        y "Umm... Maybe you're right. She had that kind of energy about wanting both of us to befriend each other each time she talks me about you."
                        mc "I see... And, what kind of things she said about me?"
                        y "Well..."
                        pass
                    scene black
                    with dissolve_scene_full
                    scene bg cafe
                    with dissolve_scene_full
                    y "Oh my god... It was delicious!"
                    mc "And our conversation was very interesting."
                    y "Indeed."
                    y "Thank you very much for sharing this moment with me."
                    y "I hope we can repeat it again someday..."
                    mc "Me too Yuri."
                    pass
                elif ch1_winner == "Natsuki":
                    scene bg cafe
                    with wipeleft_scene
                    if ch1_choice == "yuri":
                        n "Hmph!"
                        n "Don't think I came here because you like the idea."
                        n "I guess you owe me an apology."
                        mc "What?!"
                        mc "Natsuki, please! Forget about that..."
                        n "..."
                        mc "Hush...! Listen."
                        mc "I-I'm sorry, okay?"
                        mc "I didn't wanted to hurt you or anything... I was, trying to be the more neutral what I could, that's all."
                        n "Hmph!"
                        pass
                    else:
                        n "Well, I'm here."
                        n "And thanks for inviting me to eat something!"
                        n "I'm dying for hungry..."
                        pass
                    pass
                elif ch1_winner == "Monika":
                    scene bg cafe
                    with wipeleft_scene
                    m "[player]! Thanks for inviting me for a coffee~!"
                    mc "No problem Monika..."
                    pass
                pass
            "Camilla" if backyard_check == True:
                mc "That's right! I must thank her for her will helping me."
                mc "I'm gonna call her so we can meet in the cafe."
                scene bg cafe
                with wipeleft_scene
                mcf2 "Hey~! [player]~! It's good to see you!"
                "She hugs me strongly..."
                mc "Me too Camilla."
                "I hug her back."
                mcf2 "Look, I saw that portion of cake and that give me hungry.. a lot to be exactly."
                mcf2 "Oh! And I want this banana smoothie too..."
                mc "No problem Camilla, for you, I could buy the entire cafeteria!"
                mcf2 "Hmm... Don't worry about the money. I will pay it."
                mc "C-Camilla, it's supposed it was me who invited you. It's my duty paying for anything we eat!"
                mcf2 "And what's the problem? I want to contribute with something too."
                "Geez... She wants to be nice to me at all costs."
                "I mean, since when the guest must pay for what the host invited her?"
                mcf2 "Ehm... Did you said something?"
                mc "What? Oh... It's nothing, I was rambling around because the Literature Club, that's all..."
                mcf2 "Oh! Sorry, I thought I said something bad."
                mc "Hehe... You didn't said anything bad Camilla."
                mc "In fact, I want to thank you again for the mission of searching Sayori."
                mcf2 "Hehe~! It was nothing darling, you know I will do anything for you."
                "She grabs my hands."
                mcf2 "Anything you ask, I will be there to help you."
                mc "Thanks Camilla... It's very nice from your part."
                mc "And remember that I can help you too if you need help in something."
                mcf2 "I know. After all, that's what friends do. Right?"
                "She's giving me a sweet and irresistible smile."
                "I imitate her..."
                mc "Right!"
                pass
            "Go alone":
                mc "Ahh, fuck it!"
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
                pass

        $ cafe_closed = True
        scene bg residential_day
        with wipeleft_scene
        $ stamina -= 1

        return

    label ch1_post_go_to_gaming_store:
        mc "I want to see that game I've looking for so long."
        mc "Let's check the gaming store if it's available to buy..."
        scene bg gaming store
        with wipeleft_scene
        mc "Hmm..."
        "Here it is!"
        "That new 'Car Thief' game for PC it's here. But..."
        mc "That shit costs $6000???"
        mc "Fuck!"
        mc "I don't even know if this can run in my computer..."
        mc "Eh???"
        mc "Wow! Symbol of Blaze: Destiny is finally here!"
        menu:
            mc "..."

            "Buy\n Car Thief 5 ($6000)":
                if money >= 6000:
                    mc "Ok, I hope it's worth..."
                    $ bag_inventory.add_item("mcvideogame", score=1)
                    $ money -= 6000
                    "[player] bought Car Thiefs 5."
                    pass
                else:
                    mc "No! I don't have such money by the way..."
                    pass
            "Buy\n Symbol of Blaze: Destiny ($3000)"
                if money >= 3000:
                    mc "Ok, I hope it's worth..."
                    $ bag_inventory.add_item("yvideogame", score=1)
                    $ money -= 3000
                    "[player] bought Symbol of Blaze: Destiny."
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

    label ch1_post_go_to_library:
        mc "Let's go to a library."

        if persistent.ytellyouherbookstore == True:
            "Let's go to the bookstore Yuri mentioned."
            scene bg library old
            with wipeleft_scene
            mc "..."
            "Fuck! No Yuri signals..."
            "Damn, I wanted to choose a book she likes."
            "Anyway, let's buy a book or let's get out of here."
            pass
        else:
            scene bg library day
            with wipeleft_scene
            "Alright, let's choose a book."
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

        "I think I'm done. Let's go somewhere else..."
        $ library_closed = True
        scene bg residential_day
        with wipeleft_scene
        $ stamina -= 1

        return

label ch1_post_go_home:
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
    scene bg bedroom dark
    mc "Yeah!"
    mc "Let's do that poem shit another time..."
    mc "Zzzzzzzzzzz..."
    scene black
    with dissolve_scene_full
    pause 1.0
    scene bg bedroom dark
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


                call ch1_go_to_cafe
                pass
            "Go to the gaming store" if not gamestore_closed:
                $ ch1_activities += 1
                call ch1_go_to_gaming_store
                pass
            "Go to the library" if not library_closed:
                $ ch1_activities += 1
                call ch1_go_to_library
                pass
            "Go home":
                jump ch1_go_home
                pass

        pass
    jump ch1_go_home

    label ch1_go_to_park:
        mc "Well then, let's have a walk in the park."
        mc "I need to do some exercises anyway..."
        scene bg park way
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
        #jump ch1_post_loop

        return

    label ch1_go_to_cafe:
        mc "Hmm..."
        if ch0_winner == "sayori" and backyard_check == False:
            $ menutext2 = "Should I invite Sayori?"
        else:
            $ menutext2 = "I want to share it with someone else... But with who?"

        menu:
            "[menutext2]"

            "Sayori":
                mc "Good idea, she will love this!"
                mc "Let's go to her home to pick up her and then let's go to the cafe."
                call ch1_cafe_choose_sayori
                pass
            "[ch0_winner]" if not ch0_winner == "sayori":
                mc "It's not bad idea after all... I can get more chances to know her better!"
                mc "I feel bad about not inviting Sayori, but my wallet is not so big, you know..."
                mc "I'm gonna call her so we can meet in the cafe."
                if ch0_winner == "yuri":
                    call ch1_cafe_choose_yuri
                elif ch0_winner == "natsuki":
                    call ch1_cafe_choose_natsuki
                elif ch0_winner == "monika":
                    call ch1_cafe_choose_monika
                pass
            "Camilla" if backyard_check == True:
                mc "That's right! I must thank her for her will helping me."
                mc "I'm gonna call her so we can meet in the cafe."
                call ch1_cafe_choose_camilla
                pass
            "Go alone":
                mc "Ahh, fuck it!"
                call ch1_cafe_choose_alone
                pass

        label ch1_cafe_choose_alone:
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

        label ch1_cafe_choose_sayori:
            scene bg cafe
            with wipeleft_scene
            s "Thank you very much for taking me to eat [player]!"
            s "That's why you are my favourite person in the entire World!"
            mc "Hehe-! If you say so..."
            pass

        label ch1_cafe_choose_yuri:
            scene bg cafe
            with wipeleft_scene
            if ch1_choice == "yuri":
                y "Thank you for inviting me to eat [player], it's very nice from your part..."
                y "I-If you don't mind, I brought a book with me... I mean, if you want to read something while we're waiting for our food."
                mc "Hehe-! No problem Yuri. I was planing to talk about each other, but if you want to read then-"
                y "I..."
                y "Well, that's nice too..."
                "Oh-oh, I'm in trouble..."
                menu:
                    "Let's read":
                        mc "I don't want to force you to talk if you don't want. I..."
                        mc "I guess reading is, something to share our interests too..."
                        mc "Right?"
                        y "You got a point!"
                        y "Well, don't you mind if we read something called..."
                        pass
                    "Let's talk":
                        mc "Listen Yuri, you know how much I love to read with you..."
                        mc "But, don't you think a little talk can help us to know each other a bit better?"
                        mc "I mean, I want to tell you stories about my life, the things what I love, your interests, and check if we have compatibilities on something we like."
                        mc "Isn't that how socializing works?"
                        y "I... I guess you're right..."
                        y "I would love to talk about m-my life too..."
                        y "Umm..."
                        y "Who starts first?"
                        pass
            elif ch1_choice == "natsuki":
                y "Thank you for inviting me to eat [player], it's very nice from your part..."
                y "I-I hope the thing what happened in the club doesn't..."
                mc "Don't worry Yuri, it wasn't your fault."
                mc "In fact, I wanted to apologize about what I said in that moment."
                mc "I mean, I knew Natsuki was wrong... But I thought the thing what I said was a neutral position, because I don't want troubles with anyone in the club."
                mc "I never wanted to hurt you... You are a wonderful girl, you deserve the best."
                "If with 'the best' I'm meaning to myself, I'm gonna laugh out loud... Hahahahahaha!"
                y "That's... That's nice from your part..."
                y "And yes, I will forgive you. Afterwards, you tried to calm the things down."
                mc "Thank you very much Yuri... I wished for this!"
                "I grab Yuri's hands in thanks."
                y "It's nothing..."
                y "I-I hope Natsuki stop beign so hot-headed... If she feels somebody is against to her ideologies, she starts to be defensive and tends to attack the people, even the ones she loves."
                mc "Really? I never thought that she could behave like this."
                mc "Well, maybe yes. She was the only one who wasn't nice to me when I enter in the club for first time, you know..."
                y "It's a shame... She's a nice girl if she wants."
                y "I hope we can do something for her, I have the feeling she's hiding something that got her in that state..."
                mc "Hmm... Maybe you're right."
                mc "Well, how much do you know about her?"
                pass
            else:
                y "Thank you for inviting me to eat [player], it's very nice from your part..."
                y "I thought you could like more spending time with Sayori, but..."
                mc "Hey."
                mc "She's just my best friend. Also, it was for her we met each other."
                mc "Maybe she wants me to spend time with you. At least that's what I think."
                y "Umm... Maybe you're right. She had that kind of energy about wanting both of us to befriend each other each time she talks me about you."
                mc "I see... And, what kind of things she said about me?"
                y "Well..."
                pass
            scene black
            with dissolve_scene_full
            pause 1.0
            scene scene bg cafe
            with dissolve_scene_full
            y "Oh my god... It was delicious!"
            mc "And our conversation was very interesting."
            y "Indeed."
            y "Thank you very much for sharing this moment with me."
            y "I hope we can repeat it again someday..."
            mc "Me too Yuri."

            return

        label ch1_cafe_choose_natsuki:
            scene bg cafe
            with wipeleft_scene
            if ch1_choice == "yuri":
                n "Hmph!"
                n "Don't think I came here because you like the idea."
                n "I guess you owe me an apology."
                mc "What?!"
                mc "Natsuki, please! Forget about that..."
                n "..."
                mc "Hush...! Listen."
                mc "I-I'm sorry, okay?"
                mc "I didn't wanted to hurt you or anything... I was, trying to be the more neutral what I could, that's all."
                n "Hmph!"
                pass
            else:
                n "Well, I'm here."
                n "And thanks for inviting me to eat something!"
                n "I'm dying for hungry..."
                pass

        label ch1_cafe_choose_monika:
            scene bg cafe
            with wipeleft_scene
            m "[player]! Thanks for inviting me for a coffee~!"
            mc "No problem Monika..."
            pass

        label ch1_cafe_choose_camilla:
            scene bg cafe
            with wipeleft_scene
            mcf2 "Hey~! [player]~! It's good to see you!"
            "She hugs me strongly..."
            mc "Me too Camilla."
            "I hug her back."
            mcf2 "Look, I saw that portion of cake and that give me hungry.. a lot to be exactly."
            mcf2 "Oh! And I want this banana smoothie too..."
            mc "No problem Camilla, for you, I could buy the entire cafeteria!"
            mcf2 "Hmm... Don't worry about the money. I will pay it."
            mc "C-Camilla, it's supposed it was me who invited you. It's my duty paying for anything we eat!"
            mcf2 "And what's the problem? I want to contribute with something too."
            "Geez... She wants to be nice to me at all costs."
            "I mean, since when the guest must pay for what the host invited her?"
            mcf2 "Ehm... Did you said something?"
            mc "What? Oh... It's nothing, I was rambling around because the Literature Club, that's all..."
            mcf2 "Oh! Sorry, I thought I said something bad."
            mc "Hehe... You didn't said anything bad Camilla."
            mc "In fact, I want to thank you again for the mission of searching Sayori."
            mcf2 "Hehe~! It was nothing darling, you know I will do anything for you."
            "She grabs my hands."
            mcf2 "Anything you ask, I will be there to help you."
            mc "Thanks Camilla... It's very nice from your part."
            mc "And remember that I can help you too if you need help in something."
            mcf2 "I know. After all, that's what friends do. Right?"
            "She's giving me a sweet and irresistible smile."
            "I imitate her..."
            mc "Right!"
            pass


        scene bg residential_day
        with wipeleft_scene
        $ stamina -= 2

        return

    label ch1_go_to_gaming_store:
        mc "I want to see that game I've looking for so long."
        mc "Let's check the gaming store if it's available to buy..."
        scene bg gaming store
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
        #jump ch1_post_loop

        return

    label ch1_go_to_library:
        mc "If I want to impress Yuri or anybody from the Literature Club, the first thing I must do is..."
        mc "Going to a library and get some 'Literature skills'."

        if persistent.ytellyouherbookstore == True:
            "Let's go to the bookstore Yuri mentioned."
            scene bg library day
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
            scene bg library day
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
            show bg yuri house
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
        #jump ch1_post_loop

        return

label ch1_go_home:
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
    scene bg bedroom dark
    mc "Yeah!"
    mc "Let's do that poem shit another time..."
    mc "Zzzzzzzzzzz..."
    scene black
    with dissolve_scene_full
    pause 1.0
    scene bg bedroom dark
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

