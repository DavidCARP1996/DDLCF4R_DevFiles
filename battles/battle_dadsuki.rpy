label battle_dadsuki:

    # Deshabilita el Skip y el sistema de Guardar/Cargar.

    $ _skipping = False
    $ save_load_system = False
    hide screen freeroam_hud
    $ boss_battle = True

    # Define al rival.

    image enemy = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/m.png")
    define enemy = DynamicCharacter('nd_name', image='natsukidad', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

    $ enemy = "Natsuki's Dad"
    $ enemy_lvl = 1
    $ enemy_hp_max = 100
    $ enemy_hp = enemy_hp_max
    $ enemy_mp_max = 1
    $ enemy_mp = enemy_mp_max
    $ enemy_atk_base = 4
    $ enemy_def_base = 7
    $ enemy_spd_base = 5
    $ enemy_mat_base = 2
    $ enemy_mdf_base = 2

    $ enemy_lvl = enemy_lvl * choosen_lvl
    $ enemy_hp_max = enemy_hp_max * enemy_lvl
    $ enemy_hp = enemy_hp_max
    $ enemy_mp_max = enemy_mp_max * enemy_lvl
    $ enemy_mp = enemy_mp_max
    $ enemy_atk_base = enemy_atk_base * enemy_lvl
    $ enemy_def_base = enemy_def_base * enemy_lvl
    $ enemy_spd_base = enemy_spd_base * enemy_lvl
    $ enemy_mat_base = enemy_mat_base * enemy_lvl
    $ enemy_mdf_base = enemy_mdf_base * enemy_lvl

    $ enemy_atk = enemy_atk_base
    $ enemy_def = enemy_def_base
    $ enemy_spd = enemy_spd_base
    $ enemy_mat = enemy_mat_base
    $ enemy_mdf = enemy_mdf_base

    # Comienza el dialogo

    stop music fadeout 2.0

    scene bg natsuki hallway
    with wipeleft_scene

    mc "Muy bien... ¿Dónde estás, maldito?"
    nd "¡¿Quién anda ahí?!"
    "Su voz se escuchó del piso de arriba, iré a revisar."
    scene bg natsuki bedroom
    with wipeleft_scene
    mc "¡¿Dónde...{nw}"
    play sound slap
    show noise onlayer front:
        alpha 0.1
        easeout 0.1 alpha 0
    "!"
    show natsukidad 1b at t11 zorder 2
    nd "¿Me buscabas?"
    mc "Hijo de re mil p{nw}"
    play music final_battle
    play sound slap
    show noise onlayer front:
        alpha 0.1
        easeout 0.1 alpha 0
    mc "¡Vas a pagar por lo que le has hecho a Natsuki!"
    nd 3a "¿Natsuki? Ja, ella desobedeció mis órdenes por enésima vez, ya era hora de darle un correctivo adecuado a ver si se le pasa."
    mc "¡¿Y por qué tuviste que pegarle tan bruscamente?!"
    mc "Esta será la última vez que le harás daño..."
    nd 4m "¡¿Quieres pelea, maldito pendejo?!"
    mc "¡Me he enfrentado a tipos peores que tú, no te tengo miedo!"

    hide natsukidad 
    show enemy at i11 zorder 2
    pause 2.0

    show screen stats
    with dissolve
    

    # Aquí comienza la pelea.

    while (mc_hp > 0) and (enemy_hp > 0):

        $ mc_evasion_rate = renpy.random.randint(1, 100)
        $ mc_critical_rate = renpy.random.randint(1, 100)
        $ enemy_critical_rate = renpy.random.randint(1, 100)

        if mc_spd > enemy_spd:
            call Hud
            if enemy_hp > 0:
                call enemy_turn
            else:
                pass
        else:
            call enemy_turn
            if mc_hp > 0:
                call Hud
            else:
                pass

        if mc_hp <= 0 and mc_mp >= 150:
            $ timeout = 1.0
            $ timeout_label = "battle_dadsuki_end"
            menu:
                mc "Shit! I'm dying...!"
                "CURE YOURSELF":
                    $ timeout = 5.0
                    $ timeout_label = None
                    call mgc_cure
                    mc "Phew! That was close...!"

    #
    ####        
       
label battle_dadsuki_end:

    $ boss_battle = False
    
    $ exp_earned = mc_lv * 50
    $ money_earned = 500
    
    call battle_results

    hide screen stats
    with Dissolve(.5)
    $ _skipping = True
    $ save_load_system = True
    $ enemy_hp = enemy_hp_max
    hide screen levelup_stats_hud
    hide screen battle_hud
    stop music fadeout 1