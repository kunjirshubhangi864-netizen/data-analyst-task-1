import pandas as pd

# --------------------------------------------------
# TASK 1: DATA CLEANING AND PREPROCESSING
# --------------------------------------------------

# 1. Load dataset
df = pd.read_csv("C:/Users/DELL/Downloads/sales_data.csv")

print("\n========== ORIGINAL DATA ==========")
print(df.head())

print("\nOriginal Shape:")
print(df.shape)

# --------------------------------------------------
# 2. Check column names
# --------------------------------------------------

print("\n========== ORIGINAL COLUMN NAMES ==========")
print(df.columns.tolist())

# --------------------------------------------------
# 3. Clean column names
# lowercase
# remove spaces
# replace spaces with underscore
# --------------------------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\n========== CLEAN COLUMN NAMES ==========")
print(df.columns.tolist())

# --------------------------------------------------
# 4. Check missing values
# --------------------------------------------------

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# --------------------------------------------------
# 5. Remove duplicate rows
# --------------------------------------------------

duplicates_before = df.duplicated().sum()

print("\nDuplicate rows found:")
print(duplicates_before)

df = df.drop_duplicates()

duplicates_after = df.duplicated().sum()

print("Duplicate rows after cleaning:")
print(duplicates_after)

# --------------------------------------------------
# 6. Standardize text columns
# --------------------------------------------------

text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].astype(str).str.strip()

# --------------------------------------------------
# 7. Convert date columns
# --------------------------------------------------

for column in df.columns:
    if "date" in column.lower():
        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )

# --------------------------------------------------
# 8. Handle missing values
# --------------------------------------------------

numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Fill missing text values
text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].fillna("Unknown")

# --------------------------------------------------
# 9. Check data types
# --------------------------------------------------

print("\n========== DATA TYPES ==========")
print(df.dtypes)

# --------------------------------------------------
# 10. Check missing values after cleaning
# --------------------------------------------------

print("\n========== MISSING VALUES AFTER CLEANING ==========")
print(df.isnull().sum())

# --------------------------------------------------
# 11. Check duplicates after cleaning
# --------------------------------------------------

print("\n========== DUPLICATES AFTER CLEANING ==========")
print(df.duplicated().sum())

# --------------------------------------------------
# 12. Final dataset information
# --------------------------------------------------

print("\n========== FINAL DATA ==========")

print(df.head())

print("\nFinal Shape:")
print(df.shape)

# --------------------------------------------------
# 13. Save cleaned dataset
# --------------------------------------------------

df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("File: cleaned_sales_data.csv")

# --------------------------------------------------
# 14. Save Excel version
# --------------------------------------------------

df.to_excel("cleaned_sales_data.xlsx", index=False)

print("Excel file saved successfully!")
print("File: cleaned_sales_data.xlsx")
