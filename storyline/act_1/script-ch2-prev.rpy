label ch2_prev:
    stop music fadeout 2.0
    with dissolve_scene_full
    
    scene bg bedroom
    with dissolve_scene_full
    mc "Aaaand it's done!"
    mc "Well, I guess I will play some videogames."
    "..."
    "If only I had bought that game..."
    mc "It's 22 PM."
    mc "I think I'd better go to sleep. I don't have such interesting games in my library to play."
    pause 0.5
    play sound click
    scene bg bedroom_night
    pause 0.5
    scene black
    with dissolve_scene_full
    if persistent.monika_help == True:
        pause 2.0
        show mask_2
        show mask_3
        with dissolve_scene_full
        play music m1
        "Once again, I'm having this dream..."
        mc "Hey, mysterious lady! I know you're behind of this. Show yourself because I want to know what's your real purpose..."
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        show monika sdwf1 at t11 zorder 2
        "???" "Did you call me?"
        mc "Yes."
        mc "Don't you think this kind of \"dreams\" are so unneccesary?"
        mc "I can't even have an decent dream because everytime I sleep I'm spawned here..."
        mc "I want at least ONCE have a dream with Yuri{nw}"
        "???" "Enough!"
        "???" "I understand what do you mean."
        "???" "But I can't allow you this pleasure. Not until I fulfill my objective."
        mc "Oh come on!"
        mc "I'm getting tired of all this, and... well, if at least you tell me exactly what's your objective without beign so mysterious..."
        mc "I could possibly help to you fulfill your objective faster."
        "???" "You shouldn't have to know that."
        mc "Shit..."
        if ch1_battle_2_won == True:
            "???" "At least thank me for saving you of beign arrested."
            mc "I knew it!"
            mc "Thanks anyway, and sorry for not thanking you before, I was disconcerted for the suddently situation."
            "???" "No problem. I will let it pass for now."
        else:
            pass
        "???" "..."
        "???" "If you want an advice: Get away from some sort of girls."
        mc "Who?"
        "???" "I won't say it."
        mc "I know a lot of girls, which ones are I supposed to get away from?"
        "???" "I won't say it, damn it!"
        "... ... ..."
        $ persistent.monika_help = False
        "???" "Alright! If you want me to leave you alone, then so be it. I won't bother you anymore."
        "???" "However, from now on I won't protect you of anything if you're in danger."
        menu:
            "Fine...":
                pass
        "???" "Good bye!"
        show screen tear(20, 0.1, 0.1, 0, 40)
        hide monika
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        pause 1.0
        mc "I don't need your protection, you hear...?"
        "..."
        mc "Fuck!"
        pause 3.0
        stop music fadeout 2.0
        scene bg bedroom_night
        with dissolve_scene_full
        "..."
        mc "Hmm... 2 AM?"
        mc "Damn it!"
        mc "..."
        mc "I'm gonna sleep."
        scene black
        with dissolve_scene_full
        pass
    else:
        pass
    scene bedroom
    with dissolve_scene_full
    "6:30 AM"
    mc "Yes!"
    mc "Finally I'm having normal dreams!"
    "*Grrrr~*"
    mc "Eh? I'm hungry..."
    "At this hour, the cafeteria must be open."
    menu:
        "Could I go?"

        "Yes":
            "Alright!"
            $ HKBShowButtons()
            $ ch2_prev_activities_m = 0
            $ stamina = 10
            $ hr_hour = 6
            $ park_closed = False
            $ cafe_closed = False
            $ library_closed = False
            $ gamestore_closed = False
            $ ch2_tell_sayori_meet_later = False
            $ ch2_battle_3_event = False
            $ accept_kickboxingclub_offer = "No"
            jump ch2_prev_loop
        "No":
            mc "Oh, come on!"
            jump ch2_prev_go_sleep

label ch2_prev_loop:
    while (stamina > 0) and (hr_hour <= 7):
        show screen freeroam_hud
        with Dissolve(.5)
        play music t5
        if ch2_prev_activities_m == 0:
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
                if ch1_battle_2_won == True:
                    mc "I don't want to come back to the park for now..."
                else:
                    mc "I have a bad feeling about going there."
                    mc "I'd better go somewhere else."
                $ park_closed = True
                pass
            "Go to the cafe" if not cafe_closed:
                $ ch2_prev_activities_m += 1
                jump ch2_prev_go_to_cafe
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
                jump ch2_prev_go_home
                pass
            "Go to school":
                jump ch2_prev_go_play
                pass
        pass
    jump ch2_prev_go_home

