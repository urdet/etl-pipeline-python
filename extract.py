import pandas as pd
from sqlalchemy import create_engine
from config import MYSQL_URI

engine = create_engine(MYSQL_URI)

def extract_orders(last_run):
    query = f"""
        SELECT order_id, customer_id, quantity, unit_price,
               status, updated_at
        FROM orders
        WHERE updated_at > '{last_run}'
    """
    df = pd.read_sql(query, engine)
    return df
