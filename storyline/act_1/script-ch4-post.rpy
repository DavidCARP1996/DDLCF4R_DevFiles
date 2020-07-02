label ch4_post:
    $ ch4_activities = 0
    $ stamina = 10
    $ hr_hour = 17
    $ park_closed = False
    $ cafe_closed = False
    $ gamestore_closed = False
    $ library_closed = False
    $ sayori_visited = False
    $ ch4scene_visited = False
    $ mount_achieved = False
    $ mount_point_7_ending = "Middle"
    stop music fadeout 2.0
    with dissolve_scene_full
    scene black
    with dissolve_scene_full
    pause 1.0
    "A few minutes later..."
    scene black
    with dissolve_scene_full
    scene bg bedroom
    with dissolve_scene_full
    pause 1.0
    "..."
    mc "Man..."
    mc "I don't know what's wrong with me."
    if sayori_confess == True:
        mc "I told Sayori how much I love her, but seems like it's not enought!"
        mc "Why?!"
        mc "WHY???!!!"
        call mc_pain2
        mc "Why!"
        call mc_pain2
        mc "The!"
        call mc_pain2
        mc "Fuck!"
        call mc_pain2
        mc "I!"
        call mc_pain2
        mc "Can't!"
        call mc_pain2
        mc "Be!"
        call mc_pain2
        mc "Fucking!"
        call mc_pain2
        mc "HAPPYYYY!!!"
        call mc_pain2
        pause 3.0
        pass
    elif sayori_confess == False:
        mc "I told Sayori we'll keep beign the best friends forever. Or maybe..."
        mc "Maybe there's the mistake!"
        mc "Right! That's it!"
        mc "Sayori expressed her love to me and I just fucking friendzoned her!!!"
        mc "FUUUUUUUUCK!!!"
        call mc_pain2
        mc "Fuck!"
        call mc_pain2
        mc "Me!"
        call mc_pain2
        mc "Fuck!"
        call mc_pain2
        mc "My!"
        call mc_pain2
        mc "Life!"
        call mc_pain2
        mc "And!"
        call mc_pain2
        mc "Fuck!"
        pause 0.5
        call mc_pain2
        mc "EVERYTHING!!!"
        pause 2.0
        call mc_pain2
        call mc_pain2
        call mc_pain2
        mc "{i}AAAAAAAAAAAAAaaaaaaaaaaaAAAAAAAAAAAAhhhhhhHHHHHhhh!!!!!!!!!!!{/i}"
        pause 3.0
        pass
    mc "... ... ..."
    mc "I need a walk!"
    mc "Yes...{w} I need it!"
    mc "I cannot stand here all my life!"
    mc "I need to take a good fucking breath!"
    mc "Yeah! Let's go before I lost my will..."
    scene bg house with wipeleft_scene
    pass

