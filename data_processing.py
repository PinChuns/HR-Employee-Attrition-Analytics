import pandas as pd
import sqlite3

# =========================================================
# 步驟 1：用 Python (Pandas) 讀取原始資料與檢查
# =========================================================
df = pd.read_csv('hr_employee_attrition.csv')

print("--- 1. 資料前幾筆內容 ---")
print(df.head(3))

print("\n--- 2. 檢查是否有缺值 ---")
print(df.isnull().sum())  # 確認資料品質，沒有缺值才能做後續分析


# =========================================================
# 步驟 2：載入 SQLite 資料庫，用 SQL 做數據聚合計算
# =========================================================
conn = sqlite3.connect(':memory:')
df.to_sql('hr_data', conn, index=False)

# SQL 查詢 1：計算各部門離職率與平均薪資
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

# SQL 查詢 2：計算常態加班 (OverTime) 對離職率的影響
sql_overtime = """
SELECT 
    OverTime,
    COUNT(*) AS total_staff,
    ROUND(AVG(CASE WHEN Attrition = 'Yes' THEN 1.0 ELSE 0.0 END) * 100, 1) AS attrition_rate_pct
FROM hr_data
GROUP BY OverTime;
"""

print("\n--- 3. SQL 計算結果：各部門離職率與平均薪資 ---")
dept_result = pd.read_sql_query(sql_dept, conn)
print(dept_result)

print("\n--- 4. SQL 計算結果：加班對離職率的影響 ---")
ot_result = pd.read_sql_query(sql_overtime, conn)
print(ot_result)