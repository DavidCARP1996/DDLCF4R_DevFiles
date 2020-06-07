# Chapter 1 static content. Poem responses called from here are in script-poemresponses.rpy

label ch1_main:
    scene bg club_day
    with dissolve_scene_half
    play music t2
    show monika 5 at t11 zorder 2

    m "Hi again, [player]!"
    m "Glad to see you didn't run away on us. Hahaha!"
    mc "Nah, don't worry."
    mc "This might be a little strange for me, but I at least keep my word."
    show monika at thide zorder 1
    hide monika
    "Well, I'm back at the Literature Club."
    "I was the last to come in, so everyone else is already hanging out."
    show yuri 1a at t32 zorder 2
    y "Thanks for keeping your promise, [player]."
    y "I hope this isn't too overwhelming of a commitment for you."
    y 1u "Making you dive headfirst into literature when you're not accustomed to it..."
    show natsuki 4e at t33 zorder 2
    n "Oh, come on! Like he deserves any slack."
    n "Sayori told me you didn't even want to join any clubs this year."
    n "And last year, too!"
    n 4c "I don't know if you plan to just come here and hang out, or what..."
    n "But if you don't take us seriously, then you won't see the end of it."
    show monika 2b at l41
    m "Natsuki, you certainly have a big mouth for someone who keeps her manga collection in the clubroom."
    n 4o "M-M-M...!!"
    show monika at lhide
    hide monika
    "Natsuki finds herself stuck between saying \"Monika\" and \"Manga\"."
    show natsuki at h33
    n 1v "Manga is literature!!"
    show natsuki at thide zorder 1
    hide natsuki
    "Swiftly defeated, Natsuki plops back into her seat."
    show yuri at t22 zorder 2
    show sayori 2x at f21 zorder 3
    s "Don't worry, guys~"
    s "[player] always gives it his best as long as he's having fun."
    s "He helps me with busywork without me even asking."
    s "Like cooking, cleaning my room..."
    show sayori 2a at t21 zorder 2
    show yuri at f22 zorder 3
    y 2m "How dependable..."
    show yuri at t22 zorder 2
    mc "Sayori, that's because your room is so messy it's distracting."
    mc "And you almost set your house on fire once."
    show sayori at s21
    s 5 "Is that so... Ehehe..."
    show yuri at f22 zorder 3
    y 1s "You two are really good friends, aren't you?"
    y "I might be a little jealous..."
    show yuri at t22 zorder 2
    show sayori at f21 zorder 3
    s 1 "How come? You and [player] can become good friends too!"
    show sayori at t21 zorder 2
    show yuri at f22 zorder 3
    y 4b "U-Um..."
    show yuri at t22 zorder 2
    mc "S-Sayori--"
    show sayori at f21 zorder 3
    s "Hmm?"
    show sayori at t21 zorder 2
    mc "..."
    "As usual, Sayori seems oblivious to the weird situation she just put me into."
    show sayori at f21 zorder 3
    s 4x "Oh, oh! Yuri even brought you something today, you know~"
    show sayori at t21 zorder 2
    show yuri at f22 zorder 3
    y 3n "W-Wait! Sayori..."
    show yuri at t22 zorder 2
    mc "Eh? Me?"
    show yuri at f22 zorder 3
    y 3o "Um... Not really..."
    show yuri at t22 zorder 2
    show sayori at f21 zorder 3
    s 4r "Don't be shy~"
    show sayori at t21 zorder 2
    show yuri at f22 zorder 3
    y "It's really nothing..."
    show yuri at t22 zorder 2
    mc "What is it?"
    show yuri at f22 zorder 3
    y 4c "N-Never mind!"
    y "Sayori made it sound like a big deal when it's really not..."
    y "Uuuuh, what do I do..."
    show yuri at t22 zorder 2
    show sayori at f21 zorder 3
    s 1g "Eh? I'm sorry, Yuri, I wasn't thinking..."
    show sayori at thide zorder 1
    hide sayori
    show yuri at t11 zorder 2
    "I guess that means it's up to me to rescue this situation..."
    mc "Hey, don't worry about it."
    mc "First of all, I wasn't expecting anything in the first place."
    mc "So any nice gesture from you is a pleasant surprise."
    mc "It'll make me happy no matter what."
    y 3v "I-Is that so..."
    mc "Yeah. I won't make it a big deal if you don't want it to be."
    y "Alright..."
    y 1a "Well, here."
    "Yuri reaches into her bag and pulls out a book."
    y "I didn't want you to feel left out..."
    y "So I picked out a book that I thought you might enjoy."
    y "It's a short read, so it should keep your attention, even if you don't usually read."
    y "And we could, you know..."
    show yuri at sink
    y 4b "Discuss it...if you wanted..."
    "Th-This is..."
    "How is this girl accidentally being so cute?"
    "She even picked out a book she thinks I'll like, despite me not reading much..."
    mc "Yuri, thank you! I'll definitely read this!"
    "I enthusiastically take the book."
    show yuri 2m at t11 zorder 2
    y "Phew..."
    y 2a "Well, you can read it at your own pace."
    y "I look forward to hearing what you think."
    show yuri at thide zorder 1
    hide yuri

    #Exclusive scene starts here
    "Now that everyone's settled in, I expected Monika to kick off some scheduled activities for the club."
    "But that doesn't seem to be the case."
    "Sayori and Monika are having a cheery conversation in the corner."
    "Yuri's face is already buried in a book."
    "I can't help but notice her intense expression, like she was waiting for this chance."
    "Meanwhile, Natsuki is rummaging around in the closet."
    
    #Call exclusive scene
    $ nextscene = poemwinner[0] + "_exclusive_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene

    #After exclusive scene, we go back to poem responses
    show monika 1 at t21 zorder 2
    hide sayori
    hide natsuki
    hide yuri
    m "By the way, did you remember to write a poem last night?"
    mc "Y-Yeah..."
    "My relaxation ends."
    "I can't believe I agreed to do something so embarrassing."
    "I couldn't really find much inspiration, since I've never really done this before."
    m "Well, now that everyone's ready, why don't you find someone to share with?"
    show sayori 4q at t22 zorder 2
    s "I can't wait~!"
    show sayori at thide zorder 1
    show monika at thide zorder 1
    hide sayori
    hide monika
    "Sayori and Monika enthusiastically pull out their poems."
    "Sayori's is on a wrinkled sheet of loose leaf torn from a spiral notebook."
    "On the other hand, Monika wrote hers in a composition notebook."
    "I can already see Monika's pristine handwriting from where I sit."
    "Natsuki and Yuri reluctantly comply as well, reaching into their bags."
    "I do the same, myself."

    return


