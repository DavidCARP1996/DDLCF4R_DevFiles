image exception_bg = "#dadada"
image fake_exception = Text("An exception has occurred.", size=40, style="_default")
image fake_exception2 = Text("File \"game/script-ch5.rpy\", line 307\nSee traceback.txt for details.", size=20, style="_default")

image splash_glitch:
    subpixel True
    "images/bg/splash-glitch.png"
    alpha 0.0
    pause 0.5
    linear 0.5 alpha 1.0
    pause 2.5
    linear 0.5 alpha 0.0
    "gui/menu_bg.png"
    topleft
    alpha 0.0
    parallel:
        xoffset 0 yoffset 0
        linear 0.25 xoffset -100 yoffset -100
        repeat
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        ypos 0
        pause 1.0
        easeout 1.0 ypos -500
image splash_glitch2:
    subpixel True
    "gui/menu_bg.png"
    topleft
    block:
        xoffset 0 yoffset 0
        linear 0.05 xoffset -100 yoffset -100
        repeat

image splash_glitch_m:
    subpixel True
    "gui/menu_art_m.png"
    zoom 0.5
    xpos 0.5 ypos 0.5
    pause 0.1
    parallel:
        xpos 0.3 ypos 1.2
        linear 0.08 ypos 0.1
        repeat
    parallel:
        pause 0.5
        alpha 0.0

image splash_glitch_n:
    subpixel True
    "gui/menu_art_n.png"
    zoom 0.5
    pause 0.2
    xpos 0.8 ypos 0.8
    pause 0.05
    xpos 0.2 ypos 0.7
    pause 0.05
    xpos 0.4 ypos 0.2
    pause 0.05
    xpos 0.7 ypos 1.2
    pause 0.05
    xpos 0.1 ypos 1.0
    pause 0.05
    xpos 0.2 ypos 0.6
    pause 0.05
    xpos 0.9 ypos 0.4
    pause 0.05
    alpha 0.0

image splash_glitch_y:
    subpixel True
    "gui/menu_art_y.png"
    zoom 0.5
    ypos 1.3
    block:
        xpos 0.85
        pause 0.02
        xpos 0.81
        pause 0.02
        repeat

#####################################
########## Sayori is saved ##########
#####################################

