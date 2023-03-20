#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect("data/noahs.sqlite")
curs = conn.cursor()

# Select the person from queens village who buys the most cat stuff
curs.execute("""
    SELECT
      a.name,
      a.phone
    FROM customers a
    JOIN orders b
      ON a.customerid = b.customerid
      AND a.citystatezip LIKE '%Queens Village%'
    JOIN orders_items c
      ON b.orderid = c.orderid
    JOIN products d
      ON c.sku = d.sku
      AND LOWER(d.desc) LIKE '%cat%'
    GROUP BY a.phone
    ORDER BY COUNT(*) DESC
    LIMIT 1
""")
name, phone = curs.fetchone()
print(f"{name}: {phone}")  # Answer is 315-492-7411

curs.close()
conn.close()
