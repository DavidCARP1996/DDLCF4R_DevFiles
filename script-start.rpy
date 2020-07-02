label start_fighting_for_reality:

    play sound select_echo
    $ dokisaved = persistent.dokisaved

    if persistent.playthrough == 0: # Sayori act (save Sayori)
        $ s_name = "???"
        $ m_name = "???"
        $ n_name = "Girl 2"
        $ y_name = "Girl 1"

        $ chapter = 0
        
        call ch0_prev   # Madrugada 1, prólogo
        call ch0_main   # Escuela 1, conociendo el club
        call ch0_post   # Después de la escuela 1

        call poem
        
        $ chapter = 1

        call ch1_prev   # Madrugada 2
        call ch1_main   # Escuela 2, 1er dia de poemas
        call poemresponse_start
        call ch1_main_end
        call ch1_post   # Despues de la escuela 2

        call poem
        
        $ chapter = 2

        call ch2_prev   # Madrugada 3
        call ch2_main   # Escuela 3, 2do dia de poemas
        call poemresponse_start
        call ch2_main_end
        call ch2_post   # Después de la escuela 3

        call poem
        
        $ chapter = 3

#        call ch3_prev   # Madrugada 4
        call ch3_main   # Escuela 4, 3er dia de poemas
        call poemresponse_start
        call ch3_main_end
#        call ch3_post   # Después de la escuela 4
        
        $ chapter = 4

#        call ch4_prev   # Madrugada 5, fin de semana
        call ch4_main   # Fin de semana, visita Yuri/Natsuki
        call ch4_post   # Fin de semana, una última cosa que hacer

        python:
            try: renpy.file(config.basedir + "/hxppy thxughts.png")
            except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
        
        $ chapter = 5
        call ch5_prev   # BOSS BATTLE, ¡salva a Sayori!
        #call ch5_main   # Fin del Acto 1, dia del Festival
        $ persistent.autoload = None
        $ nextchapter = "ch5_" + dokisaved + "_main"     # Fin del acto 1, dia del festival
        call expression nextchapter
        
        #$ persistent.playthrough = 1
        call mc_stats_cache

        return

    elif persistent.playthrough == 1: # Yuri act (save Yuri)
        $ chapter = 0
        
        $ nextchapter = "ch10_" + dokisaved + "_prev"     # Madrugada 1
        call expression nextchapter
        $ nextchapter = "ch10_" + dokisaved + "_main"        # Este es el mismo sistema usado para definir los call de los resultados del poemgame...
        call expression nextchapter                            # ...los capítulos están divididos dependiendo las Dokis salvadas, esto ahorra muchos if/elif para llamar el capítulo correspondiente.
        $ nextchapter = "ch10_" + dokisaved + "_post"     # Despues de la escuela 1
        call expression nextchapter

        call poem
        python:
            try: renpy.file(config.basedir + "/CAN YOU HEAR ME.txt")
            except: open(config.basedir + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())

        $ chapter = 1

        $ nextchapter = "ch11_" + dokisaved + "_prev"     # Madrugada 2
        call expression nextchapter
        $ nextchapter = "ch11_" + dokisaved + "_main"     # Escuela 2, 1er dia de poemas
        call expression nextchapter
        call poemresponse_start
        $ nextchapter = "ch11_" + dokisaved + "_main_end"
        call expression nextchapter
        $ nextchapter = "ch11_" + dokisaved + "_post"     # Despues de la escuela 2
        call expression nextchapter

        call poem (False)
        python:
            try: renpy.file(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
            except: open(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())

        $ chapter = 2

        $ nextchapter = "ch12_" + dokisaved + "_prev"     # Madrugada 3
        call expression nextchapter
        $ nextchapter = "ch12_" + dokisaved + "_main"     # Escuela 3, 2do dia de poemas
        call expression nextchapter
        call poemresponse_start
        $ nextchapter = "ch12_" + dokisaved + "_main_end"
        call expression nextchapter
        $ nextchapter = "ch12_" + dokisaved + "_post"     # Despues de la escuela 3
        call expression nextchapter

        call poem (False)

        $ chapter = 3

        $ nextchapter = "ch13_" + dokisaved + "_prev"     # Madrugada 4
        call expression nextchapter
        $ nextchapter = "ch13_" + dokisaved + "_main"     # Escuela 4, 3er dia de poemas
        call expression nextchapter
        if y_appeal >= 3:
            call poemresponse_start2
        else:
            call poemresponse_start
        $ nextchapter = "ch13_" + dokisaved + "_main_end"     # BOSS BATTLE ¡salva a Yuri!
        call expression nextchapter
        if in_yuri_kill == False:
            $ nextchapter = "ch13_" + dokisaved + "_post"     # Despues de la escuela 4 (si es que salvaste a Yuri)
            call expression nextchapter
        else:
            $ nextchapter = "ch13_" + dokisaved + "_post"     # Despues de la escuela 4 (si perdiste a Yuri + Game Over)
            call expression nextchapter
            $ persistent.playthrough = 2
            call mc_stats_cache
            jump gameover

        $ chapter = 4
        $ nextchapter = "ch14_" + dokisaved + "_prev"     # Madrugada 5, fin de semana
        call expression nextchapter
        $ nextchapter = "ch14_" + dokisaved + "_main"     # Fin de semana, cita con Yuri
        call expression nextchapter
        $ nextchapter = "ch14_" + dokisaved + "_post"     # Fin de semana, una última cosa que hacer
        call expression nextchapter

        $ chapter = 5
        $ nextchapter = "ch15_" + dokisaved + "_prev"     # Madrugada 6
        call expression nextchapter
        $ nextchapter = "ch15_" + dokisaved + "_main"     # Fin del acto 2, dia del festival
        call expression nextchapter

        $ persistent.playthrough = 2
        call mc_stats_cache

        return

    elif persistent.playthrough == 2: # Natsuki act (save Natsuki)
        $ chapter = 0

        $ nextchapter = "ch20_" + dokisaved + "_main"
        call expression nextchapter

        $ persistent.playthrough = 3
        call mc_stats_cache

        return

    elif persistent.playthrough == 3: # Save Monika?
        $ chapter = 0

        $ nextchapter = "ch30_" + dokisaved + "_main"
        call expression nextchapter

        $ persistent.playthrough = "LETSFINISHTHIS"
        call mc_stats_cache

        return

    elif persistent.playthrough == "LETSFINISHTHIS": # Fight Monika!
        $ nextchapter = "chXX_" + dokisaved + "_main"
        call expression nextchapter

        $ persistent.playthrough = "LETSFINISHTHIS"
        call mc_stats_cache

        return

    elif persistent.playthrough == "X": # Just RedMC
        jump chX_X_main

    elif persistent.playthrough == "JUSTMONIKA": # Just Monika
        jump chX_JustMonika_main

    elif persistent.playthrough == 4: # You got it!
        $ chapter = 0

        $ nextchapter = "ch40_" + dokisaved + "_main"
        call expression nextchapter

        if in_mc_kill == False:
            $ persistent.playthrough = 5
            call mc_stats_cache
        else:
            jump credits

        return

    elif persistent.playthrough == 5: # Enjoy!
        $ chapter = 0

        $ nextchapter = "ch50_" + doki_choose + "_main"
        call expression nextchapter

        $ persistent.playthrough = 6
        call mc_stats_cache

        return

    elif persistent.playthrough == 6: # The End
        $ nextchapter = "chEnd_" + doki_choose + "_main"
        call expression nextchapter
        
        jump credits