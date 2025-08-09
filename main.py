import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("bread_sales_dataset.csv")

# 1. Quantity sold over time
df.groupby("Date")["Quantity_Sold"].sum().plot(figsize=(8,5), title="Quantity Sold Over Time")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("quantity_sold_over_time.png")
plt.close()  

# 2. Total sales over time
df.groupby("Date")["Total_Sales"].sum().plot(figsize=(8,5), title="Total Sales Over Time")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("total_sales_over_time.png")
plt.close()

# 3. Quantity sold by bread type
df.groupby("Bread_Type")["Quantity_Sold"].sum().plot(kind="bar", figsize=(8,5), title="Total Quantity Sold by Bread Type")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.savefig("quantity_sold_by_bread_type.png")
plt.close() 

# 4. Average unit price by bread type
df.groupby("Bread_Type")["Unit_Price"].mean().plot(kind="bar", figsize=(8,5), title="Average Unit Price by Bread Type")
plt.ylabel("Average Price ($)")
plt.tight_layout()
plt.savefig("average_unit_price_by_bread_type.png")
plt.close()

# 5. Total sales by store location
df.groupby("Store_Location")["Total_Sales"].sum().plot(kind="bar", figsize=(8,5), title="Total Sales by Store Location")
plt.ylabel("Total Sales ($)")
plt.tight_layout()
plt.savefig("total_sales_by_store_location.png")
plt.close()

# 6. Sales share by bread type (pie chart)
df.groupby("Bread_Type")["Total_Sales"].sum().plot(kind="pie", autopct="%1.1f%%", figsize=(6,6), title="Sales Share by Bread Type")
plt.ylabel("")
plt.tight_layout()
plt.savefig("sales_share_by_bread_type.png")
plt.close()

# 7. Quantity sold distribution (histogram)
df["Quantity_Sold"].plot(kind="hist", bins=20, figsize=(8,5), title="Quantity Sold Distribution")
plt.xlabel("Quantity Sold")
plt.tight_layout()
plt.savefig("quantity_sold_distribution.png")
plt.close()

# 8. Scatter plot: Unit Price vs Quantity Sold
df.plot(kind="scatter", x="Unit_Price", y="Quantity_Sold", figsize=(8,5), title="Unit Price vs Quantity Sold")
plt.tight_layout()
plt.savefig("unit_price_vs_quantity_sold.png")
plt.close()

# 9. Correlation heatmap (simple)
corr = df[["Quantity_Sold", "Unit_Price", "Total_Sales"]].corr()
plt.matshow(corr, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap", pad=20)
plt.savefig("correlation_heatmap.png")
plt.close()
