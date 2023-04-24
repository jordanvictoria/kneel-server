import sqlite3
import json
from models import Metal

def get_all_metals(query_params):
    """Method docstring."""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        sort_by = ""

        if len(query_params) != 0:
            param = query_params[0]
            [qs_key, qs_value] = param.split("=")

            if qs_key == "_sortBy":
                if qs_value == "price":
                    sort_by = "ORDER BY price"

        sql_to_execute = f"""
        SELECT
            a.id,
            a.metal,
            a.price
        FROM metal a
        {sort_by}
        """
        db_cursor.execute(sql_to_execute)

        metals = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            metal = Metal(row['id'], row['metal'], row['price'])
            

            metals.append(metal.__dict__)

    return metals
def get_single_metal(id):
    """Method docstring."""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.metal,
            a.price
        FROM metal a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        metal = Metal(data['id'], data['metal'], data['price'])

        return metal.__dict__

def update_metal(id, new_metal):
    """Method docstring."""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE metal
            SET
                metal = ?,
                price = ?
        WHERE id = ?
        """, (new_metal['metal'], new_metal['price'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