label ch4_post_loop:
    while (stamina > 0) and (hr_hour <= 20):
        if not renpy.music.get_playing(channel='music') == audio.parallel:
            play music parallel fadeout 1.0
        show screen freeroam_hud
        with Dissolve(.5)
        $ HKBShowButtons()
        if ch4_activities == 0:
            $ menutext = "Where should I go first?"
        else:
            $ menutext = "Where should I go next?"
        menu:
            "[menutext]"

            "Go to Sayori's house" if not sayori_visited:
                $ ch4_activities += 1
                mc "May I sound selfish, but I guess it's not time to pay a visit to Sayori for now..."
                mc "I will give her some free time, so let's stop stalking her."
                $ sayori_visited = True
                pass
            "Go to the mountain" if not mount_achieved:
                $ ch4_activities += 1
                call ch4_go_to_mount
                pass
            "Go to Yuri's house" if ch4_scene == "yuri" and not ch4scene_visited:
                $ ch4_activities += 1
                call ch4_visit_yuri
                pass
            "Go to Natsuki's house" if ch4_scene == "natsuki" and not ch4scene_visited:
                $ ch4_activities += 1
                call ch4_visit_natsuki
                pass
            "Go to the park" if not park_closed:
                $ ch4_activities += 1
                call ch4_go_to_park
                pass
            "Go to the cafe" if not cafe_closed:
                $ ch4_activities += 1
                call ch4_go_to_cafe
                pass
            "Go to the gaming store" if not gamestore_closed:
                $ ch4_activities += 1
                mc "Naaah, I'm not in mood to buy videogames..."
                mc "Let's go there another day."
                pass
            "Go to the library" if not library_closed:
                $ ch4_activities += 1
                call ch4_go_to_library
                pass
            "Go home" if ch4_activities > 5:
                jump ch4_go_home
                pass

        pass
    jump ch4_go_home

    label ch4_go_to_mount:
        mc "Good idea, the mount is a perfect place to reflect."
        mc "Quiet, 100\% nature, fresh air...{w} I guess I can invite Sayori to come with me..."
        "*Dialing Sayori*"
        pause 1.0
        "No answers."
        mc "Fuck... I guess she wants to be alone."
        "Then let's go solo."
        scene black zorder 4
        with wipeleft_scene
        pause 2.0
        scene bg seaside_road_day
        with wipeleft_scene
        mc "Thank goodness I catched a bus just in time. Otherwise I would cancelled this trip."
        mc "So... According to a guide; If I take the dirt way it will take me to the famous and relaxing waterfalls of the city."
        mc "Let's go!"
        scene bg forest_way_day
        with wipeleft_scene
        mc "Geez, the path seems very long."
        mc "I must be careful of not fall into an ambush. Or else I'm fucking dead in the middle of the nothing."
        scene bg forest_way_day
        with wipeleft_scene
        mc "Oh, crap! Two paths and without a fucking sign."
        menu mount_point_1:
            "Where should I go?"

            "Left":
                mc "Alright!"
                scene bg forest_bush
                with wipeleft_scene
                mc "A dead end..."
                scene bg forest_way_day
                with wipeleft_scene
                jump mount_point_1
            "Right":
                mc "Alright!"
                pass
            "Back" if not mount_achieved:
                mc "No. I won't turn back."
                jump mount_point_1
            "Back" if mount_achieved == True:
                mc "Alright, it's over."
                scene bg residential_day with wipeleft_scene
                return
        
        scene bg forest_way_day
        with wipeleft_scene
        mc "More deviations..."
        mc "But hey, I'm spoting a sunlight in the right path. Maybe it's the end of the path..."
        menu mount_point_2:
            "Where should I go?"

            "Left":
                mc "Alright!"
                scene bg forest_bush
                with wipeleft_scene
                mc "Another dead end... Shit!"
                scene bg forest_way_day
                with wipeleft_scene
                jump mount_point_2
            "Middle":
                mc "Alright!"
                pass
            "Right":
                mc "Alright!"
                scene bg nature
                with wipeleft_scene
                mc "It's a lake... Nice view but it's not what I'm looking for."
                scene bg forest_way_day
                with wipeleft_scene
                jump mount_point_2
            "Back":
                mc "Alright!"
                jump mount_point_1
            
        scene bg forest_way_day
        with wipeleft_scene
        mc "Hey, finally I'm spoting another sunlight! Maybe it's the real exit..."
        scene bg meadow_day
        with dissolve_cg
        mc "Yeah... That's what I'm talking about..."
        mc "But according to the guide; I'm still far from the waterfalls. So let's keep going!"
        menu mount_point_3:
            "Where should I go?"

            "Left":
                mc "Alright!"
                scene bg deadend_rocky
                with wipeleft_scene
                mc "Once again a fucking dead end..."
                scene bg meadow_day
                with wipeleft_scene
                jump mount_point_3
            "Middle":
                mc "Alright!"
                pass
            "Right":
                mc "Alright!"
                scene bg nature
                with wipeleft_scene
                mc "Once again the same lake..."
                scene bg meadow_day
                with wipeleft_scene
                jump mount_point_3
            "Back":
                mc "Alright!"
                scene bg forest_way_day
                with wipeleft_scene
                jump mount_point_2

        scene bg riverside_bridge
        with wipeleft_scene
        mc "That bridge... That river... That means we are closer to the waterfalls..."
        mc "Come on! There's no time to waste!"
        scene bg forest_way_day
        with wipeleft_scene
        mc "Alright, once again there are two ways..."
        mc "The waterfalls are at the right. But {i}maybe{/i} it's a deadend and the left takes a longer but direct path."
        menu mount_point_4:
            "Where should I go?"

            "Left":
                mc "Alright!"
                pass
            "Right":
                mc "Alright!"
                scene bg deadend_rocky
                with wipeleft_scene
                mc "I knew it!"
                scene bg forest_way_day
                with wipeleft_scene
                jump mount_point_4
            "Back":
                mc "Alright!"
                scene bg meadow_day
                with dissolve_cg
                jump mount_point_3

        scene bg forest_way2
        with wipeleft_scene
        mc "Geez! It never ends, isn't?"
        menu mount_point_5:
            "Where should I go?"

            "Middle":
                mc "Alright!"
                pass
            "Right":
                mc "Alright!"
                scene bg forest_bush
                with wipeleft_scene
                mc "Nothing there..."
                scene bg forest_way2
                with wipeleft_scene
                jump mount_point_5
            "Back":
                mc "Alright!"
                scene bg forest_way_day
                with dissolve_cg
                jump mount_point_4
        
        scene bg forest_way2
        with wipeleft_scene
        mc "How long it takes? Fuck!"
        menu mount_point_6:
            "Where should I go?"

            "Left":
                mc "Alright!"
                scene bg meadow_day
                with wipeleft_scene
                mc "A landscape without course. Let's back to the path."
                scene bg forest_way2
                with wipeleft_scene
                jump mount_point_6
            "Right":
                mc "Alright!"
                pass
            "Back":
                mc "Alright!"
                scene bg forest_way2
                with dissolve_cg
                jump mount_point_5
        
        scene bg forest_way_day
        with wipeleft_scene
        mc "Eh?"
        mc "I can hear flowing water..."
        mc "I'm closer, I'm sure!"
        menu mount_point_7:
            "Let's go!!!"

            "[mount_point_7_ending]":
                pass
            "Back":
                scene bg forest_way2
                with wipeleft_scene
                jump mount_point_6

        scene bg riverside_waterfall
        with wipeleft_scene
        stop music fadeout 3.0
        play sound waterfalls fadeout 2.0
        if not mount_achieved:
            mc "Finally!"
            mc "The famous relaxing waterfalls..."
            mc "All what I need to do is relax while I watch this view. This God creation."
            "... ... ..."
            pause 5.0
            "Now that I think about it..."
            if sayori_confess == True:
                mc "I did well at saying Sayori \"Yes\" to her confession."
                mc "No matter if I want to hang around with Yuri, Natsuki, Monika or even Camilla..."
                mc "To make Sayori happy, I must love only her."
                mc "I guess I'm not so worthless after all..."
                "... ... ..."
                mc "Unless..."
                mc "This time... I didn't make that decision by myself... But YOU did the choice for ME!"
                mc "Yeah, it was YOU!"
                mc "When I wasn't able to choose the right answer, YOU picked the right one for me."
                mc "Thanks dude! I owe you a huge one..."
                mc "Together, we can change this world for a good one."
                mc "YOU can SAVE/LOAD for me and change the fate of this world as you like."
                mc "..."
                mc "Listen, I have an idea:"
                mc "What if we get back in time and you make me spend time with ALL the girls of the Club?"
                $ if all(clear for clear in persistent.clear): persistent.clearch4 = True
                if persistent.clearch4:
                    mc "Wait a minute..."
                    mc "Seems like you already made it. Nice!"
                    mc "Alright! I made everyone happy... So, I guess there's nothing else to do here."
                else:
                    mc "Since we haven't spend time with all the girls, let's give a chance to the ones which I haven't dated."
                    mc "Something says to me that Sayori could be very happy if I make everyone happy, despite if it's on different timelines..." 
                    mc "I don't know why, but I have that feeling."
                mc "Alright! Are you ready?"
                mc "Let's go back to my house and do whatever we need to do!"
                mc "Let's goooooo!!!"
                pass
            else:
                mc "My biggest mistake was saying \"No\" to her confession."
                mc "No matter if I want to hang around with Yuri, Natsuki, Monika or even Camilla..."
                mc "To make Sayori happy, I must love only her."
                mc "I am a stupid motherfucking worthless..."
                mc "I deserve the worst..."
                pause 5.0
                "... ... ..."
                mc "No..."
                mc "This time... I didn't make that decision by myself... But YOU did the choice for ME!"
                mc "Yeah, it was YOU!!!"
                mc "YOU are the motherfucker in this story!"
                mc "YOU've been making the choices for ME all this time!"
                mc "Since I joined the Literature Club YOU've been doing all the job what everyone thoughts I've done..."
                mc "So from that part, any mistakes of mine are YOUR responsabilities!"
                mc "I BLAME YOU FOR BREAKING SAYORI'S HEART!!! I BLAME YOUR FOR{nw}"
                $ gtext2 = glitchtext(500)
                mc "[gtext2]{nw}"
                call glitch1
                mc "What the...?"
                "..."
                "I don't know what happened, I felt like a hit in my neck when I was blaming you."
                "My anger get freezed for some reason... So for now, I'll stop fighting with you."
                mc "But... that effect... it's familiar..."
                mc "Does it...? Yeah!"
                mc "It's the same glitch effect when the {i}Mysterious girl{/i} spawns and dissapears..."
                mc "Now I'm more confused than before... Why would she stop OUR arguing? Does she thinks I'm talking alone or something?"
                mc "... ... ..."
                mc "Fuck it!"
                "I plop to the grass looking at the sky."
                mc "What the fuck I'm doing?"
                mc "Isn't supposed YOU and I together we can change the story?"
                mc "I mean... YOU can SAVE/LOAD for me and change the fate of this world as you like."
                mc "So... WE can make all the girls happy even in different timelines."
                mc "That's!"
                mc "It's a good idea!"
                mc "Let's go back in time and fix this shit we have done!"
                mc "But first let's go back to the town because I would have something pending to do..."
                pass
            $ persistent.mount_achieved = True
            $ mount_achieved = True
            $ mount_point_7_ending = "Waterfalls"
        else:
            mc "Nice view..."
            mc "But we have work to do! Let's go!"
            pass
        stop sound fadeout 2.0
        play music parallel fadeout 1.0
        scene bg forest_way_day with wipeleft_scene
        jump mount_point_7

    return
    
    label ch4_visit_yuri:
        mc "I guess it's a good idea. Maybe she can help me with this."
        scene bg yuri_house
        with wipeleft_scene
        "*ding* *dong*"
        show yuri 1ba at t11 zorder 2
        y "[player]?"
        y "What a surprise... I-I'm glad you're here..."
        mc "Me too Yuri, but I came here because I need to tell you something important... May I come in?"
        y "Sure, you're welcome~!"
        scene bg yuri_livingroom
        with wipeleft_scene
        "Yuri went to the kitchen to make some tea while I wait for her in the living room."
        "I told Yuri everything what happened between Sayori and me."
        show yuri 1ba at t11 zorder 2
        y "[player], I'm so sorry about what happened earlier..."
        y "I-I guess... Sayori's current situation was my fault..."
        mc "No Yuri, you're wrong. It was completely my fault."
        mc "All this time I didn't know that Sayori was hiding her depression."
        mc "If I had known it from the beginning, I would have done something about it."
        mc "I'm her \"best friend\" after all."
        if sayori_confess == True:
            "I don't want to tell her yet that Sayori and I are a couple now. Not until she finds someone else to love..."
        elif sayori_confess == False:
            "After saying that, it makes me want to pour the hot tea directly to my balls. After all, these words are the cause of Sayori's heart breaking to pieces."
        mc "Just like Sayori has been doing for me since she noticed my post-accident depression."
        y "I understand..."
        y "If-If it makes you feel better, nobody in the club noticed that she was suffering depression..."
        y "I swear to God that everyone would have done something for her if we had known about it."
        mc "I know."
        mc "But there is something that worries me..."
        y "Eh?"
        mc "Sayori said \"Monika was right... I should just...\" and then she stops."
        mc "I don't want to be pessimist with Monika, but I have the weird feeling that she is {i}somehow{/i} behind of this."
        mc "How much do you know about Monika? Because Sayori all this time she's been told me only nice things about her."
        mc "It's not like I want to directly blame her, but she wasn't so nice to me last year... However, I can't imagine seeing her asking someone to... I don't know... commit suicide?"
        y "That's true... Even I can't imagine such terrible thing about her..."
        y "Unfortunately, I don't know much about Monika..."
        y "All what Natsuki and I we know is she's have the aptitudes to be a Club President, and she's very social despite her excuse that she's not so good with people..."
        mc "Yeah, that's true..."
        y "Umm... May I give you a suggestion?"
        mc "Sure."
        y "Well, if Sayori does not want to answer phone calls or SMS. Then we should wait until tomorrow to see what's up with her..."
        y "But... If she already mentioned something that can derive to suicide, then we cannot lost any track of her if in case she try to do something dangerous."
        y "So... Try to visit her frequently, or try to convince her spend the night together so you can make sure she is safe."
        mc "Good said! I will try to do that."
        mc "Thanks Yuri..."
        y "It's nothing really, I hope I could do something for her too..."
        "I hug Yuri, she's surprised for such reaction of mine."
        mc "No... I was about to give up. But you just gave me a little push to keep a eye on her."
        "But then she wraps her arms tightly around me."
        y "Well, I..."
        mc "This talk with you was very helpful, remember that Yuri."
        y "Y-Yeah..."
        "I release her, then she release me too."
        mc "Alright, thank you very much for the talk and the tea, it was delicious..."
        y "I'm glad you like it, and I'm so glad that I'm beign helpful to you and Sayori."
        y "I hope she recovers for tomorrow."
        mc "Me too Yuri..."
        mc "I will do my best to keep her safe. I promise!"
        y "Well said!"
        scene bg yuri_house
        with wipeleft_scene
        y "Good luck [player]! And take care of Sayori..."
        mc "Thanks Yuri! I will do my best."
        y "We hope so..."
        show yuri at thide
        hide yuri
        "Alright! Now I feel calmer..."
        "Let's do whatever we need to do!"

        $ ch4scene_visited = True

        return

    label ch4_visit_natsuki:
        mc "I guess it's a good idea. Maybe she can help me with this."
        "I will text Natsuki if she's able to receive visits..."
        "... ... ..."
        n "Okay, but come here quick. My dad will come here soon."
        "Alright... Let's go!"
        scene bg natsuki_house
        with wipeleft_scene
        "*knock* *knock*"
        n "Come on! Enter in..."
        mc "Hey! What's wrong--"
        "She pulls me inside her house."
        scene bg natsuki_bedroom
        with wipeleft_scene
        "I told Natsuki everything what happened between Sayori and me."
        n "I see..."
        if sayori_confess == True:
            n "So even after you accepted her confession, she's still acting like if she doesn't want to know anything about the world..."
            n "What's wrong with her?"
            mc "I don't know, that's why I wanted to talk with you, if you can give me an advice or something..."
            n "I'm not a psychologist, I don't know how to deal with such stuff."
            pass
        elif sayori_confess == False:
            n "You are a stupid jerk!"
            n "How dare you to broke her heart like this?"
            call mc_pain2
            "She punches my stomach with anger."
            n "You deserve this!"
            mc "Y-Ye-Yeah... You...You're r-right..."
            pass
        n "Hmm..."
        n "But maybe..."
        n "Our activity in your house could affected her?"
        n "I mean if she was in love with you that means she could be feeling jealous at seeing you spending time with someone who doesn't she."
        n "So, I guess, I'm in sort guilty for her current status..."
        mc "No Natsuki, you're wrong, it was completely my fault."
        mc "All this time I didn't know that Sayori was hiding her depression."
        mc "If I had known it from the beginning, I would have done something about it."
        mc "All this time I was her \"best friend\" after all."
        if sayori_confess == True:
            "I don't want to tell her yet that Sayori and I are a couple now. Not until she finds someone else to love..."
        elif sayori_confess == False:
            "After saying that, it makes me want to pour the hot tea directly to my balls. After all, these words are the cause of Sayori's heart breaking to pieces."
        mc "Just like Sayori has been doing for me since she noticed my post-accident depression."
        n "Well, you got a point."
        n "However, nobody else noticed that she was depressed."
        n "Anyone on the club could have done something for her before you notice it."
        mc "I know."
        mc "But there is something that worries me..."
        n "What?"
        mc "Sayori said \"Monika was right... I should just...\" and then she stops."
        mc "I don't want to be pessimist with Monika, but I have the weird feeling that she is {i}somehow{/i} behind of this."
        mc "How much do you know about Monika? Because Sayori all this time she's been told me only nice things about her."
        mc "It's not like I want to directly blame her, but she wasn't so nice to me last year... However, I can't imagine seeing her asking someone to... I don't know... commit suicide?"
        n "That's a terrible accusation!"
        n "But... I don't know much about Monika neither..."
        n "All what Yuri and I we know is she's good to being a Club President, and a bit bully too..."
        mc "Yeah, that's true..."
        n "May I give you a suggestion?"
        mc "Sure."
        n "Keep insisting on stalking Sayori."
        n "At least to make sure if she's fine."
        n "Otherwise she maybe wants to recompose herself... In that case there's no more option than let her alone for a time."
        mc "Good said! I will try to do that."
        mc "Thanks Natsuki..."
        n "It was nothing."
        mc "No... I was about to give up. But you just gave me a little push to keep a eye on her."
        mc "This talk with you was very helpful, remember that Yuri."
        n "It's...It's not like I'm helping you because you're asking, I'm doing this for Sayori instead."
        mc "Alright, sure. Anyway I'm very thankful for this conversation."
        n "Whatever..."
        n "I hope she recovers for tomorrow."
        mc "Me too Natsuki..."
        mc "I will do my best to keep her safe. I promise!"
        n "I hope so..."
        scene bg natsuki_house
        with wipeleft_scene
        n "[player], please take care of Sayori..."
        n "Try to make her go to the festival tomorrow."
        mc "Thanks Natsuki! I will do my best."
        n "Good bye... And get out of here before my dad drops by!"
        show natsuki at thide
        hide natsuki
        mc "Alright! Alright!"
        scene bg streets2_day
        with wipeleft_scene
        "Geez... I wonder what kind of dad she have to make me run away..."
        "Alright! Now I feel calmer..."
        "Let's do whatever we need to do!"

        $ ch4scene_visited = True

        return

    label ch4_go_to_park:
        scene bg park_way
        with wipeleft_scene
        pause 1.0
        mc "I'm get the fuck out of here!"
        scene bg residential_day with wipeleft_scene
        $ stamina -= 1
        $ park_closed = True

        return

    label ch4_go_to_cafe:
        mc "Let's get something to eat..."
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
                $ money -= 250
                pass
            "Orange juice & ham and cheese toast - $280":
                mc "..."
                pause 5.0
                $ mc_hp = mc_hp_max
                $ mc_mp = mc_mp_max
                $ money -= 280
                pass
            "Strawberry smoothie & portion of cake - $320":
                mc "..."
                pause 5.0
                $ mc_hp = mc_hp_max
                $ mc_mp = mc_mp_max
                $ money -= 320
                pass
        "Alright, let's pay the bill and let's go somewhere else..."
        scene bg residential_day with wipeleft_scene
        $ stamina -= 1
        $ cafe_closed = True

        return

    label ch4_go_to_library:
        mc "..."
        if persistent.ytellyouherbookstore == True:
            "Let's go to the bookstore Yuri mentioned."
            if ch4_scene == "yuri" and not ch4scene_visited:
                "If I found her there, I can talk with her about that..."
                pass
            elif ch4_scene == "natsuki":
                "If I found her there, I can talk with her about that..."
            else:
                pass
            scene bg library_old
            with wipeleft_scene
            mc "..."
            "Fuck! No Yuri signals..."
            pass
        else:
            mc "Naaah, I'm not in mood to buy a book. Also I already have the one Yuri gifted to me if I want to read."
            pass

        "Anyway, let's get out of here."
        scene bg residential_day with wipeleft_scene
        $ library_closed = True
        $ stamina -= 1

        return

