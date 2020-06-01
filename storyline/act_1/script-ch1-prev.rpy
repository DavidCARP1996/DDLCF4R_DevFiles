label ch1_prev:
    stop music fadeout 2.0
    with dissolve_scene_full
    
    scene bg bedroom_night
    with dissolve_scene_full
    mc "Fuck."
    mc "Look at the hour."
    mc "I must go to sleep."
    scene black
    with dissolve_scene_full
    pause 3.0
    "After a few minutes trying to consilate the sleep, I'm success..."
    scene black
    with dissolve_scene_full
    if persistent.monika_help == True:
        pause 3.0
        show mask_2
        show mask_3
        with dissolve_scene_full
        play music m1
        "But sudently, I'm in a weird dream. Again."
        mc "Wait, again?!"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        show monika sdwf1 at t11 zorder 2
        mc "You?!"
        if persistent.ytellyouherbookstore == True:
            "???" "... ... ..."
            mc "Hey! I must thank you for this Save/Load script..."
            mc "I just did something that made my day happy and..."
            "???" "..."
            mc "Ehm... Are you okay?"
            "???" "What in the world are you doing?"
            mc "What?"
            "???" "Don't play dumb."
            "???" "I know what have you done."
            "???" "Did you changed your course of the bookstore because you wanted to see that violet-haired girl?!"
            mc "And what's wrong with that?"
            mc "You gave me this power to make the right decisions, right?"
            "???" "You Idiot!"
            "???" "You already fucked up that timeline. When you regret for that there is no going back anymore..."
            mc "Well, maybe I will NEVER regret that!"
            "???" "Hush! I knew you would be a motherfucking asshole!"
            mc "..."
            "???" "Anyway..."
            pass
        else:
            "???" "Well..."
            pass
        "???" "Did you enjoy wasting your time writing a poem?"
        "???" "It's almost time to wake up."
        "???" "I feel bad for your misserable life."
        "???" "You weirdo freak."
        mc "Was that insult so neccesary?"
        "???" "Yes."
        "???" "But listen."
        if poemwinner[0] == "Monika":
            "???" "Hmmm...?"
            "???" "Wow!"
            "???" "Nice!"
            "???" "I didn't know you were very good with poems."
            "???" "Seems like I was right choosing you~!"
            mc "What are you talking about?"
            mc "That poem is not even for you!"
            mc "Give it back, please!"
            "???" "Okay~... Hehe~"
            "???" "You know? You're going in the right way..."
            "???" "This poem is the proof of that."
            mc "What?!"
            mc "It's just a fucking poem, it doesn't change anything."
            mc "Are you saying that the right way was entering in the Literature Club? Is that it?"
            "???" "..."
            "???" "Shut up!"
            "???" "Even if you're an good poet, looks like you're still an idiot."
            "???" "Look, just watch your back, ok?"
            "???" "I'll see you later..."
            pass
        else:
            "???" "Hmmm..."
            "???" "I see."
            "???" "You was just wasting your time."
            "???" "No."
            "???" "I'm wasting my time on YOU."
            mc "What are you talking about?"
            mc "That poem is not even for you, why are you acting so mad for this?"
            mc "And give it back, please!"
            "???" "Whatever, it doesn't worth anyway..."
            "???" "But I warn you that you are going the wrong way..."
            "???" "I can see it in this crappy poem."
            mc "What?!"
            mc "It's just a fucking poem, it doesn't change anything."
            mc "Are you saying that the wrong way was entering in the Literature Club? Is that it?"
            "???" "..."
            "???" "Shut up!"
            "???" "Look, just watch your back, ok?"
            "???" "I'm outta here..."
            pass
        $ gtext = glitchtext(20)
        "???" "{cps=60}[gtext]{/cps}{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        hide monika
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        call hideconsole
        mc "..."
        pause 2.0
        "Fuck."
        "She's really a strange woman."
        "Should I take that aware? Is something bad going to happen?"
        stop sound
        pause 3.0
        stop music fadeout 2.0
        pass
    else:
        pass

    scene bg bedroom_dark
    with dissolve_scene_full
    "..."
    "Wha-"
    mc "Hmm... 6 AM. It's very early."
    mc "Could I take the opportunity to go for a walk? Or sleep a bit more?"

    menu:

        "Take a morning walk":
            "Alright!"
            $ HKBShowButtons()
            $ ch1_prev_activities_m = 0
            $ stamina = 6
            $ hr_hour = 6
            $ park_closed = False
            $ cafe_closed = False
            $ library_closed = False
            $ gamestore_closed = False
            jump ch1_prev_loop
        "Sleep a bit more":
            "..."
            jump ch1_prev_go_sleep

