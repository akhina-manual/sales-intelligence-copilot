import streamlit as st
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


@st.cache_data
def load_data():
    df = pd.read_csv(
        BASE_DIR / "data" / "processed" / "superstore_features.csv",
        encoding="latin1"
    )

    forecast = pd.read_csv(
        BASE_DIR / "data" / "processed" / "sales_forecast.csv",
        encoding="latin1"
    )

    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
    forecast["Date"] = pd.to_datetime(forecast["Date"])

    return df, forecast