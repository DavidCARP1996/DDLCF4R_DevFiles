#style battle_bar:
#    ysize 18
#    base_bar Frame("gui/scrollbar/horizontal_hover_bar.png", tile=False)
#    thumb Frame("gui/scrollbar/horizontal_hover_thumb.png", top=6, right=6, tile=True)

style battle_bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_hover_bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_hover_thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)