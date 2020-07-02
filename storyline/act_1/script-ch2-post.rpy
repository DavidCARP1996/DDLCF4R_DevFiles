label ch2_post:
    $ ch2_post_activities = 0
    $ stamina = 10
    $ hr_hour = 17
    $ park_closed = False
    $ cafe_closed = False
    $ gamestore_closed = False
    $ library_closed = False
    $ ch2_mc_busted = None
    $ ch2_battle_2_won = False
    $ fightingclub_closed = False
    stop music fadeout 2.0
    scene bg house
    with wipeleft_scene
    pause 3.0
    "..."
    jump ch2_post_loop

label ch2_post_loop:
    while (stamina > 0) and (hr_hour <= 20):
        if not renpy.music.get_playing(channel='music') == audio.t5:
            play music t5 fadeout 1.0
        $ HKBShowButtons()
        show screen freeroam_hud
        with Dissolve(.5)
        if ch2_post_activities == 0:
            $ menutext = "Where should I go first?"
        else:
            $ menutext = "Where should I go next?"
        menu:
            "[menutext]"

            "Go to the park" if not park_closed:
                if ch1_battle_2_won == True:
                    mc "I don't want to come back to the park for now..."
                else:
                    mc "I have a bad feeling about going there."
                    mc "I'd better go somewhere else."
                $ park_closed = True
                pass
            "Go to the cafe" if not cafe_closed:
                $ ch2_post_activities += 1
                call ch2_post_go_to_cafe
                pass
            "Go to the gaming store" if not gamestore_closed:
                $ ch2_post_activities += 1
                call ch2_post_go_to_gaming_store
                pass
            "Go to the library" if not library_closed:
                $ ch2_post_activities += 1
                call ch2_post_go_to_library
                pass
            "Go to the Kick boxing Club" if not fightingclub_closed:
                $ ch2_post_activities += 1
                call ch2_post_go_to_fightingclub
                pass
            "Go home":
                jump ch2_post_go_home
                pass

        pass
    jump ch2_post_go_home

    label ch2_post_go_to_fightingclub:
        mc "The Kickboxing Club..."
        if accept_kickboxingclub_offer == "Yes":
            "I said I will go. I will not break that promise to Ryoma."
            pass
        elif accept_kickboxingclub_offer == "Maybe":
            "I guess I can enter in... But I didn't confirmed that."
            menu:
                mc "Hmm..."
                "Yes":
                    pass
                "No":
                    mc "Naaaah, honestly I'm not in mood..."
                    mc "Maybe the next time."
                    $ fightingclub_closed = True
                    jump ch2_post_loop
                    pass
            pass
        elif accept_kickboxingclub_offer == "No":
            "I told Ryoma that I don't have enough time for his club, but honestly, it was a silly lie to not hurt him."
            "But {i}maybeee{/i} I can change of mind and join in anyways..."
            menu:
                mc "Hmm..."
                "Yes":
                    pass
                "No":
                    mc "Naaaah, honestly I'm not in mood..."
                    mc "Maybe the next time."
                    $ fightingclub_closed = True
                    jump ch2_post_loop
                    pass
            pass
        else:
            "I saw a pamphlet about a Kickboxing Club founded by Ryoma, which announces a new schedule for activities, post-school to be exact."
            "I wasn't interested before, but now I'm thinking that I need to do some exercises anyway."
            "And yeah, it has something to do with [ch2_winner]..."
            menu:
                mc "Hmm..."
                "Yes":
                    pass
                "No":
                    mc "Naaaah, honestly I'm not in mood..."
                    mc "Maybe the next time."
                    $ fightingclub_closed = True
                    jump ch2_post_loop
                    pass
            pass
        "Alright. Let's go then."
        call ch2_fightingclub_activities
        mc "Well, see you tomorrow then."
        "Ryoma & Camilla" "See ya~"

        $ fightingclub_closed = True
        scene bg residential_day
        with wipeleft_scene
        $ stamina -= 5

        return

    label ch2_post_go_to_cafe:
        mc "Hmm..."
        if ch2_winner == "Sayori" and backyard_check == False:
            $ menutext2 = "Should I invite Sayori?"
        else:
            $ menutext2 = "I want to share it with someone else... But with who?"

        menu:
            "[menutext2]"

            "Sayori": # Cita con Sayori
                mc "Good idea, she will love this!"
                mc "Let's go to her home to pick up her and then let's go to the cafe."
                scene bg cafe
                with wipeleft_scene
                show sayori 4br at t11 zorder 1
                s "Thank you very much for taking me to eat [player]!"
                s 4bs "That's why you are my favourite person in the entire World!"
                mc "Hehe-! If you say so..."
                if ch2_winner == "Yuri":
                    s "So...What do you think about Yuri?"
                    mc "I...I... Why are you asking such thing?!"
                    s "Sorry, I thought you and she..."
                    mc "Well, back to the topic:"
                    mc "She's a pretty girl, smart, with a simple but quiet and natural personality, beautiful..."
                    menu:
                        "I guess she's Perfect.":
                            pass
                        "I like her qualities.":
                            pass
                    s "Aha-! I knew you will be very interested on her."
                    s "And your poem said it too."
                    mc "Well..."
                    menu:
                        "You got a point.":
                            s "Well, all this time I knew that you two were for each other."
                            mc "Really?"
                            s "Yes. Both behaved like lone wolves until they both met each other."
                            s "I love to see how both are sharing a nice moment like reading a book..."
                            s "I hope you and she reach their relationship more far~!"
                            mc "-!"
                            menu:
                                "I hope so too...":
                                    s "Hehe~"
                                    pass
                                "S-S-Sayori-!":
                                    s "Hehe~"
                                    pass
                            pass
                        "But I still prefer spend time with you Sayori.":
                            s "Eh???"
                            s "But I liked how both of you were reading that book..."
                            s "I thought, well, you two were for each other?"
                            mc "-!"
                            pass
                    pass
                elif ch2_winner == "Natsuki":
                    s "So...What do you think about Natsuki?"
                    mc "I... Why are you asking such thing?!"
                    s "Sorry, I thought you and she..."
                    mc "Well, back to the topic:"
                    mc "She's seems to be an annoying bipolar person. But after the chat we had in the club I knew her better..."
                    menu:
                        mc "I didn't knew she..."

                        "...was suffering familiar abuse from her dad.":
                            s "What? I never heard that. Did Natsuki herself told you such thing?"
                            mc "Yeah, she told me that she's saving her manga collection in the club because her dad doesn't want to see them in their house. Something like that."
                            mc "All what I manage to understand is she's not having a good time while she's in her house, I'm feeling a bit bad about her..."
                            s "Seriously, I didn't knew that."
                            s "In fact, nobody knows that."
                            mc "I see... Then that's why she was a sort of honest when she told me that."
                            mc "And considering nobody else knows that... Will you kept that as a secret? It will be very shamefull for Natsuki if more people knows that."
                            mc "Without mention that she will kill me for telling that to you or anyone."
                            s "Okay, let's keep it as a secret between both of us."
                            mc "Thanks Sayori."
                            pass
                        "...nevermind.":
                            s "What?"
                            "Oh shit... Did she knows about Natsuki's situation?"
                            "If in case she doesn't, I'll invent something obvious."
                            mc "She... she likes the same anime like me, that's all."
                            s "Oh, so was that."
                            mc "Yes."
                            pass
                    pass
                elif ch2_winner == "Monika":
                    s "So...What do you think about Monika?"
                    mc "W-Why are you asking such thing?!"
                    s "Sorry, I thought you and she..."
                    mc "Well, back to the topic:"
                    mc "She's obviously the most popular girl, in first place I thought I'll have no hopes to be friends with her."
                    mc "But the fact that she wants to spend time with me took me as a surprise. I don't know what to do..."
                    s "She's a nice girl [player], you should give her an opportunity like she does with you."
                    mc "Maybe I'll try..."
                    menu:
                        "Yes! I will!":
                            s "That's the attitude!"
                            s "Do your best and be the king of the world bro~!"
                            mc "Thanks, I will..."
                            pass
                        "But I still prefer spend time with you Sayori.":
                            s "Eh???"
                            s "Will you dare to skip that chance just to still spend time with me?"
                            mc "Yep."
                            s "What a meanie..."
                            pass
                        "I don't know if she wants to talk to me anymore after... you know." if ch1_choice == "mc":
                            s "Oh, don't worry about that. She already forgiven you, don't you remember?"
                            mc "Do you think so?"
                            s "Yes! She's a nice person, with a big heart."
                            "She tries to shape a full body-sized heart with her arms. What an exaggeration."
                            pass
                    pass
                else:
                    s "[player], there's something I wanted to ask you..."
                    s "Aren't you interested on anyone from the Literature Club?"
                    mc "Why are you asking such thing?"
                    s "I brought you there so you can make friends with everyone, but you're still holding to me."
                    s "There's something wrong about them?"
                    mc "No! That's not..."
                    menu:
                        mc "It's just..."
                        "I love to still spending time with you, that's all.":
                            s "..."
                            pass
                        "I like them as I like you, there's no problem with that, isn't?":
                            s "No... I guess it's nice."
                            s "But make an effort and spend some time with anyone of them. Okay?"
                            mc "Alright... Whatever you say Sayori."
                            s "Hehe~!"
                            pass
                        "It's the habit of not talking to anyone other than you.":
                            s "Hum! Seems like you're still the same as usual. I thought the Literature Club will change you a bit, but I think I failed."
                            mc "Well, you got a point about I didn't changed anything, but why should I change anyway?"
                            mc "What if the other girls doesn't like how I really am? Because you're the only one who supports for me with my defects."
                            s "But... Everybody seems they like you anyway."
                            s "Yuri gifted you a book for example, what kind of person does something like that? The ones who loves you of course."
                            mc "I think you are exaggerating. She said it; she made that gift for me as a reason to welcome."
                            mc "It's obvious it was a nice gesture, but not for that means she's in love for me or something, at least we'll don't know that until she and me have some private chit chat."
                            s "Okay..."
                            s "In that case, spend more time with her, okay? Do it for me at least."
                            mc "Alright... I'll keep it in mind."
                            pass
                    pass
                s "Anyway, shall we make our order? I'm hungry!"
                mc "Oh! Sorry, I'll call the waiter."
                scene black
                with dissolve_scene_full
                scene bg cafe
                with dissolve_scene_full
                show sayori 3bd at t11 zorder 1
                s "Mmmmmmmmmmm! Delicious as usual!"
                s "Thanks [player], I really enjoyed it."
                mc "Don't mention it."
                s "Alright, let's back to home?"
                mc "Sure!"
                pass
            
            "[ch2_winner]" if ch2_winner != "Sayori": # Cita con Yuri/Natsuki/Monika dependiendo de cuál ruta elegiste al escribir el poema.
                mc "It's not bad idea after all... I can get more chances to know her better!"
                mc "I feel bad about not inviting Sayori, but my wallet is not so big, you know..."
                mc "I'm gonna call her so we can meet in the cafe."
                scene bg cafe
                with wipeleft_scene
                if ch2_winner == "Yuri": # Cita con Yuri
                    if ch1_choice == "yuri":
                        show yuri 1ba at t11 zorder 1
                        y "Thank you for inviting me to eat [player], it's very nice from your part..."
                        y 2bc "If-If you don't mind, I brought a book with me... I mean, if you want to read something while we're waiting for our food."
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
                    elif ch1_choice == "mc":
                        show yuri 1ba at t11 zorder 1
                        y "Thank you for inviting me to eat [player], it's very nice from your part..."
                        y "I-I hope the thing what happened in the club doesn't..."
                        mc "Don't worry Yuri, it wasn't your fault."
                        mc "In fact, I wanted to apologize about that."
                        mc "I don't know what I've been thinking... I-I was blinded by my own rage, seeing Sayori almost crying made me very angry."
                        mc "And... It wasn't the first time what that happened..."
                        y "I see..."
                        y "Sorry about that."
                        mc "Don't worry Yuri."
                        mc "You know, I feel a bit bad for yelling at Monika..."
                        mc "...and do the same to you and Natsuki."
                        mc "Geez, I disgust myself."
                        y "No [player], that's not... Ehm..."
                        y "How can I say it...?"
                        mc "Leave it Yuri, there is no justification for the damage what I've done."
                        "I knew entering the Literature Club was a mistake for my 'natural' attitude, but I couldn't say No to Sayori and the rest of teh girls, after all, they needed my help."
                        y "No! Ummm..."
                        mc "Should we make our order while you're thinking on the words what you'll use?"
                        y "Oh, right! Sorry...."
                        mc "It's nothing.
                        pass"
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
                elif ch2_winner == "Natsuki": # Cita con Natsuki
                    scene bg cafe
                    with wipeleft_scene
                    if ch1_choice == "yuri":
                        n "Hmph!"
                        n "Don't think I came here because you like the idea."
                        n "I guess you owe me an apology."
                        mc "What?!"
                        mc "Natsuki, please! Forget that..."
                        n "..."
                        mc "Hush...! Listen."
                        mc "I-I'm sorry, okay?"
                        mc "I didn't wanted to hurt you or anything... I was, trying to be the more neutral what I could, that's all."
                        n "Hmph!"
                        n "Whatever, just make our order quick, okay?"
                        mc "Okaaay..."
                        pass
                    elif ch1_choice == "mc":
                        n "I can't believe you dare to inviting me to eat after you yelled at us in the club."
                        n "What a hypocrite!"
                        mc "Listen, I'm very ashamed for that. Okay?"
                        mc "I want to apologize to everyone. Sayori already forgived me, I texted Yuri and Monika, now I want to apologize you face to face because..."
                        mc "...well, I thought a nice food with you would be perfect."
                        n "Hmph!"
                        n "Whatever, just make our order quick, okay?"
                        n "I will forgive you later."
                        mc "Okaaay..."
                        pass
                    else:
                        n "Well, I'm here."
                        n "And thanks for inviting me to eat something!"
                        n "I'm starving..."
                        mc "You're welcome."
                        pass
                    pass
                elif ch2_winner == "Monika": # Cita con Monika
                    scene bg cafe
                    with wipeleft_scene
                    m "[player]! Thanks for inviting me for a coffee~!"
                    mc "No problem Monika..."
                    pass
                pass

            "Camilla" if backyard_check == True: # Cita con Camilla
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
                mcf2 "Uhuhu~! Don't mention it [player]."
                mcf2 "Thanks to you for inviting me to eat this delicious food."
                mc "You're welcome."
                mc "And if you want, we can go to a bar and drink some beers someday. What do you think?"
                mcf2 "Good idea!"
                mcf2 "Alright, call me if you want to hang with me again."
                mc "I'll do."
                mcf2 "Goodbye [player]! Best wishes..."
                mc "Best wishes for you too Camilla. Good bye!"
                pass
            
            "Go alone": # No invitas a nadie, tacaño '¬.¬
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

    label ch2_post_go_to_gaming_store:
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

    label ch2_post_go_to_library:
        mc "Let's go to a library."

        if persistent.ytellyouherbookstore == True:
            "Let's go to the bookstore Yuri mentioned."
            scene bg library_old
            with wipeleft_scene
            mc "..."
            "Fuck! No Yuri signals..."
            "Anyway, let's buy a book or let's get out of here."
            pass
        else:
            scene bg library
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

label ch2_post_go_home:
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
        "..."
        mc "You know what?"
        mc "Let's write the poem."
    scene bg bedroom
    with wipeleft_scene
    pause 1.0
    mc "Okay? Let's go!"

return

