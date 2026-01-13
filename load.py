from sqlalchemy import create_engine
from config import POSTGRES_URI

engine = create_engine(POSTGRES_URI)

def load_orders(df):
    df.to_sql(
        "fact_orders",
        engine,
        if_exists="append",
        index=False,
        method="multi"
    )
