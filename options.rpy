## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
# _() marks strings eligable for translation

define config.name = "Doki Doki Fighting for Reality"

## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

# True shows the name on main menu, False hides it
define gui.show_name = False

# Version of the game
define config.version = "9.12.2018"

# text placed on about screen
define gui.about = _("")

# short name used in executables and dirs.
# ASCII-only, no spaces, no colons, no semis
define build.name = "DDLC"

## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.
define config.has_sound = True
define config.has_music = True
define config.has_voice = True

# main menu music
#define config.main_menu_music = audio.t1

## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = audio.title_theme
# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)

## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None

## Used when entering the main menu after the game has ended.
define config.end_game_transition = Dissolve(.5)

# Controls when dialogue window is displayed:
#   show - always displayed
#   hide - only displayed if dialogue is present
#   auto - hidden before scene statements and shown when dialogue is shown
#
## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.
# this can be changed with "window <type>" statements
define config.window = "auto"

## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 50

## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15

# default volumes
default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75

## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "DDLC-Fighting4Reality"

## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"

# True means we allow skipping, False means not
define config.allow_skipping = True

# True means we can autosave, false means not
define config.has_autosave = False

# True means autosave when we quit, False means not
define config.autosave_on_quit = False

# Number of autosave slots to use
define config.autosave_slots = 0

# layers that screens / images / anything can be displayed on. Best not to
# mess with this
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]

# Other things to not mess with
define config.image_cache_size = 64
define config.predict_statements = 50
define config.rollback_enabled = config.developer
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"


init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)



# BUILD CONFIG

init python:

    # the following functions take file pattersn:
    # file patterns are case-insensitive and matched against the path relative to the 
    # base directory, with and without a leading /. If multiple patterns match
    # the first is used.
    #
    # / is directory separator
    # * matches all characters, exxcept directory separator
    # ** matches all characters, including directory separator
    #
    # EXAMPLES
    # *.txt - - matches txt files in base directory
    # game/**.ogg - mathces ogg files in game directory or subdirs of game
    # **.psd - matches psd files anywhere in project
    #
    # Classify files as None to exclusde them from the built distributions
    #

    # packaged ZIP for distibution
    build.package(build.directory_name + "Mod",'zip',build.name,description='DDLC Compatible Mod')

    # archives to create
    build.archive("scripts",build.name)
    build.archive("mod_assets",build.name)
    build.archive("submods",build.name)

    # folder / files to put in archives
    build.classify("game/mod_assets/**","mod_assets")
    build.classify("game/submods/**","submods")
    build.classify('game/**.rpyc',"scripts")
    build.classify('game/advanced_scripts/**',"scripts")
    build.classify('game/original_story_scripts/**',"scripts")

    # stuff to ignore
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('**.rpa',None)

    # stuff not in archive
    build.classify('README.html',build.name)
    
    # Doki Doki Mod Manager metadata file
    build.classify('ddmm-mod.json',build.name)

    # mark as documentation
    build.documentation('README.html')

    build.include_old_themes = False