label ch1_main_end:
    stop music fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    play music t3
    mc "Phew..."
    "I guess that's everyone."
    "I glance around the room."
    "That was a little more stressful than I anticipated."
    "It's as if everyone is judging me for my mediocre writing abilities..."
    "Even if they're just being nice, there's no way my poems can stand up to theirs."
    "This is a literature club, after all."
    "I sigh."
    "I guess that's what I ended up getting myself into."
    "Across the room, Sayori and Monika are happily chatting."
    "My eyes land on Yuri and Natsuki."
    show yuri 2g at t21 zorder 2
    show natsuki 1g at t22 zorder 2
    "They gingerly exchange sheets of paper, sharing their respective poems."
    show yuri 2i at t21
    "As they read in tandem, I watch each of their expressions change."
    "Natsuki's eyebrows furrow in frustration."
    "Meanwhile, Yuri smiles sadly."
    show natsuki at f22 zorder 3
    n 1q "{i}(What's with this language...?){/i}"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 2f "Eh?"
    y "Um...did you say something?"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 2c "Oh, it's nothing."
    "Natsuki dismissively returns the poem to the desk with one hand."
    n "I guess you could say it's fancy."
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 2i "Ah-- Thanks..."
    y "Yours is...cute..."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 2h "Cute?"
    n 1h "Did you completely miss the symbolism or something?"
    n "It's clearly about the feeling of giving up."
    n "How can that be cute?"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 3f "I-I know that!"
    y "I just meant..."
    y 3h "The language, I guess..."
    y "I was trying to say something nice..."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n "Eh?"
    n 4w "You mean you have to try that hard to come up with something nice to say?"
    n "Thanks, but it really didn't come out nice at all!"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 1i "Um..."
    y "Well, I do have a couple suggestions..."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 5x "Hmph."
    n "If I was looking for suggestions, I would have asked someone who actually liked it."
    n "Which people {i}did{/i}, by the way."
    n 5e "Sayori liked it."
    n "And [player] did, too!"
    n "So based on that, I'll gladly give you some suggestions of my own."
    n "First of all--"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 2l "Excuse me..."
    y "I appreciate the offer, but I've spent a long time establishing my writing style."
    y 2h "I don't expect it to change anytime soon, unless of course I come across something particularly inspiring."
    y "Which I haven't yet."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1o "Nn...!"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 1k "And [player] liked my poem too, you know."
    y "He even told me he was impressed by it."
    stop music fadeout 1.0
    "Natsuki suddenly stands up."
    "Oh-oh!"
    "If Natsuki dares to do something bad to Yuri, I will..."
    "No! {p}Let's keep listening to them and wait where will it go."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 4y "Oh?"
    n "I didn't realize you were so invested in trying to impress our new member, Yuri."
    play music t7
    "What? {p}I mean, I hope so. That means she's really interested on me... uhuhu~!"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 1n "E-Eh?!"
    y "That's not what I...!"
    y 1o "Uu..."
    y "You...You're just..."
    "Yuri stands up as well."
    "It's gonna get ugly..."
    y 2r "Maybe you're just jealous that [player] appreciates my advice more than he appreciated yours!"
    show yuri at t21 zorder 2
    show natsuki 1e at f22 zorder 3
    "Well, she got a point..."
    n "Huh! And how do you know he didn't appreciate {i}my{/i} advice more?"
    n "Are you that full of yourself?"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 3h "I...!"
    y "No..."
    y "If I was full of myself..."
    y 1r "...I would deliberately go out of my way to make everything I do overly cutesy!"
    show yuri at t21 zorder 2
    show natsuki 1o at f22 zorder 3
    "Oooooooooooh~!"
    n "Uuuuuu...!"
    show sayori 2l at l41 behind yuri,natsuki
    show yuri at t32 zorder 2
    show natsuki at t33 zorder 2
    s "U-Um!!"
    s "Is everyone okay...?"
    "Did they ignored Sayori? What the fuck is wrong with them?"
    "I would say something about that, but I prefer not to intruding them."
    show sayori 2 at lhide
    hide sayori
    show natsuki at f33 zorder 3
    n 1f "Well, you know what?!"
    n "I wasn't the one whose boobs magically grew a size bigger as soon as [player] started showing up!!"
    show yuri 3p at h32
    show natsuki at t33 zorder 2
    "Whooohohoooo~! Wait what?!"
    y "N-Natsuki!!"
    show monika 3l at l41 behind yuri,natsuki
    m "Um, Natsuki, that's a little--"
    show monika at h41
    show yuri 3p at f32 zorder 3
    show natsuki 1e at f33 zorder 3
    ny "This doesn't involve you!"
    show monika at lhide
    hide monika
    show yuri at t32 zorder 2
    show natsuki at t33 zorder 2
    show sayori 4p at l41 behind yuri,natsuki
    s "I-I don't like fighting, guys...!"
    show sayori at lhide
    hide sayori
    show yuri at t21 zorder 2
    show natsuki 1g at t22 zorder 2
    "Poor Sayori... Should I do something right now?"
    "Suddenly, both girls turn towards me, as if they just noticed I was standing there."
    show yuri at f21 zorder 3
    y 2n "[player]...!"
    y "She-- She's just trying to make me look bad...!"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 4w "That's not true!"
    n "She started it!"
    n 4e "If she could get over herself and learn to appreciate that {i}simple{/i} writing is more effective..."
    n "Then this wouldn't have happened in the first place!"
    n "What's the point in making your poems all convoluted for no reason?"
    n "The meaning should jump out at the reader, not force them to have to figure it out."
    n 1f "Help me explain that to her, [player]!"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 3o "W-Wait!"
    y "There's a reason we have so many deep and expressive words in our language!"
    y 3w "It's the only way to convey complex feelings and meaning the most effectively."
    y "Avoiding them is not only unnecessarily limiting yourself...it's also a waste!"
    y 1t "You understand that, right, [player]?"
    show yuri at t21 zorder 2
    mc "Um...!"
    show yuri 1t at f21 zorder 3
    show natsuki 1e at f22 zorder 3
    ny "Well??"
    mc "..."
    show yuri at t21 zorder 2
    show natsuki 1g at t22 zorder 2
    "How did I get dragged into this in the first place?!"
    "It's not like I know anything about writing..."
    "But whomever I agree with, they'll probably think more highly of me!"
    menu:
        "So, of course that's going to be...!"
        "Yuri.":
            call ch1_end_yuri
        "Natsuki.":
            call ch1_end_natsuki
        "Help me, Sayori!!":
            call ch1_end_sayori
        "Monika, you're the President! Do something!":
            call ch1_end_monika
        "EVERYBODY SHUT THE FUCK UP!!!":
            call ch1_end_mc

    scene bg club_day
    show monika 4b at t11 zorder 2
    with wipeleft_scene
    m "Okay, everyone!"
    m "It's just about time for us to leave."
    m "How did you all feel about sharing poems?"
    show monika 4a
    show sayori 4x at t31 zorder 2
    s "It was a lot of fun!"
    show sayori at thide behind yuri
    show yuri 1i at t31 zorder 2
    hide sayori
    y "Well, I'd say it was worth it."
    show yuri at thide behind natsuki
    show natsuki 4q at t31 zorder 2
    hide yuri
    n "It was alright. Well, mostly."
    show natsuki at thide zorder 1
    hide natsuki
    m 1a "[player], how about you?"
    mc "...Yeah, I'd say the same."
    mc "It was a neat thing to talk about with everyone."
    m 1j "Awesome!"
    m 1a "In that case, we'll do the same thing tomorrow."
    m "And maybe you learned something from your friends, too."
    m 3b "So your poems will turn out even better!"
    mc "..."
    show monika at thide zorder 1
    hide monika
    "I think to myself."
    "I did learn a little more about the kinds of poems everyone likes."
    "With any luck, that means I can at least do a better job impressing those I want to impress."
    if books_bought == 0:
        "And I guess I don't need the thematic books anymore."
    "I nod to myself with newfound determination."
    show sayori 1x at t11 zorder 2
    s "[player]!"
    s "Ready to walk home?"
    mc "Sure, let's go."
    s 4q "Ehehe~"
    "Sayori beams at me."
    "It truly has been a while since Sayori and I have spent this much time together."
    "I can't really say I'm not enjoying it, either."
    scene bg residential_day
    show sayori 1a at t11 zorder 2
    with wipeleft_scene
    mc "Sayori..."
    mc "About what happened earlier..."
    s 1b "Eh? What do you mean?"
    mc "You know, between Yuri and Natsuki."
    mc "Does that kind of thing happen often?"
    s 4j "No, no, no!"
    s "That's really the first time I've seen them fight like that..."
    s "I promise they're both wonderful people."
    show sayori at s11
    s 1g "You don't... You don't hate them, do you??"
    mc "No, I don't hate them!"
    mc "I just wanted your opinion, that's all."
    mc "I can see why they'd make good friends with you."
    show sayori at t11 zorder 2
    s 1d "Phew..."
    s "You know, [player]..."
    s "It's nice that I get to spend time with you in the club."
    s "But I think seeing you get along with everyone is what makes me the happiest."
    s 1x "And I think everyone really likes you, too!"
    mc "That's--!"
    s 4q "Ehehe~"
    s "Every day is going to be so much fun~"
    mc "Yes... I guess..."
    "It looks like Sayori still hasn't caught onto the kind of situation I'm in."
    "Sure, being friends with everyone is nice, but..."
    "...Does it really need to stop there?"
    mc "We'll just have to see what the future holds, Sayori."
    "I pat Sayori on the head."
    "I said that more to myself than to her, but it's easy to use Sayori as an internal monologue sometimes."
    show sayori at h11
    s 1x "Okay~!"
    "Yeah..."
    "Let's do this!"
    return
    