label ch2_prev_go_to_cafe:
    scene bg cafe_dark
    with wipeleft_scene
    mc "..."
    mc "Eh?"
    "He is...?"
    "Guy" "Hey [player]! What's up man?"
    show ryoma at t11 zorder 1
    mc "Ryoma?!"
    "That guy is Ryoma. Fortunately my best friend between the most important boys in the entire school."
    "We becamed friends since we teamed up in the soccer club, I was the defender and he was the scorer, I've used to give him assistences too."
    "When I'm having problems with anybody from his circle, he always shows up to stop us and save my ass."
    "He always does his best to make the convivence peacefully as possible. He doesn't a troublemaker like the other popular boys because he knows bullying people to feel important is a waste of time."
    if backyard_check == True:
        "Oh! Did I mention he and Camilla are the ones who always overprotecting me?"
        "Their are my best dynamic duo..."
    mcf1 "What are you doing here? I thought you'be still sleeping..."
    mcf1 "And how is Sayori?"
    mc "Nah, I slept sooner and woke up sooner too..."
    mc "And Sayori is fine thank goodness."
    mcf1 "It's nice to hear that. She's a pretty girl, you're lucky having her always at your side."
    mc "Hehe, you got a point."
    mcf1 "And what a coincidence, I was about to go to my new club's spot earlier to make preparatives. So I decided to have breakfast here."
    mc "Nice."
    mcf1 "Come on, choose anything you want, I'll pay."
    mc "No, it's not neccesary, I will pay my food."
    mcf1 "Don't worry about it, I have enough money to invite an entire group."
    mc "If you say so..."
    mcf1 "Now that we are here, tell me: How is that Literature Club that Monika founded?"
    mc "Well..."
    scene black
    with dissolve_scene_full
    scene bg cafe
    with dissolve_scene_full
    show ryoma at t11 zorder 1
    mcf1 "There's nothing better than a coffee and a ham & cheese toast..."
    mc "Indeed."
    mc "Thanks Ryoma."
    mcf1 "Don't mention it."
    mcf1 "Oh! I almost forgot..."
    mcf1 "Before you entered to the Literature Club I was about to inviting you to my club, but..."
    mc "Sorry about that."
    mcf1 "Wait, I guess you can be a 'member' there at the same time..."
    mcf1 "But there's a problem:"
    mc "What?"
    mcf1 "How your leg is?"
    mc "This? I guess it's fixed."
    mc "The accident was about 2 years ago, at the first year of rehabilitation I was able to run again, so I can do anything."
    mc "Why are you asking?"
    mcf1 "Well... the fact it's my club is..."
    mcf1 "A Kick boxing Club."
    mc "Oh, I see..."
    mc "Well, I guess my leg is in conditions to beat people. But why should I join in?"
    mcf1 "It's easy... First: We need some promotion, if people see someone has interests in the club activities they could be interested too."
    mcf1 "And for some reason, the Literature Club got more attention when you joined in. But everybody is waiting for the Festival to see what the club 'really' offers."
    mcf1 "Second: If you reach the Top of every \"Mini Tournament\", you will get some cash as reward."
    mcf1 "And Third: We don't have the same schedule like the Literature Club, you can go there after school if you want, we have two schedules."
    mc "Aha!"
    mc "Well, it sounds good."
    menu:
        "Should I join the Kickboxing Club? (I won't quit the Literature Club for this, it's just more activities and EXP farming included)"

        "Yes.":
            mc "I'm in!"
            mc "Also, I need to do some exercises."
            mcf1 "Thank you very much [player]!"
            mc "It's nothing."
            mc "If the school has no problems about participating in two clubs at the same time, you can count on me."
            mcf1 "Alright! It's official then."
            mcf1 "Welcome to the Kick boxing Club!"
            mc "Thanks Ryoma..."
            mcf1 "You're welcome bro."
            $ accept_kickboxingclub_offer = "Yes"
            pass
        "I'm gonna think about it...":
            mc "I need to check my agenda, but don't worry, I will consider your offer..."
            mcf1 "Okay, I will wait for your answer then. The doors will be open for you if you decide to join in."
            mc "Alright, thanks Ryoma."
            mcf1 "Don't mention it."
            $ accept_kickboxingclub_offer = "Maybe"
            pass
        "No.":
            mc "Sorry, but I'm affraid I don't have enough time."
            mcf1 "Too bad..."
            mcf1 "Well, if for some reason you change of mind, just tell me okay?"
            mc "Okay, thanks fot the offer anyway Ryoma."
            mcf1 "Don't mention it."
            $ accept_kickboxingclub_offer = "No"
            pass
    mcf1 "Alright then... See you later?"
    if accept_kickboxingclub_offer == "Yes":
        mc "Yeah Ryoma, I'll see you in the Kickboxing club."
        pass
    else:
        mc "Yeah Ryoma, I'll see you later."
    mc "Oh, wait!"
    mc "Why are you going to your club so sooner?"
    mcf1 "You see, we have our club in an abandoned dojo in addition to the school gym."
    mcf1 "That is you must go to that dojo if you're in the Literature Club in our school hour."
    mcf1 "I'm going sooner because I need to clean some mess up, that's all."
    mc "Oh, I see..."
    if accept_kickboxingclub_offer != "No":
        mcf1 "Come with me if you want, and then I can teach you some tips about our club. And in the way you can go to school sooner."
        mcf1 "Unless you want to know all of this later..."
        menu:
            mc "Well..."

            "Go with Ryoma.":
                mcf1 "Nice! Then let's go..."
                mc "Yeah!"
                jump ch2_prev_go_fightingclub
                pass
            "Pass.":
                mc "Sorry..."
                mcf1 "Don't worry, we can do this afterschool if you want."
                pass
            "I don't know, I need to pick up Sayori in time to go to school.":
                mcf1 "Shit dude, that's true!"
                mcf1 "She's been overslepting more frequently, isn't? You should do something at the respect."
                "Fuck, he's true... But, it's not like I don't want to help her, she's just retracts and says \"I'm okay\" everytime I asking her and deflects the subject..."
                mc "I'm doing my best, but she says everytime that she's fine..."
                mcf1 "I see..."
                mcf1 "Well, take good care of her, and come to my club afterschool if you want."
                mc "Alright!"
                pass
    else:
        pass
    mc "Thanks again..."
    mcf1 "Don't mention it."
    mcf1 "See you later!"
    $ stamina -= 1
    $ cafe_closed = True
    jump ch2_prev_loop
    
    return

