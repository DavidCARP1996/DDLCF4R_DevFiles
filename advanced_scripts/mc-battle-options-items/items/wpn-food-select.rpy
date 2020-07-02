label weapon_select:
    menu:

        "Excalibur" if bag_inventory.has_item("excalibur"):
            $ mc_current_weapon = "Excalibur"
            $ mc_current_weapon_type = "sword"
            $ mc_wpn_buff = 9000
            "[player] equiped the legendary Excalibur."
        
        "Jackknife" if bag_inventory.has_item("jackknife"):
            $ mc_current_weapon = "Jackknife"
            $ mc_current_weapon_type = "knife"
            $ mc_wpn_buff = 10
            "[player] equiped Jackknife."

        "9mm Pistol" if bag_inventory.has_item("pistol"):
            $ mc_current_weapon = "9mm Pistol"
            $ mc_current_weapon_type = "handgun"
            $ mc_wpn_buff = 100
            "[player] equiped 9mm Pistol."

        "Remove current weapon" if mc_current_weapon != None:
            $ mc_current_weapon = None
            $ mc_wpn_buff = 0
            "[player] saved his weapon."

        "Back":
            return
#

label eat_item:
    menu:

        "Cinnamon Bun" if bag_inventory.has_item("cmonbun"):
            mc "Munch, munch!"
            mc "This food remains me to Sayori..."
            $ bag_inventory.score_item("cmonbun", score=-1)
            $ mc_hp = mc_hp_max
            $ mc_mp = mc_mp_max
            "[player] restored all HP and MP"

        "Oolong Tea" if bag_inventory.has_item("yuritea"):
            mc "Slurp, slurp!"
            mc "Yuri's tea is the best tea, oh yeah!"
            $ bag_inventory.score_item("yuritea", score=-1)
            $ mc_hp = mc_hp_max
            $ mc_mp = mc_mp_max
            "[player] restored all HP and MP"

        "Nat's Cupcake" if bag_inventory.has_item("natcake"):
            mc "Munch, munch!"
            mc "Natsuki's cupcakes are the best, no doubt about it!"
            $ bag_inventory.score_item("natcake", score=-1)
            $ mc_hp = mc_hp_max
            $ mc_mp = mc_mp_max
            "[player] restored all HP and MP"

        "Tarbrush coffee" if bag_inventory.has_item("monicoffee"):
            mc "Slurp, slurp!"
            mc "Now I see why Monika likes this coffee so much..."
            $ bag_inventory.score_item("monicoffee", score=-1)
            $ mc_hp = mc_hp_max
            $ mc_mp = mc_mp_max
            "[player] restored all HP and MP"

        "Cookie" if bag_inventory.has_item("cookie"):
            mc "Munch, munch!"
            $ bag_inventory.score_item("cookie", score=-1)
            $ mc_hp += 100
            $ mc_mp += 50
            "[player] restored 100 HP and 50 MP"

        "Protein bar" if bag_inventory.has_item("proteinbar"):
            mc "Munch, munch!"
            $ bag_inventory.score_item("proteinbar", score=-1)
            $ mc_hp += 40
            $ mc_mp += 80
            "[player] restored 40 HP and 80 MP"

        "Cupcake" if bag_inventory.has_item("cupcake"):
            mc "Munch, munch!"
            $ bag_inventory.score_item("cupcake", score=1)
            $ mc_hp = mc_hp_max
            $ mc_mp += 120
            "[player] restored all HP and 120 MP"

        "Sports drink" if bag_inventory.has_item("sportdrink"):
            mc "Slurp, slurp!"
            mc "I can feel it, I'm recovering my stamina!"
            $ bag_inventory.score_item("sportdrink", score=1)
            $ mc_hp += 35
            $ mc_mp = mc_mp_max
            "[player] restored 35 HP and all MP"

        "Chocolate" if bag_inventory.has_item("chocolate"):
            mc "Munch, munch!"
            $ bag_inventory.score_item("chocolate", score=1)
            $ mc_hp += 100
            $ mc_mp += 50
            "[player] restored 100 HP and 50 MP"

        "Soda" if bag_inventory.has_item("soda"):
            mc "Slurp, slurp!"
            $ bag_inventory.score_item("soda", score=1)
            $ mc_hp += 25
            $ mc_mp += 20
            "[player] restored 25 HP and 20 MP"

        "Back":
            return

