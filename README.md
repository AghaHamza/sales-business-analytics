# Sales & Business Performance Analytics

## Project Overview

This project analyzes retail sales data using Python to identify business performance trends, evaluate profitability, and uncover areas for improvement.

The analysis covers sales, profit, profit margins, product categories, subcategories, monthly performance, and regional results.

## Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* CSV data analysis

## Dataset

The dataset contains retail transaction records with order dates, regions, states, product categories, subcategories, customer segments, sales, profit, and quantity.

* Original records: 9,994
* Exact duplicate records removed: 2
* Cleaned records: 9,992
* Date range: January 2014 – December 2017
* Missing values: None detected

## Key Performance Indicators

| Metric                   |        Result |
| ------------------------ | ------------: |
| Total Sales              | $2,296,914.56 |
| Total Profit             |   $286,408.34 |
| Total Units Sold         |        37,869 |
| Overall Profit Margin    |        12.47% |
| Cleaned Transaction Rows |         9,992 |

*Transaction rows should not be interpreted as unique orders because the dataset does not contain an order ID.*

## Key Findings

### Category Performance

* Technology generated approximately $836,154 in sales and $145,455 in profit.
* Office Supplies generated approximately $122,491 in profit.
* Furniture had the lowest category profit margin, at approximately 2.49%.

<img width="1350" height="750" alt="sales_by_category" src="https://github.com/user-attachments/assets/ce331793-0a0d-4bab-80ac-6b7ca8451770" />
<img width="1350" height="750" alt="profit_by_category" src="https://github.com/user-attachments/assets/83b5d8a2-6734-4e6b-8aad-33b3bc2c0329" />



### Subcategory Performance

* Copiers generated the highest total profit, at approximately $55,618.
* Phones generated approximately $44,516 in profit.
* Tables recorded a loss of approximately $17,725.
* Bookcases recorded a loss of approximately $3,473.

<img width="1500" height="1050" alt="profit_by_subcategory" src="https://github.com/user-attachments/assets/b4b2a461-8f5f-4663-9510-77df9fe81d4c" />


### Monthly Performance

* November 2017 was the highest-sales month, with approximately $118,448 in sales.
* February 2014 was the lowest-sales month, with approximately $4,520 in sales.
* December 2016 generated the highest monthly profit, at approximately $17,885.
* January 2015 recorded the lowest monthly profit, at approximately -$3,281.

<img width="1800" height="750" alt="monthly_sales_trend" src="https://github.com/user-attachments/assets/9aa3ce72-c5e0-473a-9016-7f14f7b2af9b" />
<img width="1800" height="750" alt="monthly_profit_trend" src="https://github.com/user-attachments/assets/6e91dc0d-ec24-4f7f-8b22-b6176212cdfb" />



### Regional Performance

* West led in sales and profit, generating approximately $725,458 in sales and $108,418 in profit.
* West also had the highest regional profit margin, at approximately 14.94%.
* Central had the lowest regional profit margin, at approximately 7.92%, making it a useful area for further investigation.

<img width="1950" height="750" alt="regional_performance" src="https://github.com/user-attachments/assets/a95f3123-6d2d-4db4-be18-eb222b4770f0" />


## Project Workflow

1. Loaded and inspected the raw dataset.
2. Standardized column names and converted order dates.
3. Identified and removed exact duplicate records.
4. Checked missing values and basic data-quality issues.
5. Calculated KPIs and profit margins.
6. Analyzed category and subcategory performance.
7. Evaluated monthly trends and regional results.
8. Exported cleaned data, summary reports, and visualizations.

## How to Run

Clone this repository, navigate to the project directory, and install the dependencies:

```bash
pip install -r requirements.txt
```

Run the analysis:

```bash
python analysis.py
```

The script generates cleaned data, CSV summary reports, and chart images.

## Future Improvements

* Build an interactive dashboard using Power BI or Tableau.
* Investigate discounting and loss-making products.
* Add customer-segment analysis.
* Develop a sales forecasting model.
* Expand the analysis with statistical testing and deeper business recommendations.

## Author

Hamza — Computer Science Student | Aspiring Data Scientist
