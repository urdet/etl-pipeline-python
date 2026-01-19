import pandas as pd
from sqlalchemy import create_engine, text
from config import MYSQL_URI

engine = create_engine(MYSQL_URI)

def extract_orders(last_run=None):
    if last_run:
        query = text("""
            SELECT order_id, customer_id, quantity, unit_price,
                   status, updated_at
            FROM orders
            WHERE updated_at > :last_run
        """)
        df = pd.read_sql(query, engine, params={"last_run": last_run})
    else:
        query = text("""
            SELECT order_id, customer_id, quantity, unit_price,
                   status, updated_at
            FROM orders
        """)
        df = pd.read_sql(query, engine)

    return df