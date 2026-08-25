import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 載入資料
df = pd.read_csv('hr_employee_attrition.csv')

# 2. 計算整體離職率
total_employees = len(df)
attrition_count = (df['Attrition'] == 'Yes').sum()
attrition_rate = (attrition_count / total_employees) * 100

print(f"總員工數: {total_employees}")
print(f"整體離職率: {attrition_rate:.2f}%")

# 3. 按部門統計離職率
dept_attrition = df.groupby('Department')['Attrition'].apply(lambda x: (x == 'Yes').mean() * 100).reset_index()
print("\n--- 各部門離職率 ---")
print(dept_attrition)

# 4. 加班與離職率交叉分析
overtime_attrition = df.groupby('OverTime')['Attrition'].apply(lambda x: (x == 'Yes').mean() * 100).reset_index()
print("\n--- 加班狀態離職率 ---")
print(overtime_attrition)

# 5. 視覺化圖表繪製
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 圖 1：部門離職率比較
sns.barplot(data=dept_attrition, x='Department', y='Attrition', ax=axes[0], palette='Blues_d')
axes[0].set_title('Attrition Rate by Department (%)', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Attrition Rate (%)')
axes[0].tick_params(axis='x', rotation=20) # 把 X 軸文字旋轉 20 度避免重疊

# 圖 2：加班對離職率影響
sns.barplot(data=overtime_attrition, x='OverTime', y='Attrition', ax=axes[1], palette='Oranges_d')
axes[1].set_title('Attrition Rate: OverTime vs No OverTime (%)', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Attrition Rate (%)')

plt.tight_layout() # 自動調整間距
plt.savefig('attrition_analysis.png', dpi=300)
plt.show()