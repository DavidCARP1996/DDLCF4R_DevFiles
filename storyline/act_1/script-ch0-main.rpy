label ch0_main:

    if ch0_breakfast == True:

        scene bg house
        with dissolve_scene_full
        play music t2

        s "Oh, seems like I came just in time."
        s "Hellooo [player]~!!!"
        mc "...!"
        "After I go out, a cute girl appears in front of my house waving her arms in the air."
        "That girl is Sayori, my neighbor, my best and only friend since we were children."
        "You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?"
        "We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."
        "But this time, seems like she was waiting for me."
        "I go out to the street and salute her."
        $ s_name = "Sayori"
        mc "Hey, Sayori! What's up?"
        show sayori 1a at t11 zorder 2
        s 1a "So, who's the sleepy one now... Huh?"
        "I yawn."
        mc "Uh-huh."
        mc "Here's a first time for anything, remember that."
        s 4p "That's not true, you always waited for me. Until you get bored and continues leaving me alone in the way to school."
        mc "..."
        "She's right... But I'm a guy with low patience, if she doesn't comes out in less than 30 minutes, I quit."
        "Who could be so late anyway?"
        s 3a "Well... Let's go?"
        mc "Yeah, sure..."

    elif ch0_breakfast == False:

        scene bg residential_day
        with dissolve_scene_full
        play music t2

        s "Heeeeeeeyyy!!"
        "I see an loud girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
        "That girl is Sayori, my neighbor, my best and only friend since we were children."
        "You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?"
        "We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."
        "Some people could run away from her if she's going to chase after them like this."
        "However, I let Sayori catch up to me."
        $ s_name = "Sayori"
        show sayori 4p at t11 zorder 2
        s 4p "Haaahhh...haaahhh..."
        s "I overslept again!"
        s "But I caught you again!"
        mc "Yes, I can see that."
        mc "But remember, some people can't have same the patience I have for you."
        show sayori at s11
        s 5c "Eeehhhhh, you say that like you were thinking about ignoring me!"
        s "That's mean, [player]!"
        mc "Well, it's not good if people stare at you for acting like that and think you're weird."
        show sayori at t11 zorder 2
        s 1a "Fine, fine."
        s "But you did wait for me, after all."
        s "I guess you don't have it in you to be mean even if you want to~"
        mc "Whatever you say, Sayori..."
        s 1q "Ehehe~"

    pause 1.0
    
    if bag_inventory.has_item("cookie"):
        mc "Oh, Sayori."
        s 1a "Eh?"
        mc "I have a gift for you."
        show sayori 4m at t11 zorder 2
        $ bag_inventory.remove_item("cookie")
        "I give her the cookie I take from the kitchen."
        s 4m "Ahhh..."
        #show sayori at t11 zorder 2
        s 4r "T-Thank you very much [player]!"
        s "I know you love me so much~!"
        "I blush."
        "But I'm so happy to see her eating the cookie I gifted to her..."
        pass

    else:
        "That cookie... it was for her..."
        "Why the fuck I ate it?!"
        show sayori 1b
        "I'm start to feel very bad now..."
        s "[player]? Something is wrong?"
        mc "Eh? Oh... it's nothing, I'm just rambling because I didn't sleep well, that's all."
        s 1l "Thank goodness! The next time try to sleep a bit earlier, okay?"
        mc "Sure..."
        "If she knows I ate a cookie I saved for her, she will be very, very upset..."
        pass

    scene bg residential_day
    with dissolve_scene_full
    #show sayori at thide zorder 1
    #hide sayori
    "We cross the street together and make our way to school."
    "As we draw near, the streets become increasingly speckled with other students making their daily commute."
    show sayori 3a at t11 zorder 2
    s "By the way, [player]..."
    s "Have you decided on a club to join yet?"
    mc "A club?"
    "That's true, I was in the soccer club years ago. But I quit after an accident which left me a serious injury."
    "I haven't joined on any other club since then. I hate to see the others look at me like a defeated dog considering I was a promise in the soccer club."
    menu:
        "However..."
        "Agree":
            mc "Well..."
            mc "I was thinking about joining a club."
            mc "However, I'm not so decided yet."
            show sayori at s11
            s 4h "Eh?"
            s "You told me you would join a club this year!"
            s "And without excuses!"
            pass
        "Reject":
            mc "I told you already, I'm really not interested in joining any clubs."
            mc "I haven't been looking, either."
            show sayori at s11
            s 4h "Eh? That's not true!"
            s "You told me you would join a club this year!"
            pass
    mc "Did I...?"
    "I'm sure it's possible that I did, in one of our many conversations where I dismissively go along with whatever she's going on about."
    "Without mention the fact I have some memory problems? Probably sounds like a excuse, but it's the main reason why my notes are too low haha."
    "Anyway, Sayori likes to worry a little too much about me, when I'm perfectly content just getting by on the average while spending my free time on games and anime."
    s 4j "Uh-huh!"
    s "I was talking about how I'm worried that you won't learn how to socialize or have any skills before college."
    s "Your happiness is really important to me, you know!"
    s "And I know you're happy now, but I'd die at the thought of you becoming a HERMIT in a few years because you're not used to the real world!"
    s 4g "You trust me, right?"
    s "Don't make me keep worrying about you..."
    mc "Alright, alright..."
    mc "I'll look at a few clubs if it makes you happy."
    mc "No promises, though."
    s 1h "Will you at least promise me you'll try a little?"
    mc "Yeah, I guess I'll promise you that."
    show sayori at t11 zorder 2
    s 4r "Yaay~!"
    "Why do I let myself get lectured by such a carefree girl?"
    "More than that, I'm surprised I even let myself relent to her."
    "I guess seeing her worry so much about me makes me want to ease her mind at least a little bit - even if she does exaggerate everything inside of her head."

    scene bg class_day
    with wipeleft_scene

    "The school day is as ordinary as ever, and it's over before I know it."
    "After I pack up my things, I stare blankly at the wall, looking for an ounce of motivation."
    mc "Clubs..."
    "Sayori wants me to check out some clubs."
    "I can't come back to the soccer club, I can't even choose any sports clubs because of my fucking injury." 
    "I guess I have no choice but to start with the anime club..."
    "At least during my innactivity period, I was entertaining myself with anime. So maybe I can be included with the otakus groups."

    s "Hellooo?"
    show sayori 1b at t11 zorder 2
    mc "Sayori...?"
    "Sayori must have come into the classroom while I was spacing out."
    "I look around and realize that I'm the only one left in the classroom."
    s 1a "I thought I'd catch you coming out of the classroom, but I saw you just sitting here and spacing out, so I came in."
    s "Honestly, you're even worse than me sometimes... I'm impressed!"
    mc "You don't need to wait up for me if it's going to make you late to your own club."
    s 1y "Well, I thought you might need some encouragement, so I thought, you know..."
    mc "Know what?"
    s 1a "Well, that you could come to my club!"
    menu:
        "Wha-what?!"

        "Accept":
            mc "Sayori..."
            s 3a "Yeah??"
            mc "I..."
            "Oh fuck, don't be shy you stupid shit, say YES now!!!"
            mc "Ok, I'm gonna come to your club."
            s 4r "Yes~!"
            "Sayori is vice president of the Literature Club."
            "Not that I was ever aware that she had any interest in literature."
            "In fact, I'm 99\% sure she only did it because she thought it would be fun to help start a new club."
            "Since she was the first one to show interest after the one who proposed the club, she inherited the title \"Vice President\"."
            "That said, I'm gonna try to be a little interested in literature... At least to give her a good impresion."
            mc "With one condition:"
            s 1b "What?"
            mc "Don't be so excited about this. I'm just gonna give a try to your club..." 
            mc "At least I know having you at my side I can feel more comfortable than socialize with unknown and weirdos otakus."
            s 4r "Ahahahaha!"
            s 1 "Don't worry. I'm gonna make the best to make you feel comfortable~!"
            s "That's my duty as the vice president after all..."
            s 1b "..."
            s "But... You sounded like you was thinking about joining the anime club, isn't?"
            "How did she noticed that? Oh, yeah, I mentioned the \"otakus\" word..."
            s 4r "Even you don't believe it, we have an \"otaku\" girl in our club."
            s "She also can bake cupcakes for us, and let's us eat them."
            mc "Oh really?"
            mc "What's more?"
            s "Well..."
            s 4r "We also have a beautiful girl who seems very passionate about the literature thing~!"
            mc "Interesting..."
            s "And also, you must know the president... She's{nw}"
            show sayori 1b at h11
            mc "Okay okay!"
            mc "I'm gonna meet all of them when I come to the club, okay?"
            if ch0_breakfast == True:
                pass
            if ch0_breakfast == False:
                mc "Also, I want to taste these cupcakes you mentioned. I have not had breakfast, I'm hungry."   
            pass
        "Reject purpose":
            mc "Sayori..."
            s 3a "Yeah??"
            mc "...There is no way I'm going to your club."
            show sayori at s11
            s 5d "Eeeehhhhh?! Meanie!"
            "Sayori is vice president of the Literature Club."
            "Not that I was ever aware that she had any interest in literature."
            "In fact, I'm 99\% sure she only did it because she thought it would be fun to help start a new club."
            "Since she was the first one to show interest after the one who proposed the club, she inherited the title \"Vice President\"."
            "That said, At least I'm gonna try to give her a good impresion. However, I'm not interested in literature. Shame for her..."
            mc "Yeah. I'm going to the anime club."
            show sayori at t11 zorder 2
            s 1g "C'mon, please?"
            mc "Why do you care so much, anyway?"
            s 5b "Well..."
            s "I kind of told the club yesterday I would bring in a new member..."
            s "And Natsuki made cupcakes and everything..."
            s "Ehehe..."
            mc "Don't make promises you can't keep!"
            "I can't tell if Sayori is really that much of an airhead, or if she's so cunning as to have planned all of this out."
            "I let out a long sigh."
            if ch0_breakfast == True:
                mc "Fine... I'll stop by. But because I like to make you happy, even if I'm not with it. Okay?"
                pass
            if ch0_breakfast == False:
                mc "Fine... I'll stop by for a cupcake. Because I'm hungry, okay?"
                pass
    show sayori at h11
    s 4r "Yes! Let's go~!"

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    if ch0_breakfast == True:
        "And thus, today marks the day I sold my soul to Sayori and her irresistible smile."
        pass
    if ch0_breakfast == False:
        "And thus, today marks the day I sold my soul for a cupcake."
        pass
    $ renpy.notify("Notice: inventory will be temporarily disabled.")
    $ HKBShowButtons()
    $ HKBHideButtons()
    "I follow Sayori across the school and upstairs - a section of the school I rarely visit, being generally used for third-year classes and activities."
    "Sayori, full of energy, swings open the classroom door."

    scene bg club_day
    with wipeleft
    play music t3
    show sayori 4 at l41
    s "Everyone! The new member is here~!"
    mc "I told you, don't call me a 'new member--'"
    show sayori at lhide
    hide sayori
    "Eh? I glance around the room."
    show yuri 1a at t11 zorder 2
    y "Welcome to the Literature Club. It's a pleasure meeting you."
    y "Sayori always says nice things about you."
    "Oh, boy... She's so..." 
    "SEXY!!!"
    "Wait! What could think Sayori about if I'm just gonna act like a horny?"
    "Stay calm, let's wait the best moment to meet her..."
    show yuri at t22 zorder 2
    show natsuki 4c at t21 zorder 2
    n "Seriously? You brought a boy?"
    n "Way to kill the atmosphere."
    "Great, the smurf ruined my sexual climax."
    "Wait again! Just dissolve your disgust about her attitude and everything will be okay..."
    $ m_name = "Girl 3"
    show yuri at t33 zorder 2
    show natsuki at t32 zorder 2
    show monika 1k at t31 zorder 2
    m "Ah, [player]! What a nice surprise!"
    m "Welcome to the club!"
    show monika 1a
    mc "Huh?"
    "She could be...?"
    "..."
    "No! Just stop rambling around!"
    pause 0.5

    "All words escape me in this situation."
    "This club..."
    "{i}...is full of incredibly cute girls!!{/i}"

    show monika at thide zorder 1
    show yuri at thide zorder 1
    show natsuki at f32 zorder 3

    hide monika
    hide yuri

    n 2c "What are you looking at?"
    n "If you want to say something, say it."
    mc "S-Sorry..."
    "Fuck you!"
    "Hehe..."
    show natsuki at t32 zorder 2
    show yuri 2l at f33 zorder 3
    y "Natsuki..."
    $ n_name = 'Natsuki'
    show yuri at t33 zorder 2
    show natsuki at f32 zorder 3
    n 5s "Hmph."
    show natsuki at t32 zorder 2

    "The girl with the sour attitude, whose name is apparently Natsuki, is one I don't recognize."
    "Her small figure makes me think she's probably a first-year."
    "She is also the one who made cupcakes, according to Sayori."
    "So MAYBE I must be nice to her, even if I can't tolerate her attitude."

    show sayori 2q at f31 zorder 3
    s "You can just ignore her when she gets moody~"
    "Sayori says that quietly into my ear, then turns back toward the other girls."
    s 1x "Anyway! This is Natsuki, always full of energy."
    s "And this is Yuri, the smartest in the club!"
    $ y_name = 'Yuri'
    show sayori at t31 zorder 2
    show yuri at f33 zorder 3
    y 4b "D-Don't say things like that..."
    "Yuri, who appears comparably more mature and timid, seems to have a hard time keeping up with people like Sayori and Natsuki."
    "By the way, her shy attitude is similar to mine. So MAYBE we can become friends even faster than I though."
    show yuri at t33 zorder 2
    mc "Ah... Well, it's nice to meet both of you."
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    hide yuri
    hide natsuki
    show sayori at f31 zorder 3
    s 1a "And it sounds like you already know Monika, is that right?"
    $ m_name = 'Monika'
    show sayori at t31 zorder 2
    show monika 2a at f32 zorder 3
    m "That's right."
    m "It's great to see you again, [player]."
    show monika 5a at hop
    "Monika smiles sweetly."
    "We do know each other - well, we rarely talked, but we were in the same class last year."
    "Monika was probably the most popular girl in class - smart, beautiful, athletic."
    "Basically, completely out of my league."
    "It's obvious that we never get some friendly chat while we were at the same class, we only talked when I asked her what are the topics we need to study for the Finals of biology."
    "After that, we only know each other like 'just a classmate'."
    "So, having her smile at me so genuinely feels a little, weird."
    mc "Y-You too, Monika."
    show monika at thide zorder 1
    hide monika
    show sayori at f31 zorder 3
    s 4x "Come sit down, [player]! We made room for you at the table, so you can sit next to me or Monika."
    s "I'll get the cupcakes~"
    show sayori at t31 zorder 2
    show natsuki 1e at f32 zorder 3
    n "Hey! I made them, I'll get them!"
    show natsuki at t32 zorder 2
    show sayori at f31 zorder 3
    s 5a "Sorry, I got a little too excited~"
    show sayori at t31 zorder 2
    show yuri 1a at f33 zorder 3
    y "Then, how about I make some tea as well?"
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    if ch0_breakfast == True:
        "Hot tea and cupcakes? Why the fuck did I take breakfast? Well, at least I'm a bit hungry yet."
        pass
    if ch0_breakfast == False:
        "Hot tea and cupcakes? What a good service!"
        pass
    "The girls have a few desks arranged to form a table."
    "As Sayori mentioned, it's been widened so that there is one space next to Monika and one space next to Sayori."
    "Natsuki and Yuri walk over to the corner of the room, where Natsuki grabs a wrapped tray and Yuri opens the closet."
    "Still feeling awkward, I take a seat next to Sayori."
    "Natsuki proudly marches back to the table, tray in hand."
    show natsuki 2z at t32 zorder 2
    n "Okaaay, are you ready?"
    n "...Ta-daa!"
    show sayori 4m at t31 zorder 2
    show monika 2d at t33 zorder 2
    s "Uwooooah!"
    "Natsuki lifts the foil off the tray to reveal a dozen white, fluffy cupcakes decorated to look like little cats."
    "The whiskers are drawn with icing, and little pieces of chocolate were used to make ears."
    show sayori at f31 zorder 3
    s 4r "So cuuuute~!"
    show sayori at t31 zorder 2
    show monika at f33 zorder 3
    m 2b "I had no idea you were so good at baking, Natsuki!"
    show monika at t33 zorder 2
    show natsuki at f32 zorder 3
    n 2d "Ehehe. Well, you know."
    n "Just hurry and take one!"
    "Sayori grabs one first, then Monika. I follow."
    show natsuki at t32 zorder 2
    show sayori at f31 zorder 3
    s 4q "It's delicious!"
    "Sayori talks with her mouth full and has already managed to get icing on her face."
    "I turn the cupcake around in my fingers, looking for the best angle to take a bite."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    hide sayori
    hide monika
    show natsuki 1c at t32 zorder 2
    "Natsuki is quiet."
    "I can't help but notice her sneaking glances in my direction."
    "Is she waiting for me to take a bite?"
    "I finally bite down."
    "The icing is sweet and full of flavor - I wonder if she made it herself."
    mc "This is really good."
    mc "Thank you, Natsuki."
    n 5h "W-Why are you thanking me? It's not like I...!"
    show natsuki at s32
    n 5s "...Made them for you or anything."
    "{i}(Haven't I heard this somewhere before...?){/i}"
    mc "Eh? I thought you technically did. Sayori said--"
    show natsuki at t32 zorder 2
    n 12c "Well, maybe!"
    n "But not for, y-you know, {i}you!{/i} Dummy..."
    mc "Alright, alright..."
    show natsuki at thide zorder 1
    hide natsuki
    "I give up on Natsuki's weird logic and dismiss the conversation."
    "Geez, I must take intensive courses of patience if I want to deal with her..."
    "Yuri returns to the table, carrying a tea set."
    "She carefully places a teacup in front of each of us before setting down the teapot next to the cupcake tray."
    show yuri 1a at t21 zorder 2
    mc "You keep a whole tea set in this classroom?"
    y "Don't worry, the teachers gave us permission."
    y "After all, doesn't a hot cup of tea help you enjoy a good book?"
    mc "Ah... I-I guess..."
    show monika 4a at t22 zorder 2
    m "Ehehe, don't let yourself get intimidated, Yuri's just trying to impress you."
    show yuri at h21
    y 3n "Eh?! T-That's not..."
    "Insulted, Yuri looks away."
    "That expression... It's the real meaning of \"cute\". I love it!"
    y 4b "I meant that, you know..."
    mc "I believe you."
    mc "Well, tea and reading might not be a pastime for me, but I at least enjoy tea."
    y 2u "I'm glad..."
    "Yuri faintly smiles to herself in relief."
    "Monika raises an eyebrow, then smiles at me."
    show yuri at thide zorder 1
    hide yuri
    show monika at t11 zorder 2
    m 1 "So, you were at the soccer club 2 years ago, right?"
    m "It's a shame that you should left it by that injury. It was a nice career for the future..."
    m "But I saw your skills on computing, I though you could go by the computing club instead."
    m "Anyway... What made you consider the Literature Club?"
    mc "Um..."
    "I was afraid of this question."
    "Something tells me I shouldn't tell Monika that I was practically dragged here by Sayori."
    mc "Well, I haven't joined any clubs yet, and Sayori seemed really happy here, so..."
    m 1j "That's okay! Don't be embarrassed!"
    m 1b "We'll make sure you feel right at home, okay?"
    m "As president of the Literature Club, it's my duty to make the club fun and exciting for everyone!"
    show monika 1a
    mc "Monika, I'm surprised."
    mc "How come you decided to start your own club?"
    mc "You could probably be a board member for any of the major clubs."
    mc "Weren't you a leader of the debate club last year?"
    m 5 "Ahaha, well, you know..."
    m "To be honest, I can't stand all of the politics around the major clubs."
    m "It feels like nothing but arguing about the budget and publicity and how to prepare for events..."
    m "I'd much rather take something I personally enjoy and make something special out of it."
    m 1b "And if it encourages others to get into literature, then I'm fulfilling that dream!"
    show monika 1a
    show sayori 3q at t31 zorder 2
    s "Monika really is a great leader!"
    show yuri 1 at t33 zorder 2
    "Yuri also nods in agreement."
    show sayori at thide zorder 1
    show yuri at thide zorder 1
    hide sayori
    hide yuri
    mc "Then I'm surprised there aren't more people in the club yet."
    mc "It must be hard to start a new club."
    m 3b "You could put it that way."
    m "Not many people are very interested in putting out all the effort to start something brand new..."
    m "Especially when it's something that doesn't grab your attention, like literature."
    m "You have to work hard to convince people that you're both fun and worthwhile."
    m "But it makes school events, like the festival, that much more important."
    m 2k "I'm confident that we can all really grow this club before we graduate!"
    m "Right, everyone?"
    show monika 2a at t22 zorder 2
    show sayori 4r at t21 zorder 2
    s "Yeah!"
    show monika at t33 zorder 2
    show sayori at t32 zorder 2
    show yuri 1a at t31 zorder 2
    y "We'll do our best."
    show monika at t44 zorder 2
    show sayori at t43 zorder 2
    show yuri at t42 zorder 2
    show natsuki 4d at t41 zorder 2
    n "You know it!"
    "Everyone enthusiastically agrees."
    "Such different girls, all interested in the same goal..."
    "Monika must have worked really hard just to find these three."
    "Maybe that's why they were all so delighted by the idea of a new member joining."
    "Though I still don't really know if I can keep up with their level of enthusiasm about literature..."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    show natsuki at thide zorder 1
    show yuri at t32 zorder 2
    hide sayori
    hide monika
    hide natsuki
    y "So, [player], what kinds of things do you like to read?"
    mc "Well... Ah..."
    "Considering how little I've read these past few years, I don't really have a good way of answering that."
    "What kind of literature genre could impress her? I only read one thing but I don't think she could..."
    "You know what? Fuck it, let's better be honest!"
    mc "...Manga..."
    "I mutter quietly to myself, half-joking."
    show natsuki 1c at t41 zorder 2
    "Natsuki's head suddenly perks up."
    "It looks like she wants to say something, but she keeps quiet."
    show natsuki at thide zorder 1
    hide natsuki
    y 3u "N-Not much of a reader, I guess..."
    mc "...Well, that can change..."
    "What am I saying?"
    "I spoke without thinking after seeing Yuri's sad smile."
    mc "Anyway, what about you, Yuri?"
    y 1l "Well, let's see..."
    "Yuri traces the rim of her teacup with her finger."
    y 1a "My favorites are usually novels that build deep and complex fantasy worlds."
    y "The level of creativity and craftsmanship behind them is amazing to me."
    y 1f "And telling a good story in such a foreign world is equally impressive."
    "Yuri goes on, clearly passionate about her reading."
    "She seemed so reserved and timid since the moment I walked in, but it's obvious by the way her eyes light up that she finds her comfort in the world of books, not people."
    "She looks like me, except that I prefer video games, soccer, anime or any internet things."
    y 2m "But you know, I like a lot of things."
    y "Stories with deep psychological elements usually immerse me as well."
    y 2a "Isn't it amazing how a writer can so deliberately take advantage of your own lack of imagination to completely throw you for a loop?"
    y "Anyway, I've been reading a lot of horror lately..."
    mc "Ah, I read a horror book once..."
    "I desperately grasp something I can relate to at the minimal level."
    "At this rate, Yuri might as well be having a conversation with a rock."
    show monika 1d at f33 zorder 3
    m "Really? I wouldn't have expected that, Yuri."
    m "For someone as gentle as you..."
    show monika at t33 zorder 2
    show yuri at f32 zorder 3
    y 1a "I guess you could say that."
    y "But if a story makes me think, or takes me to another world, then I really can't put it down."
    y "Surreal horror is often very successful at changing the way you look at the world, if only for a brief moment."
    show yuri at t32 zorder 2
    show natsuki 5q at f31 zorder 3
    n "Ugh, I hate horror..."
    show natsuki at t31 zorder 2
    show yuri at f32 zorder 3
    y 1f "Oh? Why's that?"
    show yuri at t32 zorder 2
    show natsuki at f31 zorder 3
    n 5c "Well, I just..."
    "Natsuki's eyes dart over to me for a split second."
    n 5q "Never mind."
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 1a "That's right, you usually like to write about cute things, don't you, Natsuki?"
    show monika at t33 zorder 2
    show natsuki 1o at f31 zorder 3
    n "W-What?"
    n "What gives you that idea?"
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 3b "You left a piece of scrap paper behind last club meeting."
    m "It looked like you were working on a poem called--"
    show monika at t33 zorder 2
    show natsuki 1p at f31 zorder 3
    n "Don't say it out loud!!"
    n "And give that back!"
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 1j "Fine, fine~"
    show monika at thide zorder 1
    show yuri at thide zorder 1
    hide monika
    hide yuri
    show natsuki 1r at t42 zorder 2
    show sayori 4q at l41 behind natsuki
    s "Ehehe, your cupcakes, your poems..."
    s "Everything you do is just as cute as you are~"
    show sayori at t21 behind natsuki
    "Sayori sidles up behind Natsuki and puts her hands on her shoulders."
    show natsuki at h42
    n 1v "{i}I'm not cute!!{/i}"
    show natsuki at t11 zorder 2
    show sayori at thide zorder 1
    hide sayori
    mc "Natsuki, you write your own poems?"
    n 1c "Eh? Well, I guess sometimes."
    n "Why do you care?"
    mc "I think that's impressive."
    mc "Why don't you share them sometime?"
    n 5q "N-No!"
    "Natsuki averts her eyes."
    n "You wouldn't...like them..."
    mc "Ah...not a very confident writer yet?"
    show yuri 2f at t31 zorder 2
    y "I understand how Natsuki feels."
    y "Sharing that level of writing takes more than just confidence."
    y 2k "The truest form of writing is writing to oneself."
    y "You must be willing to open up to your readers, exposing your vulnerabilities and showing even the deepest reaches of your heart."
    show natsuki at thide zorder 1
    hide natsuki
    show monika 2a at t33 zorder 2
    m "Do you have writing experience too, Yuri?"
    m "Maybe if you share some of your work, you can set an example and help Natsuki feel comfortable enough to share hers."
    show yuri at s31
    y 3o "..."
    mc "I guess it's the same for Yuri..."
    show sayori 2g at t32 zorder 2
    s "Aww... I wanted to read everyone's poems..."
    mc "Don't worry Sayori, that time will come someday... I guess."
    s "..."
    mc "..."
    m "..."
    y "..."
    n "..."
    show sayori at thide zorder 1
    show yuri at thide zorder 1
    show monika at thide zorder 1
    hide sayori
    hide yuri
    hide monika
    "We all sit in silence for a moment."
    m "..."
    show monika 5a at f32 zorder 3
    m "Okay!"
    m "I have an idea, everyone~"
    show yuri 3e at t31 zorder 2
    show natsuki 2k at t33 zorder 2
    ny "...?"
    "Natsuki and Yuri look quizzically at Monika."
    m 2b "Let's all go home and write a poem of our own!"
    m "Then, next time we meet, we'll all share them with each other."
    m "That way, everyone is even!"
    show monika 2a at t32 zorder 2
    show natsuki at f33 zorder 3
    n 5q "U-Um..."
    show natsuki at t33 zorder 2
    show yuri 3v at f31 zorder 3
    y "..."
    show natsuki at t44 zorder 2
    show monika at t43 zorder 2
    show yuri at t42 zorder 2
    show sayori 4r at l41
    s "Yeaaah! Let's do it!"
    show monika at f43 zorder 3
    m 1a "Plus, now that we have a new member, I think it will help us all get a little more comfortable with each other, and strengthen the bond of the club."
    m "Isn't that right, [player]?"
    show monika at t43 zorder 2
    "Monika smiles warmly at me once again."
    "It's weird, in last year she usually looked at me with disgust. Why is she trying to be nice with me now? Is she plotting something?"
    mc "Hold on...there's still one problem."
    show monika at f43 zorder 3
    m 1d "Eh? What's that?"
    "Now that we're back to the original topic of me joining the club, I bluntly come forth with what's been on my mind the entire time."
    show monika at t43 zorder 2
    "I stare at Monika with a suspicious expression, however, I'm going to the main topic..."
    menu:
        "Accept":
            "If writing poems is the price I need to pay in order to spend every day with these beautiful girls..."
            mc "N-nevermind."
            mc "The thing is, I was planning to join another club in first place but..."
            show monika 1g
            show sayori 1g
            show natsuki 4g
            show yuri 2e
            "..."
            show sayori 4b at t41 zorder 2
            mc "... I've noticed Sayori really need someone special for her in this Club, maybe that's why she insisted me to join. So I made my choice."
            show monika 1e at t43 zorder 2
            show yuri 3f at t42 zorder 2
            show natsuki 1k at t44 zorder 2
            mc "I'll join the Literature Club."
            pass
        "Reject":
            mc "I never said I would join this club!"
            mc "Sayori may have convinced me to stop by, but I never made any decision."
            mc "I still have other clubs to look at, and...um..."
            show monika 1g
            show sayori 1g
            show natsuki 4g
            show yuri 2e
            "I lose my train of thought."
            "All four girls stare back at me with dejected eyes."
            show monika at s43
            m 1p "B-But..."
            show yuri at s42
            y 2v "I'm sorry, I thought..."
            show natsuki at s44
            n 5s "Hmph."
            show sayori at s41
            s 1k "[player]..."
            mc "Y-You all..."
            "I...I'm defenseless against these girls."
            "How am I supposed to make a clear-headed decision when it's like this?"
            "That is, if writing poems is the price I need to pay in order to spend every day with these beautiful girls..."
            mc "...Right."
            mc "Okay, I've decided, then."
            mc "I'll join the Literature Club."
            show monika 1e at t43 zorder 2
            show yuri 3f at t42 zorder 2
            show natsuki 1k at t44 zorder 2
            show sayori 4b at t41 zorder 2
            "One by one, the girls' eyes light up."
            pass
    show sayori at h41
    s 4r "Yesss! I'm so happyyy~"
    "Sayori wraps her arms around me, jumping up and down."
    mc "H-Hey--"
    show yuri at f42 zorder 3
    y 1m "You really did scare me for a moment..."
    show yuri at t42 zorder 2
    show natsuki at f44 zorder 3
    n 5q "If you really just came for the cupcakes, I would be super pissed."
    show natsuki at t44 zorder 2
    show monika at f43 zorder 3
    m 5 "Then that makes it official!"
    m "Welcome to the Literature Club!"
    show monika at t43 zorder 2
    mc "Ah...thanks, I guess."
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    show sayori at thide zorder 1
    show monika at t11 zorder 2
    hide yuri
    hide natsuki
    hide sayori
    m 3b "Okay, everyone!"
    m "I think with that, we can officially end today's meeting on a good note."
    m "Everyone remember tonight's assignment:"
    m "Write a poem to bring to the next meeting, so we can all share!"
    "Monika looks over at me once more."
    "I can't hide my suspicious expression, I still can't believe why is she beign so nice to me suddently."
    m 1a "[player], I look forward to seeing how you express yourself."
    show monika 5 at hop
    m "Ehehe~"
    mc "Y-Yeah..."
    show monika at thide zorder 1
    hide monika
    "Can I really impress the class star Monika with my mediocre writing skills? Or even the beautiful Yuri? I'm more worried about her thoughts sincerely."
    "I already feel the anxiety welling up inside me."
    "Meanwhile, the girls continue to chit-chat as Yuri and Natsuki clean up their food."
    show sayori 1a at t11 zorder 2
    s "Hey, [player], since we're already here, do you want to walk home together?"
    "That's right - Sayori and I haven't walk home together anymore because she always stayed after school for clubs, and when I was in the soccer club we had different departure time."
    mc "Of course!."
    s 4q "Yaay~"

    scene bg residential_day
    with wipeleft_scene

    "With that, the two of us depart the clubroom and make our way home."
    "The whole way, my mind wanders back and forth between the four girls:"
    show sayori 1 at t41 zorder 2
    "Sayori,"
    show natsuki 4 at t42 zorder 2
    "Natsuki,"
    show yuri 1 at t43 zorder 2
    "Yuri,"
    show monika 1 at t44 zorder 2
    "and Monika."
    "Will I really be happy spending every day after school in a literature club?"
    "Perhaps I'll have the chance to grow closer to one of these girls..."
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "Alright!"
    "I'll just need to make the most of my circumstances, and I'm sure good fortune will find me."
    "And I guess that starts with writing a poem tonight..."

    return