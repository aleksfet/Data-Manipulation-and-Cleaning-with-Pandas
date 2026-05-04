# Module 10 Assignment: Data Manipulation and Cleaning with Pandas
# UrbanStyle Customer Data Cleaning

# Import required libraries
import pandas as pd

# Welcome message
print("=" * 60)
print("URBANSTYLE CUSTOMER DATA CLEANING")
print("=" * 60)

# ----- USE THE FOLLOWING CODE TO SIMULATE A CSV FILE (DO NOT MODIFY) -----
from io import StringIO

# Simulated CSV content with intentional data issues
csv_content = """customer_id,first_name,last_name,email,phone,join_date,last_purchase,total_purchases,total_spent,preferred_category,satisfaction_rating,age,city,state,loyalty_status
CS001,John,Smith,johnsmith@email.com,(555) 123-4567,2023-01-15,2023-12-01,12,"1,250.99",Menswear,4.5,35,Tampa,FL,Gold
CS002,Emily,Johnson,emily.j@email.com,555.987.6543,01/25/2023,10/15/2023,8,$875.50,Womenswear,4,28,Miami,FL,Silver
CS003,Michael,Williams,mw@email.com,(555)456-7890,2023-02-10,2023-11-20,15,"2,100.75",Footwear,5,42,Orlando,FL,Gold
CS004,JESSICA,BROWN,jess.brown@email.com,5551234567,2023-03-05,2023-12-10,6,659.25,Womenswear,3.5,31,Tampa,FL,Bronze
CS005,David,jones,djones@email.com,555-789-1234,2023-03-20,2023-09-18,4,350.00,Menswear,,45,Jacksonville,FL,Bronze
CS006,Sarah,Miller,sarah_miller@email.com,(555) 234-5678,2023-04-12,2023-12-05,10,1450.30,Accessories,4,29,Tampa,FL,Silver
CS007,Robert,Davis,robert.davis@email.com,555.444.7777,04/30/2023,11/25/2023,7,$725.80,Footwear,4.5,38,Miami,FL,Silver
CS008,Jennifer,Garcia,jen.garcia@email.com,(555)876-5432,2023-05-15,2023-10-30,3,280.50,ACCESSORIES,3,25,Orlando,FL,Bronze
CS009,Michael,Williams,m.williams@email.com,5558889999,2023-06-01,2023-12-07,9,1100.00,Menswear,4,39,Jacksonville,FL,Silver
CS010,Emily,Johnson,emilyjohnson@email.com,555-321-6547,2023-06-15,2023-12-15,14,"1,875.25",Womenswear,4.5,27,Miami,FL,Gold
CS006,Sarah,Miller,sarah_miller@email.com,(555) 234-5678,2023-04-12,2023-12-05,10,1450.30,Accessories,4,29,Tampa,FL,Silver
CS011,Amanda,,amanda.p@email.com,(555) 741-8529,2023-07-10,,2,180.00,womenswear,3,32,Tampa,FL,Bronze
CS012,Thomas,Wilson,thomas.w@email.com,,2023-07-25,2023-11-02,5,450.75,menswear,4,44,Orlando,FL,Bronze
CS013,Lisa,Anderson,lisa.a@email.com,555.159.7530,08/05/2023,,0,0.00,Womenswear,,30,Miami,FL,
CS014,James,Taylor,jtaylor@email.com,555-951-7530,2023-08-20,2023-10-10,11,"1,520.65",Footwear,4.5,,Jacksonville,FL,Gold
CS015,Karen,Thomas,karen.t@email.com,(555) 357-9512,2023-09-05,2023-12-12,6,685.30,Womenswear,4,36,Tampa,FL,Silver
"""

# Create a StringIO object (simulates a file)
customer_data_csv = StringIO(csv_content)

# Now you can load this as if it was a CSV file:
# raw_df = pd.read_csv(customer_data_csv)
# ----- END OF SIMULATION CODE -----


# TODO 1: Load and Explore the Dataset
# 1.1 Load the dataset and display basic information
# REQUIRED: Store DataFrame in variable 'raw_df'
# Your code here
raw_df = pd.read_csv(customer_data_csv)

print("\nFirst 5 Rows:")
print(raw_df.head())
print("\nDataFrame Information:")
raw_df.info()

print("\nDataFrame Shape:")
print(raw_df.shape)

# 1.2 Assess the data quality issues (missing values, incorrect formats, duplicates)
# REQUIRED: Store initial missing value counts in 'initial_missing_counts' (pandas Series)
# REQUIRED: Store duplicate count in variable 'initial_duplicate_count' (int)
# Your code here
initial_missing_counts = raw_df.isnull().sum()
initial_duplicate_count = int(raw_df.duplicated().sum())

# TODO 2: Handle Missing Values
# 2.1 Identify and count missing values
# REQUIRED: Store in variable 'missing_value_report' (pandas Series)
# Your code here
missing_value_report = raw_df.isnull().sum()

