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
    "I'm hungry... I want to go to the cafeteria and eat something."
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
                $ money += 100
                "[player] received $100."
                mc "Ehm... Thank you...(?)"
                "I said that with a mix of gratitude and WTF expressions."
                "Cop" "It was nothing boy, good luck!"
                "The cop leaves me alone."
                mc "..."
                scene bg park way
                with wipeleft_scene
                $ money += 100
                "I move away from the scene, giving back the wallet to the woman on the way."
                "She gave me $100 too."
                "I take a sit un a bench."
                mc "What the fuck did just happened?"
                mc "First I kill that asshole and the cop was trying to arrest me, but then he changed of mind..."
                mc "*sigh*"
                pause 1.0
                show monika at t11 zorder 1
                m 1d "[player], are you okay?"
                mc "Monika?! What are you doing here?"
                mc "I-I mean... Have you seen ev-"
                m 2a "Yes, I do."
                m "Thank goodness you were able to win."
                m 2l "Otherwise, we'll be still 4 members in the club. Hahaha~!"
                "What's so funny? I would be fucking dead right now!"
                m 1b "Anyway. I'm so glad you're okay after all!"
                m "Sayori could be very sad if something happens to you."
                "After Monika said that, I feel like my stomach is twisting for no reason."
                m 5 "So, do you want I take you to your house?"
                menu:
                    "Sorry, but I have things to do...":
                        m 1e "Hmm... Okay!"
                        m 1k "Good luck with your bussiness~!"
                        mc "Thanks Monika."
                        mc "I see you later!"
                        show monika at thide zorder 1
                        hide monika
                        "Alright, let's go somewhere else..."
                        pass
                    "Sure...":
                        m 1j "Alright! I'll take you in my car then."
                        m "Come with me."
                        mc "Okay!"
                        scene bg house
                        with wipeleft_scene
                        m 1a "Here we are."
                        mc "Thanks Monika, I owe you one."
                        m "It was nothing."
                        m 1b "So, see you tomorrow?"
                        mc "Yes Monika, see you tomorrow."
                        m 5 "Fine. Good luck bro~!"
                        show monika at thide zorder 1
                        hide monika
                        "Monika's car is gone in the horizon..."
                        mc "Now what?"
                        pass
                $ stamina -= 3
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
                show sayori 4br at t11 zorder 1
                s "Thank you very much for taking me to eat [player]!"
                s 4bs "That's why you are my favourite person in the entire World!"
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
                        show yuri 1ba at t11 zorder 1
                        y "Thank you for inviting me to eat [player], it's very nice from your part..."
                        y 2bc "I-If you don't mind, I brought a book with me... I mean, if you want to read something while we're waiting for our food."
                        mc "Hehe-! No problem Yuri. I was planing to talk about each other, but if you want to read then-"
                        y 1bh "I..."
                        y 1bj "Well, that's nice too..."
                        "Oh-oh, I'm in trouble..."
                        menu:
                            "Let's read":
                                show yuri 1bf
                                mc "I don't want to force you to talk if you don't want. I..."
                                mc "I guess reading is, something to share our interests too..."
                                mc "Right?"
                                y 2bd "You got a point!"
                                y 1bd "Well, don't you mind if we read something called..."
                                pass
                            "Let's talk":
                                show yuri 1bf
                                mc "Listen Yuri, you know how much I love to read with you..."
                                mc "But, don't you think a little talk can help us to know each other a bit better?"
                                show yuri 1bv
                                mc "I mean, I want to tell you stories about my life, the things what I love, your interests, and check if we have compatibilities on something we like."
                                mc "Isn't that how socializing works?"
                                y 1bt "I... I guess you're right..."
                                y 1bs "I would love to talk about m-my life too..."
                                y "Umm..."
                                y 2bq "Who starts first?"
                                pass
                    elif ch1_choice == "natsuki":
                        show yuri 1ba at t11 zorder 1
                        y "Thank you for inviting me to eat [player], it's very nice from your part..."
                        y "I-I hope the thing what happened in the club doesn't..."
                        mc "Don't worry Yuri, it wasn't your fault."
                        mc "In fact, I wanted to apologize about what I said in that moment."
                        mc "I mean, I knew Natsuki was wrong... But I thought the thing what I said was a neutral position, because I don't want troubles with anyone in the club."
                        mc "I never wanted to hurt you... You are a wonderful girl, you deserve the best."
                        "If with \"the best\" I'm meaning to myself, I'm gonna laugh out loud... Hahahahahaha!"
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
                        show yuri 1ba at t11 zorder 1
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
                    show yuri 3bd at t11 zorder 1
                    y "Oh my god... It was delicious!"
                    mc "And our conversation was very interesting."
                    y 1bc "Indeed."
                    y 2bs "Thank you very much for sharing this moment with me."
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
                show camilla at t11 zorder 1
                mcf2 "Hey~! [player]~! It's good to see you!"
                "She hugs me strongly..."
                mc "Me too Camilla."
                "I hug her back."
                mcf2 "Look, I saw that portion of chocolate cake and that give me hungry.. a lot to be exactly."
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
                scene black
                with dissolve_scene_full
                scene bg cafe
                with dissolve_scene_full
                show camilla at t11 zorder 1
                mcf2 "This is awesome! The best chocolate cake and banana smoothie I've tasted ever!"
                mc "Indeed, the food here is delicious. That's why every time I have to get up early, I come here for breakfast."
                mcf2 "You know, you must invite to one of your friends from the Literature Club to eat here too."
                mc "Well, I already invited Sayori here many times... But I will take your offer about the others too."
                mc "Thanks Camilla."
                mcf2 "Uhuhu~! It was nothing [player]."
                mcf2 "Thanks to you for inviting me to eat this delicious food."
                mc "Don't mention it."
                mc "And if you want, we can go to a bar and drink some beers."
                mcf2 "Good idea!"
                mcf2 "Alright, call me if you want to hang with me again."
                mc "I'll do."
                mcf2 "Goodbye [player]! Best wishes..."
                mc "Best wishes for you too Camilla. Good bye!"
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
            "Buy\n Symbol of Blaze: Destiny ($4000)":
                if money >= 4000:
                    mc "Ok, I hope it's worth..."
                    $ bag_inventory.add_item("yvideogame", score=1)
                    $ money -= 4000
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
                "Happy Thoughts \n $650" if not bag_inventory.has_item("sbook1"):
                    mc "..."
                    mc "Sayori may like this one..."
                    menu:
                        "Buy Happy Thoughts ($650)?"
                        "Yes":
                            $ money -= 650
                            $ bag_inventory.add_item("sbook1", score=1)
                            "You bought the book \"Happy Thoughts\"."
                            $ books_bought += 1
                        "No":
                            pass
                "Dark in the blossoms \n $680" if not bag_inventory.has_item("ybook1"):
                    mc "..."
                    mc "Could Yuri love this?"
                    menu:
                        "Buy Dark in the blossoms ($680)?"
                        "Yes":
                            $ money -= 680
                            $ bag_inventory.add_item("ybook1", score=1)
                            "You bought the book \"Dark in the blossoms\"."
                            $ books_bought += 1
                        "No":
                            pass
                "Anime & Stuff \n $760" if not bag_inventory.has_item("nbook1"):
                    mc "..."
                    mc "Maybe this can help me with Natsuki..."
                    menu:
                        "Anime & Stuff ($760)?"
                        "Yes":
                            $ money -= 760
                            $ bag_inventory.add_item("nbook1", score=1)
                            "You bought the book \"Anime & Stuff\"."
                            $ books_bought += 1
                        "No":
                            pass
                "Shadows of epiphany \n $500" if not bag_inventory.has_item("mbook1"):
                    mc "..."
                    mc "So, this is the book that Monika talked about..."
                    menu:
                        "Buy Shadows of epiphany ($500)?"
                        "Yes":
                            $ money -= 500
                            $ bag_inventory.add_item("mbook1", score=1)
                            "You bought the book \"Shadows of epiphany\"."
                            $ books_bought += 1
                        "No":
                            pass
                "Car Thief 5 - The Guide \n $300" if not bag_inventory.has_item("mcbook1"):
                    mc "Oh my God!"
                    mc "The Official guide of Car Thief 5!"
                    menu:
                        "Buy Car Thief 5 - The Guide ($300)?"
                        "Yes":
                            $ money -= 300
                            $ bag_inventory.add_item("mcbook1", score=1)
                            "You bought the book \"Car Thief 5 - The Guide\"."
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
        scene bg house
        with wipeleft_scene
        mc "Finally! Home sweet home..."
        mc "I'm tired, you know?"
        "..."
        mc "Let's write the poem."
    else:
        mc "You know what?"
        mc "Fuck this shit."
        mc "Let's just write a poem and I'm gonna sleep."
    scene bg bedroom
    with wipeleft_scene
    pause 1.0
    mc "Okay? Let's go!"

return

