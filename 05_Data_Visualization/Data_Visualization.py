"""
Data Visualization Script for Data_Visualization.xlsx (Stage 5)
Processes cleaned transaction data and produces 10 high-resolution visual charts matching the project sheets.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_all_charts():
    # Configure global visual aesthetic styling
    sns.set_theme(style="whitegrid", font="sans-serif")
    plt.rcParams.update({
        'font.size': 11,
        'axes.labelsize': 12,
        'axes.titlesize': 14,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'figure.titlesize': 16
    })

    excel_file = "Data_Visualization.xlsx"
    fallback_csv = "cleandata.csv"
    fallback_xls = "cleandata (3).csv.xls"

    # Load dataset
    if os.path.exists(excel_file):
        print(f"Loading data from: {excel_file}")
        try:
            df = pd.read_excel(excel_file, sheet_name="Clean_Data")
        except Exception:
            df = pd.read_excel(excel_file, sheet_name=0)
    elif os.path.exists(fallback_csv):
        print(f"Loading data from: {fallback_csv}")
        df = pd.read_csv(fallback_csv)
    else:
        print(f"Loading data from fallback: {fallback_xls}")
        df = pd.read_csv(fallback_xls)

    # Clean header names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    df['invoice_date'] = pd.to_datetime(df['invoice_date'])
    if 'total_spend' not in df.columns:
        df['total_spend'] = df['quantity'] * df['price']

    # Age group categorization
    if 'age_group' not in df.columns:
        bins = [17, 30, 45, 60, 100]
        labels = ['18–30 (Young Adult)', '31–45 (Adult)', '46–60 (Middle Age)', '60+ (Senior)']
        df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

    if 'year_month' not in df.columns:
        df['year_month'] = df['invoice_date'].dt.to_period('M').astype(str)

    # Output directory setup
    output_dir = "charts_output"
    os.makedirs(output_dir, exist_ok=True)

    # Color Palette Definitions
    palette_primary = "Blues_r"
    palette_secondary = "Greens_r"
    palette_accent = "Purples_r"
    gender_colors = {'Female': '#3498db', 'Male': '#e74c3c'}
    payment_colors = ['#2ecc71', '#3498db', '#e74c3c']

    print("Generating Chart 1: Category Revenue Ranking...")
    # Chart 1: Category Revenue Ranking
    cat_rev = df.groupby('category')['total_spend'].sum().reset_index().sort_values(by='total_spend', ascending=False)
    plt.figure(figsize=(10, 6))
    ax1 = sns.barplot(data=cat_rev, x='total_spend', y='category', palette=palette_primary)
    plt.title('1. Category Revenue Ranking ($)', pad=15, fontweight='bold', color='#1f4e79')
    plt.xlabel('Total Revenue ($)')
    plt.ylabel('Category')
    for p in ax1.patches:
        val = f"${p.get_width():,.2f}"
        ax1.annotate(val, (p.get_width(), p.get_y() + p.get_height() / 2.),
                     ha='left', va='center', xytext=(7, 0), textcoords='offset points', fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '1_Category_Revenue_Ranking.png'), dpi=300)
    plt.close()

    print("Generating Chart 2: Category Revenue Split by Gender...")
    # Chart 2: Category Revenue Split by Gender
    cat_gen = df.groupby(['category', 'gender'])['total_spend'].sum().reset_index()
    plt.figure(figsize=(12, 6))
    ax2 = sns.barplot(data=cat_gen, x='category', y='total_spend', hue='gender', palette=gender_colors)
    plt.title('2. Category Revenue Split by Gender ($)', pad=15, fontweight='bold', color='#1f4e79')
    plt.xlabel('Category')
    plt.ylabel('Total Revenue ($)')
    plt.legend(title='Gender')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '2_Category_Gender_Split.png'), dpi=300)
    plt.close()

    print("Generating Chart 3: Revenue by Shopping Mall...")
    # Chart 3: Shopping Mall Revenue
    mall_rev = df.groupby('shopping_mall')['total_spend'].sum().reset_index().sort_values(by='total_spend', ascending=False)
    plt.figure(figsize=(10, 6))
    ax3 = sns.barplot(data=mall_rev, x='total_spend', y='shopping_mall', palette=palette_secondary)
    plt.title('3. Revenue by Shopping Mall ($)', pad=15, fontweight='bold', color='#1f4e79')
    plt.xlabel('Total Revenue ($)')
    plt.ylabel('Shopping Mall')
    for p in ax3.patches:
        val = f"${p.get_width():,.2f}"
        ax3.annotate(val, (p.get_width(), p.get_y() + p.get_height() / 2.),
                     ha='left', va='center', xytext=(7, 0), textcoords='offset points', fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '3_Shopping_Mall_Revenue.png'), dpi=300)
    plt.close()

    print("Generating Chart 4: Payment Method Share...")
    # Chart 4: Payment Method Proportions
    pay_share = df['payment_method'].value_counts().reset_index()
    pay_share.columns = ['payment_method', 'count']
    plt.figure(figsize=(8, 8))
    plt.pie(pay_share['count'], labels=pay_share['payment_method'], autopct='%1.1f%%',
            startangle=140, colors=payment_colors, explode=(0.03, 0.03, 0.03),
            textprops={'fontsize': 11, 'fontweight': 'bold'})
    plt.title('4. Payment Method Transaction Share', pad=15, fontweight='bold', color='#1f4e79')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '4_Payment_Method_Share.png'), dpi=300)
    plt.close()

    print("Generating Chart 5: Age Group Spending Capacity...")
    # Chart 5: Spending Capacity by Customer Age Brackets
    age_rev = df.groupby('age_group', observed=False)['total_spend'].sum().reset_index()
    plt.figure(figsize=(9, 6))
    ax5 = sns.barplot(data=age_rev, x='age_group', y='total_spend', palette=palette_accent)
    plt.title('5. Spending Capacity by Customer Age Brackets ($)', pad=15, fontweight='bold', color='#1f4e79')
    plt.xlabel('Age Group')
    plt.ylabel('Total Revenue ($)')
    for p in ax5.patches:
        val = f"${p.get_height():,.2f}"
        ax5.annotate(val, (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha='center', va='bottom', xytext=(0, 5), textcoords='offset points', fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '5_Age_Group_Spending.png'), dpi=300)
    plt.close()

    print("Generating Chart 6: Monthly Purchasing Revenue Trend Over Time...")
    # Chart 6: Time-Series Revenue Trend
    monthly_trend = df.groupby('year_month')['total_spend'].sum().reset_index().sort_values(by='year_month')
    plt.figure(figsize=(14, 6))
    plt.plot(monthly_trend['year_month'], monthly_trend['total_spend'], marker='o', linewidth=2.5, color='#008080')
    plt.title('6. Monthly Purchasing Revenue Trend Over Time ($)', pad=15, fontweight='bold', color='#1f4e79')
    plt.xlabel('Year-Month')
    plt.ylabel('Monthly Revenue ($)')
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '6_Monthly_Sales_Trend.png'), dpi=300)
    plt.close()

    print("Generating Chart 7: Revenue by Purchase Quantity...")
    # Chart 7: Revenue by Purchase Quantity
    qty_rev = df.groupby('quantity')['total_spend'].sum().reset_index()
    plt.figure(figsize=(9, 6))
    ax7 = sns.barplot(data=qty_rev, x='quantity', y='total_spend', palette="Blues_d")
    plt.title('7. Revenue by Purchase Quantity ($)', pad=15, fontweight='bold', color='#1f4e79')
    plt.xlabel('Items Purchased per Order (Quantity)')
    plt.ylabel('Total Revenue ($)')
    for p in ax7.patches:
        val = f"${p.get_height():,.2f}"
        ax7.annotate(val, (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha='center', va='bottom', xytext=(0, 5), textcoords='offset points', fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '7_Quantity_vs_Revenue.png'), dpi=300)
    plt.close()

    print("Generating Chart 8: Category x Gender Revenue Stacked...")
    # Chart 8: Category x Gender Revenue Stacked
    cat_gen_pivot = df.pivot_table(index='category', columns='gender', values='total_spend', aggfunc='sum')
    cat_gen_pivot = cat_gen_pivot.loc[cat_gen_pivot.sum(axis=1).sort_values(ascending=True).index]
    ax8 = cat_gen_pivot.plot(kind='barh', stacked=True, figsize=(10, 6), color=['#3498db', '#e74c3c'])
    plt.title('8. Category x Gender Revenue Stacked ($)', pad=15, fontweight='bold', color='#1f4e79')
    plt.xlabel('Total Revenue ($)')
    plt.ylabel('Category')
    plt.legend(title='Gender')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '8_Category_Gender_Stacked.png'), dpi=300)
    plt.close()

    print("Generating Chart 9: Average Order Value (AOV) per Shopping Mall...")
    # Chart 9: AOV per Mall
    mall_aov = df.groupby('shopping_mall')['total_spend'].mean().reset_index().sort_values(by='total_spend', ascending=False)
    plt.figure(figsize=(10, 6))
    ax9 = sns.barplot(data=mall_aov, x='total_spend', y='shopping_mall', palette="YlGnBu_r")
    plt.title('9. Average Order Value (AOV) per Shopping Mall ($)', pad=15, fontweight='bold', color='#1f4e79')
    plt.xlabel('Average Spend ($)')
    plt.ylabel('Shopping Mall')
    for p in ax9.patches:
        val = f"${p.get_width():,.2f}"
        ax9.annotate(val, (p.get_width(), p.get_y() + p.get_height() / 2.),
                     ha='left', va='center', xytext=(7, 0), textcoords='offset points', fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '9_AOV_per_Shopping_Mall.png'), dpi=300)
    plt.close()

    print("Generating Chart 10: Total Product Volume Sold (Units)...")
    # Chart 10: Product Volume Units
    cat_units = df.groupby('category')['quantity'].sum().reset_index().sort_values(by='quantity', ascending=False)
    plt.figure(figsize=(10, 6))
    ax10 = sns.barplot(data=cat_units, x='quantity', y='category', palette="Oranges_r")
    plt.title('10. Total Product Volume Sold (Units)', pad=15, fontweight='bold', color='#1f4e79')
    plt.xlabel('Total Units Sold')
    plt.ylabel('Category')
    for p in ax10.patches:
        val = f"{int(p.get_width()):,} units"
        ax10.annotate(val, (p.get_width(), p.get_y() + p.get_height() / 2.),
                     ha='left', va='center', xytext=(7, 0), textcoords='offset points', fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '10_Product_Volume_Units.png'), dpi=300)
    plt.close()

    print("All 10 charts generated and saved successfully into 'charts_output/'!")

if __name__ == "__main__":
    generate_all_charts()
