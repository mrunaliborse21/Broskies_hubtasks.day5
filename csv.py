# ✅ Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Optional for Jupyter
# %matplotlib inline

# ✅ Step 2: Set CSV file path (EITHER same folder OR full path)
file_path = r"C:\Users\Mrunali\Desktop\sales_data.csv"   # <-- change this line to match your file location

# ✅ Step 3: Load CSV file
try:
    df = pd.read_csv(file_path)
    print("✅ CSV file loaded successfully!\n")
except FileNotFoundError:
    print(f"❌ Error: File '{file_path}' not found. Please check the file path.")
    exit()

# ✅ Step 4: Explore dataset
print("---- First 5 rows ----")
print(df.head())

print("\n---- Dataset Info ----")
print(df.info())

print("\n---- Summary Statistics ----")
print(df.describe())

# ✅ Step 5: Analysis - Total Sales by Product
if 'Product' in df.columns and 'Sales' in df.columns:
    sales_by_product = df.groupby('Product')['Sales'].sum()
    print("\n---- Total Sales by Product ----")
    print(sales_by_product)

    sales_by_product.plot(kind='bar', figsize=(10, 5), color='skyblue')
    plt.title('Total Sales by Product')
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("\n⚠️ Please check your CSV columns. Expected: 'Product' and 'Sales'")

# ✅ Step 6: Optional - Sales by Month (if Date column exists)
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Month'] = df['Date'].dt.to_period('M')
    sales_by_month = df.groupby('Month')['Sales'].sum()

    print("\n---- Total Sales by Month ----")
    print(sales_by_month)

    sales_by_month.plot(kind='line', marker='o', figsize=(10, 5), color='orange')
    plt.title('Total Sales by Month')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
