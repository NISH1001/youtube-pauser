#!/usr/bin/env python3

"""
    Utility module for system related tasks
"""

import os
import subprocess

def exe(command):
    """
        Executes the given system command
    """
    command = command.strip()
    c = command.split()
    output, error = subprocess.Popen(c,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE).communicate()
    output = output.decode('utf-8').strip()
    error = error.decode('utf-8').strip()
    return (output, error)


def main():
    pass

if __name__ == "__main__":
    main()

