import pandas as pd
import sqlite3

# Load Excel dataset
df = pd.read_excel("dataset/SQL_Sales_Dataset_200_Rows.xlsx")

# Create SQLite database
connection = sqlite3.connect("database/sales.db")

# Save Excel data as a SQL table
df.to_sql("sales", connection, if_exists="replace", index=False)

connection.close()

print("Database created successfully!")
print(f"Rows inserted: {len(df)}")