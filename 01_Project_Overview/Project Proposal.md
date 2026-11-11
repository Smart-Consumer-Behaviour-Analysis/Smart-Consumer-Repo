# Power BI Waterfall Chart Field Mapping & Smart Consumer Behaviour Analysis Project Proposal

---

## Part 1: Power BI Waterfall Chart Field Mapping (`DAV5-Retail` Dataset)

A **Waterfall Chart** illustrates how an initial starting value increases or decreases sequentially through intermediate steps to arrive at a final total.

### Field Configuration Matrix

| Field Bucket in Power BI Visual | Recommended Dataset Field | Purpose & Behavior |
| :--- | :--- | :--- |
| **Category** (X-Axis) | `Category` or `Seasonality` | Groups horizontal steps into distinct categories (`Clothing`, `Electronics`, `Furniture`, `Groceries`, `Toys`). |
| **Breakdown** *(Optional)* | `Weather Condition` | Sub-divides each category column into stacked micro-variances (e.g., `Sunny`, `Rainy`, `Snowy`). |
| **Y-Axis** (Values) | `Units Sold` or `Inventory Level` | Defines the height and direction (increase/decrease) of each cumulative step bar. |

---

### Step-by-Step Setup in Power BI Desktop
1. Select the **Waterfall Chart** icon from the **Visualizations** pane.
2. Drag **`Category`** into the **Category** well.
3. Drag **`Units Sold`** (or `Inventory Level`) into the **Y-Axis** well.
4. Set the bar colors (Green for increases, Red for decreases, Blue for Total) under **Format visual** > **Visual** > **Colors**.

---

# Part 2: Smart Consumer Behaviour Analysis — Project Proposal

## 1. Introduction
Consumer behaviour refers to how customers make purchasing decisions and choose products. This project analyzes customer transaction data such as age, gender, product category, quantity, price, payment method, shopping mall, and invoice date. Data analytics and visualization will be used to identify useful consumer patterns and present the results through an interactive dashboard.

## 2. Problem Statement
Businesses have large amounts of customer transaction data, but it can be difficult to identify useful patterns from raw data. This project analyzes the available data to understand product preferences, customer groups, payment methods, shopping mall activity, and purchasing trends.

## 3. User Needs
1. Understand customer preferences based on age and gender.
2. Identify the most preferred product categories.
3. Understand payment method preferences.
4. Compare customer activity across shopping malls.
5. Analyze purchasing quantity and spending patterns.

## 4. Proposed Solution
1. Collect and organize customer transaction data.
2. Clean and prepare the dataset.
3. Analyze customer, product, payment, mall, and purchasing patterns.
4. Create charts and graphs to present the findings.
5. Develop an interactive dashboard for exploring consumer behaviour.

## 5. Aim
To analyze consumer purchasing behaviour using data analytics and visualization techniques and present meaningful insights through an interactive dashboard.

## 6. Objectives
1. To analyze customer preferences based on age and gender.
2. To identify the most purchased product categories.
3. To analyze payment method preferences.
4. To study purchasing patterns across shopping malls and dates.
5. To visualize consumer behaviour and develop an interactive dashboard.

## 7. Scope
The project covers customer demographics, product categories, purchase quantity and price, payment methods, shopping malls, and purchasing trends over time. The analysis is limited to the information available in the selected dataset.

## 8. Dataset
The dataset contains 2,000 original records and 11 columns: Serial Number, Invoice Number, Customer ID, Gender, Age, Category, Quantity, Price, Payment Method, Invoice Date, and Shopping Mall. The raw dataset will be collected and converted to CSV format before cleaning.

## 9. Methodology
The project follows six stages: 
1. Project Proposal
2. Data Collection
3. Data Cleaning
4. Data Analytics
5. Data Visualization
6. Interactive Dashboard

Each stage produces the input or output required for the next stage.

## 10. Tools and Technologies
* **Python**: Used for data cleaning and analysis.
* **Pandas & NumPy**: Used for data processing and calculations.
* **Matplotlib & Seaborn**: Used for exploratory data visualization.
* **Power BI**: Used to develop the interactive dashboard.
* **Excel / CSV**: Used for data storage and inspection.

## 11. Expected Outcomes
The project is expected to identify popular product categories, customer preferences by age and gender, preferred payment methods, shopping mall patterns, purchasing trends, and relationships between quantity and price.

## 12. Benefits
The project helps businesses understand customers, identify popular products, compare customer groups, understand purchasing patterns, and make data-driven decisions. It also provides practical experience in data analysis, visualization, and dashboard development.

## 13. Limitations
The results depend on the quality and completeness of the dataset. The dataset may represent only a limited group of consumers, and the analysis can identify patterns but may not explain every reason behind customer decisions.

## 14. Future Enhancements
Future versions can include machine learning for customer segmentation, purchase prediction, product recommendation, real-time data, and predictive sales analysis.

## 15. Project Deliverables
1. Project Proposal
2. Raw Dataset
3. Cleaned Dataset
4. Data Cleaning Python File
5. Data Analytics Results
6. Data Visualizations
7. Interactive Dashboard
8. Final Project Report and Presentation

---

## 16. Ten Questions and Answers

### Q1: What is the main purpose of this project?
**Answer:** The main purpose is to analyze customer transaction data and identify consumer preferences, purchasing patterns, spending behaviour, and trends using data analytics and visualization.

### Q2: What problem does the project solve?
**Answer:** It converts raw customer transaction data into meaningful information so that important purchasing patterns and customer preferences can be understood more easily.

### Q3: Who are the intended users of the project?
**Answer:** The main users are businesses, managers, analysts, and decision-makers who need to understand customer purchasing behaviour and make data-driven decisions.

### Q4: What data is required for this project?
**Answer:** The project uses customer transaction information including gender, age, product category, quantity, price, payment method, invoice date, shopping mall, invoice number, and customer ID.

### Q5: Where does the data come from?
**Answer:** The project uses the provided customer transaction dataset. The original Excel file is converted into CSV format and used as the raw dataset for the project.

### Q6: What will be done with the collected data?
**Answer:** The data will first be cleaned and prepared. It will then be analyzed to find patterns in customers, products, purchases, payment methods, shopping malls, and dates.

### Q7: What questions will the analysis answer?
**Answer:** The analysis will determine which categories are most purchased, which age and gender groups are more active, which payment methods are preferred, which malls have higher activity, and how quantity and price are related.

### Q8: What types of graphs will be used?
**Answer:** Bar charts can compare categories, age groups, gender, and shopping malls. Pie charts can show payment method proportions. Line charts can show trends over time. Scatter plots can show relationships such as quantity versus price.

### Q9: What will the interactive dashboard contain?
**Answer:** The dashboard will contain important KPIs and visualizations such as total transactions, total quantity, total sales, average transaction value, category analysis, payment methods, age groups, gender, shopping malls, and time trends. Filters can be added for easier exploration.

### Q10: What is the final outcome of the project?
**Answer:** The final outcome will be an interactive dashboard supported by cleaned data, analytical results, and visualizations. It will provide clear insights into consumer behaviour and support data-driven decision-making.

---

## 17. Project Workflow

```
[Project Proposal] ➔ [Data Collection] ➔ [Data Cleaning] ➔ [Data Analytics] ➔ [Data Visualization] ➔ [Interactive Dashboard]
```

---

## 18. Conclusion
Smart Consumer Behaviour Analysis transforms customer transaction data into useful consumer insights through data cleaning, analytics, visualization, and an interactive dashboard. The project provides a clear understanding of customer and purchasing patterns.