label ch1_prev_loop:
    while (stamina > 0) and (hr_hour <= 7):
        show screen freeroam_hud
        with Dissolve(.5)
        play music t5
        if ch1_prev_activities_m == 0:
            scene bg house_morning
            with wipeleft_scene
            $ menutext = "Where should I go first?"
        else:
            scene bg residential_morning
            with wipeleft_scene
            $ menutext = "Where should I go next?"
        menu:
            "[menutext]"

            "Go to the park" if not park_closed:
                $ ch1_prev_activities_m += 1
                call ch1_prev_go_to_park
                pass
            "Go to the cafe" if not cafe_closed:
                $ ch1_prev_activities_m += 1
                call ch1_prev_go_to_cafe
                pass
            "Go to the gaming store" if not gamestore_closed:
                mc "The game store is closed right now."
                $ gamestore_closed = True
                pass
            "Go to the library" if not library_closed:
                mc "The library is closed right now."
                $ library_closed = True
                pass
            "Go home":
                jump ch1_prev_go_home
                pass
            "Go to school":
                jump ch1_prev_go_play
                pass
        pass
    jump ch1_prev_go_home

    label ch1_prev_go_to_park:
        mc "Well then, let's have a walk in the park."
        mc "I need to do some exercises anyway..."
        scene bg park_way_morning
        with wipeleft_scene
        mc "Perfect!"
        mc "Nobody is around~!"
        hide screen freeroam_hud
        with Dissolve(.5)
        $ HKBShowButtons()
        $ HKBHideButtons()
        pause 1.0

        call ch1_battle_1

        $ HKBShowButtons()
        mc "Phew! That was close..."
        "..."
        mc "Nobody is here."
        mc "Not even a fucking cop!"
        mc "One mistake and I could be so fucking dead!"
        mc "Hmmm..."
        mc "Let's just... take 'my rewards'..."
        $ bag_inventory.add_item("jackknife", score=1)
        "[player] received a Jackknife."
        mc "Nice!!!"
        if battle_extra_rewards_rate <= 5:
            mc "!"
            mc "Wow! Look at this!"
            $ money += 1000
            "[player] received $1000 additional."
            $ bag_inventory.add_item("proteinbar", score=1)
            "[player] received Protein bar."
            mc "It's awesome!"
        mc "Now I can handle myself against the bad guys."
        "Well, let's get the fuck out of here before someone comes."
        
        $ park_closed = True
        $ stamina -= 5

        return

    label ch1_prev_go_to_cafe:
        mc "I'm hungry."
        mc "I guess I'll take a sooner breakfast..."
        scene bg cafe_dark
        with wipeleft_scene
        mc "Hmm..."
        menu:
            "What should I have for eat?"

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

        $ stamina += 3

        return

label ch1_prev_go_home:
    stop music fadeout 2.0
    hide screen freeroam_hud
    with Dissolve(.5)

    mc "..."
    mc "You know what?"
    mc "Damn..."
    mc "Should I try to sleep a bit more? There's still more free time before go to school..."
    scene bg bedroom
    with wipeleft_scene
    pause 1.0
    $ HKBShowButtons()
    $ HKBHideButtons()
    play sound click
    scene bg bedroom_dark
    mc "Zzzzzzzzzzz..."
    scene black
    with dissolve_scene_full
    jump ch1_prev_go_school

return

label ch1_prev_go_sleep:

    "..."
    mc "Nah!"
    mc "I'm fucking sleepy..."
    mc "Let's just... sleep a bit more... okay...?"
    mc "Zzzzzzzzzzzzz...."
    scene black
    with dissolve_scene_full
    jump ch1_prev_go_school

