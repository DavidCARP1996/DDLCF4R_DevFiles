### Aquí se llamarán a las variables que definirán los puntos de daño para el MC y su enemigo.

label regular_atk_mc:
    # Genera un multiplicador para el daño
    $ mc_damage_rand = renpy.random.randint(1, 5)
    # Daño generado con los puntos de ataque y el buff adicional por arma equipada
    $ mc_regular_dmg = mc_atk + mc_wpn_buff
    # Se aplica el multiplicador
    $ mc_regular_dmg = mc_regular_dmg * mc_damage_rand
    # El daño se reduce por la defensa del rival
    $ mc_damage = mc_regular_dmg - enemy_def
    # Este IF ayudará al sistema a que si por un error de cálculos, el daño hace un "daño" de -5 (por ejemplo), este que sólo haga daño de 1 en vez de curar al oponente.
    if mc_damage <= 0:
        $ mc_damage = 1
        
        if mc_critical_rate < 10:
            $ mc_damage = mc_damage * 2
        else:
            pass
    else:
        pass

    return

label magic_atk_mc:

    $ mc_damage_rand = renpy.random.randint(1, 5)
    $ mc_magic_dmg = mc_mat * mc_damage_rand
    $ mc_damage = mc_magic_dmg - enemy_mdf
    if mc_damage <= 0:
        $ mc_damage = 1

        if mc_critical_rate < 10:
            $ mc_damage = mc_damage * 2
        else:
            pass
    else:
        pass

    return

label magic_self_mc:

    $ mc_damage_rand = renpy.random.randint(1, 5)
    $ mc_magic_dmg = mc_mat * mc_damage_rand
    $ mc_damage = mc_magic_dmg
    if mc_damage <= 0:
        $ mc_damage = 1

        if mc_critical_rate < 10:
            $ mc_damage = mc_damage * 2
        else:
            pass
    else:
        pass

    return

label regular_atk_enemy:

    $ enemy_damage_rand = renpy.random.randint(1, 5)
    $ enemy_regular_dmg = enemy_atk * enemy_damage_rand
    $ enemy_damage = enemy_regular_dmg - mc_def
    if enemy_damage <= 0:
        $ enemy_damage = 1
    else:
        pass

    return

label magic_atk_enemy:

    $ enemy_damage_rand = renpy.random.randint(1, 5)
    $ enemy_magic_dmg = enemy_mat * enemy_damage_rand
    $ enemy_damage = enemy_magic_dmg - mc_mdf
    if enemy_damage <= 0:
        $ enemy_damage = 1
    else:
        pass

    return

label magic_self_enemy:

    $ enemy_damage_rand = renpy.random.randint(1, 5)
    $ enemy_magic_dmg = enemy_mat * enemy_damage_rand
    $ enemy_damage = enemy_magic_dmg
    if enemy_damage <= 0:
        $ enemy_damage = 1
    else:
        pass

    return