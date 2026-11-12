import pandas as pd

# Load raw data
df = pd.read_csv("customer_2000_entries_raw.csv")

# Standardize column names
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
)

# Remove empty rows and duplicates
df = df.dropna(how="all").drop_duplicates()

# Clean text values
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

# Convert numeric columns
for col in ["serial_number", "age", "quantity", "price"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Convert date
df["invoice_date"] = pd.to_datetime(df["invoice_date"], errors="coerce")

# Fill missing numeric values with median
for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].median())

# Fill missing text values with mode
for col in df.select_dtypes(include="object").columns:
    if not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])

# Fill missing dates with median date
if df["invoice_date"].isna().any():
    dates = df["invoice_date"].dropna().sort_values()
    df["invoice_date"] = df["invoice_date"].fillna(dates.iloc[len(dates)//2])

# Fix invalid numeric values
df.loc[df["age"] <= 0, "age"] = df["age"].median()
df.loc[df["quantity"] <= 0, "quantity"] = df["quantity"].median()
df.loc[df["price"] < 0, "price"] = df["price"].median()

# Save cleaned data
df.to_csv("cleandata.csv", index=False)

print("Data cleaning completed successfully.")
print("Rows:", len(df))
print("Columns:", len(df.columns))