# 2.2 Fill missing satisfaction_rating with the median value
# REQUIRED: Store median value used in variable 'satisfaction_median' (float)
# Your code here
satisfaction_median = float(raw_df["satisfaction_rating"].median())
df_missing = raw_df.copy()
df_missing["satisfaction_rating"] = df_missing["satisfaction_rating"].fillna(satisfaction_median)

# 2.3 Fill missing last_purchase dates appropriately
# REQUIRED: Store strategy used in variable 'date_fill_strategy' (string: 'forward_fill', 'backward_fill', or 'drop')
# Your code here
date_fill_strategy = "forward_fill"

# Fill so no missing dates remain
df_missing["last_purchase"] = df_missing["last_purchase"].ffill()
df_missing["last_purchase"] = df_missing["last_purchase"].bfill()

# 2.4 Handle other missing values as needed
# REQUIRED: Store cleaned DataFrame in variable 'df_no_missing'
# Your code here
df_missing["last_name"] = df_missing["last_name"].fillna("Unknown")
df_missing["phone"] = df_missing["phone"].fillna("Unknown")
df_missing["loyalty_status"] = df_missing["loyalty_status"].fillna("Bronze")
age_median = raw_df["age"].median()
df_missing["age"] = df_missing["age"].fillna(age_median)
df_no_missing = df_missing.copy()

# TODO 3: Correct Data Types
# 3.1 Convert join_date and last_purchase to datetime
# REQUIRED: Work with 'df_no_missing' and store result in 'df_typed'
# Your code here
df_typed = df_no_missing.copy()
df_typed["join_date"] = pd.to_datetime(df_typed["join_date"], errors="coerce")
df_typed["last_purchase"] = pd.to_datetime(df_typed["last_purchase"], errors="coerce")

# 3.2 Convert total_spent to numeric (handle currency symbols and commas)
# REQUIRED: Continue working with 'df_typed'
# Your code here
df_typed["total_spent"] = df_typed["total_spent"].astype(str)
df_typed["total_spent"] = df_typed["total_spent"].str.replace("$", "", regex=False)
df_typed["total_spent"] = df_typed["total_spent"].str.replace(",", "", regex=False)
df_typed["total_spent"] = pd.to_numeric(df_typed["total_spent"], errors="coerce")

# 3.3 Ensure other numeric fields (total_purchases, age) are correct types
# REQUIRED: Store final typed DataFrame in 'df_typed'
# Your code here
df_typed["total_purchases"] = pd.to_numeric(df_typed["total_purchases"], errors="coerce")
df_typed["age"] = pd.to_numeric(df_typed["age"], errors="coerce")
df_typed["satisfaction_rating"] = pd.to_numeric(df_typed["satisfaction_rating"], errors="coerce")
df_typed["total_purchases"] = df_typed["total_purchases"].astype(int)
df_typed["age"] = df_typed["age"].astype(int)

# TODO 4: Clean and Standardize Text Data
# 4.1 Standardize case for first_name and last_name (proper case)
# REQUIRED: Work with 'df_typed' and store result in 'df_text_cleaned'
# Your code here
df_text_cleaned = df_typed.copy()
df_text_cleaned["first_name"] = df_text_cleaned["first_name"].str.strip().str.title()
df_text_cleaned["last_name"] = df_text_cleaned["last_name"].str.strip().str.title()

# 4.2 Standardize category names (consistent capitalization)
# REQUIRED: Continue working with 'df_text_cleaned'
# Your code here
df_text_cleaned["preferred_category"] = df_text_cleaned["preferred_category"].str.strip().str.title()


# 4.3 Standardize phone numbers to a consistent format
# REQUIRED: Store standardized phone format used in variable 'phone_format' (string)
# Your code here
phone_format = "(###) ###-####"
def format_phone(phone_value):
    phone_str = str(phone_value)
    digits_only = ""

    for ch in phone_str:
        if ch.isdigit():
            digits_only += ch

    if len(digits_only) == 10:
        return f"({digits_only[0:3]}) {digits_only[3:6]}-{digits_only[6:10]}"
    else:
        return "Unknown"

df_text_cleaned["phone"] = df_text_cleaned["phone"].apply(format_phone)

# TODO 5: Remove Duplicates
# 5.1 Identify duplicate records
# REQUIRED: Store duplicate count in variable 'duplicate_count' (int)
# Your code here
duplicate_count = int(df_text_cleaned.duplicated().sum())

# 5.2 Remove duplicates while keeping the appropriate record
# REQUIRED: Work with 'df_text_cleaned' and store result in 'df_no_duplicates'
# Your code here
df_no_duplicates = df_text_cleaned.drop_duplicates().copy()

# TODO 6: Add Derived Features
# 6.1 Calculate days_since_last_purchase
# REQUIRED: Work with 'df_no_duplicates' and add column 'days_since_last_purchase'
# Your code here
anchor_date = df_no_duplicates["last_purchase"].max()
df_no_duplicates["days_since_last_purchase"] = (anchor_date - df_no_duplicates["last_purchase"]).dt.days


# 6.2 Calculate average_purchase_value (total_spent / total_purchases)
# REQUIRED: Add column 'average_purchase_value' to DataFrame
# Your code here
df_no_duplicates["average_purchase_value"] = (
    df_no_duplicates["total_spent"] /
    df_no_duplicates["total_purchases"]
)

