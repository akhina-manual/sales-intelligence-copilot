import streamlit as st
import plotly.express as px

import pandas as pd


from components.charts import style_chart




def render(df, forecast):
    st.title("Sales Analytics")
    st.caption("Revenue trends, forecast performance, and sales behavior.")

    st.divider()

    monthly = (
        df.set_index("Order Date")
        .sort_index()
        .resample("ME")["Sales"]
        .sum()
        .reset_index()
    )

    last_actual = monthly["Sales"].iloc[-1]
    projected_revenue = forecast["Forecast Sales"].iloc[-1]

    change = ((projected_revenue - last_actual) / last_actual) * 100 if last_actual != 0 else 0

    c1, c2, c3 = st.columns(3)

    c1.metric("Last Actual Revenue", f"${last_actual:,.0f}")
    c2.metric("Next Forecast", f"${projected_revenue:,.0f}")
    c3.metric("Forecast Change", f"{change:.2f}%")

    st.divider()

    left, right = st.columns(2)

    with left:
        revenue_fig = px.line(
            monthly,
            x="Order Date",
            y="Sales",
            markers=True,
            color_discrete_sequence=["#2563EB"]
        )

        revenue_fig.update_xaxes(tickformat="%b %Y")
        revenue_fig = style_chart(revenue_fig, "Monthly Revenue Trend")

        st.plotly_chart(revenue_fig, use_container_width=True)

    with right:
        forecast_fig = px.line(
            forecast,
            x="Date",
            y="Forecast Sales",
            markers=True,
            color_discrete_sequence=["#10B981"]
        )

        forecast_fig.update_xaxes(tickformat="%b %Y")
        forecast_fig = style_chart(forecast_fig, "Sales Forecast")

        st.plotly_chart(forecast_fig, use_container_width=True)

    st.divider()

    weekday_sales = (
    df.groupby("Order DayOfWeek")["Sales"]
    .sum()
    .reset_index()
)

    day_order = [
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
]

    weekday_sales["Order DayOfWeek"] = pd.Categorical(
    weekday_sales["Order DayOfWeek"],
    categories=day_order,
    ordered=True
)

    weekday_sales = weekday_sales.sort_values("Order DayOfWeek")

    weekday_fig = px.bar(
        weekday_sales,
        x="Order DayOfWeek",
        y="Sales",
        color="Sales",
        
    )
    weekday_fig.update_traces(
    marker_color="#2563EB"
)
    weekday_fig = style_chart(weekday_fig, "Sales by Day of Week")

    st.plotly_chart(weekday_fig, use_container_width=True)

    st.divider()

    if change > 0:
        st.success(f"Revenue is forecasted to increase by {change:.2f}% compared with the last actual period.")
    elif change < 0:
        st.warning(f"Revenue is forecasted to decrease by {abs(change):.2f}% compared with the last actual period.")
    else:
        st.info("Forecast revenue is expected to remain stable.")