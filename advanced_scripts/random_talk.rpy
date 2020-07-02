##Código que hace funcionar los díalogos random.

init python:
  def random_talk():
     renpy.say(None, renpy.random.choice(dialogue))

#Ejemplo a usar en los scripts-ch:
#
# dialogue = [("There's a soccer trial this afternoon!", "soccer"), ("New teacher coming in today", "NewTeacher")]
# random_talk_tag = "soccer" #opens soccer related plots