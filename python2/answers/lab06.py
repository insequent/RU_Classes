#!/usr/bin/python3

"""
    Lab06 - Decorators
"""

import inspect
import random

names = ["Susan","Carol","Bob","Jeanette","Larry","John"]

def bouncer(func):
    def kick_bob(attendees):
        print("Looking for Bob...")
        if "Bob" in attendees:
            print("Dropping Bob...")
            attendees.remove("Bob")
        func(attendees)
    return kick_bob

@bouncer
def party(attendees):
    print("List of people going to the party: {}".format(", ".join(attendees)))

party(names)

print(party)
print(bouncer)
looksee = inspect.getmembers(bouncer)
for x, y in looksee:
    if type(y) is not dict:
        print("{}: {}".format(x, y))
