import streamlit as st
from groq import Groq
import pandas as pd

def get_groq_client():
    return Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )


def build_summary(df, forecast):
    df = df.copy()

    # Ensure date column is datetime
    df["Order Date"] = pd.to_datetime(df["Order Date"])

    yearly_sales = (
        df.groupby(df["Order Date"].dt.year)["Sales"]
        .sum()
        .round(2)
        .to_dict()
    )

    yearly_profit = (
        df.groupby(df["Order Date"].dt.year)["Profit"]
        .sum()
        .round(2)
        .to_dict()
    )

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .round(2)
        .sort_values(ascending=False)
        .to_dict()
    )

    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .round(2)
        .sort_values(ascending=False)
        .to_dict()
    )

    top_products = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .round(2)
        .to_dict()
    )

    monthly_sales = (
        df.set_index("Order Date")
        .resample("ME")["Sales"]
        .sum()
        .round(2)
        .tail(6)
    )

    monthly_sales = {
        date.strftime("%b %Y"): value
        for date, value in monthly_sales.items()
    }

    best_year = max(yearly_sales, key=yearly_sales.get)
    worst_year = min(yearly_sales, key=yearly_sales.get)

    summary = {
        "Overall KPIs": {
            "Total Sales": f"${df['Sales'].sum():,.2f}",
            "Total Profit": f"${df['Profit'].sum():,.2f}",
            "Orders": int(df["Order ID"].nunique()),
            "Average Discount": f"{df['Discount'].mean():.2%}",
            "Average Profit Margin": f"{df['Profit Margin'].mean():.2%}",
            "Loss Orders": int((df["Profit"] < 0).sum()),
        },

        "Yearly Sales": yearly_sales,
        "Yearly Profit": yearly_profit,

        "Year Performance": {
            "Best Sales Year": int(best_year),
            "Best Sales Amount": f"${yearly_sales[best_year]:,.2f}",
            "Worst Sales Year": int(worst_year),
            "Worst Sales Amount": f"${yearly_sales[worst_year]:,.2f}",
        },

        "Recent Monthly Sales": monthly_sales,

        "Category Sales": category_sales,
        "Region Sales": region_sales,
        "Top Products": top_products,

        "Forecast": {
            "Next Forecast Revenue": f"${forecast['Forecast Sales'].iloc[-1]:,.2f}",
            "Forecast Start Date": forecast["Date"].min().strftime("%b %Y"),
            "Forecast End Date": forecast["Date"].max().strftime("%b %Y"),
        }
    }

    return summary


def ask_ai(question, summary):
    client = get_groq_client()

    prompt = f"""
You are a senior Business Intelligence Analyst.

Use ONLY the dashboard summary below to answer.

Dashboard Summary:
{summary}

Rules:
- Keep the response under 120 words.
- Be concise and executive-friendly.
- Do not mention hidden calculations.
- If the answer is not available, say:
  "This information is not available in the dashboard."

Format:
**Answer:** <short answer>

**Recommendation:** <short recommendation>

User Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content