return

label ch1_prev_go_play:
    stop music fadeout 2.0
    hide screen freeroam_hud
    with Dissolve(.5)

    mc "I still have some free time before going to school."
    mc "Maybe I should play some videogames, right?"
    mc "Yeah, good idea..."
    mc "Let's get back home!"
    scene bg bedroom
    with wipeleft_scene
    pause 0.5
    $ HKBShowButtons()
    $ HKBHideButtons()
    mc "Now let's turn on the console and..."
    scene black
    with dissolve_scene_full
    jump ch1_prev_go_school

return

label ch1_prev_go_school:
    scene bg bedroom
    with wipeleft_scene
    pause 1.0

    mc "..."
    mc "Alright! 7:15 AM, it's time to get prepared."
    mc "I have time enough to take a bath and eat something."
    "Hang on."
    scene black
    with dissolve_scene_full
    pause 2.0
    scene bg bedroom
    with wipeleft_scene
    "8:00 AM"
    mc "Hmm... I've been thinking..."
    mc "Sayori is oversleeping more and more frequently lately."
    mc "Yesterday we saw each other at 8:30 AM, 30 minutes before the school's gates close."
    menu:
        mc "Maybe should I wait for her today?"

        "Yes, do it for her.":
            mc "Fine."
            mc "Let's play more videogames then."
            scene black
            with dissolve_scene_full
            pause 2.0
            jump ch1_prev_go_schoolA
            pass
        "No, you'll arrive very late.":
            mc "Are you sure?"
            mc "I don't want to be selfish with her, she doesn't deserve it..."
            menu:
                "You got a point.":
                    mc "Haha! See?"
                    mc "Don't worry, I'll wait for her at 8:30 AM. If she's not coming out, then I'll go alone."
                    mc "Let's play more videogames then."
                    scene black
                    with dissolve_scene_full
                    pause 2.0
                    jump ch1_prev_go_schoolA
                "Do what you want then!":
                    mc "Fuck you!"
                    mc "..."
                    mc "Whatever, just let's hope she doesn't get mad for this."
                    scene black
                    with wipeleft_scene
                    pause 0.5
                    jump ch1_prev_go_schoolB

label ch1_prev_go_schoolA:
    scene bg house
    with wipeleft_scene
    play music t2
    $ HKBShowButtons()
    "8:15 AM"
    "Time enough to wait for Sayori and go to the school together..."
    mc "Sayori!"
    "If she's not showing up until 8:30, I will go alone."
    mc "SAYOOORIIIIIIIIIIIIIIIIIII-!!!{nw}"
    s "I'M COMING~!"
    mc "What the..."
    "It's me or Sayori sounded a bit upset? Geez, does she know what hour it is now?"
    "The door is opening gently."
    show sayori 4a at t11 zorder 2
    s "Hi [player]! I'm so glad you waited for me again~!"
    mc "It's a pleasure."
    "She doesn't look so good, look at her: her hair is messy, one of the buttons is opened..."
    show sayori 1b
    "But no matter what defects she's having, she's still perfect for me."
    "(...or for someone else. Honestly, She doesn't deserves an asshole like me.){nw}"
    s 1c "Hey!"
    s 3c "It's me or are you rambling?"
    mc "Wha-"
    "Fuck!"
    "Well, let's stop fucking around and let's take her to the school..."
    show sayori 1b
    mc "Ehm... It's nothing Sayori, I just... not take a good sleep... that's all..."
    s 4r "Me either, hahaha~!"
    mc "Hahaha!"
    $ sayori_wait1 = True
    jump ch1_prev_schooltime
return

label ch1_prev_go_schoolB:
    scene bg residential_day
    with wipeleft_scene
    play music t2
    $ HKBShowButtons()
    mc "..."
    mc "You know, it feels weird walking to the school without Sayori, but she's not coming up to chasing me like she did before."
    mc "I can feel the ausence of her enjoying aura. Without her the atmosphere feels so empty now..."
    mc "..."
    "I want to check if she'll coming up, but if I turn back to our neighborhood, I'll have no time enough to get into the school at time."
    mc "Hmm..."
    "After realising a bit, I almost cross a street with red light. I evaded a fucking car coming from the nothing just in time!"
    mc "Shit!"
    mc "Hush! Fuck this shit! I'll go to the fucking school anyway!"
    mc "I will wait for Sayori later."
    $ sayori_wait1 = False
    jump ch1_prev_schooltime
