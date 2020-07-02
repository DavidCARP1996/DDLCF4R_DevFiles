label battle_results:

    if enemy_hp <= 0:
        if mc_hp <= 0:
            show screen levelup_stats_hud
            "DOUBLE K.O."
            $ mc_exp += exp_earned
            "[player] won [exp_earned] EXP!"
            call exp_levelup
            $ money += money_earned
            "[player] won $[money_earned]!"
            if no_death_battle == True:
                pass
            else:
                mc "... ... ..."
                "... ... ..."
                "However..."
                "[player] as whited out."
                $ _skipping = True
                $ save_load_system = True
                hide screen stats
                hide screen battle_hud
                hide screen levelup_stats_hud
                scene black
                with Dissolve(.5)
                call gameover
            
        else:
            show screen levelup_stats_hud
            "[player] WINS!!!"
            $ mc_exp += exp_earned
            "[player] won [exp_earned] EXP!"
            call exp_levelup
            $ money += money_earned
            "[player] won $[money_earned]!"
            
    else:

        "YOU LOSE!!!"
        if no_death_battle == True:
            show screen levelup_stats_hud
            $ exp_earned = exp_earned / 2
            mc "... ... ..."
            $ mc_exp += exp_earned
            "[player] won [exp_earned] EXP!"
            call exp_levelup
            pass
        else:
            mc "... ... ..."
            "... ... ..."
            "[player] as whited out."
            $ _skipping = True
            $ save_load_system = True
            hide screen stats
            hide screen battle_hud
            hide screen levelup_stats_hud
            scene black
            with Dissolve(.5)
            call gameover
        