import streamlit as st

from components.cards import info_card, status_card


def render(df, forecast):
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order ID"].nunique()
    avg_margin = df["Profit Margin"].mean()
    avg_discount = df["Discount"].mean()

    st.title("Executive Dashboard")
    st.caption("A high-level overview of sales performance.")

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Revenue", f"${total_sales:,.0f}")
    c2.metric("Orders", f"{total_orders:,}")
    c3.metric("Profit", f"${total_profit:,.0f}")
    c4.metric("Margin", f"{avg_margin:.1%}")

    st.divider()

    left, right = st.columns([2, 1])

    with left:
        st.subheader("Operations Summary")

        a, b, c = st.columns(3)

        with a:
            info_card("Average Discount", f"{avg_discount:.1%}", "🏷️", "#F59E0B")

        with b:
            info_card("Unique Products", df["Product Name"].nunique(), "📦", "#2563EB")

        with c:
            info_card("Profit Margin", f"{avg_margin:.1%}", "💰", "#10B981")

        st.subheader("Top Revenue Drivers")

        top_categories = (
            df.groupby("Category")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(3)
        )

        for i, (category, sales) in enumerate(top_categories.items(), start=1):
            info_card(
                f"#{i} {category}",
                f"${sales:,.0f}",
                "🏆",
                "#4F46E5"
            )

    with right:
        st.subheader("Business Health")

        if avg_margin >= 0.20:
            status_card(
                "Strong Profitability",
                "Margins are healthy and business performance looks strong.",
                "#10B981",
                "🟢"
            )
        elif avg_margin >= 0.10:
            status_card(
                "Moderate Profitability",
                "Margins are acceptable, but there is room for improvement.",
                "#F59E0B",
                "🟡"
            )
        else:
            status_card(
                "Low Profitability",
                "Margins need attention. Review discounts and loss-making products.",
                "#EF4444",
                "🔴"
            )

        loss_orders = df[df["Profit"] < 0].shape[0]
        high_discount = df[df["Discount"] > 0.30].shape[0]

        st.subheader("Risk Indicators")

        info_card("Loss Orders", loss_orders, "⚠️", "#EF4444")
        info_card("High Discount Orders", high_discount, "🏷️", "#F59E0B")

    st.divider()

    best_category = df.groupby("Category")["Sales"].sum().idxmax()

    st.subheader("Executive Summary")

    st.markdown(
        f"""
        - Revenue reached **${total_sales:,.0f}**
        - Profit generated was **${total_profit:,.0f}**
        - Total unique orders: **{total_orders:,}**
        - Best-performing category: **{best_category}**
        - Average profit margin: **{avg_margin:.1%}**
        """
    )