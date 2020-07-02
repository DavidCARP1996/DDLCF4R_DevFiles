label wpn_skill_exp:

    if mc_current_weapon_type == "knife":
        $ mc_knife_exp +=1
    elif mc_current_weapon_type == "sword":
        $ mc_sword_exp +=1
    elif mc_current_weapon_type == "melee":
        $ mc_melee_exp +=1
    elif mc_current_weapon_type == "chainsaw":
        $ mc_chainsaw_exp +=1
    elif mc_current_weapon_type == "handgun":
        $ mc_handgun_exp +=1
    elif mc_current_weapon_type == "machinegun":
        $ mc_machinegun_exp +=1
    else:
        pass
    
    if mc_sword_exp >= 10:
        $ mc_sword_skill += 1
        $ mc_sword_exp = 0
        $ renpy.notify("Sword Skill Rank up!")
    elif mc_knife_exp >= 10:
        $ mc_knife_skill += 1
        $ mc_knife_exp = 0
        $ renpy.notify("Knife Skill Rank up!")
    elif mc_melee_exp >= 10:
        $ mc_melee_skill += 1
        $ mc_melee_exp = 0
        $ renpy.notify("Melee weapons Skill Rank up!")
    elif mc_chainsaw_exp >= 10:
        $ mc_chainsaw_skill += 1
        $ mc_chainsaw_exp = 0
        $ renpy.notify("Chainsaw Skill Rank up!")
    elif mc_handgun_exp >= 10:
        $ mc_handgun_skill += 1
        $ mc_handgun_exp = 0
        $ renpy.notify("Handguns Skill Rank up!")
    elif mc_machinegun_exp >= 10:
        $ mc_machinegun_skill += 1
        $ mc_machiengun_exp = 0
        $ renpy.notify("Machienguns Skill Rank up!")
    elif mc_magic_exp >= 10:
        $ mc_magic_skill += 1
        $ mc_magic_exp = 0
        $ renpy.notify("Magic Skill Rank up!")
    else:
        pass

    return