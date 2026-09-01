import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
df = pd.read_csv('hr_employee_attrition.csv')

# 2. Calculate attrition rate
total_employees = len(df)
attrition_count = (df['Attrition'] == 'Yes').sum()
attrition_rate = (attrition_count / total_employees) * 100

print(f"Employees: {total_employees}")
print(f"Attrition_Rate: {attrition_rate:.2f}%")

# 3. Attrition Rate by Department
dept_attrition = df.groupby('Department')['Attrition'].apply(lambda x: (x == 'Yes').mean() * 100).reset_index()
print("\n--- Attrition Rate by Department ---")
print(dept_attrition)

# 4. Impact of Overtime on Employee Turnover
overtime_attrition = df.groupby('OverTime')['Attrition'].apply(lambda x: (x == 'Yes').mean() * 100).reset_index()
print("\n--- Impact of Overtime on Employee Turnover ---")
print(overtime_attrition)

# 5. Chart
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Chart1：Cross-Departmental Attrition Comparison
sns.barplot(data=dept_attrition, x='Department', y='Attrition', ax=axes[0], palette='Blues_d')
axes[0].set_title('Attrition Rate by Department (%)', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Attrition Rate (%)')
axes[0].tick_params(axis='x', rotation=20)

# Chart2：The Impact of Overtime on Attrtion Rate
sns.barplot(data=overtime_attrition, x='OverTime', y='Attrition', ax=axes[1], palette='Oranges_d')
axes[1].set_title('Attrition Rate: OverTime vs No OverTime (%)', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Attrition Rate (%)')

plt.tight_layout()
plt.savefig('attrition_analysis.png', dpi=300)
plt.show()