#!/usr/bin/env python3

"""
    Monolothic module to play/pause the youtube video in the browser
"""

import config_loader
import time
from sysutils import exe

def play_pause():
    config = config_loader.load_config("config.json")
    #exe("xdotool search --name {} windowactivate".format(config['window_name']))
    command_switch = "xdotool key --clearmodifiers Alt+{}".format(config['desktop_number'])
    exe("xdotool key --clearmodifiers Alt+{}".format(config['desktop_number']))
    time.sleep(0.1)
    exe("xdotool key --clearmodifiers space")

def main():
    play_pause()

if __name__ == "__main__":
    main()