return

label ch1_prev_schooltime:

    scene bg class_day
    with wipeleft_scene

    mc "Finally..."
    mc "A few minutes before recess."

    if sayori_wait1 == True:
        "You know, I'm getting used to this already."
        "I mean, I know we're getting late for school. But at least walking together is better than walking alone."
        "I can't imagine how could Sayori feel if I left her alone in this situation."
        pass
    if sayori_wait1 == False:
        "I'm feeling a bit bad for what I've done earlier."
        "You know, lefting Sayori back and walk to the school myself without her company..."
        "I'm beign so selfish from one moment to another. I'm an idiot, that's for sure."
        pass

    play sound school_bell

    mc "Oh! It's time..."
    mc "Let's go to the dining room."

    scene bg school_dining_room
    with wipeleft_scene

    mc "Here we are..."
    "This place is always full crowded. I can across some assholes as like I'm getting all the attention I never asked."
    "Seriously, I hate this crap."
    mc "Hmm..."
    mc "No hints of Yuri or Natsuki..."
    stop music fadeout 5.0
    mc "Hey! Where is Sayori?"
    if sayori_wait1 == True:
        "She's always finding a place where we can eat together avoiding those motherfuckers of the popular class (the same where Monika comes from ironically)."
        "But now, she's not even here. Where did she go?"
        "I would scream for her, but it will call some attention. So I better get out of here..."
        "I guess I'll eat this later. I'm gonna find Sayori first."
        pass
    if sayori_wait1 == False:
        "Shit! We haven't met in the entrance either. Where did she go?"
        "It's supposed she's finding a place where we can eat together. But now she's not anywhere."
        "My heart starts to pound very hard... Did something bad happened to her in the way to the school?"
        "I'll save the lunch and ran away from this place!"
        pass
    $ bag_inventory.add_item("schoollunch", score=1)

    scene bg school_stairs1
    with wipeleft_scene
    play music midnight_piano
    $ menutext = "Where should I go first?"
    $ ch1_prev_activities_s = 0
    $ sayori_found = False
    $ s_classroom_check = False
    $ mc_classroom_check = False
    $ backyard_check = False
    $ entrance_check = False
    $ roof_check = False
    jump ch1_prev_schooltime1_loop

