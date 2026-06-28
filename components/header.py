import streamlit as st


def show_header():
    st.markdown(
        """
        <div class="main-header">
            <h1>📊 Sales Intelligence Copilot</h1>
            <p>AI-powered sales analytics, forecasting, and business insights</p>
        </div>
        """,
        unsafe_allow_html=True
    )