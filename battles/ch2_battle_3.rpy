label ch2_battle_3:

    # Deshabilita el Skip y el sistema de Guardar/Cargar.

    $ _skipping = False
    $ save_load_system = False
    $ boss_battle = True
    $ no_death_battle = True

    # Define al rival.

    $ enemy = "Ryoma"
    $ enemy_lv = 7
    $ enemy_hp_max = 200
    $ enemy_hp = enemy_hp_max
    $ enemy_mp_max = 0
    $ enemy_mp = enemy_mp_max
    $ enemy_atk_base = 12
    $ enemy_def_base = 12
    $ enemy_spd_base = 17
    $ enemy_mat_base = 0
    $ enemy_mdf_base = 0

    $ enemy_atk = enemy_atk_base
    $ enemy_def = enemy_def_base
    $ enemy_spd = enemy_spd_base
    $ enemy_mat = enemy_mat_base
    $ enemy_mdf = enemy_mdf_base

    $ enemy_current_weapon = None

    # Comienza el dialogo

    pause 1.0
    show screen stats
    with dissolve
    play music demobattle
    mcf1 "Let's start with a first strike, prepare your reflexes!"
    mc "Okay!"
    $ timeout = 0.2

    $ timeout_label = "ch2_battle_3_B"
    menu:
        "Attack him!":
            jump ch2_battle_3_A
            pass
            #$ timeout -= 0.2

    jump ch2_battle_3_A

    label ch2_battle_3_A:
        $ timeout = 5.0
        $ timeout_label = None
        $ enemy_hp -= (25 * enemy_hp_max) / 100
        mcf1 "-!"
        mc "Are you okay?"
        mcf1 "Yes, it's fine... Let's go!"
        jump ch2_battle_3_C

    label ch2_battle_3_B:
        $ timeout = 5.0
        $ timeout_label = None
        $ mc_hp -= (25 * mc_hp_max) / 100
        call mc_pain1
        mc "Ah-!"
        mcf1 "Are you okay?"
        mc "Yes, it's fine... Let's go!"
        jump ch2_battle_3_C

    show screen stats
    with dissolve

    # Aquí comienza la pelea.
label ch2_battle_3_C:
    while (mc_hp > 0) and (enemy_hp > 0):

        $ battle_extra_rewards_rate = renpy.random.randint(1, 100)
        $ mc_evasion_rate = renpy.random.randint(1, 100)
        $ mc_miracle_rate = renpy.random.randint(1, 100)
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

        if mc_hp <= 0 and mc_miracle_rate <= 5:
            $ mc_hp = 1
            mcf1 "What the...?!"
            mc "Impressed? I won't dare to fall so easy!"
            mcf1 "Well said! Now let's keep going!"

    #
    ####        
        
label ch2_battle_3_end:

    $ boss_battle = False
    $ ch2_battle_3_victory = False
    
    $ exp_earned = mc_lv * 75
    $ money_earned = 100
    if enemy_hp <= 0:
        hide ryoma
        with Dissolve(.5)
        $ total_npc_defeated += 1
        $ ch2_battle_3_victory = True
    
    call battle_results

    hide screen stats
    with Dissolve(.5)
    $ _skipping = True
    $ save_load_system = True
    $ enemy_hp = enemy_hp_max
    hide screen levelup_stats_hud
    hide screen battle_hud
    stop music fadeout 1