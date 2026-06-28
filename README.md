# Sales Intelligence Copilot

## Project Overview

Sales Intelligence Copilot is an AI-powered Business Intelligence dashboard developed using Streamlit to analyze retail sales data and generate actionable business insights. The project demonstrates an end-to-end analytics workflow, including data cleaning, exploratory data analysis (EDA), feature engineering, sales forecasting, anomaly detection, and an AI assistant that answers business questions using dashboard insights.

---

## Tools Used

* Python
* Pandas
* NumPy
* Plotly
* Streamlit
* Statsmodels (SARIMA)
* Groq API (Llama 3.3 70B)
* Git
* GitHub

---

## Project Workflow

### Data Cleaning

* Removed duplicate records
* Checked for missing values
* Converted date columns to datetime format
* Verified data consistency
* Exported cleaned dataset

---

### Feature Engineering

Created business-focused features including:

* Profit Margin
* Discount Impact
* Sales Outlier Flag
* Order Day of Week

The feature-engineered dataset is used throughout the dashboard for business analysis and forecasting.

---

### Exploratory Data Analysis (EDA)

Performed exploratory analysis to understand sales performance through:

* Sales trend analysis
* Category-wise sales analysis
* Region-wise sales analysis
* Profit distribution
* Discount analysis
* Customer segment analysis

---

### Sales Forecasting

Implemented a SARIMA time series forecasting model to predict future monthly sales.

Workflow:

* Monthly sales aggregation
* Train-test split
* Model training using SARIMA
* Model evaluation using Mean Absolute Error (MAE)
* Future sales prediction
* Forecast visualization in the dashboard

---

### Dashboard Development

Developed an interactive multi-page Business Intelligence dashboard using Streamlit.

Dashboard modules include:

* Executive Dashboard
* Sales Analytics
* Product Intelligence
* Profitability Analysis
* Risk Center
* AI Business Assistant

---

### AI Business Assistant

Integrated an AI-powered business assistant using the Groq API and Llama 3.3 70B model.

The assistant answers natural language business questions using dashboard-generated summaries and provides:

* Business insights
* Performance explanations
* Actionable recommendations

Example questions:

* Which category performs best?
* Which region generates the highest revenue?
* Why is profit low?
* How can sales improve?
* Did sales perform well in 2017?

---

## Key Features

* Interactive KPI Dashboard
* Sales Forecasting using SARIMA
* AI-powered Business Insights
* Executive Business Summary
* Profitability Analysis
* Product Performance Analysis
* Sales Trend Visualization
* Sales Outlier Detection
* Modular Streamlit Application

---

## Dataset

The project uses the Sample Superstore dataset.

The repository contains:

* Cleaned dataset
* Feature-engineered dataset
* Forecast dataset generated using the SARIMA model

---

## Author

**Akhina Manual**

## Live Demo

[View Live App](https://sales-intelligence-copilot.streamlit.app/)
