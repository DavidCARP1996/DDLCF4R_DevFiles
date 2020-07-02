label ch2_fightingclub_activities:
    scene bg fightingclub_clean
    with wipeleft_scene
    hide screen freeroam_hud with Dissolve(.5)
    $ HKBShowButtons()
    $ HKBHideButtons()
    $ mc_current_weapon = None
    $ mc_current_weapon_type = None
    $ renpy.notify("Notice: inventory will be temporarily disabled.")
    show ryoma at t11 zorder 2
    mcf1 "Yo, [player]!"
    if accept_kickboxingclub_offer == "Maybe":
        mcf1 "So you finally decided to join in?"
        mc "Yes."
        mcf1 "Cool then."
        pass
    elif accept_kickboxingclub_offer == "No":
        mcf1 "What a surprise. I thought you are not interested..."
        mc "Yeah, well... I changed of mind."
        mcf1 "Cool then."
        pass
    else:
        pass
    mcf1 "Welcome to the club!"
    mc "Thanks!"
    "..."
    mc "Wow, Ryoma, this place is nicely crowed..."
    mcf1 "Yeah, but most of them are new people which comes from another clubs, like you."
    mc "Oh, I see..."
    mcf2 "[player]~!"
    show ryoma at t21 zorder 2
    show camilla at t22 zorder 3
    mc "Hey, Camilla!"
    mc "It's good to see that we'll be sharing activities together guys."
    show camilla at f22
    mcf2 "Yeah~!"
    show camilla at t22 zorder 2
    mc "So... How shall I start?"
    show ryoma at f21 zorder 3
    mcf1 "I'm glad you ask."
    mcf1 "Well, today we can start with a Trio Tag Team match with switching rules."
    mcf1 "We three will battle against another Team conformed by three opponents at the same time, but in a divided 1 vs 1."
    mcf1 "After all the three finish our respective battles, another round starts but switching opponents."
    mcf1 "That switching repeats again in round 3. However, that's the final round, so after we finish our battles the winner Team will be defined by how many victories had each Team."
    mcf1 "Did everybody understood?"
    show ryoma at t21 zorder 2
    show camilla at f22 zorder 3
    mcf2 "Yes."
    show camilla at t22 zorder 2
    mc "Yes."
    menu:
        "Did you understood everything?"

        "Yes.":
            "Good then."
            "In any case, check the History list on the Menu to read everything again, I don't want to disturb Ryoma because of you."
            pass
        "No.":
            "Then check the History list on the Menu to read everything again, I don't want to disturb Ryoma because of you."
            pass
    show ryoma at f21 zorder 3
    mcf1 "Fine then."
    "After Ryoma finish his explanation, he does a loud clap to call attention."
    mcf1 "Okay, everyone!"
    mcf1 "We need 3 volunteers for a activity."
    mcf1 "Today I want to do a Trio Tag Team match which consists on 3 rounds where both teams switches opponents on each round."
    mcf1 "I already have my own Team conformed by the beautiful Camilla and my pal [player]."
    mcf1 "Who wants to challenge us?"
    scene bg fightingclub_clean
    with wipeleft_scene
    "Round 1"
    call ch2_fightingclub_battle1
    "Finish!"
    if ch2_fightingclub_battle1_victory == True:
        "Flawless victory for Ryoma's Team. Point for Ryoma's Team."
        mcf2 "Yaay~!"
        pass
    else:
        mc "Fuck!"
        "Ryoma's Team 2 - Opponents Team 1. Point for Ryoma's Team."
        mcf2 "Don't worry [player], we won anyway."
        pass
    pause 3.0
    "Round 2"
    call ch2_fightingclub_battle2
    "Finish!"
    if ch2_fightingclub_battle2_victory == True:
        "Flawless victory for Ryoma's Team. Point for Ryoma's Team."
        "Opponent" "It can't be, they're winning..."
        mcf1 "Oh come on guys! What happened to your fighting spirit?"
        mcf1 "Will you throw your towel in a simple training challenge?"
        mcf1 "Remember: we aren't doing this in a competitive way, we are just training."
        mcf1 "Come on! The last round."
        if ch2_fightingclub_battle1_victory == True:
            mc "Seems like a miracle my 2 wins streak."
            mcf2 "Nah, you're awesome. That's all..."
            pass
        else:
            mc "At least I beat that loser of Mac..."
            mcf2 "You're lifting up, that's good [player]..."
            pass
        pass
    else:
        "Ryoma's Team 2 - Opponents Team 1. Point for Ryoma's Team."
        "Opponent" "It can't be, they're winning..."
        mcf1 "Oh come on guys! What happened to your fighting spirit?"
        mcf1 "Will you throw your towel in a simple training challenge?"
        mcf1 "Remember: we aren't doing this in a competitive way, we are just training."
        mcf1 "Come on! The last round."
        if ch2_fightingclub_battle1_victory == True:
            mc "What the fuck did just happened? I beat that thin guy but I lost against that loser of Mac! It's ridiculous!!!"
            pass
        else:
            mc "Once again I'm so fucking useless..."
            pass
        mcf2 "Relax [player], everybody has a bad day."
        mcf2 "And remember, I won't get mad if you're losing, never."
        mc "Thanks Camilla..."
        pass
    pause 3.0
    "Round 3"
    call ch2_fightingclub_battle3
    "Finish!"
    if ch2_fightingclub_battle3_victory == True:
        "Flawless victory for Ryoma's Team. Point for Ryoma's Team."
        mcf2 "Yes~!" 
        mcf2 "We{w=0.5} are{w=0.5} invictus!{w=0.5} We{w=0.5} are{w=0.5} invictus!"
        "Camilla is acting euphorically, just like Sayori would do in this kind of situation..."
        "But it's because she's teaming up with me and Ryoma, otherwise she could be acting normal."
        mcf1 "Well done! Everybody did a good job today."
        "Opponent" "Whatever. All of you kicked our asses so easy."
        if ch2_fightingclub_battle1_victory == True and ch2_fightingclub_battle2_victory == True:
            mc "I did it very well to be my first day. It's a good sign..."
            mcf2 "Of course it is..."
            "She suddently hugs me."
            mcf2 "I knew you will do it amazing~!"
            mc "Hehehe, thanks Camilla..."
            pass
        elif ch2_fightingclub_battle1_victory == True and ch2_fightingclub_battle2_victory == False:
            mc "I can't believe I've lost against Mac... Fucking bullshit!"
            mcf2 "Calm down [player], it's not the end of the world."
            "She pats my head."
            pass
        elif ch2_fightingclub_battle1_victory == False and ch2_fightingclub_battle2_victory == True:
            mc "I started with the wrong foot. At least I did it better in the last two matches."
            mcf2 "Yeah, but it's normal... Nobody is so perfect to do everything good."
            mc "Yeah, you're right..."
            "She pats my head."
            pass
        else:
            mc "Finally! My first fucking victory!"
            mc "But it's still a bit shameful from my part."
            mcf2 "Don't worry [player], at least you beated the strongest one... I think you was mercyful to the others."
            mc "No... That's not."
            pass
        pass
    else:
        "Ryoma's Team 2 - Opponents Team 1. Point for Ryoma's Team."
        mcf2 "Yes~!" 
        mcf2 "We{w=0.5} are{w=0.5} invictus!{w=0.5} We{w=0.5} are{w=0.5} invictus!"
        "Camilla is acting euphorically, just like Sayori would do in this kind of situation..."
        "But it's because she's teaming up with me and Ryoma, otherwise she could be acting normal."
        mcf1 "Well done! Everybody did a good job today."
        "Opponent" "Whatever. All of you kicked our asses so easy."
        if ch2_fightingclub_battle1_victory == True and ch2_fightingclub_battle2_victory == True:
            mc "I guess that big guy was enough for me..."
            mc "Sorry guys, I ruined a nice invict."
            mcf2 "Don't worry about that [player], you did it good anyway."
            mc "Hehe, thank you Camilla..."
            pass
        elif ch2_fightingclub_battle1_victory == True and ch2_fightingclub_battle2_victory == False:
            mc "What happened? I beated the first one but I wasn't able to beat the others?"
            mc "I feel ridiculous!"
            mcf2 "Come on [player], it's not the end of the world..."
            pass
        elif ch2_fightingclub_battle1_victory == False and ch2_fightingclub_battle2_victory == True:
            mc "Incredible, the only one I manage to beat was that loser of Mac..."
            mcf2 "Hehe~"
            pass
        else:
            mc "I'm a fucking idiot..."
            mc "I wasn't able to beat anyone of them! Shame on me!"
            mcf2 "[player]..."
            mcf1 "I'm so sorry [player]."
            mcf1 "But don't worry, you can have a rematch tomorrow."
            mc "... ... ..."
            pass
        pass
    scene bg fightingclub_clean
    with wipeleft_scene
    mcf1 "Okay, everyone!"
    mcf1 "We're done for our activities today."
    mcf1 "I hope all of you enjoyed this moment."
    if ch2_fightingclub_battle1_victory == False and ch2_fightingclub_battle2_victory == False and ch2_fightingclub_battle3_victory == False:
        mc "... ... ..."
        mcf2 "[player]..."
        mcf1 "..."
        mcf1 "Anyway."
    mcf1 "If everyone are interested on keep going at this hour, you're all welcome."
    "Everyone" "Yes sensei!"
    mcf1 "Alright. See you tomorrow then."
    "..."
    if ch2_fightingclub_battle1_victory == True and ch2_fightingclub_battle2_victory == True and ch2_fightingclub_battle3_victory == True:
        mcf1 "[player], you did it excellent! I knew it was a good idea inviting you."
        mcf2 "He's right. You're great [player]!"
        mc "Thanks guys...!"
        mcf2 "Together, nobody will dare to stop us!"
        mcf1 "Well said Camilla."
        "I'm so lucky having them has friends..."
        pass
    elif ch2_fightingclub_battle1_victory == False and ch2_fightingclub_battle2_victory == False and ch2_fightingclub_battle3_victory == False:
        mc "I'm a disaster Ryoma. I don't know why you bothered to invite me..."
        mcf1 "Oh, come on [player]! Nobody starts winning everything at the first day."
        mcf2 "Ryoma is right, I have the sense you will do it better for tomorrow."
        mcf2 "Please, don't quit..."
        mc "What if I..."
        mcf2 "Then I will be sad."
        "How can I say No to that face???"
        mc "Okayyy... Tomorrow I will have my rematch."
        mcf2 "Yaay~!"
        pass
    else:
        mcf1 "Not bad [player], not bad."
        mc "Are you kidding me? Both of you were invictus and I don't..."
        mcf2 "Don't complain about it [player], at least you putted your part there. Something is something, isn't?"
        mc "Well... maybe..."
        mcf1 "Don't worry, the next time you will do it better, that's for sure."
        mcf2 "Ryoma is right, we trust on you [player]~!"
        mc "Alright... Thanks guys."
        pass
    return