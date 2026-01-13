def transform_orders(df):
    # Remove duplicates
    df = df.drop_duplicates(subset=["order_id"])

    # Business rule
    df["total_amount"] = df["quantity"] * df["unit_price"]

    # Keep only completed orders
    df = df[df["status"] == "completed"]

    # Data quality
    df = df.dropna(subset=["customer_id"])

    return df
