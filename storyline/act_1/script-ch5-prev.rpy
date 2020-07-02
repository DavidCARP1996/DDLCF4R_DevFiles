label ch5_prev:
    $ persistent.autoload = "ch5_prev"
    #$ persistent.playthrough = 1 # No turn back now baby... Fight or Die!
    "Tonight..."
    pause 1.0
    scene bg bedroom_night
    with dissolve_scene_full
    mc "{cps=30}..................................................{/cps}{nw}"
    mc "{cps=30}..................................................{/cps}{nw}"
    mc "{cps=30}..................................................{/cps}{nw}"
    mc "..."
    call glitch1
    show mask_2
    show mask_3
    #play music m1
    show monika sdwb1 at t11 zorder 2
    "???" "What's the matter? Trouble sleeping?"
    mc "You!"
    mc "I don't know if I'm right but... Did you come here to help me to save Sayori?"
    "???" "Listen, honestly the fate of your friends is not of my business."
    "???" "And I guess that friend of yours Sayori is somehow interfiering with my investigations."
    "???" "So if she wants to commit suicide,{w} then she's just doing me a favor."
    play music hb
    #show layer master at dizzy(0.5, 1.0)
    #show layer screens at dizzy(0.5, 1.0)
    #show image Solid("ff0000") as i1 onlayer front:
        #additive 1.0
    show veins onlayer front:
        additive 0.5
    show layer master at heartbeat
    mc "WHAT?!"
    if ch4_scene == "monika":
        "???" "And you know what?{w} I was ABOUT to acchieve my objective and leave you happy and alone FOREVER."
        "???" "But your idiotic friend screwed up everything."
        mc "What the fuck do you mean?!"
        "???" "Since she was making everything difficult, I had no choice but..."
    else:
        "???" "And you know what?{w} You didn't collaborated with my objective."
        "???" "I told you to stay away of some girls and you just kept closer to them..."
        mc "What the fuck do you mean?!"
        "???" "Since you insisted on disobey my indications, I had no choice but..."
    show image Solid("#440000") as i2 zorder 4:
        additive 5.0
    $ style.say_dialogue = style.edited
    "???" "{cps=7}Giving her a little push............{/cps}{nw=2.0}"
    $ style.say_dialogue = style.normal
    show s_cg3_g1 zorder 4
    pause 0.000000000000001
    show s_cg3_g2 zorder 4
    pause 0.00000001
    call glitch1
    hide hxppy_thxughts
    mc "Now everything makes sense!!!"
    mc "Monika! I had the suspicion that {b}YOU{/b} were behind all this!"
    mc "Then that explains why you've been sooooo nice to ME when I joined the Club..."
    mc "It wasn't because you changed in order to become friends and club partners with me."
    mc "But you've been hiding a strange secret that...{w=2.0} Maybe..."
    #$ style.say_dialogue = style.edited
    #mc "{cps=10}Maybe you want something what I have...{/cps}"
    #hide black onlayer front
    hide veins onlayer front
    with dissolve
    #hide i1 onlayer front
    hide i2 zorder 4
    with dissolve
    show layer master
    show layer screens
    stop music fadeout 1.0
    $ style.say_dialogue = style.edited
    mc "{cps=10}Maybe you want something what I have...{/cps}"
    #mc "{cps=4}You want the Player who controlls ME.........{w=2.0}isn't???{/cps}"
    $ style.say_dialogue = style.normal
    "Monika?" "What?!"
    mc "Yeeeeaaaahhhh........."
    mc "You delated yourself when you mentioned that was YOU who have been manipulating Sayori's conscience and make her wants to die."
    mc "And I didn't forget what Sayori said about you!"
    if ch4_scene == "monika":
        mc "And that also explains the situation when you where graving my head and talk to me like if I were a kind of microphone. Then the glitches, etcetera."
    else:
        pass
    "Monika?" ""
    mc "Tell me... Are you behind of Sayori's death wish???"
    "Monika?" "Silence!"
    "Monika?" "So... Do you want to see your little friend Sayori wakes up tomorrow?"
    "Monika?" "Then hurry up because at this hour she seems about to die already~"
    mc "{cps=2}You...{/cps}"
    pause 0.5
    call boss_battle1

    if boss_battle1_victory == True:
        mc "... ... ..."
        "Monika?" "You...{w=1.0} Asshole!!!"
        "Monika?" "I promise you...{w=1.0}you will pay for this!"
        mc "Just leave Sayori and the others alone! I don't care what do you want to do with me, don't mess with my friends!"
        mc "You heard me?"
        "Monika?" "What{w=1.0}ever...!"
        "Monika?" "Fine!{w=1.0} I...{w=1.0} will leave your Sayori a-{w=1.0}alone..."
        "Monika?" "But the next time...{w=1.0} if you dare to...{w=1.0} interfer with my...{w=1.0}{nw}"
        $ _history_list[-1].what = "But the next time, if you dare to interfer with my relatioship with the player..."
        $ style.say_dialogue = style.edited
        call glitch1
        $ gtext = glitchtext(20)
        "[gtext]" "{cps=10}I'm gonna make you suffer worse than you ever suffered in your misserable life.........{/cps}{nw}"
        $ _history_list[-1].what = "Can you read this... isn't?"
        "[gtext]" "{cps=10}See you later...{w=1.0} [player]{/cps}{w=1.0}{nw}"
        $ _history_list[-1].what = "Delete that creep for me! Please!"
        $ style.say_dialogue = style.normal
        call glitch1
        hide monika
        $ _history_list.pop()
        "... ... ..."
        window hide(None)
        window auto
        pause 3.0
        scene black
        with dissolve_scene_full
        pause 1.0
        jump ch5_sayori_saved
    else:
        mc "Why...{w=3.0}you........."
        "Monika?" "You confronted me,{w=2.0} now you will pay the consequences..."
        "Monika?" "But anyway, I was about to do something about her even if you don't interefered. Hahahaha~"
        "Monika?" "So here goes nothing.{w=0.5}.{w=0.5}."
        mc "No!{w} Stop it!"
        $ gtext = glitchtext(20)
        "Monika?" "{cps=60}[gtext]{/cps}{nw}"
        $ consolehistory = []
        call updateconsole("os.remove(\"characters/sayori.chr\")", "sayori.chr deleted successfully.")
        $ delete_character("sayori")
        "Monika?" "See you later... [player]~{w=1.0}{nw}"
        call glitch1
        window hide(None)
        window auto
        hide Monika
        call mc_pain2
        jump ch5_sayori_dead

