label regular_attacks:
    $ atk_type_choosen = "regular"
    jump mc_attack_ready
return

label mgc_attacks:

    label atk_kamehameha:
        $ atk_type_choosen = "magic"
        $ mgk_choosen_name = "Kamehameha"
        $ mgk_choosen_consuption = 5000
        jump mc_attack_ready
    return

    label atk_fire:
        $ atk_type_choosen = "magic"
        $ mgk_choosen_name = "Fire"
        $ mgk_choosen_consuption = 100
        jump mc_attack_ready
    return

    label atk_ice:
        $ atk_type_choosen = "magic"
        $ mgk_choosen_name = "Ice"
        $ mgk_choosen_consuption = 100
        jump mc_attack_ready
    return

    label atk_thunder:
        $ atk_type_choosen = "magic"
        $ mgk_choosen_name = "Thunder"
        $ mgk_choosen_consuption = 100
        jump mc_attack_ready
    return

    label atk_meteor:
        $ atk_type_choosen = "magic"
        $ mgk_choosen_name = "Meteor"
        $ mgk_choosen_consuption = 10000
        jump mc_attack_ready
    return

    label atk_ultima:
        $ atk_type_choosen = "magic"
        $ mgk_choosen_name = "Ultima"
        $ mgk_choosen_consuption = 10000
        jump mc_attack_ready
    return

label mgc_self:

    label mgc_cure:
        mc "Cure!"
        call magic_self_mc
        $ mc_hp += mc_damage
        $ mc_mp -= 150
        $ mc_magic_exp += 1
        call wpn_skill_exp
        "[player] restored [mc_damage] HP"
    return

label mc_attack_ready:
    if atk_type_choosen == "magic":
        jump atk_magic
    else:
        jump atk_regular
return

label atk_regular:
    mc "Take this!"
    call regular_atk_mc
    $ enemy_hp -= mc_damage
    call wpn_skill_exp
    "Damage dealt: [mc_damage] HP"
return

label atk_magic:
    mc "[mgk_choosen_name]!"
    call magic_atk_mc
    $ enemy_hp -= mc_damage
    $ mc_mp -= mgk_choosen_consuption
    $ mc_magic_exp += 1
    call wpn_skill_exp
    "Damage dealt: [mc_damage] HP"
return