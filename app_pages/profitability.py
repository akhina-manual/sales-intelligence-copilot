import streamlit as st
import plotly.express as px

from components.charts import style_chart


def render(df, forecast):
    st.title("Profitability")
    st.caption("Margin performance, discount impact, and profit drivers.")

    st.divider()

    total_profit = df["Profit"].sum()
    avg_margin = df["Profit Margin"].mean()
    avg_discount = df["Discount"].mean()
    loss_sales = df[df["Profit"] < 0]["Sales"].sum()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Profit", f"${total_profit:,.0f}")
    c2.metric("Avg Margin", f"{avg_margin:.1%}")
    c3.metric("Avg Discount", f"{avg_discount:.1%}")
    c4.metric("Loss-Making Sales", f"${loss_sales:,.0f}")

    st.divider()

    left, right = st.columns(2)

    with left:
        margin_df = (
            df.groupby("Category")["Profit Margin"]
            .mean()
            .reset_index()
            .sort_values("Profit Margin", ascending=False)
        )

        margin_fig = px.bar(
            margin_df,
            x="Category",
            y="Profit Margin",
            color="Category"
        )

        margin_fig = style_chart(
            margin_fig,
            "Average Profit Margin by Category"
        )

        st.plotly_chart(margin_fig, use_container_width=True)

    with right:
        discount_df = (
            df.groupby("Category")["Discount Impact"]
            .sum()
            .reset_index()
            .sort_values("Discount Impact", ascending=False)
        )

        discount_fig = px.bar(
            discount_df,
            x="Category",
            y="Discount Impact",
            color="Category"
        )

        discount_fig = style_chart(
            discount_fig,
            "Discount Impact by Category"
        )

        st.plotly_chart(discount_fig, use_container_width=True)

    st.divider()

    scatter_fig = px.scatter(
        df,
        x="Discount",
        y="Profit",
        color="Category",
        hover_data=["Product Name", "Sales"],
    )

    scatter_fig = style_chart(
        scatter_fig,
        "Discount vs Profit"
    )

    st.plotly_chart(scatter_fig, use_container_width=True)

    st.divider()

    st.subheader("Profitability Insights")

    best_margin_category = margin_df.iloc[0]["Category"]
    highest_discount_category = discount_df.iloc[0]["Category"]

    st.info(
        f"""
        **Highest margin category:** {best_margin_category}

        **Highest discount impact category:** {highest_discount_category}

        Use the Discount vs Profit chart to identify whether higher discounts are reducing profitability.
        """
    )