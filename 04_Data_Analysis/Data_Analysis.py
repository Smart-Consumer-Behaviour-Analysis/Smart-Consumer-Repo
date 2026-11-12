"""
Data Analysis Script for Smart Consumer Behaviour Analysis (Stage 4)
Processes cleaned customer transaction data and exports analytical summaries to an Excel workbook.
"""

import os
import pandas as pd
import numpy as np

def run_data_analysis():
    # 1. Load Cleaned Dataset
    data_files = ["cleandata.csv", "cleandata (3).csv.xls", "Data_Visualization.xlsx"]
    df = None
    
    for file_path in data_files:
        if os.path.exists(file_path):
            try:
                if file_path.endswith('.xlsx'):
                    df = pd.read_excel(file_path, sheet_name="Clean_Data")
                else:
                    df = pd.read_csv(file_path)
                print(f"Successfully loaded dataset from: {file_path}")
                break
            except Exception as e:
                continue

    if df is None:
        raise FileNotFoundError("Cleaned dataset file not found.")

    # Standardize column headers
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    df['invoice_date'] = pd.to_datetime(df['invoice_date'])

    # Section 2 & 3: Calculate Sales Amount (Quantity * Price)
    df['sales_amount'] = df['quantity'] * df['price']

    # Section 6: Define Age Brackets
    if 'age_group' not in df.columns:
        bins = [17, 30, 45, 60, 100]
        labels = ['18–30 (Young Adult)', '31–45 (Adult)', '46–60 (Middle Age)', '60+ (Senior)']
        df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

    # --- Section 3: Overall Performance Analysis (KPIs) ---
    total_transactions = len(df)
    unique_customers = df['customer_id'].nunique()
    total_quantity = df['quantity'].sum()
    total_sales = df['sales_amount'].sum()
    avg_transaction_val = df['sales_amount'].mean()

    kpi_summary = pd.DataFrame([
        {"Metric": "Total Transactions", "Result": f"{total_transactions:,}"},
        {"Metric": "Unique Customers", "Result": f"{unique_customers:,}"},
        {"Metric": "Total Quantity", "Result": f"{total_quantity:,}"},
        {"Metric": "Total Sales ($)", "Result": f"{total_sales:,.2f}"},
        {"Metric": "Average Transaction Value ($)", "Result": f"{avg_transaction_val:,.2f}"},
        {"Metric": "Highest Sales Category", "Result": df.groupby('category')['sales_amount'].sum().idxmax()},
        {"Metric": "Most Used Payment Method", "Result": df['payment_method'].mode()[0]},
        {"Metric": "Highest Sales Shopping Mall", "Result": df.groupby('shopping_mall')['sales_amount'].sum().idxmax()},
        {"Metric": "Highest Sales Age Group", "Result": str(df.groupby('age_group', observed=False)['sales_amount'].sum().idxmax())},
        {"Metric": "Highest Sales Gender Group", "Result": df.groupby('gender')['sales_amount'].sum().idxmax()}
    ])

    # --- Section 4: Product Category Analysis ---
    category_analysis = df.groupby('category').agg(
        transaction_count=('invoice_no', 'count'),
        total_quantity=('quantity', 'sum'),
        total_sales=('sales_amount', 'sum'),
        avg_price=('price', 'mean')
    ).reset_index().sort_values(by='total_sales', ascending=False)
    category_analysis['sales_share_%'] = (category_analysis['total_sales'] / total_sales * 100).round(2)

    # --- Section 5: Gender Analysis ---
    gender_analysis = df.groupby('gender').agg(
        transaction_count=('invoice_no', 'count'),
        total_quantity=('quantity', 'sum'),
        total_sales=('sales_amount', 'sum'),
        avg_spend=('sales_amount', 'mean')
    ).reset_index()
    gender_analysis['sales_share_%'] = (gender_analysis['total_sales'] / total_sales * 100).round(2)

    # --- Section 6: Age Group Analysis ---
    age_analysis = df.groupby('age_group', observed=False).agg(
        transaction_count=('invoice_no', 'count'),
        total_quantity=('quantity', 'sum'),
        total_sales=('sales_amount', 'sum'),
        avg_spend=('sales_amount', 'mean')
    ).reset_index()
    age_analysis['sales_share_%'] = (age_analysis['total_sales'] / total_sales * 100).round(2)

    # --- Section 7: Payment Method Analysis ---
    payment_analysis = df.groupby('payment_method').agg(
        transaction_count=('invoice_no', 'count'),
        total_sales=('sales_amount', 'sum'),
        avg_transaction=('sales_amount', 'mean')
    ).reset_index().sort_values(by='total_sales', ascending=False)
    payment_analysis['transaction_share_%'] = (payment_analysis['transaction_count'] / total_transactions * 100).round(2)

    # --- Section 8: Shopping Mall Analysis ---
    mall_analysis = df.groupby('shopping_mall').agg(
        transaction_count=('invoice_no', 'count'),
        total_quantity=('quantity', 'sum'),
        total_sales=('sales_amount', 'sum'),
        avg_transaction=('sales_amount', 'mean')
    ).reset_index().sort_values(by='total_sales', ascending=False)
    mall_analysis['sales_share_%'] = (mall_analysis['total_sales'] / total_sales * 100).round(2)

    # --- Section 9: Time-Based Monthly Analysis ---
    df['year_month'] = df['invoice_date'].dt.to_period('M').astype(str)
    monthly_analysis = df.groupby('year_month').agg(
        transaction_count=('invoice_no', 'count'),
        total_quantity=('quantity', 'sum'),
        total_sales=('sales_amount', 'sum')
    ).reset_index().sort_values(by='year_month')

    # --- Section 10: Quantity and Price Analysis ---
    quantity_price_analysis = df.groupby('quantity').agg(
        transaction_count=('invoice_no', 'count'),
        avg_unit_price=('price', 'mean'),
        total_sales=('sales_amount', 'sum'),
        avg_sales_per_order=('sales_amount', 'mean')
    ).reset_index()

    # Section 14: Export Analytical Results Workbook
    output_excel = "Data_Analysis_Results.xlsx"
    with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
        kpi_summary.to_excel(writer, sheet_name='KPI_Summary', index=False)
        category_analysis.to_excel(writer, sheet_name='Category_Analysis', index=False)
        gender_analysis.to_excel(writer, sheet_name='Gender_Analysis', index=False)
        age_analysis.to_excel(writer, sheet_name='Age_Group_Analysis', index=False)
        payment_analysis.to_excel(writer, sheet_name='Payment_Analysis', index=False)
        mall_analysis.to_excel(writer, sheet_name='Shopping_Mall_Analysis', index=False)
        monthly_analysis.to_excel(writer, sheet_name='Monthly_Trends', index=False)
        quantity_price_analysis.to_excel(writer, sheet_name='Quantity_Price_Analysis', index=False)

    print("Data analysis execution completed successfully.")
    print(f"Exported analytical workbook to: {output_excel}")

if __name__ == "__main__":
    run_data_analysis()
