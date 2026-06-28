import streamlit as st


def build_sidebar(df):
    with st.sidebar:
        st.markdown(
            """
            <div style="padding-bottom:8px;">
                <h1 style="font-size:25px;margin-bottom:0;">📊 Sales Intelligence Copilot</h1>
                <p style="color:#9CA3AF;margin-top:4px;">AI-Powered Business Intelligence Dashboard</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        page = st.radio(
            "Navigation",
            [
                "Executive Dashboard",
                "Sales Analytics",
                "Product Intelligence",
                "Risk Center",
                "Profitability",
                "AI Assistant"
            ]
        )

        st.divider()

        st.markdown("### 🔎 Filters")

        region = st.selectbox(
            "Region",
            ["All"] + sorted(df["Region"].dropna().unique())
        )

        category = st.selectbox(
            "Category",
            ["All"] + sorted(df["Category"].dropna().unique())
        )

        st.divider()

        st.caption("Version 2.0")
        st.caption("Built with Streamlit • Plotly • Groq AI")

    return page, region, category