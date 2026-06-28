import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from components.charts import style_chart


def render(df, forecast):
    st.title("Product Intelligence")
    st.caption("Category performance, top products, and loss-making orders.")

    st.divider()

    total_products = df["Product Name"].nunique()
    top_category = df.groupby("Category")["Sales"].sum().idxmax()
    loss_orders = df[df["Profit"] < 0].shape[0]

    c1, c2, c3 = st.columns(3)

    c1.metric("Unique Products", total_products)
    c2.metric("Top Category", top_category)
    c3.metric("Loss Orders", loss_orders)

    st.divider()

    category_df = (
        df.groupby("Category")[["Sales", "Profit"]]
        .sum()
        .reset_index()
    )

    fig = go.Figure()

    fig.add_bar(
        x=category_df["Category"],
        y=category_df["Sales"],
        name="Sales"
    )

    fig.add_scatter(
        x=category_df["Category"],
        y=category_df["Profit"],
        mode="lines+markers",
        name="Profit",
        yaxis="y2"
    )

    fig.update_layout(
        yaxis=dict(title="Sales"),
        yaxis2=dict(
            title="Profit",
            overlaying="y",
            side="right",
            showgrid=False
        )
    )

    fig = style_chart(fig, "Sales & Profit by Category")

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    left, right = st.columns(2)

    with left:
        region_sales = (
            df.groupby("Region")["Sales"]
            .sum()
            .reset_index()
        )

        pie_fig = px.pie(
            region_sales,
            names="Region",
            values="Sales",
            hole=0.45
        )

        pie_fig = style_chart(pie_fig, "Region Sales Share")

        st.plotly_chart(pie_fig, use_container_width=True)

    with right:
        top_products = (
            df.groupby("Product Name")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )
        top_products["Short Name"] = top_products["Product Name"].apply(
        lambda x: x if len(x) <= 35 else x[:35] + "...")

        bar_fig = px.bar(
        top_products,
        x="Sales",
        y="Short Name",
        orientation="h",
        hover_data={
        "Product Name": True,   # Full product name
        "Short Name": False,    # Hide short name in tooltip
        "Sales": ":,.0f"})

        bar_fig.update_layout(height=650,margin=dict(l=220, r=20, t=50, b=40),
        coloraxis_showscale=False)

        bar_fig.update_yaxes(title=None,tickfont=dict(size=11))

        bar_fig.update_yaxes(title=None,tickfont=dict(size=12))
        bar_fig.update_layout(yaxis=dict(autorange="reversed"))
        bar_fig.update_traces(marker_color="#2563EB")
        bar_fig = style_chart(bar_fig, "Top 10 Products")

        st.plotly_chart(bar_fig, use_container_width=True)

    st.divider()

    st.subheader("Loss-Making Orders")

    loss_df = df[df["Profit"] < 0]

    if loss_df.empty:
        st.success("No loss-making orders found.")
    else:
        st.dataframe(
            loss_df[
                [
                    "Order Date",
                    "Customer Name",
                    "Product Name",
                    "Category",
                    "Sales",
                    "Profit",
                    "Discount"
                ]
            ].sort_values("Profit"),
            use_container_width=True,
            height=400
        )