label ch1_end_yuri:
    $ ch1_choice = "yuri"
    stop music fadeout 1.0
    mc "Natsuki."
    mc "You're right that I liked your poem."
    show natsuki at f22 zorder 3
    n 1e "See??"
    show natsuki 1g at t22 zorder 2
    play music t8
    mc "Wait!"
    mc "That's not an excuse for you to be so mean!"
    mc "You shouldn't pick a fight just because someone's opinion is different."
    show natsuki at f22 zorder 3
    n 1m "That's not what happened at all!"
    n "Yuri wouldn't even take my poem seriously!"
    show natsuki at t22 zorder 2
    mc "Mm..."
    mc "I understand."
    mc "Yuri."
    show yuri at f21 zorder 3
    y 2t "Eh?"
    show yuri at t21 zorder 2
    mc "You're a seriously talented writer."
    mc "It's no secret that I was impressed."
    show yuri at f21 zorder 3
    y 2u "W-Well, that's..."
    show yuri at t21 zorder 2
    mc "But here's the thing."
    mc "No matter how simple or refined someone's writing style is..."
    mc "They're still putting feelings into it, and it becomes something really personal."
    mc "That's why Natsuki felt threatened when you said her poem was cute."
    show yuri at f21 zorder 3
    y 2v "I...see..."
    y "I didn't notice that I..."
    show yuri at t21 zorder 2
    y 2w "I-I'm sorry..."
    show yuri at s21
    y "Uuu..."
    show natsuki at t11 zorder 2
    show yuri at thide zorder 1
    hide yuri
    mc "But Natsuki, you took it way too far!"
    mc "Yuri means well, and if you just told her how you felt..."
    mc "Then this wouldn't have happened in the first place."
    n 1e "Are you kidding?"
    n "That's exactly what I did!"
    n "It was {i}her{/i} that--"
    show natsuki at t22 zorder 2
    show monika 2i at f21 zorder 3
    m "Natsuki, I think that's enough."
    m "You both said some things that you didn't mean."
    m "Yuri apologized. Don't you think you should, too?"
    show monika at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1x "Nnn...!"
    show natsuki at t22 zorder 2
    "Natsuki clenches her fists."
    "In the end, nobody has taken her side."
    "She's trapped, at this point being defiant only because she can't handle the pressure."
    "I end up even feeling bad for her."
    show monika at t32 zorder 2
    show natsuki at t33 zorder 2
    show sayori 2h at l41
    s "U-Um!"
    s "Sometimes when I'm hurt..."
    s "It helps to take a walk and clear my head!"
    show sayori at t41 zorder 2
    mc "Sayori, she doesn't need to--"
    show natsuki at f33 zorder 3
    n 2q "You know what?"
    n "I'm going to do that."
    n 2w "It'll spare me from having to look at all your faces right now."
    show natsuki at thide zorder 1
    hide natsuki
    "Without warning, Natsuki snatches her own poem up from the desk and storms out."
    "On her way out, she crumples up the poem with her hands and throws it in the trash."
    show sayori at f41 zorder 3
    s 1k "Natsuki..."
    show sayori at t41 zorder 2
    show monika at f32 zorder 3
    m 1r "She really didn't need to do that..."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    hide sayori
    hide monika
    "I look across the room."
    "Yuri has her chin buried in her hands while she stares down at her desk."
    "I gingerly approach her and sit in an adjacent chair."
    stop music fadeout 1.0
    show yuri 4b at t11 zorder 2
    y "Sigh..."
    mc "Everything alright?"
    play music t9
    y "I'm so embarrassed..."
    y "I can't believe I acted like that."
    y "You probably hate me now..."
    mc "No--Yuri!"
    mc "How could anyone not have gotten frustrated after being treated like that?"
    show yuri 4a
    mc "You handled it as well as anyone could."
    mc "I don't think any less of you."
    mc "Also, I wanted to interrupt and help you, but I didn't wanted to screw up everything, so..."
    y 2v "Well..."
    y "...Alright, I believe you."
    y 2s "Thanks, [player]. You're too kind."
    y "I'm thankful to have you a part of this club now."
    mc "Er-- It's nothing."
    y 2v "One more thing..."
    y "Um, that one thing that Natsuki said..."
    y 4c "About...you know..."
    y "I would never do anything...so shameful..."
    y "So..."
    "Yeah, the boobs thing... (I try to not laugh because, I don't know, it was funny for me even if it's false)"
    menu:
        "However..."
        "Say it!":
            mc "I know... And I know she wasn't right about that."
            menu:
                "Don't let anyone else on the world threats you so bad, never again...":
                    y 4a "I-I guess you're right..."
                    y "Thanks [player]!"
                    mc "Don't mention it."
                    mc "And if sometime, Natsuki or anyone tries to bully on you, just tell me and I'm gonna fix everything."
                    mc "No matter how threatening the person is, I'm already dealing with some idiots."
                    "I press my right fist on my left chest, suggesting that's a promise from my heart."
                    pass
                "Your boobs are real, and nice...":
                    y 3p "[player]!"
                    mc "...Eh? Did I said something wrong?"
                    pass
        "Make like you didn't heard nothing!":
            mc "...Eh?"
            mc "What thing did Natsuki say?"
            pass
    y 3n "--!"
    y "U-Um!"
    y 3q "Well, never mind that..."
    y "I-I'm going to go make some tea..."
    mc "Ah, good idea."
    mc "Make enough for more than one person, okay?"
    mc "I would love to drink some..."
    stop music fadeout 1.0
    y 3j "Y-Yeah."
    mc "Do you need some help?"
    y 3c "N-Not really... I can handle this myself. Thanks anyway."
    mc "You're welcome."
    show yuri at lhide
    hide yuri
    play music t8
    "In the end, though, Monika's right."
    "Being in the Literature Club probably means I can't spend all my time doing nothing."
    "But in the end..."
    "...I guess it's been worth it so far."
    return

