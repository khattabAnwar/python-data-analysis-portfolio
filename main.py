import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the CSV file
df = pd.read_csv("sample_sales_100.csv",encoding="latin1")
print("✅ Data Loaded Successfully!\n")
print(df.head())

# 2. Basic Info
print("\n--- Data Info ---")
print(df.info())
print("\n--- Summary Statistics ---")
print(df.describe())

# 3. Clean Data
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# 4. insights
revenue_by_item = df.groupby("Item Type")["Total Revenue"].sum()
profit_by_channel = df.groupby("Sales Channel")["Total Profit"].sum()

print("\n--- Revenue by Item Type ---")
print(revenue_by_item)
print("\n--- Profit by Sales Channel ---")
print(profit_by_channel)

# 5. Visualizations
# Revenue by Item Type
plt.figure(figsize=(8,5))
revenue_by_item.plot(kind='bar')
plt.title("Total Revenue by Item Type")
plt.ylabel("Revenue")
plt.savefig("revenue_by_item.png")   # saves chart as image
plt.show()

# Profit by Sales Channel
plt.figure(figsize=(6,6))
profit_by_channel.plot(kind='pie', autopct='%1.1f%%')
plt.title("Profit Share by Sales Channel")
plt.ylabel("")
plt.savefig("profit_by_channel.png")
plt.show()

# Trend of Units Sold over Time
units_over_time = df.groupby("Order Date")["Units Sold"].sum()
plt.figure(figsize=(10,5))
units_over_time.plot(kind='line')
plt.title("Units Sold Over Time")
plt.xlabel("Date")
plt.ylabel("Units Sold")
plt.savefig("units_over_time.png")
plt.show()
