import streamlit as st


def show_footer():
    st.markdown(
        """
        <div style="
            text-align:center;
            color:#6B7280;
            font-size:13px;
            padding:30px;
            margin-top:40px;
        ">
            Sales Intelligence Copilot • Built with Streamlit, Plotly, Pandas & Groq AI
        </div>
        """,
        unsafe_allow_html=True
    )