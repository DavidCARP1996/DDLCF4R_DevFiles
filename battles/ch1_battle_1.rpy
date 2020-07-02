label ch1_battle_1:

    # Deshabilita el Skip y el sistema de Guardar/Cargar.

    $ _skipping = False
    $ save_load_system = False
    hide screen freeroam_hud
    $ boss_battle = True
    $ no_death_battle = False
    $ battle_extra_rewards_rate = renpy.random.randint(1, 100)

    # Define al rival.

    $ enemy = "Looter"
    $ enemy_lv = 3
    $ enemy_hp_max = 100
    $ enemy_hp = enemy_hp_max
    $ enemy_mp_max = 0
    $ enemy_mp = enemy_mp_max
    $ enemy_atk_base = 7
    $ enemy_def_base = 6
    $ enemy_spd_base = 8
    $ enemy_mat_base = 0
    $ enemy_mdf_base = 0

    $ enemy_atk = enemy_atk_base
    $ enemy_def = enemy_def_base
    $ enemy_spd = enemy_spd_base
    $ enemy_mat = enemy_mat_base
    $ enemy_mdf = enemy_mdf_base

    $ enemy_current_weapon = "Jackknife"

    # Comienza el dialogo

    stop music fadeout 2.0

    pause 1.0
    mc "..."
    mc "What the..."
    "!"
    show robber at t11 zorder 2
    "Looter" "Hey, you!"
    "Looter" "You better give me your stuffs if you want to live!"
    mc "Fuck you!!!"

    pause 2.0

    show screen stats
    with dissolve
    play music demobattle
    "Watch out! He's using a Jackknife! It's a LIFE OR DEATH fight!"

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

        if mc_hp <= 0 and persistent.magic_enabled == True:
            $ timeout = 1.0
            $ timeout_label = "ch1_battle_1_end"
            menu:
                mc "Shit! I'm dying...!"
                "CURE YOURSELF":
                    $ timeout = 5.0
                    $ timeout_label = None
                    call mgc_cure
                    mc "Phew! That was close...!"

    #
    ####        
        
label ch1_battle_1_end:

    $ boss_battle = False
    
    $ exp_earned = mc_lv * 50
    $ money_earned = 500
    if enemy_hp <= 0:
        hide robber
        with Dissolve(.5)
        $ total_npc_defeated += 1
    
    call battle_results

    hide screen stats
    with Dissolve(.5)
    $ _skipping = True
    $ save_load_system = True
    $ enemy_hp = enemy_hp_max
    hide screen levelup_stats_hud
    hide screen battle_hud
    stop music fadeout 1