label ch1_end_natsuki:
    $ ch1_choice = "natsuki"
    stop music fadeout 1.0
    "Man... Really?"
    "Shit, it will be very hard to say it..."
    "Well, here goes nothing!"
    mc "Um..."
    mc "Yuri!"
    mc "You're really talented."
    show yuri 4a at s21
    y "Eh? W-Well..."
    play music t8
    mc "But Natsuki has a point!"
    mc "I think that..."
    show yuri at t21 zorder 2
    "I wrack my brain in an attempt to back myself up."
    mc "I think that conveying feelings with few words..."
    mc "Can be just as impressive as well!"
    mc "It lets the reader's imagination take over."
    mc "And Natsuki's poem did a really good job at that!"
    show natsuki at f22 zorder 3
    n 5y "...Yeah!!"
    n "It did, didn't it?!"
    n "Ahah!"
    n "Shows how much {i}you{/i} know!"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 4b "T-That's not..."
    show yuri at t21 zorder 2
    mc "Natsuki..."
    mc "I think that's enough."
    show natsuki at f22 zorder 3
    n 1m "Huh?"
    n "Me?"
    n "But she was so mean to me...!"
    "Natsuki's voice whines."
    show natsuki at t22 zorder 2
    mc "Look..."
    mc "What we talked about yesterday was right."
    mc "Writing is a really personal thing."
    mc "And sharing it can definitely be hard."
    mc "It looks like we learned that today."
    mc "Even small criticism can lead to something pretty heated."
    "I glance over my shoulder."
    "Sayori is nodding vigorously."
    mc "Yeah, so..."
    mc "You don't need to feel threatened."
    mc "You're a great writer, Natsuki."
    show natsuki at f22 zorder 3
    n 1h "Ah--"
    "Natsuki's voice gets caught in surprise."
    n 1q "...Thanks for noticing."
    "She finally mutters that, barely audible."
    show natsuki at t22 zorder 2
    mc "Yuri..."
    show yuri at f21 zorder 3
    y 4a "...?"
    "Yuri looks at me dejectedly."
    "With a face like that, I can't help but feel bad for her as well."
    "Fuck... I think I fucked you everything..."
    show yuri at t21 zorder 2
    mc "I'm sure that Natsuki didn't mean everything she said."
    mc "So you don't need to feel threatened, either."
    show yuri at f21 zorder 3
    y 2v "Well..."
    y "If you say so..."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1g "Hey...!"
    n "It's not like you need to apologize {i}for{/i} me, [player]."
    n 1w "Sheesh."
    "Natsuki takes a breath."
    n 1q "I..."
    n "The thing about..."
    n "Uu..."
    "Natsuki glances around the room."
    show natsuki at hf22 zorder 3
    n 1x "{i}Would everyone stop staring at me??{/i}"
    "Unsurprisingly, Natsuki has a harder time with it than she boasted."
    "Sayori and Monika look away."
    show natsuki at f22 zorder 3
    n 1i "Hmph."
    n "Anyway...!"
    n 1q "The thing about your boobs. I didn't mean it, okay?"
    n "That's all."
    "Natsuki looks away, avoiding eye contact with anyone."
    show natsuki at t22 zorder 2
    show sayori 4x at l41 behind yuri
    s "Yeah! You're naturally beautiful, Yuri!!"
    mc "Of course! Sayori is right... Everyone who complains abour your body is because they're jealous, that's all."
    "I try my best to cheer up Yuri after my screwed words... I hope it works..."
    show yuri 4c at f21 zorder 3
    y "..."
    y "I-I'll go make some tea..."
    show yuri at lhide
    hide yuri
    show sayori at f41 zorder 3
    "Oh shit... It didn't worked? I guess I'll comite suicide..."
    s 4h "Ehh?"
    s "I was just trying to help!"
    show sayori at t41 zorder 2
    mc "I...I'm sure she appreciated it, Sayori."
    "I pat Sayori on the shoulder."
    show sayori at thide zorder 1
    show natsuki at thide zorder 1
    show monika 4m at t11 zorder 2
    hide sayori
    hide natsuki
    m "Well, now that we're past that..."
    m 4b "Everyone's read each other's poems, right?"
    m "I hope that it was worthwhile for everyone!"
    m 5 "Especially you, [player]!"
    m "And to be honest..."
    m "It's a nice change of pace from the lazing around we got a little too used to."
    m "Ahahaha!"
    mc "Ah, so my joining the club was responsible for ruining the atmosphere..."
    "I knew it! And just SHE's telling me that!!!"
    "I strongly stamp my hand on a closer table."
    m 1d "No, not at all, not at all!"
    m "There's still time before we go home."
    m 1a "So we'll all relax for a bit."
    m "Of course, besides chatting, we do literature-related things in the clubroom..."
    m "So maybe you can take the chance to pick up a book, or do some writing."
    m 1b "After all, that's what the club is for!"
    "I rather go to the school's roof and throw myself to the empty."
    "Or better yet: go find Yuri and tell her how much I sorry for my fucking words."
    show sayori 2j at f31 zorder 3
    s "I disagree, Monika!"
    show sayori at t31 zorder 2
    show monika at f32 zorder 3
    m 1d "Eh? About what?"
    show monika at t32 zorder 2
    show sayori at f31 zorder 3
    s 2i "That's not the most important thing about the literature club!"
    s "The most important thing..."
    show sayori 4r at hf31 zorder 3
    s "Is having fun!"
    show sayori at t31 zorder 2
    show monika at f32 zorder 3
    m 2l "Ahaha, of course..."
    m 2a "Well, I guess that's why you're the Vice President, Sayori."
    show monika at t32 zorder 2
    show sayori at f31 zorder 3
    s 4q "Ehehe..."
    hide sayori
    hide monika
    with wipeleft
    "In the end, though, Monika's right."
    "Being in the Literature Club probably means I can't spend all my time doing nothing."
    "But in the end..."
    "...I guess it's been worth it so far."
    return

