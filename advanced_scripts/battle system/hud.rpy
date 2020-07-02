screen single_stat_player(name, hp, hp_max, mp, mp_max, lv, xalign):

    frame:
        xalign xalign

        vbox:
            spacing 5

            hbox:
                text "[name!t]" min_width 220
                text _(" Lv. [mc_lv]")

            hbox:
                text _("HP"):
                    min_width 40
                    yalign 0.5

                bar:
                    value AnimatedValue(hp, hp_max, 1.0)
                    xmaximum 180
                    ysize 26


                text " [mc_hp]/[mc_hp_max]":
                    yalign 0.5

            hbox:
                text _("MP"):
                    min_width 40
                    yalign 0.5

                bar:
                    value AnimatedValue(mp, mp_max, 1.0)
                    xmaximum 180
                    ysize 26


                text " [mc_mp]/[mc_mp_max]":
                    yalign 0.5

screen single_stat_enemy(name, hp, hp_max, lv, xalign):

    frame:
        xalign xalign

        vbox:
            spacing 5

            hbox:
                text "[name!t]" min_width 220
                text _(" Lv. [lv]")

            hbox:
                text _("HP"):
                    min_width 40
                    yalign 0.5

                bar:
                    value AnimatedValue(hp, hp_max, 1.0)
                    xmaximum 180
                    ysize 26


                text " [enemy_hp]/[enemy_hp_max]":
                    yalign 0.5

screen stats():
    use single_stat_player(_(player), mc_hp, mc_hp_max, mc_mp, mc_mp_max, mc_lv, 0.0)
    use single_stat_enemy(_(enemy), enemy_hp, enemy_hp_max, enemy_lv, 1.0)

screen levelup_stats_hud:
    frame:
        xalign 1.0 yalign 0.5
        #xminimum 200 xmaximum 200
        #yminimum 130 ymaximum 130
        vbox:
            text "Lv: [mc_lv]" #size 22 xalign 0.3 ypos 0.2
            text "HP: [mc_hp_max]"
            text "Atk: [mc_atk_base]"
            text "Def: [mc_def_base]"
            text "Spd: [mc_spd_base]"
            text "M.Atk: [mc_mat_base]"
            text "M.Def: [mc_mdf_base]"
            text "Evas.: [mc_evasion_base]"
            text "Exp: [mc_exp]"
            text "Next: [mc_next_lv]"
            #null height 5

menu Hud:

    "Choose your option."

    "Attack!":
        call hud_attack

    "Magic!" if persistent.magic_enabled == True:
        call hud_magic
                
    "Items!":
        call hud_inventory

    "Run!":
        if (boss_battle == False) and (mc_spd > enemy_spd):
            mc "I'm get outta here!"
            return
        else:
            mc "I can't run from this piece of shit!"

#######################################################################################################
##################################     BETA DE 1-2 VS 1-5     #########################################
#######################################################################################################

screen battle_screen:
    vbox:
        xalign 0.01 yalign 0.05
        spacing 5
        
        for each_party_member in party_list:
            frame:
                size_group "party"
                xminimum 250 xmaximum 250
                yminimum 75
                vbox:
                    text "[each_party_member[name]]" size 22 xalign 0.5
                    null height 5
                    hbox:
                        bar:
                            xmaximum 130
                            value each_party_member["current_hp"]
                            range each_party_member["max_hp"]
                            left_gutter 0
                            right_gutter 0
                            thumb None
                            thumb_shadow None
                            
                        null width 5
                        
                        text "[each_party_member[current_hp]] / [each_party_member[max_hp]]" size 16
        hbox:
            frame:
                size_group "party"
                yminimum 40
                text "Potions left - [potions_left]" yalign 0.5
            if players_turn and potions_left > 0:
                textbutton "<- Use" action Return("heal") yminimum 40
            else:
                textbutton "<- Use" action None yminimum 40
                        
                        
    vbox:
        xalign 0.99 yalign 0.05
        spacing 5
        
        if enemies_list != []:
            for i, each_enemy_member in enumerate(enemies_list):
                hbox:
                    if players_turn and each_enemy_member["current_hp"] > 0:
                        frame:
                            yminimum 75
                            textbutton _("Attack!") yminimum 65:
                                action Return(i)
 
                        #textbutton "Attack!" action Return(i) yminimum 75
                    else:
                        frame:
                            yminimum 75
                            textbutton _("Attack!") yminimum 65:
                                action None

                        #textbutton "Attack!" action None yminimum 75
                    
                    frame:
                        size_group "enemies"
                        xminimum 250 xmaximum 250
                        yminimum 75
                        vbox:
                            text "[each_enemy_member[name]]" size 22 xalign 0.5
                            null height 5
                            hbox:
                                bar:
                                    xmaximum 130
                                    value each_enemy_member["current_hp"]
                                    range each_enemy_member["max_hp"]
                                    left_gutter 0
                                    right_gutter 0
                                    thumb None
                                    thumb_shadow None
                                    
                                null width 5
                                
                                text "[each_enemy_member[current_hp]] / [each_enemy_member[max_hp]]" size 16

#######################################################################################################
##################################     OTROS HUDS     #################################################
#######################################################################################################

screen freeroam_hud:
    frame:
        xalign 1.0 yalign 0.01
        xminimum 200 xmaximum 200
        #yminimum 130 ymaximum 130
        vbox:
            #text "Hour: [hr_hour] : [hr_minutes]"
            text "Hour: [hr_hour] : 00"
            text "Stamina: [stamina] / [stamina_max]"
            text "HP: [mc_hp] / [mc_hp_max]"
            text "Money: [money]"
            #null height 5

screen poemgame_hud:
    frame:
        xalign 1.0 yalign 0.01
        xminimum 200 xmaximum 200
        #yminimum 130 ymaximum 130
        vbox:
            if bag_inventory.has_item("sbook1"):
                text "Sayori: [sPointTotal]"
            if bag_inventory.has_item("ybook1"):
                text "Yuri: [yPointTotal]"
            if bag_inventory.has_item("nbook1"):
                text "Natsuki: [nPointTotal]"
            if bag_inventory.has_item("mbook1"):
                text "Monika: [mPointTotal]"
            #null height 5
