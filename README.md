# Brazilian E-Commerce Analysis Dashboard

## Table of Contents

1. [Introduction](#introduction)
2. [Dataset Overview](#dataset-overview)
3. [Project Objectives](#project-objectives)
4. [Business Questions](#business-questions)
5. [Dashboard Structure](#dashboard-structure)
6. [Installation and Usage](#installation-and-usage)
7. [Key Insights and Recommendations](#key-insights-and-recommendations)
8. [Author](#author)

---

## Introduction

The **Brazilian E-Commerce Analysis Dashboard** is an interactive tool developed using Streamlit to analyze and visualize the Brazilian E-Commerce Public Dataset provided by Olist. This dashboard aims to uncover key trends, patterns, and insights that can inform strategic decisions for optimizing e-commerce operations.

---

## Dataset Overview

The dataset contains approximately 100,000 orders made at Olist, covering the period from 2016 to 2018. It includes various dimensions such as:

- Customer and seller details
- Product information
- Order status
- Payment methods
- Geographic data

These attributes enable a comprehensive analysis of the e-commerce ecosystem in Brazil.

---

## Project Objectives

The primary goals of this project are:

1. To identify top-performing product categories and regions.
2. To analyze customer engagement levels across cities and states.
3. To uncover sales trends over time.
4. To derive actionable recommendations for enhancing business performance.

---

## Business Questions

1. **What are the highest order and most profitable product categories?**

   - _Objective:_ Guide inventory and marketing strategies by identifying key categories contributing to revenue and order volume.

2. **Which regions and cities have the most sales or profit?**

   - _Objective:_ Understand geographic performance to uncover key markets and target areas with potential growth.

3. **Where are the regions or cities with the most active or non-active customers?**

   - _Objective:_ Improve customer engagement by analyzing customer activity across regions.

4. **What are the sales trends over time?**
   - _Objective:_ Plan marketing and inventory strategies based on seasonal trends and sales fluctuations.

---

## Dashboard Structure

### Navigation Sections

1. **Introduction**: Provides an overview of the project and dataset.
2. **Visualizations**: Interactive visualizations to answer the business questions.
   - **Product**: Insights into the highest order and most profitable categories.
   - **Location**: Analysis of sales performance by regions and cities.
   - **Customer**: Breakdown of active and non-active customers by location.
   - **Trend**: Examination of sales trends over time.
3. **Conclusion and Recommendations**: Summarizes findings and provides actionable business strategies.
4. **Author**: Information about the author.

### Key Features

- Interactive tabs for each business question.
- Visualizations using Seaborn, Matplotlib, and Plotly.
- Geographic heatmaps for location-based insights.
- Drill-down analysis for customer engagement and sales trends.

---

## Installation and Usage

### Prerequisites

- Python 3.10 or above
- Required libraries:
  - Streamlit
  - Pandas
  - Seaborn
  - Matplotlib
  - Plotly

### Installation Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/WardiansyahF/e-commerce-dashboard.git
   ```
2. Navigate to the project directory:
   ```bash
   cd e-commerce-dashboard
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit application:
   ```bash
   streamlit run dashboard.py
   ```
5. Open the dashboard in your browser at `http://localhost:8501`.

---

## Key Insights and Recommendations

### Key Insights

1. **Product Categories**:

   - The **bed_bath_table** category leads in both orders and revenue, making it a high-priority category for inventory optimization.
   - Categories like **sports_leisure** and **health_beauty** also show strong performance.

2. **Sales by Location**:

   - Major cities like **São Paulo** and **Rio de Janeiro** dominate in both orders and revenue, indicating high customer concentration and spending power.

3. **Customer Activity**:

   - The majority of customers in top cities like **São Paulo** are active, highlighting robust engagement levels in these regions.
   - Non-active customers in key cities like **Rio de Janeiro** present opportunities for targeted re-engagement campaigns.

4. **Sales Trends**:
   - Peak sales periods, such as November 2017 and January 2018, reveal seasonal demand patterns, ideal for planning promotional campaigns.

### Recommendations

- **Inventory and Marketing**:
  Focus on high-performing categories like **bed_bath_table** and **sports_leisure** to maximize profitability.
- **Regional Targeting**:
  Prioritize marketing efforts in high-performing cities like **São Paulo** and **Rio de Janeiro**.
- **Customer Engagement**:
  Implement re-engagement campaigns for non-active customers, particularly in **Rio de Janeiro**.
- **Seasonal Planning**:
  Leverage peak sales periods for marketing campaigns and inventory stocking.

---

## Author

**Wardiansyah Fauzi Abdillah**

- **Background**: Informatics student at Gunadarma University, passionate about data analysis and its applications in business strategy.
- **Contact**: [Email](mailto:ardi.dl738@gmail.com) | [LinkedIn](https://linkedin.com/in/wardiansyah-fauzi-abdillah) | [GitHub](https://github.com/WardiansyahF)

Feel free to connect with me to discuss this project or other data-related initiatives!
