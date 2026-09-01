import pandas as pd
import sqlite3

# Step1：Use Python (Pandas) Import and check raw data

df = pd.read_csv('hr_employee_attrition.csv')

print("--- 1. View data sample ---")
print(df.head(3))

print("\n--- 2. Check for missing values ---")
print(df.isnull().sum())

# Step2：Connect to SQLite and run SQL aggregations.

conn = sqlite3.connect(':memory:')
df.to_sql('hr_data', conn, index=False)

# SQL query1：Calculate attrition rate and average salary
sql_dept = """
SELECT 
    Department,
    COUNT(*) AS total_staff,
    ROUND(AVG(MonthlyIncome), 0) AS avg_income,
    ROUND(AVG(CASE WHEN Attrition = 'Yes' THEN 1.0 ELSE 0.0 END) * 100, 1) AS attrition_rate_pct
FROM hr_data
GROUP BY Department
ORDER BY attrition_rate_pct DESC;
"""
# SQL query2：Evaluate the effect of overtime on employee attrition
sql_overtime = """
SELECT 
    OverTime,
    COUNT(*) AS total_staff,
    ROUND(AVG(CASE WHEN Attrition = 'Yes' THEN 1.0 ELSE 0.0 END) * 100, 1) AS attrition_rate_pct
FROM hr_data
GROUP BY OverTime;
"""

print("\n--- 3. SQL result：Departmental Attrition Rate and Average Salary ---")
dept_result = pd.read_sql_query(sql_dept, conn)
print(dept_result)

print("\n--- 4. SQL result：The Impact of Overtime on Attrition Rate ---")
ot_result = pd.read_sql_query(sql_overtime, conn)
print(ot_result)