#!/usr/bin/env python3

import os
import subprocess
import time

def exe(command):
    command = command.strip()
    c = command.split()
    output, error = subprocess.Popen(c,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE).communicate()
    output = output.decode('utf-8').strip()
    error = error.decode('utf-8').strip()
    return (output, error)

def main():
    active_window_command = "xdotool getactivewindow"
    active_window_id, error = exe(active_window_command)

    active_window_name_command = "xdotool getwindowname {}" \
                                    .format(int(active_window_id))
    active_window_name, error = exe(active_window_name_command)
    print(active_window_name)

    with open("log", 'w') as f:
        output = ""
        exe("xdotool search --name YouTube --desktop 9 windowactivate")
        #os.system("xdotool search --name YouTube windowactivate")
        time.sleep(0.1)
        exe("xdotool key --clearmodifiers space --desktop 9")
        #os.system("xdotool key --clearmodifiers space")
        f.write(active_window_name + output)

if __name__ == "__main__":
    main()