label ch1_prev_schooltime1_loop:
    while sayori_found == False:
        if ch1_prev_activities_s == 0:
            $ menutext = "Where should I go first?"
        else:
            $ menutext = "Where should I go next?"
        menu:
            mc "[menutext]"

            "My classroom" if not mc_classroom_check:
                mc "What if she's looking for me in my classroom? Let's check it out."
                $ ch1_prev_activities_s += 1
                call ch1_prev_schooltime_loop_mcclassroom
                pass
            "The backyard" if not backyard_check:
                mc "Let's check the backyard... Sometimes I trend to go there."
                $ ch1_prev_activities_s += 1
                call ch1_prev_schooltime_loop_backyard
                pass
            "Sayori's classroom" if not s_classroom_check:
                if backyard_check == True and sayori_wait1 == True:
                    mc "Camilla said she's could be in her classroom? Let's check it out."
                else:
                    mc "Maybe she's still in her classroom? Let's check it out."
                $ ch1_prev_activities_s += 1
                call ch1_prev_schooltime_loop_sclassroom
                pass
            "The entrance" if not entrance_check:
                if backyard_check == True and sayori_wait1 == False:
                    mc "Camilla said to check the entrance? Let's go then."
                else:
                    mc "I don't know why, but I want to check the entrance."
                $ ch1_prev_activities_s += 1
                call ch1_prev_schooltime_loop_entrance
                pass
            #"The roof" if not roof_check:
            #    mc "It sounds stupid, but I want to check the building's roof... Well, here goes nothing."
            #    $ ch1_prev_activities_s += 1
            #    call ch1_prev_schooltime_loop_roof
            #    pass
            "Give up!":
                mc "No..."
                mc "I must find her!!!"
                pass
        pass
    jump ch1_prev_schooltime2

    label ch1_prev_schooltime_loop_sclassroom:
        scene bg sayori_classroom
        with wipeleft_scene
        if sayori_wait1 == True:
            mc "She must be here-"
            s "Zzzzzzzzzzzz!"
            mc "Thank goodness! She's here after all."
            if backyard_check == True:
                "I owe a huge one to Camilla."
            mc "Hey! Sayori, wake up!"
            show sayori 1k at t11 zorder 2
            s "Ummm~?"
            "She starts to look at me with sleepy face."
            s 1b "[player]? What hour it is?"
            mc "It's 12 AM, lunch time."
            mc "Hey, what happened to you? I though you'll be looking for a table where we can lunch together."
            if backyard_check == True:
                mc "Even I called for help to find you in the entire school!"
            s 1l "Aaaah... I'm so sorry [player]."
            s "I falled asleep during classes."
            s 2s "Don't worry about me, I'm fine. I just... didn't sleep well."
            mc "Whatever. Do you want to lunch here then? I have mine in my bag, we can share it."
            s 4t "Really? Thanks [player]. You really are a nice person, the best I ever meet."
            mc "Thanks again. You are special for me too."
            s 4q "Hehe~"
            $ sayori_found = True
            pass
        if sayori_wait1 == False:
            mc "She must be here..."
            "Nobody is here."
            mc "Fuck!"
            mc "Where could be she?"
            mc "Let's go somewhere else..."
            $ s_classroom_check = True
            pass
        return

    label ch1_prev_schooltime_loop_mcclassroom:
        scene bg class_day
        with wipeleft_scene

        mc "Shit. No life signals..."
        $ mc_classroom_check = True
        return

    label ch1_prev_schooltime_loop_backyard:
        scene bg school_backyard
        with wipeleft_scene

        "No Sayori signals."
        mc "Where the fuck could she be?!"
        $ mcf2_name = "Girl voice"
        stop music fadeout 3.0
        mcf2 "Ara-ara [player]... Do you missed something?"
        mc "Eh?"
        show camilla at t11 zorder 2
        $ mcf2_name = "Blonde girl"
        play music t6
        mcf2 "Hi sweetie~!"
        mc "C-Camilla...?"
        $ mcf2_name = "Camilla"
        "She is Camilla. Maybe the second most popular girl in the school..."
        "She has everything to be even better than Monika, but... just like me, she's a bit lazy to do what Monika does to deserve the school's throne."
        "Also, we are friends since I was in the soccer club. For some reason she always cheered for me, all what I know is we love the same soccer team."
        "So it's a bit curious how a girl like her is very interested on my life and wants to help if she can."
        mcf2 "What are you looking for anyway? Should you be in the dining room eating right now?"
        mc "I'm looking for my friend Sayori. I haven't seen her where we met everyday."
        mc "What about you? I haven't seen you in the dining room either..."
        mcf2 "Well... I already eat something and, I'm not hungry anymore."
        mcf2 "Anyway. May I help you with your research?"
        mc "You do? Thank you very much! I appreciate that..."
        mcf2 "No problems. That's what friends do, right? Ryoma could do the same for you."
        mc "You got a point."
        mcf2 "Excellent!"
        if sayori_wait1 == True:
            mcf2 "Here's a hint: Check in her classroom."
            mcf2 "I saw both together in the entrance. But I haven't seen her going somewhere else at lunchtime, and I have a nice view here."
            mc "Really? If you're correct, you have my gratitude."
            mcf2 "Hahaha don't worry about that."
            mcf2 "Okay, I'm gonna check for her in the women bathroom first. You go where I told you."
            mcf2 "Goodluck [player]~!"
            mc "Thank you very much Camilla..."
            mcf2 "Hehe, don't mention it~"
            show camilla at thide zorder 1
            hide camilla
            "Alright, I have an trustable hint. Let's go to her classroom."
            $ backyard_check = True
            pass
        if sayori_wait1 == False:
            mcf2 "You know, I saw you waiting for her in the entrance, but after a few minutes you entered alone."
            mcf2 "Here's a hint: Go to the entrance. I have the feeling she's coming up for lunch."
            mc "Do you think so? Why Sayori would came so late. It's too much."
            mc "Anyway, If you're correct, you have my gratitude."
            mcf2 "Hahaha don't worry about that."
            mcf2 "Okay, I'm gonna check for her in the women bathroom first. You go where I told you."
            mcf2 "Goodluck [player]~!"
            mc "Thank you very much Camilla..."
            mcf2 "Hehe, don't mention it~"
            show camilla at thide zorder 1
            hide camilla
            "Alright, I have an trustable hint. Let's go to the entrance."
            $ backyard_check = True
            pass
        stop music fadeout 1.0
        play music midnight_piano
        return

    label ch1_prev_schooltime_loop_entrance:
        scene bg school_entrance
        with wipeleft_scene

        "..."
        if sayori_wait1 == True:
            mc "Nope. No Sayori signals..."
            mc "Let's go somewhere else."
            $ entrance_check = True
            pass
        if sayori_wait1 == False:
            mc "Hmm?"
            "I'm seeing a silouette similar to Sayori... Could she be...?"
            mc "Yes! She is!"
            if backyard_check == True:
                "I owe a huge one to Camilla."
            mc "Sayori!!!"
            show sayori 1n at t11 zorder 2
            s "Eh?"
            s 4h "[player]? What are you doing here?"
            s 4i "Please don't tell me you was waiting for me all this time..."
            mc "No Sayori. I was just looking for you instead."
            mc "What happened? I've been waiting for you in the entrance until 8:50 AM but it was a waste of time."
            show sayori 1k
            mc "Why didn't you answered my calls? I've been very, very worried about you."
            if backyard_check == True:
                mc "Even I called for help to find you in the entire school!"
            s 1l "I feel asleep. I haven't heard the alarms and you phonecalls because my phone's battery drained in the night."
            s 1p "Sorry [player], sometimes I'm a dissaster."
            mc "Now don't worry Sayori. The most important is you're okay."
            mc "Well. I bring up my lunch with me. Do you want to share it with me?"
            s 1t "Really? Thanks [player]. You really are a nice person, the best I ever meet."
            mc "Thanks again. You are special for me too."
            s 1q "Hehe~"
            $ sayori_found = True
            pass
        return


