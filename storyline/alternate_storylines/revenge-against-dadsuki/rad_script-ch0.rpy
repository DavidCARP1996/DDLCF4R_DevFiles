label rad_ch0_main:

    $ choosen_lvl = 1
    $ difficult_mode = None

    if persistent.rad_finished == True:

        menu:
            "Por favor selecciona el nivel de dificultad."

            "Fácil":
                $ choosen_lvl = mc_lv * 0.5
                $ difficult_mode = 1
                $ item_cinambun = 5
                pass
            "Normal":
                $ choosen_lvl = mc_lv * 1
                $ difficult_mode = 2
                $ item_cookie = 3
                pass
            "Dificil":
                $ choosen_lvl = mc_lv * 1.5
                $ difficult_mode = 3
                pass

        menu:
            "¿Quieres ver la introducción?"

            "Si":
                play sound select_echo
                pass
            "No":
                play sound select_echo
                call battle_dadsuki
                call rad_ending
                call mc_stats_cache
                $ MainMenu(confirm=False)()
                return
    
    else:
        play sound select_echo
        pass

    stop music fadeout 2.0
    with dissolve_scene_full
    
    "Un día antes..."
    $ weekend_winner = renpy.random.choice(['Yuri', 'Natsuki'])
    "Después de que [player] recibiera la visita de [weekend_winner], Sayori entre lágrimas le confiesa su amor."
    "[player] sin dudarlo, acepta la confesión."
    "Acto seguido [player] le ofrece pasar la noche en su casa, para tratar de al menos quitarle algo de la depresión con algo de compañia."
    "Al día siguiente (hoy), después de una 'noche soñada', Sayori despierta de buen ánimo."
    if weekend_winner == "Yuri":
        "Sayori ayuda a [player] a llevar el banner que deben presentar en el Festival. Enrollándolo y cargarlo entre ambos camino a la escuela."
        pass
    else:
        "Sayori ayuda a [player] a llevar el tupper con los cupcakes para el Festival. Al ser tan sólo dos tuppers, cada uno lleva uno."
        pass
    "Y entonces..."
    scene black
    with dissolve_scene_half
    pause(2.0)

    scene bg club_day
    with wipeleft
    play music t3
    show sayori 4r at l41
    s "¡Hola a todooos~!"
    "Sayori saluda al resto de los miembros del club con mucha positividad."
    show monika 1c at t33 zorder 2
    show yuri 3c at t32 zorder 2
    "Hago lo mismo... Yuri parece estar mejor animada con mi presencia mientras que Monika..."
    "Oye... ¿Y dónde está  Natsuki?"
    y 1b "Hola [player], hola Sayori. Me alegra verlos."
    m "Si... yo también..."
    "Monika hace una sonrisa a lo Hide the pain Harold con sólo ver a Sayori. ¿Qué pretende con esto?"
    show yuri 3b
    mc "¡Yuri~!"
    show yuri 3d
    "La abrazo y beso de una forma muy cariñosa. Se ve incómoda, pero a la vez reconfortada."
    mc "Monika..."
    "Nos damos un saludo regular. Ella no parece entusiasmada por un beso y abrazo cómo Yuri..."
    show monika 1d
    mc "Oigan..."
    show yuri 1e
    mc "¿Qué pasó con Natsuki? ¿Dónde está?"
    y 1t "Ni idea."
    y 3w "Ya intentamos comunicarnos con ella, pero no ha contestado ni una llamada, ni siquiera leyó los mensajes."
    m 1l "Capaz está ocupada con un asunto familiar. Debería de resolverlo pronto."
    m "En caso contrario, empezaremos el Festival sin ella."
    show monika 1i
    mc "Monika..."
    mc "¿Cómo vas a decir algo así? Ella es nuestra amiga."
    m 1d "¿Y qué sugieres? ¿Eh? Si la vamos a buscar vamos a perder tiempo y de paso estropearemos todo el esfuerzo que hicimos para organizar esto."
    m 1c "Asíque olvídalo. Empezaremos con o sin...{nw}"
    stop music fadeout 2.0
    show yuri 3n
    s 4m "¡Natsuki!"
    "Sayori grita el nombre de Natsuki de una forma horrorizada."
    "¿Qué carajos pasó...?{nw}"
    play music descent
    show monika 1g at t44 zorder 2
    show yuri 3p at t43 zorder 2
    show natsuki nb211 at t42 zorder 2
    "¡A la mierda!"
    show sayori 1e
    mc "¡Natsuki! ¿Pero que te pasó?"
    "Yuri & Moni" "¡Natsuki!"
    n nb311 "... ... ..."
    show yuri 3t
    s "Natsuki, por favor, cuéntanos. Queremos ayudarte..."
    y "Sayori tiene razón. Por favor, cuéntanos quién te hizo esto, o que pasó..."
    show monika 1p
    n "M-m-m-m..."
    "¿...?"
    n nb411 "Mi-mi papá..."
    show sayori 4m
    show monika 1g
    show yuri 3n
    mc "¡No!"
    mc "¡No me digas que él te..."
    "Natsuki asiente la cabeza a modo de afirmación."
    show yuri 3n
    "La re puta madre... ¿Puede un padre ser tan bestia contra su hija?"
    "Cierro mis puños de la bronca al ver a Natsuki en ese estado."
    s 4k "Natsuki, cómete esta galleta, te hará mejor."
    show natsuki nb311
    mc "Sayori, creo que Natsuki no podrá aceptar esa galleta."
    s 4g "¿Qué? ¿Por qué?"
    y 3v "Mira su boca. Se ve que ese desgraciado también re rompió la boca..."
    mc "Es verdad Sayori. Mejor tráele agua mineral y pide ayuda médica. Creo que esto va a requerir una visita al hospital."
    s 4f "O-okay..."
    show natsuki nb411 at t31 zorder 2
    show monika 1o at t33 zorder 2
    show yuri at t32 zorder 2
    show sayori at lhide
    hide sayori
    "Sayori corre en busca de agua y auxilio. Si no encuentra a la enfermera espero que traiga un botiquín para que Yuri trate sus heridas por lo menos."
    "... ... ..."
    show monika 1h 
    show yuri 3f
    mc "¡Carajo!"
    m 1d "¿Y ahora que?"
    mc "No... No puedo dejar que..."
    "Empiezo a levantar mis brazos con los puños bien cerrados, mi expresión de rabia ya no se puede ocultar. Es cómo si tratara de convertirme en Super Saiyajin o algo parecido."
    m 1h "No hay tiempo para eso [player]. Sin Natsuki y sin tí no podremos empezar el festival..."
    show monika 1o
    show natsuki nb311
    mc "¡A la mierda el Festival!"
    mc "¡Ese malparido debe pagar por esto!"
    mc "¡No me voy a quedar de brazos cruzados! ¡No puedo ver a Natsuki en ese estado mientras el desgraciado que le hizo esto disfruta de la vida!"
    show natsuki nb111
    m 1p "Que ni se te ocurra..."
    y 3p "¡Pero [player], podría ser peligroso! No sabemos que te podría hacerte a tí también..."
    mc "No me importa, intentaré romperle la cabeza aunque el sujeto esté armado. ¡Pero procuraré que pague por lo que le hizo a Natsuki!"
    mc "Yuri, hazme el favor..."
    show yuri 3t
    mc "Permanece cerca de Natsuki en todo momento. Si Sayori trae un botiquín de primeros auxilios en vez de la enfermera, ya sabrás por dónde empezar."
    show natsuki nb311
    y 3w "[player]..."
    m 1i "¡[player]!"
    mc "Monika... Infórmale al director sobre esto. Si algo me pasa a mí, mínimo las autoridades harán algo al respecto."
    show monika 1r
    mc "¡Voy yendo!"
    m "Muy bien... Haz lo que quieras..."

    scene bg corridor
    with wipeleft_scene

    show sayori 4h at t11 zorder 2
    s "¡[player]! ¿A dónde vas?"
    mc "Voy a arreglar un asunto con el papá de Natsuki..."
    show sayori 4g
    mc "¡Excelente! Trajiste a la enfermera y un botiquín. ¡Gracias Sayori! Ellos sabrán que hacer."
    mc "¡Nos vemos más tarde!"
    s 4p "¡¡¡[player]!!!"
    stop music fadeout 2.0

    scene black
    with wipeleft_scene

    pause 5.0

    scene bg natsuki house
    with wipeleft_scene

    mc "¡Finalmente...!"
    "Entraré por la fuerza. No me importa nada."

    scene black
    with Dissolve(.5)

    pause 3.0

    call battle_dadsuki


    return

