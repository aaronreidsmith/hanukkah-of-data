#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect("data/noahs.sqlite")
curs = conn.cursor()

# Find the person who generates the least profit for Noah
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
    GROUP BY phone
    ORDER BY SUM(c.qty * (c.unit_price - d.wholesale_cost)) ASC
    LIMIT 1
""")
name, phone = curs.fetchone()
print(f"{name}: {phone}")  # Answer is 914-868-0316

curs.close()
conn.close()