label ch5_sayori_saved:

    $ persistent.autoload = "ch5_sayori_saved"
    $ dokisaved = "sayorisaved"
    scene bg bedroom_night
    with dissolve_scene_full
    mc "!"
    mc "Sayori!"
    "Wait a minute.{w} I was... dreaming?"
    mc "Hmm..."
    "0:00 AM"
    mc "I will go to the bathroom"
    scene black with wipeleft_scene
    "The window of the bathroom is at the side of Sayori's bedroom window, maybe I can check if she is..."
    mc "Eh?"
    mc "The lights are turn On."
    mc "What the fuck is going on there?"
    "I don't like this, I will enter in..."
    scene bg house_night with wipeleft_scene
    menu:
        mc "Should I sneak in or call her?"

        "Sneak in":
            mc "Alright..."
            pass
        "Call her":
            mc "Sayori!!!"
            "... ... ..."
            "No answers."
            "Fuck this shit let's get in by the force!"
            pass
    "Like yesterday, I open the door and let myself in."
    scene black with wipeleft
    mc "Sayori?"
    "... ... ..."
    "I swallow."
    "I can't believe I ended up doing this after all."
    "Coming her up in her own house like this..."
    if sayori_confess:
        "That really is something that a boyfriend would do, isn't it?"
    else:
        "Isn't that more like something a boyfriend would do?"
    "In any case..."
    "It just feels right."
    "Outside Sayori's room, I knock on her door."
    mc "Sayori?"
    "There's no response."
    "I really didn't want to have to enter her room like this..."
    "Isn't it kind of a breach of privacy?"
    "But she really leaves me no choice."
    "I gently open the door."
    mc "{cps=30}.......Sayo--{/cps}{nw}"
    scene bg sayori_bedroom_night with dissolve_cg
    show sayori 5dv at t11 zorder 2 with dissolve_cg
    play music tmod2
    "{cps=15}... Oh... my... god...{/cps}"
    s "[player]???"
    mc "{cps=15}S-S-S-S-S..........{/cps}"
    "I'm disconcerted... I-I don't know what to say..."
    "I point to the rope with my index finger with shiver..."
    mc "Sa...Sayori..."
    s "Y-Yeah?"
    mc "A...Ah...."
    mc "{cps=10}{i}What the fuck are you doing????????{/i}{/cps}{nw=1.0}"
    s "I... Ah..."
    show sayori 6dw
    "Sayori starts to cry..."
    s "I'm sorry [player]!!! I'M SO SORRY!!!"
    s "I don't even know what I'm doing!!!"
    s "I was... I-"
    show sayori 4dv
    "I take the rope by the force and throw it with anger outside the window."
    mc "Sayori... Tell me the truth..."
    s 1du "... ... ..."
    mc "Did Monika suggested you to commite suicide?!"
    s 4dv "What?!"
    mc "Yesterday you mentioned that \"Monika was right that you should just\" do something you never said what was exactly."
    mc "And now I see you're about to hanging yourself."
    mc "There's no other answer here... She is responsible for this!"
    mc "I'm going to talk with her tomorrow at first hour..."
    s 1dw "No [player]! Don't do anything bad to her! Please!"
    mc "I won't do anything wrong, calm down..."
    s 1dv "She didn't said that... She just... Said that I must do the right thing..."
    show sayori 1du
    mc "Sayori... Let me make you a question:"
    mc "{cps=10}How do you call {b}this{/b}{w=1.0} A RIGHT{w=1.0} FUCKING{w=1.0} THING???{/cps}"
    s 1dk "I deserve it anyway..."
    mc "Why?!"
    s 1dw "Don't you remember?{w} I RUINED YOUR LIFE [player!u]!"
    s "That accident of yours was completely my fault..."
    s "I dragged you to the Literature Club so you would forget about me and hang with anyone else!"
    s 1du "But I was weak, and I ruined your best moment with [ch4_name] just to tell you how much I loved you all this time."
    s 1dk "I don't know why I wanted to say that before I die... It's supposed it must kept in secret with me when I die."
    mc "Sayori...{w} You're completely wrong."
    s 1du "Eh?"
    mc "It wasn't your fault..."
    mc "It was MY fault instead."
    s 1dw "What are you saying?!"
    s "If I didn't crossed that street...{nw}"
    show sayori 1dv
    mc "You crossed that street because I wasn't capable to stop you..."
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    "Now I'm about to tell all of you the story of my accident."
    "It was 2 years ago..."
    "When Ryoma and me where soccer players representing our school."
    play music flashback1
    scene bg school_football_field
    with dissolve_scene_full
    "The next day from now was the Finals, so I decided to go to do some training in the school."
    show sayori 1bbl at t11 zorder 2
    "Oh, and Sayori followed me..."
    "She with long hair looks more cutier. {w}And sexier{nw}"
    s 3bll "[player], I'm a bit bored..."
    s "May I play with you? I can be a greatful help to your training."
    s 4bcl "Have you heard the saying: \"Two heads thinks better than one\"?"
    mc "Are you sure Sayori? I don't want to hurt you or anything."
    s 3bxl "Of course. I've learned a lot watching you playing... As you learned it watching that soccer anime about that Nº10 with wings."
    s 1bal "But you're most like the Nº12 with the white bandana while your friend is the Nº9 who spawns a tiger when he scores."
    mc "Hehehe... Okay."
    mc "I wanted to practice shooting, maybe you can be the Goalkeeper. You know, the guy with the cap."
    s 4brl "Yeeeey~!!!"
    scene bg school_football_field with wipeleft_scene
    "We've done a lot of penalties practice... Sometimes we turned positions because I want to practice my reflexes."
    "This time, I shot again."
    s "Come on [player]!"
    mc "Here I go!"
    "I've been practicing a shot to avoid the defense, that technique will help me to make better passes too."
    "It consists to send the ball very high but with a landing point which I need to practice to make it perfect."
    "Here we go!"
    mc "Hiyaa-!"
    "..."
    s "Eh?"
    mc "Oh no..."
    "The ball went too high that traspassed the fences and go directly to the avenue... Here comes the worst part."
    s "I will take it back~!"
    mc "Sayori wait, it could be dangerous..."
    s "Don't worry [player], there's no traffic today, see?"
    "Instead to run directly to her, I just looked the empty streets like a idiot."
    "Suddently, she dissapeared."
    mc "Oh, shit! Sayoriiii!!!"
    scene bg street_flashback
    with wipeleft_scene
    show sayori 4bal at t11 zorder 2
    s "[player]! I got it!"
    mc "SAYORIIII--!!! WATCH OUT--!!!"
    s 4bol "Wha-"
    s 4bml "*gasp*"
    hide sayori
    show bg truck_accident
    with dissolve_cg
    mc "SAYORIIIIIIIIIIIIIIIIIII--!!!!!!!!!!"
    s "[player!u]-!!! WHAT ARE YOU DOIN--"
    play sound truck_brakes
    scene black with dissolve_scene_full
    "Just right before the truck run over Sayori, I hold her while I'm jumping on her just in front of the truck, taking the impact in order to protect her."
    "After that, all what I remembered was the hit against the asphalt which left me unconscious and some pain on my right leg..."
    s "[player]???"
    s "[player!u]!!!!!!!"
    s "NOOOOOOOOoooooooOOOOOOO---!!!!!"
    pause 2.0
    "I was in the hospital a few days, all this time I didn't woke up."
    "When I started to recover the consciousness, a familiar face presents on my eyes..."
    scene bg health_room
    show sayori 1bb at face
    with open_eyes
    s "[player]?"
    mc "Uhh..."
    s 1bt "[player]! Thank God!"
    mc "S...Sayori?"
    s "Yes."
    mc "Where... am... I...?"
    s 4bv "We are in the hospital."
    s 4bw "You haven't woke up a few days! Everybody was worried about you-!"
    mc "A-A-A-A-A FEW DAYS YOU SAID???"
    show sayori 4bu at t11 zorder 2
    mc "Fuck! The Tournament!"
    s 1bk "Ehh.. about that..."
    s 1bg "I'm affraid your team lost the Finals..."
    s 1bu "... ... ..."
    s 1bw "I'M SO SORRY [player!u]!!! IT WAS MY FAULT!!!"
    mc "Sayori... You didn't..."
    s 4bw "NO!"
    s "YOU ALMOST DIED BECAUSE YOU SAVED MY LIFE FOR A MISTAKE OF MINE!!!"
    s "I DON'T DESERVE YOU!!!"
    mc "Sayori!! Calm down!! Don't say such things!!"
    mc "Calm down! Please!"
    s 1bu "... ... ..."
    mc "Look the positive side: We both are alive."
    mc "If I didn't used my body like a shield for you, you could be dead and I would lament myself your lost."
    mc "There's no trophy which can cost more than your life Sayori, remember that."
    s 1bk "But... Everybody in the school is talking bad things about you for that loss."
    mc "Fuck them! And fuck their opinions!"
    mc "Maybe I've lost the trophy and the reputation of the school. But at least I didn't lose you."
    s 3bg "[player]..."
    s 3bf "... ... ..."
    s 4bd "Alright."
    s "At least I didn't lose you neither..."
    mc "Well said!"
    scene black with dissolve_scene_full
    pause 1.0
    scene bg sayori_bedroom_night
    show sayori 1dv at i11 zorder 2 
    with dissolve_cg
    mc "If I had stoped you in that moment, then we could avoid that incident."
    mc "Your intention was good throught..."
    s "[player]..."
    #$ persistent.clear[12] = True
    scene s_cg4
    show s_cg4_exp1
    with dissolve_cg
    s "You are a excellent person [player]."
    s "That's why I always loved you, you're kind, honest, and..."
    mc "Nah."
    mc "I'm just trying to do the right things, that's all."
    if sayori_confess:
        mc "And saying Yes to your love confession was one of them."
    else:
        mc "I wish I'd never friendzoned you. I don't know what I was thinking..."
    hide s_cg4_exp1 with dissolve_cg
    s "But... What about [ch4_name]?"
    mc "It doesn't matter..."
    if ch4_scene != "monika":
        mc "[ch4_name] seems to be ok about our relationship, after all she and I haven't went too far like both of us did."
    else:
        mc "Monika wasn't my type after all, all our \"friendship\" was a sort forced... I don't know why she suddently wants something with me, but I won't fall on her enhancements so easy."
    s "I see..."
    s "If you're ok about changing a chance with her for me, then I'll not complain about it."
    mc "I'm glad to hear that."
    scene black with dissolve_scene_full
    $ if all(clear for clear in persistent.clear): persistent.clearall = True
    if persistent.clearall:
        "I guess I'm done. I've spend time with anyone from the Club... I wish to give Camilla a opportunity too."
        "Anyway, I still got Sayori at my side who is the most important here."
    else:
        "Maybe I forgot to do something important... But at least I still got Sayori at my side."
        "May reseting the game worth? I don't know... I don't suggest to do that neither."
    window hide(None)
    window auto
    stop music fadeout 2.0
    pause 3.0
    play music t10
    scene bg sayori_bedroom_night
    with dissolve_scene_full
    show sayori 1da at t11 zorder 2
    mc "Sayori."
    s "Yeah?"
    mc "Before I go back to sleep, I've been thinking..."
    mc "Do you want to sleep with me? No matter if it's on my bed or yours, it's your choice."
    s "What?!"
    s "[player]! It's a kind of perv..."
    s "But...{w} We are a couple now, isn't? So there's no problem after all."
    mc "That's right. We can even take a bath together without worrying about our privacy."
    s "[player]..."
    s "Alright. Let's go to your house."
    s "For some reason my bedroom is giving me bad chills."
    s "Like, there's still some rainclouds leftovers in my head."
    mc "I see..."
    mc "It's decided then, take all the things you must bring up to the festival tomorrow and let's go to my house."
    s "Okay~!"
    scene bg house_night with wipeleft_scene
    "Sayori and I have put together all the things that we will take to my house."
    "There's not much, so I can handle it easy."
    "Sayori will turn off all the lights and close every door."
    scene bg bedroom with wipeleft_scene
    show sayori 2dx at t11 zorder 2
    mc "Here we are..."
    s "Thank you [player]..."
    s "Umm... What now?"
    mc "Well, let's go to sleep... In my bed, of course..."
    s "Uuuuuuu..."
    s "It's a bit awkward, you know?"
    s "I mean, it's not like I don't want to sleep with you like this, contrarily I love it."
    s "But it's happening so sudden..."
    mc "Yeah, I know how do you feel..."
    mc "But don't worry, I won't hurt you, hahaha."
    s "Hehehe~"
    show sayori at thide
    hide sayori
    "Sayori lies down on my bed while I'm turning the lights off."
    play sound click
    scene bg bedroom_night
    "Now it's my turn to lay down."
    pause 1.0
    "I cuddle to Sayori..."
    "{cps=50}... ... ...{/cps}"
    "Oh shit..."
    "I'm erect{nw}"
    "Ejem... Listen, maybe the next scene is a bit...{w} sexual so to speak."
    "If you want to skip it, there's no problem. It will not affect to our progress anyway."
    menu:
        "What do you say?"

        "Watch the function":
            "Here we go then..."
            pass
        "Skip":
            "Whatever."
            jump ch5_sayori_saved_aftersex
    s "[player]?"
    mc "Yeah?"
    s "I feel something in my... back... I mean... apart of your body..."
    mc "Hahahaha don't worry Sayori, it's my body... or at least one of my parts..."
    mc "The thing is... I'm {i}excited{/i} for this moment."
    mc "Don't worry, that \"thing\" you're feeling is normal..."
    s "What?"
    mc "Listen, maybe this sounds very daring but..."
    mc "Did you know what...{w} sex is very effective against your rainclouds?"
    s "Sex?"
    s "What do you mean?"
    mc "Oh, that's true!"
    mc "You're not like me..."
    "Shit, how can I explain it to her???"
    s "I know what's sex about, but I don't understand what does it have to do with my rainclouds..."
    mc "Well, people says that sex is a very effective anti-depressing."
    mc "And I now we have the chance, so I want to test if it's true or not."
    mc "What do you think? I won't force you if you don't want to do it..."
    s "Well umm..."
    s "Okay!"
    s "Let's do this."
    mc "Uhuhuhu~ Alright!"
    s "How can we start?"
    mc "I'm affraid that we both must take of our clothes."
    mc "We can do this without need to do that, but it's more effective if we are naked."
    s "I see..."
    pause 3.0
    s "What now?"
    scene bg bed_sex
    show sayori 4na at face(y=600) 
    with dissolve_cg
    mc "Then... you will feel something between your...{w=2.0} legs..."
    s 4nb "Oh, well I-{nw}"
    s 4ne "Ahh!"
    s "..."
    s 4np "Aaaahhh!"
    s "Why it's a sort... Aaahhhh!"
    mc "*heavy breathing*"
    s "*pleasant groans*"
    pass

