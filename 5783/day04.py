#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect("data/noahs.sqlite")
curs = conn.cursor()

# Select the phone number of the person who consistently goes to Noah's between 4 and 6,
# since the question makes it seem habitual
curs.execute("""
    SELECT
      a.name,
      a.phone
    FROM customers a
    JOIN orders b
      ON a.customerid = b.customerid
      AND STRFTIME('%H', b.ordered) IN ('04', '05', '06')
    JOIN orders_items c
      ON b.orderid = c.orderid
      AND c.sku LIKE 'BKY%'
    GROUP BY phone
    ORDER BY COUNT(*) DESC LIMIT 1
""")
name, phone = curs.fetchone()
print(f"{name}: {phone}")  # Answer is 718-649-9036

curs.close()
conn.close()
