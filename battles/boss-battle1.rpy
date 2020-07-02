label boss_battle1:

    # Deshabilita el Skip y el sistema de Guardar/Cargar.

    $ _skipping = False
    $ save_load_system = False
    $ boss_battle = True
    $ no_death_battle = True
    $ battle_extra_rewards_rate = renpy.random.randint(1, 100)

    # Define al rival.

    $ enemy = "Monika?"
    $ enemy_lv = "??"
    $ enemy_hp_max = 500
    $ enemy_hp = enemy_hp_max
    $ enemy_mp_max = 0
    $ enemy_mp = enemy_mp_max
    $ enemy_atk_base = 15
    $ enemy_def_base = 20
    $ enemy_spd_base = 18
    $ enemy_mat_base = 10
    $ enemy_mdf_base = 15

    $ enemy_atk = enemy_atk_base
    $ enemy_def = enemy_def_base
    $ enemy_spd = enemy_spd_base
    $ enemy_mat = enemy_mat_base
    $ enemy_mdf = enemy_mdf_base

    $ enemy_current_weapon = None

    # Comienza el dialogo

    stop music fadeout 2.0

    pause 2.0
    show screen stats with dissolve
    play music final_battle
    "I'm in rage state, so my attack and defense are a bit buffered, and I won't faint so easly!"

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
        
        $ autorecovering_rate = renpy.random.randint(1, 100)
        if mc_hp <= 0 and autorecovering_rate <= 50:
            mc "I... I won't give up!"
            $ mc_hp = 0
            $ mc_hp = mc_hp_max / 2
            "[player] restored 50% of HP!"
            enemy "What?!"

        if mc_hp <= 0 and persistent.magic_enabled == True:
            $ timeout = 1.0
            $ timeout_label = "boss_battle1_end"
            menu:
                mc "Shit! I'm dying...!"
                "CURE YOURSELF":
                    $ timeout = 5.0
                    $ timeout_label = None
                    call mgc_cure
                    mc "Phew! That was close...!"

    #
    ####        
        
label boss_battle1_end:

    $ boss_battle = False
    $ boss_battle1_victory = False
    
    $ exp_earned = mc_lv * 200
    $ money_earned = 700
    if enemy_hp <= 0:
        $ total_npc_defeated += 1
        $ boss_battle1_victory = True
    
    call battle_results

    hide screen stats
    with Dissolve(.5)
    $ _skipping = True
    $ save_load_system = True
    $ enemy_hp = enemy_hp_max
    hide screen levelup_stats_hud
    hide screen battle_hud
    stop music fadeout 1