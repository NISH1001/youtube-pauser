#!/usr/bin/env python3

"""
    Monolothic module to play/pause the youtube video in the browser
"""

import config_loader
import time
import xdotool

def swtich_tabs(window, max_tab=50):
    """
        Switch to all the tabs
    """
    names = []
    for i in range(max_tab):
        window_name = xdotool.get_window_name(window)
        print("Current window ==> Id : {}, Name : {}".format(window, window_name))
        if window_name in names:
            break
        if "YouTube" in window_name:
            xdotool.send_keys("space")
        names.append(window_name)
        xdotool.send_keys("Ctrl", "Tab")

def swtich_windows():
    """
        Switch all the windows
    """
    config = config_loader.load_config("config.json")
    print(config)
    windows = xdotool.search_window_class(config['browser'])
    for window in windows:
        window_name = xdotool.get_window_name(window)
        xdotool.activate_window(window)
        swtich_tabs(window, max_tab=30)

def play_pause():
    swtich_windows()

def main():
    play_pause()

if __name__ == "__main__":
    main()