# 6.3 Create a purchase_frequency_category (High, Medium, Low)
# REQUIRED: Add column 'purchase_frequency_category' using these rules:
# - High: >= 10 purchases
# - Medium: 5-9 purchases
# - Low: < 5 purchases
# Your code here
def get_purchase_frequency(total_purchases):
    if total_purchases >= 10:
        return "High"
    elif total_purchases >= 5:
        return "Medium"
    else:
        return "Low"

df_no_duplicates["purchase_frequency_category"] = df_no_duplicates["total_purchases"].map(get_purchase_frequency)


# TODO 7: Clean Up the DataFrame
# 7.1 Rename columns to more readable formats
# REQUIRED: Store renamed DataFrame in 'df_renamed'
# Your code here
df_renamed = df_no_duplicates.rename(columns={
    "customer_id": "Customer_ID",
    "first_name": "First_Name",
    "last_name": "Last_Name",
    "email": "Email",
    "phone": "Phone",
    "join_date": "Join_Date",
    "last_purchase": "Last_Purchase",
    "total_purchases": "Total_Purchases",
    "total_spent": "total_spent",
    "preferred_category": "Preferred_Category",
    "satisfaction_rating": "Satisfaction_Rating",
    "age": "Age",
    "city": "City",
    "state": "State",
    "loyalty_status": "Loyalty_Status",
    "days_since_last_purchase": "Days_Since_Last_Purchase",
    "average_purchase_value": "Average_Purchase_Value",
    "purchase_frequency_category": "Purchase_Frequency_Category"
})

# 7.2 Remove any unnecessary columns
# REQUIRED: Store cleaned DataFrame in 'df_final'
# Your code here
df_final = df_renamed.drop(columns=["Email"]).copy()

# 7.3 Sort the data by a meaningful attribute
# REQUIRED: Sort 'df_final' by total_spent descending and store in 'df_final'
# Your code here
df_final = df_final.sort_values(by="total_spent", ascending=False)

# TODO 8: Generate Insights from Cleaned Data
# 8.1 Calculate average spent by loyalty_status
# REQUIRED: Store result in 'avg_spent_by_loyalty' (pandas Series)
# Your code here
avg_spent_by_loyalty = df_final.groupby("Loyalty_Status")["total_spent"].mean()

# 8.2 Find top preferred categories by total_spent
# REQUIRED: Store result in 'category_revenue' (pandas Series, sorted descending)
# Your code here
category_revenue = df_final.groupby("Preferred_Category")["total_spent"].sum().sort_values(ascending=False)

# 8.3 Calculate correlation between satisfaction_rating and total_spent
# REQUIRED: Store correlation value in 'satisfaction_spend_corr' (float)
# Your code here
satisfaction_spend_corr = float(df_final["Satisfaction_Rating"].corr(df_final["total_spent"]))

# TODO 9: Generate Final Report
print("\n" + "=" * 60)
print("URBANSTYLE CUSTOMER DATA CLEANING REPORT")
print("=" * 60)

# 9.1 Report on data quality issues found and how they were addressed
# REQUIRED OUTPUT FORMAT:
# Data Quality Issues:
# - Missing Values: X total missing entries
# - Duplicates: X duplicate records found
# - Data Type Issues: [list issues]
# Your code here
print("Data Quality Issues:")
print(f"- Missing Values: {int(initial_missing_counts.sum())} total missing entries")
print(f"- Duplicates: {initial_duplicate_count} duplicate records found")
print("- Data Type Issues: join_date and last_purchase were text, total_spent had currency symbols/commas, and numeric fields needed conversion")

# 9.2 Describe the changes made to standardize the dataset
# REQUIRED OUTPUT FORMAT:
# Standardization Changes:
# - Names: Converted to proper case
# - Categories: [describe standardization]
# - Phone Numbers: [describe format]
# Your code here
print("\nStandardization Changes:")
print("- Names: Converted to proper case")
print("- Categories: Standardized to consistent title case")
print(f"- Phone Numbers: Standardized to {phone_format}")

# 9.3 Present key business insights from the cleaned data
# REQUIRED OUTPUT FORMAT:
# Key Business Insights:
# - Customer Base: X total customers
# - Revenue by Loyalty: [show averages]
# - Top Category: [category] with $X revenue
# Your code here
top_category_name = category_revenue.idxmax()
top_category_value = category_revenue.max()
print("\nKey Business Insights:")
print(f"- Customer Base: {len(df_final)} total customers")
print("- Revenue by Loyalty:")
print(avg_spent_by_loyalty)
print(f"- Top Category: {top_category_name} with ${top_category_value:,.2f} revenue")
print(f"- Satisfaction/Spending Correlation: {satisfaction_spend_corr:.2f}")


# 9.4 Display the first few rows of the clean, analysis-ready dataset
# REQUIRED: Display first 5 rows of 'df_final'
# Your code here
print("\nFinal Cleaned Dataset:")
print(df_final.head())