label ch4_go_home:
    mc "Are you sure about this?"
    mc "I will suggest you to Save the game before proceed. I have a bad feeling about what's coming up next..."
    mc "Also make sure that we already completed every objective..."
    "..."
    menu:
        mc "Are you sure do you want to proceed?"

        "Yes":
            mc "...Okay..."
            pass
        "No":
            mc "Well, let's do whatever we need to do then..."
            jump ch4_post_loop
    stop music fadeout 2.0
    window hide(None)
    window auto
    hide screen freeroam_hud
    $ HKBShowButtons()
    $ HKBHideButtons()
    with Dissolve(.5)
    pass
    pause 5.0
    mc "... ... ..."
    scene bg bedroom
    with wipeleft_scene
    mc "... ... ..."
    mc "I will text Sayori at least to check how is she going."
    pause 2.0
    "No answers..."
    if sayori_confess == True:
        mc "I guess she's still recomposing herself. In that case I must still let her alone..."
        mc "At least I know I didn't make the wrong choice this time..."
    else:
        mc "I guess she's mad at me for rejecting her love... Geez I hate myself a lot!"
        mc "I deserve all the bad things I suffered, I'm suffering and I'll suffer."
    "... ... ..."
    mc "I don't fell so good. I'm gonna take a nap."
    scene black
    with dissolve_scene_full
    stop music fadeout 2.0
    pause 5.0

return

