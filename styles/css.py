def load_css():
    return """
    <style>
    .stApp {
        background-color: #F8FAFC;
    }

    [data-testid="stSidebar"] {
        background-color: #111827;
    }

    [data-testid="stSidebar"] * {
        color: white;
    }

    [data-testid="stSidebar"] label {
        font-weight: 600;
        color: #E5E7EB;
    }

    .main-header {
        padding: 30px;
        border-radius: 22px;
        background: linear-gradient(90deg, #2563EB, #4F46E5);
        color: white;
        margin-bottom: 28px;
        box-shadow: 0 10px 30px rgba(37,99,235,0.25);
    }

    .main-header h1 {
        margin-bottom: 6px;
        font-size: 38px;
    }

    .main-header p {
        font-size: 18px;
        margin-bottom: 0;
        opacity: 0.95;
    }

    [data-testid="stMetric"] {
        background: white;
        padding: 20px;
        border-radius: 18px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    }

    div[data-testid="stPlotlyChart"] {
        background: white;
        border-radius: 18px;
        padding: 14px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 6px 18px rgba(0,0,0,0.04);
    }

    .stButton > button {
        background: #2563EB;
        color: white;
        border: none;
        border-radius: 12px;
        height: 44px;
        font-weight: 700;
    }

    .stButton > button:hover {
        background: #1D4ED8;
        color: white;
    }

    [data-testid="stDownloadButton"] button {
        background: #111827;
        color: white;
        border-radius: 12px;
        height: 44px;
        font-weight: 700;
        border: none;
    }

    div[data-testid="stDataFrame"] {
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid #E5E7EB;
    }

    h1, h2, h3 {
        color: #111827;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """