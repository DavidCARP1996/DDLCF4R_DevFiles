label enemy_turn:
    call regular_atk_enemy
            
    if mc_evasion >= mc_evasion_rate:
        mc "Ha~!"
        "[player] dodge the attack."
    else:
        if enemy_damage <= mc_def:
            call enemy_hit_low
        elif enemy_critical_rate < 10:
            $ enemy_damage = enemy_damage * 2
            if enemy_current_weapon == None:
                call enemy_hit_critical
            else:
                call enemy_hit_bcritical
        else:
            if enemy_current_weapon == None:
                call enemy_hit_normal
            else:
                call enemy_hit_bloody
return

label enemy_hit_low:
    $ mc_hp -= enemy_damage
    call mc_pain1
    mc "Hmpt!"
    "Not so effective."
    "Damage dealt: [enemy_damage] HP"
return

label enemy_hit_normal:
    $ mc_hp -= enemy_damage
    call mc_pain2
    mc "Agh!"
    "Damage dealt: [enemy_damage] HP"
return

label enemy_hit_critical:
    $ mc_hp -= enemy_damage
    call mc_pain3
    mc "Fuck!"
    "CRITICAL"
    "Damage dealt: [enemy_damage] HP"
return

label enemy_hit_bloody:
    $ mc_hp -= enemy_damage
    call mc_pain4
    mc "Agh! Shit!"
    "Damage dealt: [enemy_damage] HP"
return

label enemy_hit_bcritical:
    $ mc_hp -= enemy_damage
    call mc_pain5
    mc "Hnnnnng!!!"
    "CRITICAL"
    "Damage dealt: [enemy_damage] HP"
return