label ch2_prev_go_home:
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
    scene bg bedroom dark
    mc "Zzzzzzzzzzz..."
    scene black
    with dissolve_scene_full
    jump ch2_prev_go_school_B

return

label ch2_prev_go_play:
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
    jump ch2_prev_go_school_B

return

label ch2_prev_go_fightingclub:
    hide screen freeroam_hud
    with Dissolve(.5)
    $ HKBShowButtons()
    $ HKBHideButtons()
    $ renpy.notify("Notice: inventory will be temporarily disabled.")
    scene bg fightingclub_dirty
    with wipeleft_scene
    show ryoma at t11 zorder 1
    mcf1 "Here we are!"
    menu:
        "My god, what a mess...":
            pass
        "Thank God I came to help you...":
            pass
        "Don't say anything...":
            pass
    mcf1 "Yeah, sorry for that."
    mcf1 "But in order to open the new schedule, I need a new space apart of the school gym."
    mc "I see..."
    mc "Well, we have time enought before the school gates open up."
    mc "So count on me! Let's make this place an nice training dojo."
    mcf1 "Well said, let's go!"
    scene black
    with dissolve_scene_full
    pause 3.0
    scene bg fightingclub_clean
    with dissolve_scene_full
    show ryoma at t11 zorder 1
    mc "Phew! I guess it's done..."
    mcf1 "Yeah, that was the last thing to do."
    mcf1 "Look at this place bro, it isn't awesome?"
    mc "Yes, indeed!"
    mcf1 "[player], I owe you a big thanks for this!"
    mc "It was nothing Ryoma, you'be been doing for me things heavier than this."
    mc "Trust me, this is just a part of my pay to all of your favors done for me."
    mc "I still owe you more..."
    mcf1 "Don't say such thing, without your help I could cleaned this place after the school hour, I could entered very late..."
    mcf1 "You did for me a giant favor, remember that. You don't owe me nothing!"
    mc "Alright... Thanks Ryoma."
    mcf1 "It's nothing bro."
    show ryoma at thide zorder 1
    hide ryoma
    "..."
    "Ryoma and I lie down to rest watching at the dojo's roof."
    "Suddently I look at the phone's hour."
    mc "HOLY SHIT!!!"
    show ryoma at t11 zorder 1
    mcf1 "What's wrong [player]?!"
    mc "It's 8 AM already!!!"
    mc "We'll be late-!!!"
    mcf1 "Hey, hey! Relax!"
    mcf1 "We take only 4 minutes walking directly to the school, don't worry!"
    mc "Oh, I forgot that... Sorry..."
    "..."
    mcf1 "Hey! I have an idea..."
    mc "?"
    mcf1 "What if we practice some fighting before school?"
    mc "Are you serious?"
    mcf1 "Well, you're a member of the Kick boxing Club now, so you must do it to proof you're done for this place."
    mcf1 "It's like when you write poems for the Literature Club..."
    mc "Well..."
    menu:
        "Okay, but first let me call Sayori to make sure she will go to school sooner.":
            mcf1 "Sure!"
            mc "Thank you..."
            "*calling Sayori*"
            s "Uh?! [player]...?"
            mc "Sayori, I'm warning you I can't go to school with you this time."
            mc "I'm helping a friend of mine with something and we'll come to school in the way, so I can't go to your house in time."
            mc "Sorry about that..."
            s "S-sure, no problem."
            mc "At least promise me we'll meet at the entrance in hour. Or you will be in school right on time."
            s "Yeah [player], don't worry about that."
            s "Thanks for calling me."
            mc "Don't mention it."
            mc "See you later Sayori..."
            s "Hehe~ See you later [player]..."
            "*click*"
            $ ch2_tell_sayori_meet_later = True
            mc "Aaand it's done!"
            call ch2_prev_fightingclub_battle
            $ ch2_battle_3_event = True
            "He watch his phone."
            mcf1 "Oh-oh! We must go to school!"
            "I watch the mine..."
            "8:50 AM"
            mc "Shit, you're right!"
            mcf1 "Let's go dude!"
            mc "Yes!"
            jump ch2_prev_go_school_B
            pass
        "Let's go!":
            call ch2_prev_fightingclub_battle
            $ ch2_battle_3_event = True
            "He watch his phone."
            mcf1 "Oh-oh! We must go to school!"
            "I watch the mine..."
            "8:50 AM"
            mc "Shit, you're right!"
            mcf1 "Let's go dude!"
            mc "Yes!"
            jump ch2_prev_go_school_B
            pass
        "Pass.":
            mcf1 "Alright then, no problem..."
            mc "Well... Shall we go to school?"
            mcf1 "If you want..."
            jump ch2_prev_go_school_B
            pass
        "I remember I need to pick up Sayori, sorry.":
            mcf1 "Really? Then let's do this later, okay?"
            mc "Sure... See you later Ryoma!"
            mc "And thanks for the invitation..."
            mcf1 "Thanks to you for accepting it!"
            jump ch2_prev_go_school_A
            pass

    label ch2_prev_fightingclub_battle:
        mcf1 "Alright [player]! Are you ready?"
        $ mc_current_weapon = None
        $ mc_current_weapon_type = None
        mc "Yes! I am!"
        mcf1 "Let's go then..."
        call ch2_battle_3
        if ch2_battle_3_victory == True:
            mc "Aaaaand K.O.!"
            "I lift Ryoma from the ground."
            show ryoma at t11 zorder 1
            mcf1 "Dude, you're very good!"
            mcf1 "Have you been training in your house or something?"
            mc "Something like that, in fact."
            mcf1 "What?"
            mc "Well, I like to punch the walls, kick everything around me, run even if it's unnecessary, and sometimes I practice some basic karate."
            mc "Even I've using Sayori to practice evasion and resistance to the hits making her hit me."
            mcf1 "Incredible..."
            pass
        elif ch2_battle_3_victory == False:
            mcf1 "Knock Out! I won..."
            "Ryoma lift me from the ground."
            show ryoma at t11 zorder 1
            mc "Ouch!"
            mcf1 "Sorry..."
            mcf1 "Too bad bro, I was expecting something better from you."
            mc "Well, I guess I'm not so ready for this..."
            mcf1 "Don't say that. You can be even better, just come here after school everytime and try to gain some fighting skills (EXP)."
            mcf1 "Me and the boys will try to train you harder in order to make you stronger!"
            menu:
                "Next time I will do my best, you can count on that!":
                    mcf1 "Perfect! That's the [player] I know..."
                    pass
                "Okay...":
                    mcf1 "Not so enthusiastic, isn't?"
                    mc "Well..."
                    "Who am I kidding? I need this kind of training to become stronger..."
                    "Alright! I will train with him!"
                    mc "You're right! And that's why I'm joining your club!"
                    mc "I will train harder as possible to become stronger!"
                    mcf1 "Perfect! That's the [player] I know..."
                    pass
                "And why should I enhance my fighting skills? What's the point?":
                    mcf1 "I already kicked your butt, and we only had a training battle..."
                    mcf1 "What do you think could happen if you were in a different situation?"
                    mc "Eeeeh..."
                    "He's fucking right! I can't do anything if I'm still weak as fuck! They can kill me!"
                    "Alright! I will train with him!"
                    mc "You're right! And that's why I'm joining your club!"
                    mc "I will train harder as possible to become stronger!"
                    mcf1 "Perfect! That's the [player] I know..."
                    pass
            pass
        else:
            "*pant* *pant*"
            show ryoma at t11 zorder 1
            mcf1 "Draw!"
            mcf1 "Incredible, are we so similar in strenght?"
            mc "I guess so..."
            pass
        mcf1 "You have been doing cool, but honestly, I was expecting a little more..."
        mc "Why? You are the athletic boy in the school, and I am an loser who waste his time playing videogames and/or watching anime."
        mcf1 "Oh come on! Don't say such thing!"
        mcf1 "Don't you remember when we were in the Soccer Club? You had a lot of potential in strenght and speed."
        mcf1 "Even in the Computing classes you had a lot of potential to be programmer, I remember how Monika was asking you for the right notes when she had absolutely zero interest on you."
        mcf1 "That's why I respect you a lot, you are a guy with potential in anything what you do."
        mcf1 "And I trust that you will become stronger if you train here everyday!"
        mcf1 "Come on! Just give me the opportunity..."
        mc "I haven't said I won't do it, it's just... I guess you've been overrating that \"potential\"."
        play music tmod2
        mc "Since that accident I'm not the same. Every problems I have I tried to fix them with violence instead of talking like normal people does."
        mc "The only reason I haven't committed suicide yet is because of Sayori. She's like a sunshine in my life of darkness."
        mc "And now I met more fantastic persons in the Literature Club..."
        mc "Yuri for example, she's my new crush now."
        mc "Natsuki seems to be an interesting person despite her bipolar personality."
        mc "And Monika has become friendlier to me since I joined. Putting aside some hypocrisy, I have seen a good side of her."
        mc "I have 4 reasons why to live, I don't know what can I do without them."
        mc "Oh, and I will never forget about you and Camilla... I guess there are 6 reasons."
        mcf1 "... ... ..."
        mcf1 "I... I don't know what to say."
        mcf1 "I didn't know you have such thoughts..."
        mcf1 "N-Now I understand why you are so withdrawn since that damned accident."
        mcf1 "Sorry bro, I..."
        mc "Don't worry Ryoma, you have nothing to sorry for."
        mc "On the contrary, I should apology to throw all my shit on you like if you were an psychologist or something like that..."
        mcf1 "No bro, it's okay if you do that."
        mcf1 "That 'shit' what you mean it's all the negative thoughts you've been retaining in your mind all this time."
        mcf1 "Don't you feel like some kind of \"freedom\"?"
        stop music fadeout 2.0
        mc "... ... ..."
        mc "Maybe..."
        play music t8
        mc "Maybe you're right!"
        mc "So was that then, all my thoughts was driving me into an negative status which asks for such thing like suicide!"
        mc "Ryoma... I owe you a big one!"
        "We do Hi-Five."
        mcf1 "No problem [player], that's what friends are for."
        pass
    return

