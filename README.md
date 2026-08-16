# SQL Sales Data Analysis

## Project Overview

This project is part of a **Week 2 internship assignment focused on SQL for Data Analysis**.

The project uses a 200-row sales dataset and demonstrates how SQL can be used to retrieve, filter, aggregate, sort, and analyze business data using SQLite.

## Objectives

The main objectives of this project are to:

- Retrieve records using `SELECT`
- Filter records using `WHERE`
- Sort data using `ORDER BY`
- Perform calculations using `SUM()`, `AVG()`, and `COUNT()`
- Group data using `GROUP BY`
- Find top customers by total sales
- Use `LIMIT` to return top results
- Create conditional categories using `CASE`
- Use a subquery for comparative analysis

## Dataset

The project uses:

`SQL_Sales_Dataset_200_Rows.xlsx`

The dataset contains **200 sales records** with the following columns:

| Column | Description |
|---|---|
| `order_id` | Unique order identifier |
| `customer_name` | Customer name |
| `order_date` | Order date |
| `category` | Product category |
| `sub_category` | Product sub-category |
| `product_name` | Product name |
| `quantity` | Quantity ordered |
| `unit_price` | Unit price |
| `total_price` | Total price of the order |
| `region` | Sales region |

## SQL Analysis Performed

### 1. SELECT

Displayed customer name, category, and total price for all orders.

### 2. WHERE

Filtered orders belonging to the **Electronics** category.

### 3. ORDER BY

Sorted orders from highest to lowest `total_price`.

### 4. GROUP BY + SUM()

Calculated total sales for each category.

### 5. GROUP BY + AVG()

Calculated the average order value for each category.

### 6. GROUP BY + COUNT()

Calculated the number of orders in each region.

### 7. Customer Sales Analysis

Calculated total sales for each customer and sorted customers by total sales.

### 8. Top 5 Customers

Identified the five customers with the highest total sales using `ORDER BY` and `LIMIT`.

### 9. CASE

Classified orders into `High` and `Low` price categories based on `total_price`.

### 10. Subquery

Identified customers whose total sales were greater than the average total sales across all customers.

## Tools & Technologies

- SQL
- SQLite
- SQLTools for VS Code
- Python
- Pandas
- SQLite3

Python was used only for the initial conversion of the Excel dataset into a SQLite database. The main analysis was performed using SQL queries.

## Project Structure

```text
SQL-Sales-Data-Analysis/
│
├── .vscode/
│
├── database/
│   └── sales.db
│
├── dataset/
│   └── SQL_Sales_Dataset_200_Rows.xlsx
│
├── screenshots/
│   ├── average_order_value.png
<img width="307" height="171" alt="average_order_value" src="https://github.com/user-attachments/assets/8cf4d618-6358-447b-bd5c-20fb9e9c4a4d" />

│   ├── case_query.png
<img width="453" height="935" alt="case_query" src="https://github.com/user-attachments/assets/a19cacc9-2292-4b8f-ae41-fac0cc698f04" />

│   ├── groupby_count.png
<img width="306" height="170" alt="groupby_count" src="https://github.com/user-attachments/assets/b712d791-58b9-47e3-ba12-1efc0e0ee5ca" />

│   ├── groupby_sum.png
<img width="306" height="171" alt="groupby_sum" src="https://github.com/user-attachments/assets/5bb06ab5-640d-439a-92c3-e2890797bc83" />

│   ├── orderby_query.png
<img width="299" height="940" alt="orderby_query" src="https://github.com/user-attachments/assets/f3ab87de-6510-439b-aab4-a2d2b294e340" />

│   ├── select_query.png
<img width="451" height="938" alt="select_query" src="https://github.com/user-attachments/assets/74457c28-b25f-4fe2-898c-4c79e2ee13e6" />

│   ├── sub_query.png
<img width="305" height="941" alt="sub_query" src="https://github.com/user-attachments/assets/d39292ad-e38c-4aa3-84cd-889284decaa7" />

│   ├── top_5_customer_limit_query.png
<img width="306" height="207" alt="top_5_customer_limit_query" src="https://github.com/user-attachments/assets/7e093544-9d79-4e07-bff7-b82c41fa2292" />

│   ├── top_customers.png
<img width="303" height="718" alt="top_customers" src="https://github.com/user-attachments/assets/6a6db660-e1ce-4891-8a39-4573a7036153" />

│   └── where_query.png
<img width="300" height="936" alt="where_query" src="https://github.com/user-attachments/assets/7bc4aef1-d1c5-40c4-8a96-41f248a2a1a2" />

│
├── sql/
│   └── sales_analysis.sql
│
├── .gitignore
├── create_database.py
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/rameswarbehera00/SQL-Sales-Data-Analysis
cd SQL-Sales-Data-Analysis
```

### 2. Database setup

The `create_database.py` script converts the Excel dataset into a SQLite database and creates the `sales` table.

```bash
python create_database.py
```

The script reads:

```text
dataset/SQL_Sales_Dataset_200_Rows.xlsx
```

and creates:

```text
database/sales.db
```

### 3. Run the SQL analysis

Open the project in VS Code and connect:

```text
database/sales.db
```

using **SQLTools**.

Then open:

```text
sql/sales_analysis.sql
```

and run the queries using the active SQLite connection.

## Learning Outcomes

Through this project, I practiced:

- Writing SQL queries for data analysis
- Filtering and sorting data
- Performing aggregate calculations
- Grouping business data
- Ranking customers by sales
- Calculating average order values
- Counting orders by region
- Creating conditional columns using `CASE`
- Using subqueries for comparative analysis
- Working with SQLite and SQLTools in VS Code

## Internship Assignment

**Week 2: SQL for Data Analysis**

The assignment focuses on basic SQL queries, filtering, grouping, ordering, aggregations, joins, subqueries, and `CASE` statements.

## Author

**Your Name**
