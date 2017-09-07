#!/usr/bin/env python3

"""
    A wrapper over Linux's xdotool
"""

from sysutils import exe

def get_window_name(id):
    """
        Fetch name of the window with corresponding id
    """
    command = "xdotool getwindowname {}".format(id)
    output, error = exe(command)
    return output.strip()

def get_window_active():
    """
        Fetch id of the currently active window
    """
    output, error = exe("xdotool getactivewindow")
    return output

def search_window_class(class_name):
    """
        Search all the windows with class name
        Eg: xdotool search --class Chromium
    """
    command = "xdotool search --class {}".format(class_name)
    output, error = exe(command)
    return output.split()

def activate_window(id):
    """
        Focus the window
    """
    command = "xdotool windowactivate {}".format(id)
    output, error = exe(command)
    return output

def send_keys(*args):
    key = '+'.join(args)
    command = "xdotool key --clearmodifiers {}".format(key)
    output, error = exe(command)
    return output

def main():
    pass

if __name__ == "__main__":
    main()

