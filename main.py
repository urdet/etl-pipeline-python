from extract import extract_orders
from transform import transform_orders
from load import load_orders
from checkpoint import get_last_run, update_last_run
import cryptography
def run_etl():
    last_run = get_last_run()

    df = extract_orders(last_run)

    if df.empty:
        print("No new data.")
        return

    df = transform_orders(df)
    load_orders(df)
    update_last_run()

    print(f"Loaded {len(df)} records")
if __name__ == "__main__":
    run_etl()
