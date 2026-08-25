# HR Employee Attrition Analytics & Interactive Dashboard

An End-to-End HR Data Analytics Project using Python, SQL, and Tableau Public

---

## Executive Summary

This project analyzes employee demographic and workplace data to identify key driver factors influencing employee attrition. By combining **Python** for data quality validation, **SQL** for analytical metrics computation, and **Tableau Public** for interactive visualization, this analysis provides actionable HR strategies to reduce turnover and enhance employee retention.

![HR Attrition Dashboard](images/dashboard.png)

---

## 📁 Data Source

* **Dataset**: [IBM HR Analytics Employee Attrition & Performance Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) (Fictional dataset created by IBM Data Scientists)
* **Scope**: 500 employee records analyzed covering demographics, department classifications, overtime status, and attrition indicators.
* **Data Pipeline**: Processed, cleaned, and validated using Python (`pandas`) and SQL (`sqlite3`).

---
## Key Business Insights

* **Impact of Overtime on Attrition**:
  * **Overtime Staff Attrition**: **39.74%**
  * **Non-Overtime Staff Attrition**: **21.22%**
  * **Insight**: Working overtime is the single largest risk factor driving employee departure. Overtime employees are nearly **2x more likely to leave** the company compared to their non-overtime peers.

* **Departmental Variations**:
  * **Sales Department**: Highest attrition rate at **32.47%**.
  * **Human Resources & Marketing**: Secondary high-risk departments at **27.08%** and **27.27%**.
  * **Finance**: Lowest attrition rate at **13.73%**.

---

## Project Architecture & Workflow

```text
HR-Employee-Attrition-Analytics/
│-- hr_employee_attrition.csv   # Raw Dataset (500 Records)
│-- data_processing.py         # Data validation & SQL-based pipeline execution
│-- analysis.py                # Python static visualization script
│-- analysis.sql               # Core SQL query script for HR aggregation metrics
│-- README.md                  # Project documentation & insights summary
└── images/
    └── dashboard.png          # Tableau Dashboard Screenshot

### 1. Data Quality & Preprocessing (`data_processing.py`)
* Loaded raw dataset into Python using `pandas`.
* Verified zero missing values across critical fields (`Department`, `Attrition`, `OverTime`).
* Simulated in-memory SQL database using `sqlite3` for production-grade analytical query testing.

### 2. Core SQL Analysis (`analysis.sql`)
* Executed SQL queries to compute department-level and overtime-level attrition rates.
* Employed conditional aggregation (`AVG(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)`) to calculate percentages accurately.

### 3. Interactive Visualization (`Tableau Public`)
* Designed an interactive dashboard containing:
  * **Department Attrition Rate Chart**: Highlighting high-turnover business units.
  * **Overtime Impact Chart**: Illustrating the risk escalation caused by extended work hours.

---

## Strategic Recommendations for HR Leadership

1. **Workload & Overtime Re-allocation**:
   * Conduct workload audits for departments with heavy overtime demands.
   * Implement temporary project-based staffing or contractors to mitigate burnout in high-volume periods.

2. **Sales Department Retention Plan**:
   * Re-evaluate incentive structures and target quotas for Sales representatives.
   * Introduce structured career development and mentorship programs to improve job satisfaction.