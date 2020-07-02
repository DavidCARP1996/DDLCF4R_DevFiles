label exp_levelup:

    while (mc_exp >= mc_next_lv):
        if mc_lv < 100:
            $ lvlup_exp_rng = 50 * mc_lv
            $ hp_exp_rng = renpy.random.randint(1, 10) * mc_lv
            $ mp_exp_rng = renpy.random.randint(1, 10) * mc_lv
            $ atk_exp_rng = renpy.random.randint(1, 10) * mc_lv
            $ def_exp_rng = renpy.random.randint(1, 10) * mc_lv
            $ spd_exp_rng = renpy.random.randint(1, 10) * mc_lv
            $ mat_exp_rng = renpy.random.randint(1, 10) * mc_lv
            $ mdf_exp_rng = renpy.random.randint(1, 10) * mc_lv
            $ evasion_exp_rng = renpy.random.randint(0, 2)
        else:
            pass

    #
        if mc_exp >= mc_next_lv or mc_next_lv != "MAX":
            #Si el nivel es 1, subirá el Nivel a 2 y subirán los stats.
            $ mc_lv += 1
            $ mc_next_lv += lvlup_exp_rng
            $ mc_hp_max += hp_exp_rng
            $ mc_hp = mc_hp_max
            $ mc_mp_max += mp_exp_rng
            $ mc_mp = mc_mp_max
            $ mc_atk_base += atk_exp_rng
            $ mc_def_base += def_exp_rng
            $ mc_spd_base += spd_exp_rng
            $ mc_mat_base += mat_exp_rng
            $ mc_mdf_base += mdf_exp_rng
            $ mc_evasion_base += evasion_exp_rng
            if mc_lv == 100:
                $ mc_next_lv = "MAX"
            "[player]'s Level up!"
        else:
            pass

#label exp_levelup:
#    if mc_exp >= mc_next_lv:
        #Si el nivel es 1, subirá el Nivel a 2 y subirán los stats.
#        if mc_lv == 2:
#            $ mc_lv = 2
#            $ mc_next_lv = 150
#            $ mc_hp_max = 150
#            $ mc_hp = mc_hp_max
#            $ mc_mp_max = 80
#            $ mc_mp = mc_mp_max
#            $ mc_atk = 15
#            $ mc_def = 13
#            $ mc_spd = 30
#            $ mc_mat = 7
#            $ mc_mdf = 8
#            pass
#        elif mc_lv == 1:
#            $ mc_lv = 100
#            $ mc_next_lv = "MAX"
#            $ mc_hp_max = 999999
#            $ mc_hp = mc_hp_max
#            $ mc_mp_max = 99999
#            $ mc_mp = mc_mp_max
#            $ mc_atk = 75126
#            $ mc_def = 62103
#            $ mc_spd = 98745
#            $ mc_mat = 72540
#            $ mc_mdf = 67896
#            pass
#        "[player]'s Level up!"
#    else:
#        pass