label ch5_sayori_saved_aftersex:
    scene black with dissolve_scene_full
    pause 2.0
    mc "So... What do you think?"
    s "Ehm..."
    s "It was... fun I guess..."
    s "I can't believe we just done that dirty thing."
    mc "Yeah, me neither."
    s "But you know what? I feel like the rainclouds are going away more faster."
    mc "That's what I wanted to hear!"
    mc "I knew this plan will work."
    mc "I'm so happy Sayori..."
    s "Hehe~ Me too [player]..."
    "We cuddle each other."
    "Seriously man, I can believe I've done that, and with Sayori."
    "Tomorrow will be a great day."
    "Let's hope that hacker girl...{w} or Monika?...{w} I don't know, the thing is let's hope she doesn't dare to hurt Sayori or anyone else..."

    return

label ch5_sayori_dead:
    
    $ persistent.autoload = "ch5_sayori_dead"
    $ dokisaved = "nonesaved"
    scene bg bedroom_night
    pause 4.0
    scene bg bedroom_dark with dissolve_cg
    pause 2.0
    scene bg bedroom with dissolve_cg
    mc "Noooooooooooooooooooooooooo{w}"
    mc "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!{w}"
    mc "!"
    "What the...?"
    mc "I was...{w} dreaming?"
    "I take a break... I don't know what the fuck just happened... it's..."
    mc "Sayori!"
    "*dialing Sayori*"
    mc "Her phone is off? Shit!"
    mc "I'm thinking about what happened \"in that dream\"..."
    mc "Could that girl be really Monika?"
    mc "It can't be a coincidence... Also, she cannot fall so easy to blame herself like that..."
    mc "Yes! I will chat with Monika to check if it was true."
    "{i}Hi Monika! How are you? Listen, everything is ready for the festival? I was about to going now but I want to check is the club is already open...{/i}"
    "... ... ..."
    "{i}Hi [player]... well, i was just about to going to the school. it's still soon you know? are you excited? everyone is... i'll be waiting for you~ <3{/i}"
    mc "A heart? From Monika?!"
    mc "The only persons in this world who dares to send me hearts are Sayori and Camilla. So, it's very weird to see it coming from Monika..."
    mc "Anyway, I guess everything was just a nightmare after all..."
    mc "I must prepare everything to go to the festival."
    mc "Let's go!"

    return