label ch5_sayorisaved_main:
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    "... ... ..."
    mc "Uwaaaaaaa~!"
    mc "Ehm... Sayori..?"
    mc "!"
    mc "Sayori?!"
    scene black
    with wipeleft_scene
    mc "Sayori!!"
    "Where the fuck is she?!"
    mc "Sayori----!!!!"
    scene bg house
    with wipeleft_scene
    mc "Oh, fuck! She's not in my house!"
    "... ... ..."
    "But, what if...?"
    mc "No!"
    mc "It cannot be a fucking dream!"
    mc "It happened for real!!"
    "I enter to her house..."
    scene black with wipeleft_scene
    mc "Sayori?"
    "My heart starts to pound stronger, I'm very nervious!"
    "It's not like I think the last night moment was just a dream, it's because I've had that kind of dreams before..."
    "I managed to dream it with Yuri once."
    "They seemed too real that I... Well... Fuck it I won't say it!"
    mc "Sayori??"
    "Now I'm in front of her bedroom door."
    "Here we go..."
    "I gently open the door."
    mc "{cps=30}.......Sayo--{/cps}{nw}"
    scene bg sayori_bedroom
    with dissolve_scene_full
    mc "...ri?"
    "What the hell?!"
    "She's not here neither..."
    play audio ringtone1
    mc "Eh?"
    "It's Sayori!"
    "{i}[player], where are you? i went to the shop to buy something to breakfast but suddently you're gone...{/i}"
    mc "{cps=30}Thank Goodness--!!!{/cps}"
    "I reply to Sayori telling her I went to take a walk. I can't tell her what I went to her house thinking she did that{w} thing."
    "Let's get out of here before she notices I invaded her house."
    scene bg house
    with wipeleft_scene
    mc "I hope she isn't turning on the oven..."
    scene bg kitchen
    with wipeleft_scene
    play music t6
    show sayori 1a at t11 zorder 2
    s "Hey! Where did you go dummy?"
    s "I start to become worried about you when you dissapeared from your bed."
    mc "I wanted to take a morning walk, that's all Sayori..."
    s "Alright... But let's take a breakfast, there's no time before the festival preparatives starts."
    "It sounds weird coming from Sayori... You know, all this time she was waking up even more and more late."
    mc "Hahahahaha, okay okay."
    "She seems renovated after last night. I don't know if it was the sex or taking away Monika, but at least she doesn't looks depressive anymore."
    "She is again the Sayori I knew all my life."
    "And everything is thanks to YOU. Seriously."
    s "Here you go [player], a sweet orange juice with cookies~!"
    mc "Thanks Sayori..."
    "I kiss her in her cheeks."
    s "Eheheheh~!"
    mc "Ehm... You will not take a breakfast Sayori?"
    s "Well, I have advanced breakfast..."
    s "I'm gonna bring you your school uniform so you can dress up here and then get going right to the school."
    mc "Oh, sure! Thanks."
    "Sayori goes to my bedroom."
    pause 3.0
    mc "Wow! It was delicious!"
    "I know everything was bought, but I want to make feel good to Sayori..."
    s "Do you think so? Hehe~ thanks [player]."
    mc "Don't mention it."
    if ch4_scene == "yuri":
        s "Here you got your uniform, put it up while I take the Banner that you and Yuri make."
        s "It's beautiful, both of you did a great job!"
        mc "I'm glad to hear that... Remember to say it to Yuri too."
        s "I will~"
    elif ch4_scene == "natsuki":
        s "Here you got your uniform, put it up while I put the cupcakes that you and Natsuki make into the tuppers."
        s "They seems so delicious... It's a shame I can't taste at least one."
        mc "Don't worry, take one if you want. In any case I will say it was me who ate the missing cupcake."
        s "Are you sure??? Oh wow, thanks~!"
    else:
        s "Here you got your uniform, put it up while I go to the bathroom."
        s "I guess I've drinking too much juice..."
        mc "Go on Sayori."
        s "Thanks."
    scene black
    with dissolve_scene_full
    stop music fadeout 2.0
    pause 3.0

    scene bg residential_day
    with wipeleft_scene
    play music t2

    "It's the day of the festival."
    "I can't believe this day will finally come. I thought the week could be larger..."
    "Meanwhile, the preparations for the event should be nearly complete."
    if ch4_scene == "yuri":
        "The banner Yuri and I painted is dry, and I gently rolled it up to take with me."
        "She sent me a pleasant text reminding me not to forget anything, and I reassured her. I want to send her love emojis but I can't do that now that I'm in couple with Sayori."
    elif ch4_scene == "natsuki":
        "Sayori is helping me to carry all the cupcakes in their tuppers."
        "Natsuki is already texting up a storm, but I can't respond because I can lost the balance if I carry the tupper with one arm while I pick my phone with the other arm."
    else:
        pass
    "Funnily enough, I probably feel the same way as Natsuki about the event."
    "I'm more excited for it to be over so I can spend time with Sayori and [ch4_name] at the festival."
    "But knowing Monika, I'm sure the event will be great, too."
    scene bg school_entrance with wipeleft_scene
    stop music fadeout 5.0
    mc "Eh?"
    s "What's wrong [player]?"
    mc "It's weird... I thought I could across with Ryoma and Camilla here but..."
    mc "They aren't here..."
    s "It's still early for the festival, maybe they'll come more later or they just entered in."
    mc "Right..."
    mc "Anyway let's go to the Literature Club."
    scene bg corridor with wipeleft_scene
    mc "What the holy fuck...?"
    s "What now?"
    mc "Didn't you notice it? The entire school is EMPTY!"
    s "..."
    s "Wow! You're right!"
    s "Why nobody is here? It's supposed to be very crowded today..."
    mc "I don't know, but I have a bad feeling about it."
    mc "Come on, let's keep going to the Literature Club. Maybe it's nothing or a surprise party or something like that."
    s "S-Sure!"
    scene bg club_day with wipeleft_scene
    show monika 5 at t11 zorder 2
    m "[player]!"
    m "You're the first one here."
    m "Thanks for being early!"
    mc "Monika, what the hell is going on here?"
    "Monika is placing little booklets on each of the desks in the classroom."
    "They must be the ones she prepared that has all the poems we're performing."
    "In the end, I found a random poem online that I thought Monika would like, and submitted it."
    "So, that's the one I'll be performing."
    m 1d "I'm surprised you didn't bring Sayori with you."
    mc "What?"
    mc "But Sayori is with me, she..."
    "Wait, where is she?"
    m 1k "Ahaha."
    m 4b "You should take a little responsibility for her, [player]!"
    m "I mean, especially after your exchange with her yesterday..."
    show monika 4a
    mc "Exchange...?"
    mc "Monika-- You know about that??"
    m 2a "Of course I do."
    m "I'm the club president, after all."
    mc "But--!"
    m 2j "Don't worry."
    m "I probably know a lot more than you think."
    mc "Eh...?"
    "Monika is being as friendly as usual, but for some reason I felt a chill down my spine after hearing that."
    "Seriously... Where did Sayori go?"
    "Maybe she went to the bathroom? She must adviced me first."
    "Well then, let's go to the main topic..."
    mc "Monika, can you tell me why the school is empty?"
    mc "I mean, we are only you, Sayori and me only."
    m "Well umm..."
    m "I'm affraid that everyone is almost waking up. Hahaha..."
    "What's so funny? I'm up to my nerves..."
    m 5 "Hey, do you want to check out the pamphlets?"
    m "They came out really nice!"
    mc "Yeah, sure."
    "I grab one of the pamphlets laid out on the desks."
    mc "Oh yeah, they really did."
    mc "Something like this will definitely help people take the club more seriously."
    m "Yeah, I thought so too!"
    show monika at thide zorder 1
    hide monika
    "I flip through the pages."
    "Each member's poem is neatly printed on its own page, giving it an almost professional feel."
    "I recognize Natsuki's and Yuri's poems from the ones they performed during our practice."
    mc "What's this...?"
    "I flip to Sayori's poem."
    "It's different from the one she practiced."
    "It's one that I haven't read before..."
    call showpoem(poem_s3, music=False)
    play music ghostmenu
    mc "Ah--"
    "{b}What the fuck is this...?{/b}"
    "Reading the poem, I get a pit in my stomach."
    "This poem feels completely different from everything else Sayori's written."
    "But more than that..."
    show monika 1d at t11 zorder 2
    m "[player]?"
    m "What's wrong?"
    mc "Monika..."
    mc "{cps=10}{b}WHAT THE FUCK IS THIS THING...???{/b}{/cps}"
    m "This is Sayori's poem. What's wrong with that?"
    mc "Do you think I'm an idiot?"
    mc "THIS IS NOT SOMETHING THAT SAYORI WOULD WRITE."
    m "But... She send me that one."
    mc "Don't even think I'm gonna fall on that!"
    mc "What the fuck is wrong with you Monika?"
    mc "First you wanted to become friends and all the shit."
    if poemwinner[0] == "monika" and poemwinner[1] == "monika" and poemwinner[2] == "monika" and ch4_choice == "monika":
        mc "Then we were about to become a couple because you saw on me something you didn't have seen on me last year..."
    mc "And now you're kidding me and playing mindgames with me like if I were stupid."
    return