label ch2_prev_go_school_A:
    scene bg house
    with wipeleft_scene
    pause 1.0
    mc "Sayoriii~!"
    "She doesn't answer..."
    mc "Shit!"
    "I call to her phone."
    s "Hmm?"
    mc "Sayori?"
    s "Ye...yeah..."
    "Oh crap, she's still sleepy."
    mc "Sayori, we'll be late for school, it's 8:30 now! What's the matter?"
    s "I'm... I'm coming..."
    s "Go forward if you want, I will catch you later."
    menu:
        "Geez! What should I do?"

        "Wait for her.":
            mc "No... I will wait for you."
            s "Okay... I'm coming~!"
            "*click*"
            "... ... ..."
            pause 5.0
            "... ... ..."
            "8:50 AM"
            s "I'm ready!"
            mc "I hope you're ready to run because the school gates will close IN 10 MINUTES!!!"
            s "Wha--"
            "I grab Sayori's arm and run like we've never runned before..."
            s "Kya~! [player]! Stop!"
            pass
        "Go to school alone.":
            mc "Jesus Christ!"
            mc "Fine, I will go alone then. Be careful in the way..."
            s "Thanks, see you soon~!"
            "*click*"
            "Alright, let's go then..."
            jump ch2_prev_go_school_B
            pass
        "Enter to her house.":
            mc "Alriiiiiight..."
            "*click*"
            "I wonder if she's lift up from the bed."
            "Let's sneak up!"
            scene black
            with wipeleft_scene
            "I silently enter to her house..."
            "Now I'm in front of her bedroom's door."
            "I gently open the door."
            mc "{cps=30}.......Sayo--{/cps}{nw}"
            scene sayori_bedroom
            "Ohmygod!"
            s "Kyaaaaaaaaaaaaaaaaaaaaaaaa-!"
            "I saw Sayori's naked ass...!!!{nw}"
            call mc_pain2
            $ mc_hp -= (25 * mc_hp_max) / 100
            mc "Aaaahh!!!"
            "She throws a shoe directly to my face, it fucking hurts!"
            s "Eh?! [player]???"
            mc "Y-yeah..."
            s "Oh my god! I'm so sorry, I thought you was a sneaky pervert."
            "I guess there's no difference between a pervert and what I've done now."
            mc "Don't worry Sayori, I'm okay..."
            mc "I received worse hits."
            s "... ... ..."
            mc "In fact, I deserve it."
            mc "I should have knock the door... or shouldn't have sneaked in in first place."
            s "..."
            s "How could an girl like me have an awesome friend like you?"
            mc "Umm... I guess it's viceversa."
            s "Do you think so?"
            s "Hahahahaha! You're great, you know that?"
            mc "You too Sayori..."
            mc "Ey, by the way..."
            mc "Put your school uniform and let's go, we'll be late."
            s "Oh, sorry! Hehe~!"
            s "Wait me in the living room, okay? You can pick something from the fridge if you want."
            mc "That's okay Sayori..."
            scene black
            with wipeleft_scene
            "What I was thinking?"
            "Seems like Sayori didn't notice it, but my boner grew up when I saw her booty."
            "I mean, what a culo she has Dios mio!"
            "I make a big ass shape with my hands upper my laps... My god, I'm a degenerated!"
            "Why I'm talking like Tony Montana? Hahahaha..."
            "... ... ..."
            s "Here I am!"
            mc "Perfect! Let's go."
            s "Yay~!"
            scene residential
            with wipeleft_scene
            pass

    return

