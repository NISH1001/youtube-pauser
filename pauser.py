#!/usr/bin/env python3

"""
    Monolothic module to play/pause the youtube video in the browser
"""

import config_loader
import time
import xdotool

def swtich_tabs(window):
    """
        Switch to all the tabs
    """
    names = []
    for i in range(50):
        window_name = xdotool.get_window_name(window)
        print("Current window ==> Id : {}, Name : {}".format(window, window_name))
        if window_name in names:
            break
        if "YouTube" in window_name:
            xdotool.send_keys("space")
        #xdotool.sleep(0.1)
        names.append(window_name)
        xdotool.send_keys("Ctrl", "Tab")

def swtich_windows():
    """
        Switch all the windows
    """
    config = config_loader.load_config("config.json")
    windows = xdotool.search_window_class(config['browser'])
    for window in windows:
        window_name = xdotool.get_window_name(window)
        #print("Current window ==> Id : {}, Name : {}".format(window, window_name))
        xdotool.activate_window(window)
        #xdotool.sleep(0.2)
        swtich_tabs(window)
        xdotool.send_keys("Escape")

def play_pause():
    swtich_windows()

def main():
    play_pause()

if __name__ == "__main__":
    main()

