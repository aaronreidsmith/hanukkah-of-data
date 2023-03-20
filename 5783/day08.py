#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect("data/noahs.sqlite")
curs = conn.cursor()

# Find the person who bought the same item (but a different color) as Emily within seconds of her purchase
curs.execute("""
    SELECT
      a.name,
      a.phone
    FROM customers a
    JOIN orders b
      ON a.customerid = b.customerid
    JOIN orders_items c
      ON b.orderid = c.orderid
    JOIN products d
      ON c.sku = d.sku
      AND d.desc LIKE 'Noah%'
    GROUP BY a.name, a.phone
    ORDER BY COUNT(DISTINCT d.desc) DESC
    LIMIT 1
""")
name, phone = curs.fetchone()
print(f"{name}: {phone}")  # Answer is 929-906-5980

curs.close()
conn.close()
