import streamlit as st


def info_card(title, value, icon="📊", color="#2563EB"):
    st.markdown(
        f"""
        <div style="
            background:white;
            padding:18px;
            border-radius:16px;
            border-left:6px solid {color};
            margin-bottom:14px;
            box-shadow:0 4px 12px rgba(0,0,0,0.05);
        ">
            <div style="color:#6B7280;font-size:14px;">
                {icon} {title}
            </div>
            <div style="font-size:26px;font-weight:700;color:#111827;">
                {value}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def status_card(title, message, color="#10B981", icon="🟢"):
    st.markdown(
        f"""
        <div style="
            background:white;
            padding:18px;
            border-radius:16px;
            border-left:6px solid {color};
            margin-bottom:14px;
            box-shadow:0 4px 12px rgba(0,0,0,0.05);
        ">
            <h4 style="margin-bottom:8px;">{icon} {title}</h4>
            <p style="color:#4B5563;margin-bottom:0;">{message}</p>
        </div>
        """,
        unsafe_allow_html=True
    )