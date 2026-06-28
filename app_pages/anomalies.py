import streamlit as st
import plotly.express as px

from components.charts import style_chart


def detect_anomalies(monthly):
    monthly = monthly.copy()

    mean_sales = monthly["Sales"].mean()
    std_sales = monthly["Sales"].std()

    monthly["Z_Score"] = (monthly["Sales"] - mean_sales) / std_sales

    anomalies = monthly[
        (monthly["Z_Score"] > 2) |
        (monthly["Z_Score"] < -2)
    ]

    return monthly, anomalies


def render(df, forecast):
    st.title("Risk Center")
    st.caption("Monthly anomalies, outlier transactions, and sales risk indicators.")

    st.divider()

    monthly = (
        df.set_index("Order Date")
        .sort_index()
        .resample("ME")["Sales"]
        .sum()
        .reset_index()
    )

    monthly, anomalies = detect_anomalies(monthly)

    order_outliers = df[df["Sales_Outlier"] == 1] if "Sales_Outlier" in df.columns else df.iloc[0:0]

    loss_orders = df[df["Profit"] < 0].shape[0]
    high_discount_orders = df[df["Discount"] > 0.30].shape[0]

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Monthly Anomalies", len(anomalies))
    c2.metric("High-Impact Orders", len(order_outliers))
    c3.metric("Loss Orders", loss_orders)
    c4.metric("High Discounts", high_discount_orders)

    st.divider()

    fig = px.line(
        monthly,
        x="Order Date",
        y="Sales",
        markers=True,
        color_discrete_sequence=["#2563EB"]
    )

    if not anomalies.empty:
        fig.add_scatter(
            x=anomalies["Order Date"],
            y=anomalies["Sales"],
            mode="markers",
            marker=dict(color="red", size=12),
            name="Anomaly"
        )

    fig.update_xaxes(tickformat="%b %Y")
    fig = style_chart(fig, "Monthly Sales Anomalies")

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("Risk Interpretation")

    if anomalies.empty:
        st.success("No significant monthly sales anomalies detected.")
    else:
        for _, row in anomalies.iterrows():
            st.warning(
                f"{row['Order Date'].strftime('%b %Y')}: "
                f"Sales were unusually {'high' if row['Z_Score'] > 0 else 'low'} "
                f"with a Z-score of {row['Z_Score']:.2f}."
            )

    st.divider()

    st.subheader("High-Impact Transactions")

    if order_outliers.empty:
        st.success("No high-impact transactions detected.")
    else:
        st.dataframe(
            order_outliers[
                [
                    "Order Date",
                    "Customer Name",
                    "Product Name",
                    "Category",
                    "Sales",
                    "Profit"
                ]
            ].sort_values("Sales", ascending=False),
            use_container_width=True,
            height=400
        )