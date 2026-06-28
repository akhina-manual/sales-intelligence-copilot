import streamlit as st

from styles.css import load_css
from utils.loader import load_data
from components.header import show_header
from components.sidebar import build_sidebar
from app_pages.executive import render as executive_page
from app_pages.sales import render as sales_page
from app_pages.products import render as products_page
from app_pages.anomalies import render as anomalies_page
from app_pages.profitability import render as profitability_page
from app_pages.ai import render as ai_page
from components.footer import show_footer

st.set_page_config(
    page_title="Sales Intelligence Copilot",
    page_icon="📊",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

df, forecast = load_data()

page, region, category = build_sidebar(df)

filtered_df = df.copy()

if region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == region]

if category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == category]

show_header()

if page == "Executive Dashboard":
    executive_page(filtered_df, forecast)

elif page == "Sales Analytics":
    sales_page(filtered_df, forecast)

elif page == "Product Intelligence":
    products_page(filtered_df, forecast)

elif page == "Risk Center":
    anomalies_page(filtered_df, forecast)

elif page == "Profitability":
    profitability_page(filtered_df, forecast)

elif page == "AI Assistant":
    ai_page(filtered_df, forecast)

else:
    st.info(f"{page} page will be added next.")


csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered Data",
    data=csv,
    file_name="filtered_sales_data.csv",
    mime="text/csv",
    use_container_width=True
)

show_footer()