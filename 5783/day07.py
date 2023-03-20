#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect("data/noahs.sqlite")
curs = conn.cursor()

# Find the person who bought the same item (but a different color) as Emily within seconds of her purchase
curs.execute("""
    WITH
      emilys_purchases AS (
        SELECT
          b.orderid,
          b.ordered,
          c.sku,
          d.desc
        FROM customers a
        JOIN orders b
          ON a.customerid = b.customerid
          AND a.phone = '914-868-0316'
        JOIN orders_items c
          ON b.orderid = c.orderid
        JOIN products d
          ON c.sku = d.sku
          AND d.desc LIKE '%)' -- Only select items that have a modifier at the end
    ),
    -- Same query for everyone EXCEPT emily (includes name and phone)
    other_purchases AS (
      SELECT
        a.name,
        a.phone,
        b.orderid,
        b.ordered,
        c.sku,
        d.desc
      FROM customers a
      JOIN orders b
        ON a.customerid = b.customerid
        AND a.phone <> '914-868-0316'
      JOIN orders_items c
        ON b.orderid = c.orderid
      JOIN products d
        ON c.sku = d.sku
        AND d.desc LIKE '%)' -- Only select items that have a modifier at the end
      WHERE DATE(b.ordered) IN (SELECT DATE(ordered) FROM emilys_purchases)
    )

    SELECT
      a.name,
      a.phone
    FROM other_purchases a
    JOIN emilys_purchases b
      ON a.desc <> b.desc
      AND SUBSTR(a.desc, 1, INSTR(a.desc, '(') - 2) = SUBSTR(b.desc, 1, INSTR(b.desc, '(') - 2)
      AND DATE(a.ordered) = DATE(b.ordered)
      AND ABS(STRFTIME('%s', a.ordered) - STRFTIME('%s', b.ordered)) < 10
""")
name, phone = curs.fetchone()
print(f"{name}: {phone}")  # Answer is 315-618-5263

curs.close()
conn.close()
