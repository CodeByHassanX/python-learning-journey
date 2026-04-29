# Sales Data Analysis

## Overview
This project analyzes a sales dataset focused on bike accessories and related products. It includes exploratory data analysis (EDA) using Python, Pandas, Matplotlib, and Seaborn in a Jupyter notebook.

Key computations:
- Total Revenue, Profit, and Quantity Sold
- Breakdowns by Product_Category, Sub_Category, Country, State, Customer_Age, Date, Month
- Visualizations: Bar plot (revenue by category), Pie chart (revenue by country), Line plot (daily revenue trend)

## Dataset: `sales_data.csv`
- **Size**: ~11,000+ records (large dataset truncated in preview)
- **Time Period**: 2013-2016
- **Columns**:
  | Column | Description |
  |--------|-------------|
  | Date | Sales date (e.g., 2013-11-26) |
  | Day | Day of month |
  | Month | Month name |
  | Year | Year |
  | Customer_Age | Age of customer |
  | Age_Group | Binned: Youth (<25), Young Adults (25-34), Adults (35-64), Seniors (64+) |
  | Customer_Gender | M/F |
  | Country | e.g., Canada, Australia, United States, France, Germany, United Kingdom |
  | State | State/region |
  | Product_Category | e.g., Accessories |
  | Sub_Category | e.g., Bike Racks, Bike Stands, Bottles and Cages |
  | Product | Specific product name |
  | Order_Quantity | Number of units |
  | Unit_Cost | Cost per unit |
  | Unit_Price | Price per unit |
  | Profit | Profit from sale |
  | Cost | Total cost |
  | Revenue | Total revenue |

- **Sample Insights**:
  - No missing values.
  - Products mainly bike accessories (racks, stands, bottles/cages).
  - High revenue from countries like US, Canada, Australia.

## Prerequisites
- Python 3.x
- Jupyter Notebook
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`

Install via:
```
pip install jupyter pandas numpy matplotlib seaborn
```

## Usage
1. Open terminal in project directory:
   ```
   cd sales_data_analysis
   ```
2. Start Jupyter:
   ```
   jupyter notebook
   ```
3. Open and run `sales_data_analysis.ipynb`.

## Key Findings (from notebook)
- **Totals**: Revenue [computed in notebook], Profit [sum], Quantity Sold [sum]
- **Top Categories**: Grouped revenue by Product_Category (visualized).
- **Top Countries**: Pie chart shows distribution.
- **Trends**: Daily revenue line plot.

## Visualizations
1. **Revenue by Category**: Bar plot.
2. **Revenue by Country**: Pie chart.
3. **Daily Revenue Trend**: Line plot.

Explore the notebook for full outputs and extend with more analysis!

## License
MIT (or as appropriate).
