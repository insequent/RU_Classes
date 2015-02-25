#!/usr/bin/python3

"""
    Lab05 Subprocess Module

"""


import platform
import subprocess
from sys import exc_info


def commander(*commands):
    """ Runs any number of given commands """

    for command in commands:
        print("Commander: running '{}'".format(command.split()))
        p = subprocess.Popen(command, stdout=subprocess.PIPE)
        result = p.communicate()
        print("DONE! Output is:\r\n{}\r\n".format(result))

if __name__ == "__main__":
    
    print("Calling 'ls -l'...")
    p = subprocess.call(("ls","-l"), stdout=subprocess.PIPE)
    print("DONE! The command {}\r\n".format("succeeded" if not p else "failed"))

    print("Calling 'ls -l'...")
    p = subprocess.call(("ls","-l"), stdout=None)
    print("DONE! The command {}\r\n".format("succeeded" if not p else "failed"))

    print("Calling '/bogus/command'...")
    try:
        p = subprocess.call("/bogus/command")
    except OSError:
        exc, exc_mess, exc_trace = exc_info()
        print("DONE! Error returned was: {}: {}\r\n".format(exc.__name__, exc_mess))

    my_os = platform.system()

    if my_os == "Linux":
        print("Oh running 'Linux' eh?... That doesn\'t actually narrow things down.")
        subprocess.call(r"echo 'Yo!' > tempy;cat tempy", shell=True)
        print("DONE! Ran: bash echo 'Yo!' > tempy;cat tempy\r\n")
    
    print("Calling 'du -h'...")
    p = subprocess.Popen(('du','-h'), stdout=subprocess.PIPE)
    result = p.communicate()
    print("DONE! Output is:\r\n{}\r\n".format(result))
