#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect("data/noahs.sqlite")
curs = conn.cursor()

curs.execute("""
    SELECT
      a.name,
      a.phone
    FROM customers a
    WHERE a.citystatezip = 'South Ozone Park, NY 11420' -- From question 2 (they live in the same neighborhood)
    AND (
      a.birthdate BETWEEN '1946-03-21' AND '1946-04-19'
      OR a.birthdate BETWEEN '1958-03-21' AND '1958-04-19'
      OR a.birthdate BETWEEN '1970-03-21' AND '1970-04-19'
      OR a.birthdate BETWEEN '1982-03-21' AND '1982-04-19'
      OR a.birthdate BETWEEN '1994-03-21' AND '1994-04-19'
      OR a.birthdate BETWEEN '2006-03-21' AND '2006-04-19'
      OR a.birthdate BETWEEN '2018-03-21' AND '2018-04-19'
    )
""")
name, phone = curs.fetchone()
print(f"{name}: {phone}")  # Answer is 516-636-7397

curs.close()
conn.close()