label rad_ending:

    mc "... ... ..."
    mc "Supongo... que se acabó..."
    "Fue duro de pelear, pero logré darle la paliza que merecía."
    "Si les soy sincero, estoy exausto..."
    nd "Mal-maldito..."
    mc "!"
    play music fororiginz
    show natsukidad 1gb at t11 zorder 2
    nd "¿Qué clase de bestia eres?"
    nd 1ib "¿Qué buscas ganar con esto?"
    mc "Sólo... quiero que no vuelvas a hacerle daño a Natsuki... es todo..."
    nd 1mb "¿Acaso eres su padre? No tienes la menor idea de que se trata todo esto."
    mc "No, pero se que para ciertas cosas hay límites."
    mc "¡La paliza que le diste a Natsuki no tiene justificación!"
    nd 1lb "Idiota..."
    mc "¡¿Qué dijiste?!"
    play sound slap
    show natsukidad 1jb
    mc "¡Eres un...!"
    "Busco un instrumento para golpear brutalmente."
    "..."
    "Encontraste Palo de escoba."
    show natsukidad 1kb
    "Le retiro la escobilla para que funcione cómo un palo regular."
    play sound slap
    nd 1pb "¡¡¡AAAAAAAHHH!!!"
    play sound slap
    mc "¡¡¡Esto por decirme idiota!!!"
    play sound slap
    mc "¡¡¡Y esto por agredir a Natsuki!!!"
    show natsukidad 1ub
    mc "..."
    "Creo que con un golpe más lo mato..."
    stop music fadeout 2.0
    menu:
        "¿Qué dicen?"

        "¡Si, hazlo!":
            mc "..."
            nd 1qb "..."
            mc "..."
            show natsukidad 1vb
            mc "HAAAAAAAAAAAAAAAAAAAAAAAAAAAA-!!!"
            play sound slap

            play sound defeated_boss
            hide natsukidad with Dissolve(1.0)
            "El padre de Natsuki...{w} Ha muerto..."
            mc "*suspiros fuertes*"
            mc "¡Al fin...!"
            mc "..."
            mc "Sólo espero...{w} que Natsuki no se lo tome a mal..."
            mc "..."
            mc "Voy a avisarle a Yuri..."
            menu:
                "Le escribo un mensaje de texto avisandole que..."

                "Maté al padre de Natsuki":
                    "..."
                    "La respuesta que recibí no es muy buena que digamos."
                    "¿En serio la cagué con esta decisión?"
                    "Pregunto cómo va todo..."
                    "..."
                    "¡Carajo!"
                    "¡¿Monika piensa denunciarme por homicidio?!"
                    "¡¿Sayori no quiere volver a hablarme?!"
                    "¡¿Natsuki está furiosa?!"
                    "¡¿Yuri me tiene miedo?!"
                    "..."
                    mc "¡¡¡LA REPUTA MADRE!!!"
                    "Arrojo el palo con bronca hacia el cadaver."
                    mc "¡¡¡Intenté solucionar esto pero empeoré todo aún más!!!"
                    mc "¡¿En qué estaba pensando?!"
                    "..."
                    mc "¡Se acabó, todo!"
                    mc "Sólo me queda...{w} Darme a la fuga..."
                    mc "Adiós Sayori."
                    mc "Adiós Yuri."
                    mc "Adiós Natsuki."
                    mc "Adiós Monik... ¡No tú vete a la mierda por alcahueta!"
                    mc "Adiós Club de Literatura."
                    "*Inserte música de vaquero que se aleja por el horizonte*"
                    "{cps=30}  G A M E   O V E R{/cps}"
                    pass
                "Murió en la pelea pero fue un accidente":
                    "..."
                    "Parece que todos quedaron consternados."
                    "¿Se creerán lo del accidente? ¿Cómo se lo habrán tomado?"
                    "Pregunto cómo va todo..."
                    "..."
                    "Monika no se lo cree...{w} ¡¿Y piensa denunciarme?!"
                    "Sayori cree que fue un accidente, pero está más preocupada por mi estado..."
                    "Natsuki se puso a llorar. No sabemos con exactitud qué piensa..."
                    "Yuri quiere creer que fue un accidente, que está segura que yo jamás haría semejante daño..."
                    "..."
                    mc "Ahora sólo me queda una opción:"
                    mc "Inventarme un argumento en el camino a la escuela, así logro convencerlas de que todo fue un accidente y que mi intención jamás fue matar al papá de Natsuki."
                    mc "Y de paso evitar que Monika haga esa denuncia."
                    mc "¿Será tan hija de puta cómo para hacer algo así?"
                    mc "¿O acaso ella...?{nw}"
                    $ gtext = glitchtext(100)
                    mc "[gtext]"
                    "{cps=30}  G A M E   O V E R{/cps}"
                    pass
                "Ya estaba muerto cuándo llegué":
                    "..."
                    "Hay muchas dudas..."
                    "¿Se creerán eso de que yo no hice nada? ¿Cómo se lo habrán tomado?"
                    "Pregunto cómo va todo..."
                    "..."
                    "Monika no se lo cree...{w} ¡¿Y piensa denunciarme?!"
                    "Sayori piensa que es cierto, y se siente tranquila..."
                    "Natsuki quedó shockeada. Creo que tardaremos en saber qué piensa sobre esto..."
                    "Yuri quiere creerme, y me ruega salir del lugar por si las dudas..."
                    "..."
                    mc "Ahora sólo me queda una opción:"
                    mc "Inventarme un argumento en el camino a la escuela, así logro convencerlas de que no fui yo quién hizo esto."
                    mc "Aunque... {w}¿No me habrán quedado huellas dactilares mías?"
                    "Miro el palo con el que ejecuté al padre de Natsuki."
                    mc "¡Carajos!"
                    "Arrojo el palo a un rincón."
                    mc "Para colmo Monika quiere denunciarme de todos modos."
                    mc "¿Será tan hija de puta cómo para hacer algo así?"
                    mc "¿O acaso ella...?{nw}"
                    $ gtext = glitchtext(100)
                    mc "[gtext]"
                    "{cps=30}  G A M E   O V E R{/cps}"
                    pass

            
            pass
        "¡No! ¿Qué pensaría Natsuki y las demás?":
            mc "..."
            nd "..."
            mc "..."
            mc "¡NO!"
            show natsukidad 1qb
            "Arrojo el palo a un rincón."
            play music forfallen
            mc "¡No voy a rebajarme a ser algo cómo tú!"
            mc "Natsuki no querría esto..."
            nd 1rb "¿Qué...?"
            mc "Tal vez no lo sepas, pero a pesar de todo ella igual te ama."
            mc "Yo no vine a matarte, sólo quería devolverte lo que le hiciste a ella."
            mc "Pue-puede que me haya propasado un poco... pero, yo suelo actuar así con la sangre hirviendo..."
            mc "Lo siento..."
            nd "¿No vas a matarme?"
            mc "No."
            show natsukidad 1qb
            pause 1.0
            "Salgo hasta la puerta del dormitorio."
            pause 2.0
            mc "Por cierto..."
            mc "Si me denuncias por esto, yo te denunciaré por maltrato familiar. Tengo a compañeros y directivos de la escuela cómo testigos de lo que le hiciste a Natsuki."
            mc "Píensalo dos veces."
            "..."
            "{cps=30}  G A M E   O V E R{/cps}"

            pass

    $ persistent.clearall = True
    jump credits

    return