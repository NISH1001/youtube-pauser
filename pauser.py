#!/usr/bin/env python3

"""
    Monolothic module to play/pause the youtube video in the browser
"""

import config_loader
import time
from sysutils import exe
import xdotool

def swtich_tab(window_id):
    window_names = []
    command_windowname = "xdotool getwindowname {}"

def swtich_windows():
    config = config_loader.load_config("config.json")
    windows = xdotool.search_window_class("Chromium")
    print(windows)
    for window in windows:
        window_name = xdotool.get_window_name(window)
        print("Current window ==> Id : {}, Name : {}".format(window, window_name))
        time.sleep(0.3)
        xdotool.activate_window(window)
        time.sleep(0.1)
        xdotool.send_keys("Ctrl", "Tab")

def play_pause():
    config = config_loader.load_config("config.json")
    #exe("xdotool search --name {} windowactivate".format(config['window_name']))
    xdotool.send_keys("Alt", config['desktop_number'])
    time.sleep(0.1)
    xdotool.send_keys("space")

def main():
    swtich_windows()

if __name__ == "__main__":
    main()