####################################
########## Sayori is dead ##########
####################################

label ch5_nonesaved_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    "It's the day of the festival."
    "Of all days, I expected this to be the one where I'd be walking to school with Sayori."
    "But Sayori isn't answering her phone."
    "I considered going to her house to wake her up, but decided that's a little too much."
    "Meanwhile, the preparations for the event should be nearly complete."
    if ch4_scene == "natsuki":
        "I managed to carry all the cupcakes myself by carefully stacking two trays."
        "Natsuki is already texting up a storm, but I can't respond, thanks to my hands being full."
    else:
        "The banner Yuri and I painted is dry, and I gently rolled it up to take with me."
        "She sent me a pleasant text reminding me not to forget anything, and I reassured her."
    "Funnily enough, I probably feel the same way as Natsuki about the event."
    "I'm more excited for it to be over so I can spend time with Sayori and [ch4_name] at the festival."
    "But knowing Monika, I'm sure the event will be great, too."

    scene bg club_day with wipeleft_scene
    show monika 5 at t11 zorder 2
    m "[player]!"
    m "You're the first one here."
    m "Thanks for being early!"
    mc "That's funny, I thought at least Yuri would be here by now."
    "Monika is placing little booklets on each of the desks in the classroom."
    "They must be the ones she prepared that has all the poems we're performing."
    "In the end, I found a random poem online that I thought Monika would like, and submitted it."
    "So, that's the one I'll be performing."
    m 1d "I'm surprised you didn't bring Sayori with you."
    mc "Yeah, she overslept again..."
    mc "That dummy."
    mc "You'd think that on days this important, she'd try a little harder..."
    "I say that, but I suddenly remember what Sayori told me yesterday..."
    "And I suddenly feel awful, knowing it's not nearly that simple for her."
    "I only said it because it's the way I'm used to thinking."
    "But..."
    "Maybe I should have gone to wake her up after all?"
    m 1k "Ahaha."
    m 4b "You should take a little responsibility for her, [player]!"
    m "I mean, especially after your exchange with her yesterday..."
    m "You kind of left her hanging this morning, you know?"
    show monika 4a
    mc "Exchange...?"
    mc "Monika-- You know about that??"
    m 2a "Of course I do."
    m "I'm the club president, after all."
    mc "But--!"
    "I stammer, embarrassed."
    "Did Sayori really tell her about it that quickly?"
    if sayori_confess:
        "That we're...a couple now?"
        "I didn't really plan on bringing it up with anyone yet..."
    else:
        "About how I basically turned down her confession?"
        "That makes me really seem like the bad guy here..."
        "But I'm the one who knows what's best for her, right?"
    mc "Jeez..."
    mc "You don't know the full story at all, so..."
    m 2j "Don't worry."
    m "I probably know a lot more than you think."
    mc "Eh...?"
    "Monika is being as friendly as usual, but for some reason I felt a chill down my spine after hearing that."
    m 5 "Hey, do you want to check out the pamphlets?"
    m "They came out really nice!"
    mc "Yeah, sure."
    "I grab one of the pamphlets laid out on the desks."
    mc "Oh yeah, they really did."
    mc "Something like this will definitely help people take the club more seriously."
    m "Yeah, I thought so too!"
    show monika at thide zorder 1
    hide monika
    "I flip through the pages."
    "Each member's poem is neatly printed on its own page, giving it an almost professional feel."
    "I recognize Natsuki's and Yuri's poems from the ones they performed during our practice."
    mc "What's this...?"
    "I flip to Sayori's poem."
    "It's different from the one she practiced."
    "It's one that I haven't read before..."
    call showpoem(poem_s3, music=False)
    mc "Ah--"
    "What is this...?"
    "Reading the poem, I get a pit in my stomach."
    show monika 1d at t11 zorder 2
    m "[player]?"
    m "What's wrong?"
    mc "Ah, nothing..."
    "This poem feels completely different from everything else Sayori's written."
    "But more than that..."
    mc "I-I changed my mind!"
    mc "I'm going to go get Sayori, so..."
    m "Ah--"
    m 1b "Well, alright!"
    m "Try not to take too long, okay?"
    scene bg corridor with wipeleft
    "I quickly leave the classroom."
    m "Don't strain yourself~"
    "Monika calls that out after me."
    "I quicken my pace."

    scene bg residential_day with wipeleft_scene
    "What was I thinking?"
    "I should have tried a little bit harder for Sayori."
    "It's not a big deal to at least wait for her, or help her wake up."
    "Even the simple gesture of walking her to school makes her really happy."
    "Besides..."
    "I told her yesterday that things will be the same as they always have been."
    "That's all she needs, and what I want to give her."

    scene bg house with wipeleft
    "I reach Sayori's house and knock on the door."
    "I don't expect an answer, since she's not picking up her phone, either."
    "Like yesterday, I open the door and let myself in."
    scene black with wipeleft
    mc "Sayori?"
    "She really is a heavy sleeper..."
    "I swallow."
    "I can't believe I ended up doing this after all."
    "Waking her up in her own house..."
    if sayori_confess:
        "That really is something that a boyfriend would do, isn't it?"
    else:
        "Isn't that more like something a boyfriend would do?"
    "In any case..."
    "It just feels right."

    "Outside Sayori's room, I knock on her door."
    mc "Sayori?"
    mc "Wake up, dummy..."
    "There's no response."
    "I really didn't want to have to enter her room like this..."
    "Isn't it kind of a breach of privacy?"
    "But she really leaves me no choice."
    "I gently open the door."
    mc "{cps=30}.......Sayo--{/cps}{nw}"
    $ persistent.playthrough = 1    #No turning back now baby
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ delete_character("sayori")
    $ in_sayori_kill = True
    $ persistent.dokisaved = "nonesaved"
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    pause 3.75
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    pause 2.0
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    pause 1.5
    show white zorder 2
    show splash_glitch zorder 2
    pause 1.5
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    pause 4.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    pause 0.75
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: sys.modules['renpy.error'].report_exception("Oh jeez...I didn't break anything, did I? Hold on a sec, I can probably fix this...I think...\nActually, you know what? This would probably be a lot easier if I just deleted her. She's the one who's making this so difficult. Ahaha! Well, here's goes nothing.", False)
        except: pass
    pause 6.0


    "..."
    hide fake_exception
    hide fake_exception2
    hide exception_bg
    "What the hell...?"
    "{i}What the hell??{/i}"
    "Is this a nightmare?"
    "It...has to be."
    "This isn't real."
    "There's no way this can be real."
    "Sayori wouldn't do this."
    "Everything was normal up until a few days ago."
    "That's why I can't believe what my eyes are showing me...!"
    scene black with dissolve_cg
    "I suppress the urge to vomit."
    "Just yesterday..."
    "I told Sayori I would be there for her."
    "I told her I know what's best, and that everything will be okay."
    "Then why...?"
    "Why would she do this...?"
    "How could I be so helpless?"
    "What did I do wrong?"
    if sayori_confess:
        "Confessing to her..."
        "I shouldn't have confessed to her."
        "That's not what Sayori needed at all."
        "She even told me how painful it is for others to care about her."
        "Then why did I confess to her, and make her feel even worse?"
    else:
        "Turning down her confession..."
        "That has to have been what pushed her over the edge."
        "Her agonized scream still echoes in my ears."
        "Why did I do that to her when she needed me the most?"
    "Why was I so selfish?"
    "This is my fault--!"
    "My swarming thoughts keep telling me everything I could have done to prevent this."
    "If I just spent more time with her."
    "Walked her to school."
    if sayori_confess:
        "And remained friends with her, like it always has been..."
    else:
        "And gave her what I know she wanted out of our relationship..."
    "...Then I could have prevented this."
    "I know I could have prevented this!"
    "Screw the Literature Club."
    "Screw the festival."
    "I just...lost my best friend."
    "Someone I grew up with."
    "She's gone forever now."
    "Nothing I do can bring her back."
    "This isn't some game where I can reset and try something different."
    "I had only one chance, and I wasn't careful enough."
    "And now I'll carry this guilt with me until I die."
    "Nothing in my life is worth more than hers..."
    "But I still couldn't do what she needed from me."
    "And now..."
    "I can never take it back."
    "Never."
    "Never."
    "Never."
    "Never."
    "Never..."

    return