label ch1_end_sayori:
    $ ch1_choice = "sayori"
    mc "N-Natsuki..."
    show natsuki 5f
    "Natsuki glares at me, drying up any words I had in my mouth."
    "So instead, I turn to Yuri."
    mc "Yuri..."
    y 4a "..."
    "But Yuri's expression is so defenseless that I can't bring myself to say anything to her."
    stop music fadeout 1.0
    mc "..."
    mc "...Sayori!"
    show sayori 4m at l31 behind yuri
    show yuri at t32 zorder 2
    show natsuki at t33 zorder 2
    s "Eh?!"
    mc "...Yeah!"
    mc "Everyone's fighting is making Sayori uncomfortable."
    mc "How can the two of you keep fighting when you know you're making your friend feel like this?"
    show sayori at f31 zorder 3
    s 4d "[player]..."
    show sayori at t31 zorder 2
    show natsuki 4w at f33 zorder 3
    n "Well... That's her problem! This isn't about her."
    show natsuki at t33 zorder 2
    show yuri 2g at f32 zorder 3
    y "I-I agree..."
    y "It's unfair for others to interject their own feelings into our conflict."
    show yuri at t32 zorder 2
    show natsuki at f33 zorder 3
    n 4c "Yeah, unless Sayori wants to tell Yuri what a stuck-up jerk she's being."
    show natsuki at t33 zorder 2
    show yuri 3r at f32 zorder 3
    play music t7
    y "She would never...!"
    y "It's your immaturity that's made her upset in the first place!"
    show yuri at t32 zorder 2
    show natsuki 1e at f33 zorder 3
    n "{i}Excuse{/i} me?"
    n "Are you listening to yourself?"
    n 1x "This is exactly why..."
    n 1w "Exactly why nobody likes--"
    show natsuki at t33 zorder 2
    show sayori 4p at h31
    stop music
    s "{i}Stop!!{/i}"
    show yuri 3f at f32 zorder 3
    show natsuki 1o at f33 zorder 3
    ny "--"
    show yuri at t32 zorder 2
    show natsuki at t33 zorder 2
    show sayori at f31 zorder 3
    play music t8
    s 1h "Natsuki! Yuri!"
    s "You guys are my friends!"
    s 1v "I-I just want everyone to get along and be happy!"
    s "My friends are wonderful people..."
    s "And I love them because of their differences!"
    s 1g "Natsuki's poems..."
    s "They're amazing because they give you so many feelings with just a few words!"
    s "And Yuri's poems are amazing because they paint beautiful pictures in your head!"
    s 4k "Everyone's so talented..."
    s "...So why are we fighting...?"
    show sayori at t31 zorder 2
    show natsuki at f33 zorder 3
    n 1r "Be-Because..."
    show natsuki at t33 zorder 2
    show yuri 3v at f32 zorder 3
    y "Well..."
    show yuri at t32 zorder 2
    show sayori at f31 zorder 3
    s 1j "Also!"
    s "Natsuki's cute and there's nothing wrong with that!"
    s 1i "And Yuri's boobs are the same as they always were!"
    show sayori at hf31
    s 1j "Big and beautiful!!"
    show sayori 1i at t31 zorder 2
    show natsuki at f33 zorder 3
    n 1o "..."
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 3n "..."
    show yuri at t32 zorder 2
    mc "Sayori..."
    "Sayori stands triumphantly."
    "Monika stands behind her with a bewildered expression."
    show yuri at s32
    y 3q "I'll...make some tea..."
    show yuri at lhide behind sayori
    hide yuri
    "Yuri rushes off."
    show natsuki at thide zorder 1
    hide natsuki
    "Natsuki sits down with a blank expression on her face, staring at nothing."
    show sayori at thide zorder 1
    show monika 1i at t11 zorder 2
    hide sayori
    mc "So, this is why Sayori is Vice President..."
    "I whisper to Monika."
    "She nods in return."
    m 1d "To be honest..."
    m "I might come off as a good leader, and I can organize things..."
    m 3e "But I'm not very good with people..."
    m "I couldn't even bring myself to interject."
    m 1m "As President, that's kind of embarrassing of me."
    m 1l "Ahaha..."
    mc "I see... Well, It's not like I can blame you."
    mc "I wasn't able to say anything, either."
    m 2a "Hmm... I guess you did that because of Sayori, isn't?"
    m "You always acted like her 'Guardian angel' or something like that..."
    mc "You got a point."
    m "Well..."
    m 2a "I guess that just means Sayori is amazing in her own ways, isn't she?"
    mc "You could say that."
    mc "She might be an airhead, but sometimes it's weirdly suspicious that she knows exactly what she's doing."
    m 5 "I see~"
    m "Take good care of her, okay?"
    m "I would hate to see her get herself hurt."
    mc "That makes two of us..."
    mc "You can count on me."
    "Monika smiles sweetly at me, causing my stomach to knot."
    "Such a genuine person really does make a good President, regardless of what she says."
    "If only I could get the chance to talk to her a little more..."
    "In the end, though, Monika's right."
    "Being in the Literature Club probably means I can't spend all my time doing nothing."
    "But in the end..."
    "...I guess it's been worth it so far."
    return