label ch1_prev_schooltime2:
    $ HKBShowButtons()
    $ HKBHideButtons()
    $ bag_inventory.remove_item("schoollunch")
    stop music fadeout 3.0
    scene bg class_day
    with wipeleft_scene
    play music t3

    mc "The worst has just ended."
    mc "I was very worried about Sayori..."
    if backyard_check == True:
        play audio ringtone1
        mc "Eh?"
        "It's Camilla. I told her I just found Sayori... What does she says?"
        "{i}I'm so glad you found Sayori, [player].\nSee you later bb~! :emoji_kiss: :heart:{/i}"
        mc "So cute..."
        "I replied with love emojis too to keep the diabetical track."
        "I wonder how a girl like her can be so nice..."
        "..."
    mc "Recess has just over, it's time to start the second half of class."

    scene black
    with dissolve_scene_full
    pause 2.0
    scene bg class_day
    with dissolve_scene_full
    play sound school_bell

    mc "Finally! It's time to go to the Literature Club."
    mc "I wonder if I must wait for Sayori to pick on me..."

    menu:
        mc "Also, she doesn't have battery, so I can't call her."

        "Go pick up Sayori":
            mc "Fine, let's pick up her first and then let's go to the club."

            scene bg sayori_classroom
            with wipeleft_scene

            mc "Hello~?"
            "Sayori's schoolmate" "Ah, you must be Sayori's boyfriend."
            "Sayori's schoolmate" "She has just parted to her boring club already."
            mc "Hey. What's wrong with the club? Have you entered before?"
            "Sayori's schoolmate" "No. But everybody knows the literature is boring..."
            mc "Well, you should enter in and check it for yourself."
            mc "And thanks for the advice, punk."
            pass
        "Go directly to the club":
            mc "At this hour she could be in the club right now."
            pass
    "Anyway, let's go to the club then."
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full

    return