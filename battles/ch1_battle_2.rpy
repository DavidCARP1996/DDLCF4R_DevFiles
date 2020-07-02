label ch1_battle_2:

    # Deshabilita el Skip y el sistema de Guardar/Cargar.

    $ _skipping = False
    $ save_load_system = False
    $ boss_battle = True
    $ no_death_battle = False

    # Define al rival.

    $ enemy = "Robber"
    $ enemy_lv = 5
    $ enemy_hp_max = 150
    $ enemy_hp = enemy_hp_max
    $ enemy_mp_max = 0
    $ enemy_mp = enemy_mp_max
    $ enemy_atk_base = 50
    $ enemy_def_base = 9
    $ enemy_spd_base = 10
    $ enemy_mat_base = 0
    $ enemy_mdf_base = 0

    $ enemy_atk = enemy_atk_base
    $ enemy_def = enemy_def_base
    $ enemy_spd = enemy_spd_base
    $ enemy_mat = enemy_mat_base
    $ enemy_mdf = enemy_mdf_base

    $ enemy_current_weapon = "9mm Pistol"

    # Comienza el dialogo

    "I'm gonna chase him silently. Let's go!"
    pause 1.0
    show screen stats
    with dissolve
    play music demobattle
    show robber at t11 zorder 2
    mc "I got you!"
    $ enemy_hp -= (25 * enemy_hp_max) / 100
    "Robber" "Aah!"
    $ timeout = 1.0

    while (enemy_hp > 0) or (timeout == 0.0):
        $ timeout_label = "ch1_battle_2_B"
        menu:
            "Attack him!":
                $ timeout -= 0.13
                #$ timeout_label = None
                play sound "sfx/slap.ogg"
                call atk_regular
                #mc "Phew! That was close...!"

    jump ch1_battle_2_A

    label ch1_battle_2_A:
        $ timeout = 0.2
        $ timeout_label = None
        mc "Take!{w} That!{w} Mother!{w} Fucker!"
        "..."
        jump ch1_battle_2_end

    label ch1_battle_2_B:
        $ timeout = 5.0
        $ timeout_label = None
        $ mc_hp -= (25 * mc_hp_max) / 100
        call mc_pain4
        mc "Aaaahhh!!!"
        mcf1 "You're dead man!"
        mc "Fuck... you!"
        pass

    show screen stats
    with dissolve

    # Aquí comienza la pelea.

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
            "Robber" "What the...?!"
            mc "I... Won't... Give... Up!"

    #
    ####        
        
label ch1_battle_2_end:

    $ boss_battle = False
    $ ch1_battle_2_victory = False
    
    $ exp_earned = mc_lv * 70
    $ money_earned = 100
    if enemy_hp <= 0:
        hide robber
        with Dissolve(.5)
        $ total_npc_defeated += 1
        $ ch1_battle_2_victory = True
    
    call battle_results

    hide screen stats
    with Dissolve(.5)
    $ _skipping = True
    $ save_load_system = True
    $ enemy_hp = enemy_hp_max
    hide screen levelup_stats_hud
    hide screen battle_hud
    stop music fadeout 1