label ch1_end_monika:
    $ ch1_choice = "monika"
    mc "Monika!"
    show monika 1d at l31 zorder 2
    show yuri at t43 zorder 2
    show natsuki at t44 zorder 2
    m "Eh?"
    mc "Do something now! Aren't you the President Club?"
    mc "How the fuck can you be the most popular girl in the school if you can't deal with two girls?"
    m 1o "[player]..."
    "I stare her with a defiant look while she's looking at me with an frustrating look."
    show monika 1h
    "Suddently, Monika's expression changed for an determinated one."
    m "..."
    show monika at f31 zorder 3
    m 1s "You are right!"
    m 2t "Listen everybody! Now!"
    stop music fadeout 1.0
    show yuri 2t at t32 zorder 2
    show natsuki 5c at t33 zorder 2
    ny "Eh?!"
    m "You two, stop fighting!"
    m 2s "This club was born to make a special place to talk about literature and make friends with everybody..."
    m 2n "Even with weebos..."
    show yuri 2w
    show natsuki 42
    "Was so neccessary looking at me when she said that? I feel insulted."
    m 2i "Not to brawl each other for some differences!"
    play music t8
    show sayori 4t at t41 zorder 1
    show monika at t42 zorder 2
    show yuri at t43 zorder 2
    show natsuki at t44 zorder 2
    s "Monika..."
    y "..."
    n "..."
    show monika at f42
    m 1h "Alright. Both of you must apologize to each other."
    m 1s "Now!"
    show monika at t42
    show yuri at s43
    y 4a "I..."
    show natsuki at s44
    n 5q "Hmm..."
    "..."
    "Seems like it works, after all, a girl like Monika is sign of respect in this school. It's easy for her to convince other people."
    "But I had to start to make her react, for some reason seems like she did not care about the situation."
    show natsuki 4c at t44
    stop music fadeout 1.0
    "However, Natsuki breaks the silence..."
    show natsuki at f44 zorder 3
    n "Well, if only Yuri stop beign a stuck-up jerk she's being."
    play music t7
    show sayori 1k
    show natsuki at t44 zorder 2
    show yuri 3r at f43 zorder 3
    y "Who are you calling jerk?"
    y "It's your immaturity that's made her upset in the first place!"
    show yuri at t43 zorder 2
    show natsuki 1e at f44 zorder 3
    n "{i}Excuse{/i} me?"
    n "Are you listening to yourself?"
    show monika 1q
    n 1x "This is exactly why..."
    "Ah shit, here we go again."
    show monika 1c zorder 3
    "I pat Monika on the back and point at them to convince her to stop them."
    show sayori 1u at s41
    "I can see Sayori beign sad about this situation, but it's Monika's responsability to make this club a non-toxic place."
    n 1w "Exactly why nobody likes--"
    show natsuki at t44 zorder 2
    stop music
    show monika at f42
    m 2t "{i}Okay, that's enough!!{/i}"
    show sayori 1v at h41
    show yuri 3f at f43 zorder 3
    show natsuki 1o at f44 zorder 3
    ny "--"
    show yuri at t43 zorder 2
    show natsuki at t44 zorder 2
    m "Natsuki, you should be more respectful to the opinions of others."
    m "Yuri is just trying to give you some advices."
    show yuri 4c at s43
    m "But she's so anti-social to say the correct words. You know?"
    show natsuki at f44 zorder 3
    n 1r "I..."
    show natsuki at t44 zorder 2
    m 2d "And Yuri..."
    show yuri at f43 zorder 3
    y 3v "..."
    m "Don't be so hostile to Natsuki's skills, she's still practicing her writing skills. Right Natsuki?"
    y "Um..."
    show yuri at t43 zorder 2
    show sayori 1t
    play music t8
    m 1b "Also. Both of you has talent for this." 
    m "I mean, Natsuki has the creativity to make special poems from her style."
    m 4b "And Yuri is already very talented with her writing emphasis, she could be very helpful in this club."
    "I stare at Sayori, she seems to start to be very happy with Monika's discourse."
    show monika 4a at t42 zorder 3
    show sayori at f41 zorder 3
    s 4t "Monika..."
    show sayori at t41 zorder 2
    show natsuki 1o
    show yuri 3n
    ny "..."
    show yuri at t43 zorder 2
    show natsuki at t44 zorder 2
    ny "Okay..."
    show monika 1a at t42
    "It's over? Thank goodness, it worked."
    show yuri at s43
    y 3q "I'll...make some tea..."
    show yuri at lhide behind sayori
    hide yuri
    "Yuri rushes off."
    show natsuki at thide zorder 1
    hide natsuki
    "Natsuki sits down with a blank expression on her face, staring at nothing."
    show sayori at f21 zorder 3
    show monika at t22
    s 4r "Didn't I told you [player]? That's why Monika is the best president ever!"
    show sayori at t21
    show monika 1n at f22
    m "Oh come on, Sayori! It was nothing..."
    m 2a "By the way, it was [player] who give me a little push."
    m 5 "He deserves some credit for that."
    show monika at t22
    "Me? Well, maybe yes, but I won't say anything about it. I don't want to be a show-off."
    show sayori 5 at f21
    s "You both make a nice couple. Maybe I should quit has Vice President and name [player] the new Vice President."
    show monika 1d
    s 5b "The Literature Club could be a better place if both of you are running it together."
    mc "S-S-Sayori...!!!"
    show sayori at t21
    "How dare she to say something so embarrasing?! Now I'm blushing so much that I look like a tomato!"
    #"If the \"School Elite\" hears it, they will hang me in the flagpole with my balls."
    show monika 2n at f22
    m "Uhuhuhu! Sayori you really are a funny girl..."
    show sayori 4s at f21
    show monika at t22
    s 4s "Hehehe! Thanks."
    show sayori at lhide zorder 1
    hide sayori
    "She lefts."
    show monika at t11
    m 1a "Well, she's not wrong after all."
    m "I mean, pushing me to stop Yuri and Natsuki fight is a hint that you have a \"determinated\" personality. Nobody will have the guts to do that with me."
    mc "But... Why didn't you stoped them yourself? I mean you're the \"most popular girl in the school\" and that means a lot of respect, they could listened to you very easy."
    m 1d "Yeah, but... To be honest..."
    m "I might come off as a good leader, and I can organize things..."
    m 3e "But I'm not very good with people..."
    m "I couldn't even bring myself to interject."
    m 1m "As President, that's kind of embarrassing of me."
    m 1l "Ahaha..."
    mc "I see... Well, It's not like I can blame you."
    mc "I wasn't able to say anything, either."
    m 2a "Hmm... I guess you did that because of Sayori, isn't?"
    m "You always acted like her 'Guardian angel' or something like that..."
    mc "You got a point."
    m 1a "Take good care of her, okay?"
    m "I would hate to see her get herself hurt."
    mc "That makes two of us..."
    mc "You can count on me."
    "Monika smiles sweetly at me, causing my stomach to knot."
    "Such a genuine person really does make a good President, regardless of what she says."
    "If only I could get the chance to talk to her a little more..."
    "In the end, though, Monika's right."
    "Being in the Literature Club probably means I can't spend all my time doing nothing."
    "But in the end..."
    "...I guess it's been worth it so far."
    return

