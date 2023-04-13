import sqlite3
import json
from models import Order, Metal, Size, Style


def get_all_orders():
    """Method docstring."""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.metal_id,
            a.size_id,
            a.style_id,
            m.metal metal_metal,
            m.price metal_price,
            z.carets size_carets,
            z.price size_price,
            y.style style_style,
            y.price style_price
        FROM `order` a
        JOIN metal m
            ON m.id = a.metal_id
        JOIN size z
            ON z.id = a.size_id
        JOIN style y
            ON y.id = a.style_id
        """)

        orders = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            order = Order(row['id'], row['metal_id'], row['size_id'], row['style_id'])

            metal = Metal(row['id'], row['metal_metal'], row['metal_price'])
            size = Size(row['id'], row['size_carets'], row['size_price'])
            style = Style(row['id'], row['style_style'], row['style_price'])

            order.metal = metal.__dict__
            order.size = size.__dict__
            order.style = style.__dict__

            orders.append(order.__dict__)

    return orders
def get_single_order(id):
    """Method docstring."""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.metal_id,
            a.size_id,
            a.style_id
        FROM `order` a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        order = Order(data['id'], data['metal_id'], data['size_id'], data['style_id'])

        return order.__dict__

def delete_order(id):
    """Method docstring."""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM `order`
        WHERE id = ?
        """, (id, ))

def update_order(id, new_order):
    """Method docstring."""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE `order`
            SET
                metal_id = ?,
                size_id = ?,
                style_id = ?
        WHERE id = ?
        """, (new_order['metal_id'], new_order['size_id'],
              new_order['style_id'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True

def create_order(new_order):
    """Method docstring."""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO `order`
            ( metal_id, size_id, style_id )
        VALUES
            ( ?, ?, ? );
        """, (new_order['metal_id'], new_order['size_id'],
              new_order['style_id'], ))

        id = db_cursor.lastrowid

        new_order['id'] = id


    return new_order