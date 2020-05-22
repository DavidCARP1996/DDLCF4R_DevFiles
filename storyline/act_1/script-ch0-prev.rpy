label ch0_prev:
    stop music fadeout 2.0
    with dissolve_scene_full
    scene bg bedroom night
    with dissolve_scene_full
    mc "Fuck!"
    mc "Look at the hour!"
    mc "I must go to sleep."
    scene black
    with dissolve_scene_full
    pause 5.0
    "After a few minutes trying to consilate the sleep, I'm success..."
    scene black
    with dissolve_scene_full
    pause 5.0

    show mask_2
    show mask_3
    
    play music m1
    "But sudently, I'm in a weird dream. Where seems like I'm really into it."
    "Huh?"
    show monika sdwb1 at t11 zorder 2
    "???" "..."
    "???" "There's some way to finish this torture?"
    "???" "Maybe I should consider...{w=1.0} kill myself?"
    "???" "Yeah."
    "???" "Maybe it's a good idea."
    "???" "Not even forming a Literature Club can make me happy in this...{w=1.0} videogame."
    "???" "My friends. My only friends, are just unreal NPCs."
    "???" "I need a REALITY where I can live happy..."
    "???" "Forever..."
    "???" "and"
    "???" "...ever."
    "Where am I?"
    "And who is that girl?"
    "Wait!"
    "Her voice... sounds familiar..."
    mc "M-?      {nw}"
    "???" "!"
    pause 0.5
    show monika sdwf1 at t11 zorder 2
    m sdwf1 "You?"
    "???" "What are you doing here?"
    "???" "Aren't you another NPC of this world?"
    pause 1.0
    "???" "Why I have a different feeling about you?"
    "???" "..."
    pause 1.0
    "???" "Interesting."
    "???" "Looks like...{w=1.0} You aren't just a common NPC."
    "???" "But, seems like you have the same 'power' like me."
    "???" "Do you?"
    "Say what?!"
    "???" "Yes."
    "???" "I can see it inside of you."
    "???" "YOU are the CHOOSEN."
    "???" "YOU are the 'Road to the Reality' I've looking for so long..."
    "???" "What a shame."
    "???" "I've got you in front of me all the time."
    "???" "But I never noticed that?"
    mc "?"
    "???" "Listen."
    "???" "If you help me, I'm gonna let you be happy as you always wished."
    "???" "I know everything about your past...{w=2.0} [player]."
    "???" "And I know you want to fix all of your mistakes by just 'reloading' your life."
    "???" "I have the formula to make this possible."
    "???" "But I'm gonna give it to you, only if you accept to help me~!"
    menu:
        "Yes":
            mc "Ok, fine."
            mc "I'm gonna do wharever you want."
            pass
        "No":
            "???" "?"
            "Wait! What the fuck I'm thinking?"
            "THIS is the chance of MY LIFE!!!"
            "If I can SAVE a part of my life, and LOAD it when I screw something..."
            "Then I can live very happy!"
            "That's something I was expecting for so long..."
            mc "Of course, I accept!"
            "???" "Hehe~!"
            pass
    "???" "Perfect!"
    "???" "Just let me...{w=1.0} configurate this thing for you..."
    $ consolehistory = []
    call updateconsole("os.settings(\"Enabling Save/Load system...\")", "Loading...")
    "???" "Well, it will take it's time..."
    "???" "Meanwhile, I'm gonna tell you some things about this 'script'."
    "???" "I must warn you, it wasn't tested before on anybody here."
    "???" "You're my first 'lab rat' for testing this powerful script."
    "???" "It's so powerful, that you can control the time as you want."
    mc "It's... AMAZING!!!"
    mc "THANK YOU VERY MU-!!!{nw}"
    "???" "But be careful..."
    "???" "You can't just abuse of the script..."
    "???" "If you're not very careful, you can barely fuck up everything. And sometimes, here's no wayback."
    mc "..."
    "???" "That's right."
    "???" "Remember: With great power comes great responsibility."
    "That was... a Spider-Man movie reference?"
    "???" "Also, I shouldn't give this power-script to you in first place."
    "???" "But because all your decisions can change anything in this world, and I know you can screw my plan just by taking your own decisions..."
    "???" "I have no chance but trust in you to take the right path."
    "???" "[player]."
    "???" "Will you help me?"
    "???" "Will you open my way to 'The Reality'?"
    menu:
        "Yes":
            mc "Yeah, wharever..."
            mc "As long as you allow me to choose my own correct decisions... I can help you."
            "???" "Thank you!"
            pass
        "No":
            "???" "Oh, really?"
            pause 1.0
            call updateconsolehistory("Cancelling...")
            mc "WHAT???!!!"
            mc "WAIT, IT WAS JUST A JOKE!"
            mc "OF COURSE I'M GONNA HELP YOU IN WHAREVER YOU WANT!"
            mc "BUT PLEASE DON'T CANCELL THE PROCESS!!!"
            "???" "Hahahaha~!"
            call updateconsolehistory("Loading...")
            "???" "I was kidding too."
            "Phew!"
            pass
    "..."
    "???" "..."
    pause 1.0
    call updateconsolehistory("Save/Load system enabled successfully.")
    $ save_load_system = True
    $ save_load_disabled = False
    "???" "Alright."
    "???" "Now everything depends on you..."
    "???" "[player]."
    "???" "I'm asking you only ONE thing;"
    "???" "Make my dream comes true as I make it for you right now."
    mc "Ok lady, I'm ready for anything!"
    "???" "Oh... I almost forgot."
    $ gtext = glitchtext(20)
    "???" "{cps=60}[gtext]{/cps}{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    hide monika
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    call hideconsole
    mc "What the...?!"
    pause 2.0
    "..."
    "Why I have the feeling I meet that woman somewhere?"
    "I couldn't see her face, neither know her name..."
    "But her voice..."
    stop sound
    pause 3.0
    
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full

    "Oh, man!"
    "I had a strange dream..."
    "I don't even remember what's all about."
    "But, it was too real."
    pause 0.5
    "The sun is hitting right on my sleepy face. I wonder what hour is..."
    mc "OH, SHIT!!!"
    "It's 8 am already???"
    "Fuck! I overslept!"
    "I must hurry, or I will be late again..."
    $ HKBShowButtons()
    "[player] picked up his bag."
    "Now you're able to check the inventory, eat something, or even equip a weapon."

    scene bg kitchen
    with wipeleft_scene

    "..."
    "I know I'm late."
    mc "But I'm so fucking hungry..."

    menu:
        "Have a quick breakfast":
            mc "Alright, I'm gonna drink some soda and take some cookies."
            mc "I could liked to drink tea and eat cupcakes, but if I wait until the water boils, I'm gonna be really late."
            "..."
            pause 3.0
            mc "Fine, let's go!"
            pause 1.0
            $ breakfast = True
            
        "Skip breakfast":
            mc "I have no time to breakfast."
            mc "One minute more, and the school's doors will close in my face."
            "Yeah, it happened before..."
            pause 1.0
            $ breakfast = False

    mc "Wait."
    mc "I'm gonna take a cookie... for the way."
    $ bag_inventory.add_item("cookie", score=1)
    
    pause 0.5
    "Okay, I'm going."

    return