# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

# El juego comienza aquí.

label start:


    # Set the ID of this playthrough
    $ anticheat = persistent.anticheat
    # We'll keep track of the chapter we're on for poem response logic and other stuff
    $ chapter = 0
    #If they quit during a pause, we have to set _dismiss_pause to false again (I hate this hack)
    $ _dismiss_pause = config.developer

    # Aqui agregaré funciones nuevas del Mod.
    $ player = persistent.playername # En screens.rpy hay una función que te permite usar el nombre $ del MC al pulsar OK si no pusiste nada. Este script ayuda a asignar a "player" cómo el nombre que hayas elegido para MC.
    #$ playerCaps = str.upper(player) # El nombre del MC pero en mayúsculas.
    $ save_load_system = False  # El truco que define que el MC no pueda guardar ni cargar partidas.
    $ save_load_disabled = True # Lo de arriba x2 para evitar errores.
    $ total_progress = 0    # Define el porcentaje del progreso del juego... aún WIP
    $ total_npc_defeated = 0    # Define cuántos NPCs venciste en combate.
    $ money = 3500      # Tu dinero
    $ mc_current_weapon = None # Define qué arma estás usando. "None" significa que no está usando nada.
    $ mc_current_weapon_type = None # Define el tipo de arma que usas. Esto ayuda a identificar el tipo de arma para aumentar la EXP con dicho tipo de armas.
    $ mc_wpn_buff = 0 # Define un buffereo de arma, o sea que si te equipaste con un arma, tu Atk aumentará dependiendo qué arma escogiste. (Si no equipas nada, siempre será 0)
    $ enemy_current_weapon = None # Define si el enemigo usa un tipo de arma. Si es así, la aniamción de dolor del MC será sangrienta.

    # Configuración de las batallas.
    $ boss_battle = False       # Define si la batalla es contra un jefe, lo que determina si se puede escapar o no.
    $ no_death_battle = False   # Define si el MC muere o no en una batalla, así cuándo pierdas un duelo que no es a muerte, el juego no se reinicia.

    # Declaraciones en la historia
    $ books_bought = 0
    $ accept_kickboxingclub_offer = None

    # Las variables del poemgame para que el Hud no tire error u.u
    $ sPointTotal = 0
    $ nPointTotal = 0
    $ yPointTotal = 0
    $ mPointTotal = 0

    # Stats del MC Nivel 1
    $ mc_lv = persistent.mc_lv_base

    $ mc_hp_max = persistent.mc_hp_max_base
    $ mc_hp = mc_hp_max
    $ mc_mp_max = persistent.mc_mp_max_base
    $ mc_mp = mc_mp_max

    $ mc_atk_base = persistent.mc_atk_base
    $ mc_def_base = persistent.mc_def_base
    $ mc_spd_base = persistent.mc_spd_base
    $ mc_mat_base = persistent.mc_mat_base
    $ mc_mdf_base = persistent.mc_mdf_base
    $ mc_evasion_base = persistent.mc_evasion_base
    $ mc_atk = mc_atk_base
    $ mc_def = mc_def_base
    $ mc_spd = mc_spd_base
    $ mc_mat = mc_mat_base
    $ mc_mdf = mc_mdf_base
    $ mc_evasion = mc_evasion_base

    $ mc_exp = persistent.mc_exp_base
    $ mc_next_lv = persistent.mc_next_lv_base

    $ mc_sword_skill = persistent.mc_sword_skill
    $ mc_sword_exp = persistent.mc_sword_exp
    $ mc_knife_skill = persistent.mc_knife_skill
    $ mc_knife_exp = persistent.mc_knife_exp
    $ mc_melee_skill = persistent.mc_melee_skill
    $ mc_melee_exp = persistent.mc_melee_exp
    $ mc_chainsaw_skill = persistent.mc_chainsaw_skill
    $ mc_chainsaw_exp = persistent.mc_chainsaw_exp
    $ mc_handgun_skill = persistent.mc_handgun_skill
    $ mc_handgun_exp = persistent.mc_handgun_exp
    $ mc_machinegun_skill = persistent.mc_machinegun_skill
    $ mc_machinegun_exp = persistent.mc_machinegun_exp
    $ mc_magic_skill = persistent.mc_magic_skill
    $ mc_magic_exp = persistent.mc_magic_exp

    # Define nombre de los Protagonistas
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    # Define nombre de los NPCs
    $ mcf1_name = "Ryoma"
    $ mcf2_name = "Camilla"
    $ mcf3_name = "Joe"
    $ mcf4_name = "Mac"
    $ mgf_name = "Maxxi"
    $ mf1_name = "Selene"
    $ ft_name = "Profesora"
    $ mt_name = "Profesor"
    $ mcmom_name = "Mamá"
    $ mcdad_name = "Papá"
    $ smom_name = "Mamá de Sayori"
    $ sdad_name = "Papá de Sayori"
    $ ymom_name = "Mamá de Yuri"
    $ ydad_name = "Papá de Yuri"
    $ nmom_name = "Mamá de Natsuki"
    $ nd_name = "Nat's Dad"
    $ ndad_name = "Papá de Natsuki"
    $ mmom_name = "Mamá de Monika"
    $ mdad_name = "Papá de Monika"
    $ f1mom_name = "Mamá de Ryoma"
    $ f1dad_name = "Papá de Ryoma"
    $ f2mom_name = "Mamá de Camilla"
    $ f2dad_name = "Papá de Camilla"

    # Configuraciones de quick menu, style de dialogo, muertes, y el text skip
    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ in_yuri_kill = None
    $ in_natsuki_kill = None
    $ in_monika_kill = None
    $ in_mc_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    # Aquí llama la historia del juego y sus capítulos
    call start_fighting_for_reality

# Pantalla de Game Over
label gameover(pause_length=10.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    play music "<from 16.0>bgm/6s.ogg" noloop
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    $ MainMenu(confirm=False)()
    return

# Pantalla final que incluye un mensaje del autor para el jugador.
label thankyou:
    play sound page_turn
    show poem_end with Dissolve(1)
    $ persistent.autoload = None
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    show poem_end #Show special ending message
    $ pause()
    #Make player quit
    return

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