label ch1_end_mc:
    $ ch1_choice = "mc"
    stop music
    show sayori 1g at l41 zorder 2
    show monika 1c at l42 zorder 2
    show yuri at t43 zorder 2
    show natsuki at t44 zorder 2
    mc "EVERYONE SHUT THE FUCK UP!!!!!"
    show sayori 1h at h41 zorder 2
    show monika 1d at h42 zorder 2
    show yuri 3p at h43 zorder 2
    show natsuki 1p at h44 zorder 2
    "Everyone stops and look at me with a surprised expression."
    mc "Don't you see that?! Your fighting bullshit is making Sayori sad!"
    mc "Just look at her face!!!"
    show sayori 1v at f41 zorder 2
    show monika 1i at f42 zorder 2
    show yuri 3t at f43 zorder 2
    show natsuki 4f at f44 zorder 2
    "Everyone" "[player]..."
    show sayori at t41
    show monika at t42
    show yuri at t43
    show natsuki at t44
    mc "Monika."
    mc "Isn't you supposed to be the President Club here?"
    mc "Why the fuck you're doing NOTHING?! WHY?!"
    show monika 2p at f42 zorder 3
    m "[player], stop it!"
    show monika at t42
    mc "Stop? Stop?!"
    show monika 2r
    mc "YOU must stop the riots here! YOU are a Club President, a {i}popular girl{/i}, not a fucking good for nothing like me!"
    show monika zorder 2
    show yuri 3n at h43 zorder 3
    show natsuki 1e at h44 zorder 3
    ny "[player]!"
    show yuri at t43 zorder 2
    show natsuki at t44 zorder 2
    show sayori 4w at f41 zorder 3
    s "[player], please stop!"
    "Is Sayori crying for MY FAULT???"
    "Fuck!"
    "I stare anger at Monika."
    show sayori 1u at t41 zorder 2
    show monika 1c at f42 zorder 3
    mc "Look!"
    mc "One thing that makes me so angry is seeing Sayori crying for a stupid shitty fight between her friends."
    mc "She knows that, I'm always pissed off when something or someone makes her sad!"
    show monika at t42 zorder 2
    "I'm looking at Sayori."
    show sayori at f41 zorder 3
    mc "Sayori... I'm so sorry."
    s 1v "Eh?"
    mc "I'm gonna try to fix this myself..."
    s 4t "[player]..."
    show sayori at t41 zorder 2
    play music t8
    show yuri at f43 zorder 3
    mc "Yuri..."
    y 4a "..."
    mc "No matter if someone dares to insult you with anything, you must ignore them."
    mc "Also, I must say... You have a {i}sexy body{/i}. {nw}"
    y 3n "[player]--!"
    "Oops! Did I really say that?"
    show yuri 3o
    mc "Listen, There's nothing wrong about that, okay?"
    show natsuki 5g
    mc "If Natsuki or somebody else complains about your body, tell me and I'm gonna solve it."
    show yuri 3f
    "I pat Yuri on the shoulder and wink her with a smile."
    y 3q "T-T-Thank you..."
    show yuri at t43 zorder 2
    show natsuki at f44 zorder 3
    mc "Natsuki..."
    n 5e "What?!"
    mc "You seriously have a problem, your aggresive personality drives you at a bully behavior in situations like that."
    mc "Yuri was trying to give you a friendly advice about your writing skills and..."
    n 1f "Shut up, jerk! What do you know about literature to say that?"
    mc "Calm down! I'm trying to say that your poems are okay. I mean, your poem was really inspirating no matter how simple was at first look."
    mc "You have potential, that's what I'm trying to say."
    n 5r "Well, you're right. But you know? You must say THAT to Yuri."
    show yuri 4c
    mc "Geez, okay I'mgonnasaythattoYuritoo..."
    mc "But one more thing about you:"
    show natsuki 5g
    mc "If somebody reviews your poems and give you an advice to enhance your skills, don't take that like an fucking insult please..."
    n 5w "Hmph! Whatever..."
    show natsuki at t44 zorder 2
    mc "Yuri..."
    show yuri at f43 zorder 3
    y 2t "Eh?!"
    mc "You should review Natsuki's stuffs less heavier, you already know how she reacts if you take the opposite."
    show natsuki 5k
    mc "Also, today's Natsuki poem was very interesting. Even for the simpliest way it was writed."
    mc "I might give her an opportunity... You should do that too."
    y 2u "... okay ..."
    show yuri at t43 zorder 2
    mc "Ah! Both of you, one more thing:"
    show yuri 1f at f43 zorder 3
    show natsuki 2c at f44 zorder 3
    ny "..."
    mc "Make peace between both of you, at least in front to Sayori, please..."
    show yuri at s43 zorder 2
    y 3t "Alright."
    show natsuki at s44 zorder 2
    n 42b "Okay fine..."
    show sayori at f41 zorder 3
    s 4t "[player]... Thank you very much! You're awesome!"
    show sayori 4s at h41
    "Sayori jumps on me in order to hug me strongly."
    mc "A-Ah.. It was nothing Sayori..."
    show sayori at t41 zorder 2
    show yuri at s43 zorder 3
    y 3q "I'll...make some tea..."
    show yuri at lhide behind sayori
    hide yuri
    "Yuri rushes off."
    show natsuki at thide zorder 1
    hide natsuki
    "Natsuki sits down with a blank expression on her face, staring at nothing."
    show sayori at t21
    show monika at f22 zorder 3
    m 2d "[player], I'm surprised, I never thought you have such strong personality to make peace and order on a group."
    m 2l "I guess I underestimated you all this time~! Hahahaha..."
    show monika at t22 zorder 2
    mc "Ahahahaha..."
    "I make a fake laugh, her \"joke\" wasn't funny, but I'm trying to sympathize with her too."
    mc "I... I guess you're right..."
    "I don't even know what I'm saying."
    "Suddently, I'm getting a lot of attention from Monika since I'm member. I'm getting scared."
    show sayori at f21 zorder 3
    s 3x "Have you see that Monika? I told you [player] is a awesome guy!"
    s "Even if the doesn't pretend it, he is a man with strong and determinated nature."
    show sayori at t21 zorder 2
    mc "Hehehe, yes. I guess..."
    show sayori at lhide zorder 1
    hide sayori
    "Sayori suddently lefts."
    show monika at t11
    m 2b "Well, I was about to ask about your aggresive attitude, but considering that the cause was Sayori becoming sad was enough answer."
    mc "Sorry about that Monika."
    m 1a "Don't worry."
    mc "By the way... There's something I don't understand. Why didn't you stoped them yourself?"
    show monika 1d
    mc "I mean you're the \"most popular girl in the school\" and that means a lot of respect, they could listened to you very easy."
    m "To be honest..."
    m "I might come off as a good leader, and I can organize things..."
    m 3e "But I'm not very good with people..."
    m "I couldn't even bring myself to interject."
    m 1m "As President, that's kind of embarrassing of me."
    m 1l "Ahaha..."
    mc "I see... Well, It's not like I can blame you."
    mc "I wasn't able to say anything good, either."
    mc "I'm only good at swearing for anything."
    m 2a "Hmm... You did all this because of Sayori, isn't?"
    m "You always acted like her 'Guardian angel' or something like that...?"
    m "And if she's sad, you're sad too, isn't?"
    mc "I guess you got a point."
    m "Well..."
    m 2a "I guess that just means Sayori is amazing in her own ways, isn't she?"
    mc "You could say that."
    mc "She might be an airhead, but sometimes it's weirdly suspicious that she knows exactly what she's doing."
    m 5 "I see~"
    m "Take good care of her, okay?"
    m "I would hate to see her get herself hurt."
    mc "That makes two of us..."
    mc "You can count on me."
    "Monika smiles sweetly at me, causing my stomach to knot."
    "Such a genuine person really does make a good President, regardless of what she says."
    "If only I could get the chance to talk to her a little more..."
    "In the end, though, Monika's right."
    "Being in the Literature Club probably means I can't spend all my time doing nothing."
    "But in the end..."
    "...I guess it's been worth it so far."

    return