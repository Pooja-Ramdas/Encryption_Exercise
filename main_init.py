# This program checks if the dependencies are installed or not and if not, it installs them.

import subprocess
import sys
import time


def __init():

    c = 4
    div = 100/c
    n = 0

    try:
        import subprocess
        print("subprocess is installed")
        n += div
    except ImportError:
        print("subprocess is not installed")
        print("installing subprocess")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'uuid'])
        print("subprocess is now installed")
        import subprocess
        n += div
        
    try:
        import sys
        print("sys is installed")
        n += div
    except ImportError:
        print("sys is not installed")
        print("installing sys")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'sys'])
        print("sys is now installed")
        import sys
        n += div


    try:
        import hashlib
        print("hashlib is installed")
        n += div
    except ImportError:
        print("hashlib is not installed")
        print("installing hashlib")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", 'hashlib'])
        print("hashlib is now installed")
        import hashlib
        n += div
    print("If the code breaks down in the next step please run the program again.")
    time.sleep(2)

    try:
        import tkinter
        print("tkinter is installed")
        n += div
    except ImportError:
        print("tkinter is not installed")
        print("installing tkinter")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", 'tkinter'])
        print("tkinter is now installed")
        import tkinter
        n += div

    if round(n) == 100:
        print("All Packages are installed\nInitialising Encryptor[main.py]")
    else:
        print("Some Packages are not installed")
        print("Please restart the program again")
        time.sleep(2)
        exit()


__init()