label ch2_prev_go_school_B:
    scene bg school_entrance
    with wipeleft_scene
    pause 1.0
    show ryoma at t11 zorder 1
    mc "Here we are..."
    show ryoma at t21 zorder 2
    show camilla at t22 zorder 2
    mcf2 "What's up guys?!"
    "[player] & Ryoma" "Camilla!"
    show camilla at h22 zorder 2
    "She hugs us at the same time very enthusiastic."
    show camilla at f22 zorder 2
    mcf2 "Sooo... Where did you come from?"
    if ch2_battle_3_event == True:
        mcf2 "Both are sweating!"
        show camilla at t22 zorder 2
        mcf1 "Yeah..."
    else:
        show camilla at t22 zorder 2
        pass
    mc "We came from Ryoma's dojo."
    mcf2 "A dojo?"
    show ryoma at f21 zorder 2
    mcf1 "I invited [player] to join my Kick boxing Club, and he helped me with the refactions."
    if ch2_battle_3_event == True:
        mcf1 "We also had a training fight to test his skills..."
    show camilla at f22
    show ryoma at t21
    mcf2 "Oh, I see..."
    mcf2 "May I join in too?"
    show camilla at t22
    show ryoma at f21
    mcf1 "If you want..."
    mcf1 "At least everybody knows you have a strong physique, even if you don't appear to."
    mcf1 "So there's no problem on participating in the competitions."
    show camilla at f22
    show ryoma at t21
    mcf2 "Hehe~!"
    show camilla at t22
    mc "That's great!"
    menu:
        "I wish you both join my Literature Club too...":
            show camilla at f22
            mcf2 "I hope so..."
            show camilla at t22
            show ryoma at f21
            mcf1 "Sounds good, but Camilla, you got a \"serious problem\" in that club about, you know..."
            show ryoma at t21
            show camilla at f22
            mcf2 "What it is?"
            mcf2 "Oh true, that green eyed girl is the President."
            mcf2 "[player], how do you spend time in the same room with her? You're very psychologically strong to stand her..."
            show camilla at t22
            mc "Yeah... well..."
            if ch1_winner != "Monika":
                mc "I'm trying to ignore her."
            else:
                mc "I'm trying to give her an opportunity, she's beign so nice to me since I joined in..."
            mc "In fact, seems like she's not so dumbass to me like before. However the other girls seems like they're having a bad time at her side."
            mc "I don't know why she's beign so nice to me suddently... Even I don't understand it."
            mc "Sayori says Monika is a great person. Instead Yuri and Natsuki doesn't seems to be agreed at all."
            show camilla at f22
            mcf2 "I see. Poor girls, especially Sayori..."
            show camilla at t22
            mc "Anyway, I guess Monika is changing progressively, I hope she treats the others better too."
            show camilla at f22
            mcf2 "I don't know... You must be careful darling. I have a bad feeling about this."
            show camilla at t22
            mc "I'll keep it in mind. Thanks Camilla."
            show camilla at f22
            mcf2 "Hehe~! Don't mention it."
            "She pats my head."
            show camilla at t22
            pass
        "We'll be a great team!":
            show camilla at f22
            mcf2 "I agree..."
            show camilla at t22
            show ryoma at f21
            mcf1 "Me too..."
            show ryoma at t21
            pass
    "The school bells sounds."
    show ryoma at f21
    mcf1 "Oh oh! It's time to enter in..."
    show ryoma at t21
    mc "Wait a minute!"
    mc "Have you seen Sayori enter in while we been talking?"
    show ryoma at f21
    mcf1 "No."
    show ryoma at t21
    show camilla at f22
    mcf2 "No."
    show camilla at t22
    mc "Fuck!"
    "I dial to Sayori's phone..."
    s "Hello?"
    mc "Sayori, where are you?"
    s "I'm at one square from the school..."
    s "Hey! I see you!"
    "I spot a Sayori-shaped girl in the horizon..."
    show camilla at f22
    mcf2 "Look, here comes Sayori!"
    show camilla at t22
    mc "Thank Goodness!"
    show ryoma at f21
    mcf1 "Yeah!"
    show sayori 1a at f31 zorder 3
    show ryoma at t32 zorder 2
    show camilla at t33 zorder 2
    s "Hello everyone~!"
    show sayori at t31 zorder 2
    show camilla at f33 zorder 3
    show ryoma at f32 zorder 3
    "Everyone" "Hi Sayori!"
    show sayori at f31 zorder 3
    show camilla at t33 zorder 2
    show ryoma at t32 zorder 2
    s "Ready for a new class day?"
    show sayori at t31 zorder 2
    mc "Sure! Let's go everyone..."
    scene black
    with dissolve_scene_full
    
    return