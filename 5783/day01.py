#!/usr/bin/env python3

import sqlite3

translation = {
    "a": "2", "b": "2", "c": "2",
    "d": "3", "e": "3", "f": "3",
    "g": "4", "h": "4", "i": "4",
    "j": "5", "k": "5", "l": "5",
    "m": "6", "n": "6", "o": "6",
    "p": "7", "q": "7", "r": "7", "s": "7",
    "t": "8", "u": "8", "v": "8",
    "w": "9", "x": "9", "y": "9", "z": "9"
}

conn = sqlite3.connect("data/noahs.sqlite")
curs = conn.cursor()

curs.execute("SELECT name, phone FROM customers")
for customer in curs.fetchall():
    name, phone = customer
    last_name = name.split(" ")[1].lower()
    translated = "".join(translation[letter] for letter in last_name)
    if translated == phone.replace("-", ""):
        print(f"{name}: {phone}")  # Answer is 488-836-2374
        break

curs.close()
conn.close()
