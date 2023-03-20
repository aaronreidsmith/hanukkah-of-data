#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect("data/noahs.sqlite")
curs = conn.cursor()

curs.execute("""
    SELECT
      a.name,
      a.phone
    FROM customers a
    JOIN orders b
      ON a.customerid = b.customerid
      AND b.ordered < '2018-01-01'
    JOIN orders_items c
      ON b.orderid = c.orderid
    JOIN products d
      ON c.sku = d.sku
      AND d.desc LIKE '%Bagel'
    WHERE SUBSTR(SUBSTR(a.name, 1, INSTR(a.name, ' ') - 1), 1, 1) = 'J'
    AND SUBSTR(SUBSTR(a.name, INSTR(a.name, ' ') + 1), 1, 1) = 'D'
""")
name, phone = curs.fetchone()
print(f"{name}: {phone}")  # Answer is 212-771-8924

curs.close()
conn.close()
