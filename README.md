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

### Subcategory Performance

* Copiers generated the highest total profit, at approximately $55,618.
* Phones generated approximately $44,516 in profit.
* Tables recorded a loss of approximately $17,725.
* Bookcases recorded a loss of approximately $3,473.

### Monthly Performance

* November 2017 was the highest-sales month, with approximately $118,448 in sales.
* February 2014 was the lowest-sales month, with approximately $4,520 in sales.
* December 2016 generated the highest monthly profit, at approximately $17,885.
* January 2015 recorded the lowest monthly profit, at approximately -$3,281.

### Regional Performance

* West led in sales and profit, generating approximately $725,458 in sales and $108,418 in profit.
* West also had the highest regional profit margin, at approximately 14.94%.
* Central had the lowest regional profit margin, at approximately 7.92%, making it a useful area for further investigation.

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
